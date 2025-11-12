from typing import List
from ..resources import NetlistProject, AST, ASTNode, ReportEntry, Error

class ASTToObjectModelConverter:
    """
    Конвертер из AST в объектную модель проекта
    """
    
    def convert(self, ast: AST, project_name: str, reports: List) -> tuple[NetlistProject, List[ReportEntry]]:
        """
        Основной метод конвертации AST в объектную модель
        """
        project = NetlistProject(project_name)
        
        primitive_definitions = self._analyze_primitive_definitions(ast)
        
        # создание всех определений блоков
        self._create_all_block_definitions(ast, project, primitive_definitions, reports)
        
        # заполнение содержимого блоков
        self._populate_blocks_content(ast, project, reports)
        
        # подключение пинов блоков
        self._connect_interface_pins(ast, project, reports)
        
        # подключение сетей к пинам
        self._connect_nets(ast, project, reports)
        
        return project, reports

    def _analyze_primitive_definitions(self, ast: AST) -> dict:
        """
        Анализирует AST для обнаружения примитивных блоков
        """
        primitive_definitions = {}
        
        # находим все узлы объявления инстансов
        instance_nodes = ast.find_nodes('instance_declaration')
        
        for node in instance_nodes:
            instance_type = node.attributes.get('instance_type')
            if instance_type:
                block_nodes = {n.value for n in ast.find_nodes('block_definition')}
                if instance_type not in block_nodes:
                    if instance_type not in primitive_definitions:
                        primitive_definitions[instance_type] = set()
                    
                    # находим все соединения для этого инстанса, чтобы определить пины
                    connection_nodes = ast.find_nodes('connection')
                    for conn_node in connection_nodes:
                        if (conn_node.attributes.get('instance') == node.value and 
                            conn_node.attributes.get('block') == node.attributes.get('block')):
                            pin_name = conn_node.attributes.get('pin')
                            if pin_name:
                                primitive_definitions[instance_type].add(pin_name)
        
        return primitive_definitions

    def _create_all_block_definitions(self, ast: AST, project: NetlistProject, 
                                    primitive_definitions: dict, reports: List[ReportEntry]):
        """
        Создает все определения блоков в проекте
        """
        self._create_primitive_blocks(project, primitive_definitions, reports)
        self._create_regular_blocks(ast, project, reports)

    def _create_primitive_blocks(self, project: NetlistProject, primitive_definitions: dict, 
                               reports: List[ReportEntry]):
        """
        Создает примитивные блоки
        """
        for primitive_name, pin_names in primitive_definitions.items():
            try:
                project.add_primitive_block(primitive_name, list(pin_names))
            except Exception as e:
                reports.append(ReportEntry(
                    error=Error.DUPLICATE_NAME,
                    message=f"Cannot create primitive block '{primitive_name}': {e}",
                    location=f"primitive:{primitive_name}"
                ))

    def _create_regular_blocks(self, ast: AST, project: NetlistProject, reports: List[ReportEntry]):
        """
        Создает регулярные блоки, явно объявленные в AST через block_definition
        """
        block_nodes = ast.find_nodes('block_definition')
        
        for node in block_nodes:
            block_name = node.value
            
            try:
                project.add_block(block_name)
                
                pin_nodes = [child for child in ast.get_children(node) if child.node_type == 'pin_declaration']
                for pin_node in pin_nodes:
                    pin_name = pin_node.value
                    project.add_pin_to_block(block_name, pin_name)
                    
            except Exception as e:
                reports.append(ReportEntry(
                    error=Error.DUPLICATE_NAME,
                    message=f"Cannot create block '{block_name}': {e}",
                    location=f"block:{block_name}"
                ))

    def _populate_blocks_content(self, ast: AST, project: NetlistProject, reports: List[ReportEntry]):
        """
        Наполняет блоки инстансами и создает пустые определения цепей
        """
        block_nodes = ast.find_nodes('block_definition')
        
        for node in block_nodes:
            block_name = node.value
            
            instance_nodes = []
            connection_nodes = []
            
            for child in ast.get_children(node):
                if child.node_type == 'instance_declaration':
                    instance_nodes.append(child)
                elif child.node_type == 'connection':
                    connection_nodes.append(child)
            
            for instance_node in instance_nodes:
                self._process_instance(instance_node, block_name, project, reports)
            
            for connection_node in connection_nodes:
                self._process_net_creation(connection_node, block_name, project, reports)

    def _process_instance(self, instance_node: ASTNode, block_name: str, 
                         project: NetlistProject, reports: List[ReportEntry]):
        """
        Обрабатывает создание инстанса блока внутри родительского блока
        """
        instance_name = instance_node.value
        instance_type = instance_node.attributes.get('instance_type')
        
        if not instance_name or not instance_type:
            return
            
        if block_name not in project.blocks:
            reports.append(ReportEntry(
                error=Error.MISSING_BLOCK,
                message=f"Parent block '{block_name}' not found for instance '{instance_name}'",
                location=f"instance:{instance_name}",
                line=getattr(instance_node, 'line', None)
            ))
            return
            
        if instance_type not in project.blocks:
            reports.append(ReportEntry(
                error=Error.MISSING_BLOCK,
                message=f"Block type '{instance_type}' not found for instance '{instance_name}'",
                location=f"instance:{instance_name}",
                line=getattr(instance_node, 'line', None)
            ))
            return

        target_block = project.blocks[instance_type]
        if not target_block.interface_pins:
            reports.append(ReportEntry(
                error=Error.PIN_MISMATCH,
                message=f"Block '{instance_type}' has no pins defined",
                location=f"instance:{instance_name}",
                line=getattr(instance_node, 'line', None)
            ))
            return
        
        try:
            project.add_instance_to_block(block_name, instance_name, instance_type)
            
        except KeyError as e:
            missing_key = str(e).strip("'")
            if missing_key == instance_type:
                reports.append(ReportEntry(
                    error=Error.MISSING_BLOCK,
                    message=f"Block '{instance_type}' not properly initialized",
                    location=f"instance:{instance_name}",
                    line=getattr(instance_node, 'line', None)
                ))
            else:
                reports.append(ReportEntry(
                    error=Error.PIN_MISMATCH,
                    message=f"Cannot create instance '{instance_name}': key '{missing_key}' not found in block '{instance_type}'",
                    location=f"instance:{instance_name}",
                    line=getattr(instance_node, 'line', None)
                ))
        except Exception as e:
            reports.append(ReportEntry(
                error=Error.SYNTAX_ERROR,
                message=f"Internal error creating instance '{instance_name}': {e}",
                location=f"instance:{instance_name}",
                line=getattr(instance_node, 'line', None)
            ))

    def _process_net_creation(self, connection_node: ASTNode, block_name: str, 
                            project: NetlistProject, reports: List[ReportEntry]):
        """
        Создает сети внутри блоков на основе узлов соединений
        """
        net_name = connection_node.attributes.get('net')
        
        if not net_name:
            return
            
        try:
            current_block = project.blocks.get(block_name)
            if current_block and net_name not in current_block.nets:
                project.add_net_to_block(block_name, net_name)
        except Exception as e:
            reports.append(ReportEntry(
                error=Error.DUPLICATE_NAME,
                message=f"Cannot create net '{net_name}': {e}",
                location=f"net:{net_name}",
                line=getattr(connection_node, 'line', None)
            ))

    def _connect_nets(self, ast: AST, project: NetlistProject, reports: List[ReportEntry]):
        """
        Подключает пины экземпляров к сетям на основе информации о соединениях
        """
        connection_nodes = ast.find_nodes('connection')
        
        for node in connection_nodes:
            block_name = node.attributes.get('block')
            instance_name = node.attributes.get('instance')
            pin_name = node.attributes.get('pin')
            net_name = node.attributes.get('net')
            
            if not all([block_name, pin_name, net_name]):
                continue
                
            try:
                current_block = project.blocks.get(block_name)
                if not current_block:
                    reports.append(ReportEntry(
                        error=Error.MISSING_BLOCK,
                        message=f"Block '{block_name}' not found",
                        location=f"connection:{instance_name}.{pin_name}",
                        line=getattr(node, 'line', None)
                    ))
                    continue
                
                pin_ref_to_connect = self._find_pin_reference(current_block, instance_name, pin_name)
                
                if pin_ref_to_connect:
                    if net_name not in current_block.nets:
                        project.add_net_to_block(block_name, net_name)
                    
                    project.connect_pin_to_net_in_block(block_name, net_name, pin_ref_to_connect)
                else:
                    if instance_name:
                        instance = current_block.instances.get(instance_name)
                        if not instance:
                            reports.append(ReportEntry(
                                error=Error.MISSING_BLOCK,
                                message=f"Instance '{instance_name}' not found in block '{block_name}'",
                                location=f"instance:{instance_name}",
                                line=getattr(node, 'line', None)
                            ))
                        else:
                            available_pins = list(instance.interface_pins.keys())
                            block_pins = list(instance.type.interface_pins.keys())
                            reports.append(ReportEntry(
                                error=Error.PIN_MISMATCH,
                                message=f"Pin '{instance_name}.{pin_name}' not found. "
                                    f"Instance has pins: {available_pins}, "
                                    f"block '{instance.type.name}' has pins: {block_pins}",
                                location=f"instance:{instance_name}",
                                line=getattr(node, 'line', None)
                            ))
                    else:
                        available_pins = list(current_block.interface_pins.keys())
                        reports.append(ReportEntry(
                            error=Error.PIN_MISMATCH,
                            message=f"Pin '{pin_name}' not found in block '{block_name}'. "
                                f"Available pins: {available_pins}",
                            location=f"block:{block_name}",
                            line=getattr(node, 'line', None)
                        ))
                        
            except Exception as e:
                reports.append(ReportEntry(
                    error=Error.SYNTAX_ERROR,
                    message=f"Connection error: {e}",
                    location=f"connection:{instance_name}.{pin_name}",
                    line=getattr(node, 'line', None)
                ))

    def _find_pin_reference(self, block, instance_name: str, pin_name: str):
        """
        Находит пин в блоке или его экземплярах
        """
        if instance_name and instance_name in block.instances:
            instance = block.instances[instance_name]
            if pin_name in instance.interface_pins:
                return instance.interface_pins[pin_name]
        elif not instance_name and pin_name in block.interface_pins:
            return block.interface_pins[pin_name]
        
        return None
    
    def _connect_interface_pins(self, ast: AST, project: NetlistProject, reports: List[ReportEntry]):
        """
        Подключает пины блоков к внутренним сетям, обрабатывает объявления пинов с привязкой к сетям
        """
        pin_nodes = ast.find_nodes('pin_declaration')
        
        for pin_node in pin_nodes:
            block_name = pin_node.attributes.get('block')
            pin_name = pin_node.value
            net_name = pin_node.attributes.get('net')
            has_net = pin_node.attributes.get('has_net', False)
            
            # пропускаем пины без привязки к сети или с неполной информацией
            if not all([block_name, pin_name]) or not has_net or not net_name:
                continue
                
            try:
                current_block = project.blocks.get(block_name)
                if not current_block:
                    reports.append(ReportEntry(
                        error=Error.MISSING_BLOCK,
                        message=f"Block '{block_name}' not found for pin '{pin_name}'",
                        location=f"pin:{pin_name}",
                        line=getattr(pin_node, 'line', None)
                    ))
                    continue
                
                if pin_name in current_block.interface_pins:
                    pin_ref = current_block.interface_pins[pin_name]
                    
                    if net_name not in current_block.nets:
                        project.add_net_to_block(block_name, net_name)
                    
                    project.connect_pin_to_net_in_block(block_name, net_name, pin_ref)
                else:
                    reports.append(ReportEntry(
                        error=Error.PIN_MISMATCH,
                        message=f"Pin '{pin_name}' not found in block '{block_name}'",
                        location=f"pin:{pin_name}",
                        line=getattr(pin_node, 'line', None)
                    ))
                    
            except Exception as e:
                reports.append(ReportEntry(
                    error=Error.SYNTAX_ERROR,
                    message=f"Pin connection error: {e}",
                    location=f"pin:{pin_name}",
                    line=getattr(pin_node, 'line', None)
                ))

def getattr(node, attr, default=None):
    """
    Безопасный getattr для узлов AST
    """
    return getattr(node, attr, default) if hasattr(node, attr) else default