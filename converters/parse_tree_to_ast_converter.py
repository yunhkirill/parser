from ..resources import AST

class ParseTreeToASTConverter:
    """
    Конвертер из ParseTree в AST
    """
    def __init__(self):
        """
        Инициализация конвертера
        """
        self.ast = AST()
        self.current_block = None  # устанавливаем текущий блок в None

    def convert(self, parse_tree) -> AST:
        """
        Основной метод конвертации ParseTree в AST
        """
        netlist_node = self.ast.add_node(node_type="netlist", value="root")
        self._process_prog(parse_tree, netlist_node)
        return self.ast

    def _process_prog(self, prog_node, parent_ast_node):
        """
        Обработка корневого узла
        Проходит по всем дочерним узлам и распределяет их по типам:
        1) Main_block
        2) Named_block
        3) Element
        """
        for i in range(prog_node.getChildCount()):
            child = prog_node.getChild(i)
            child_type = type(child).__name__
            
            if hasattr(child, 'getRuleIndex'):
                # определяется тип узла и вызываем соответствующий обработчик
                if 'Main_blockContext' in child_type:
                    self._process_main_block(child, parent_ast_node)
                elif 'Named_blockContext' in child_type:
                    self._process_named_block(child, parent_ast_node)
                elif 'ElementContext' in child_type:
                    self._process_element(child, parent_ast_node, "main")

    def _process_main_block(self, main_block_node, parent_ast_node):
        """
        Обработка главного блока (main block)
        """
        main_block_ast = self.ast.add_node(
            parent=parent_ast_node,
            node_type="block_definition",
            value="main"
        )
        
        for i in range(main_block_node.getChildCount()):
            child = main_block_node.getChild(i)
            child_type = type(child).__name__
            
            if 'Block_contentContext' in child_type:
                self._process_block_content(child, main_block_ast, "main")
                break

    def _process_named_block(self, named_block_node, parent_ast_node):
        """
        Обработка именованного блока
        """
        # получение имени блока (первый значимый текстовый узел, не ':' и не '\n')
        block_name = None
        for i in range(named_block_node.getChildCount()):
            child = named_block_node.getChild(i)
            if hasattr(child, 'getText') and child.getText() not in [':', '\n']:
                block_name = child.getText()
                break
        
        if not block_name:
            return
        
        # создаем узел блока с найденным именем
        named_block_ast = self.ast.add_node(
            parent=parent_ast_node,
            node_type="block_definition",
            value=block_name
        )
        
        for i in range(named_block_node.getChildCount()):
            child = named_block_node.getChild(i)
            child_type = type(child).__name__
            
            if 'Block_contentContext' in child_type:
                self._process_block_content(child, named_block_ast, block_name)
                break

    def _process_block_content(self, block_content_node, parent_ast_node, block_name):
        """
        Обработка содержимого блока
        """
        # обрабатываем все элементы внутри блока
        for i in range(block_content_node.getChildCount()):
            child = block_content_node.getChild(i)
            child_type = type(child).__name__
            
            if 'ElementContext' in child_type:
                self._process_element(child, parent_ast_node, block_name)

    def _process_element(self, element_node, parent_ast_node, block_name):
        """
        Обработка элемента блока.
        Элемент может быть:
        1) Pin_decl (объявление пина)
        2) Instance_decl (объявление экземпляра)
        3) Net_decl (объявление соединения)
        """
        # определяем тип элемента и вызываем соответствующий обработчик
        for i in range(element_node.getChildCount()):
            child = element_node.getChild(i)
            child_type = type(child).__name__
            
            if 'Pin_declContext' in child_type:
                self._process_pin_decl(child, parent_ast_node, block_name)
            elif 'Instance_declContext' in child_type:
                self._process_instance_decl(child, parent_ast_node, block_name)
            elif 'Net_declContext' in child_type:
                self._process_net_decl(child, parent_ast_node, block_name)

    def _process_pin_decl(self, pin_decl_node, parent_ast_node, block_name):
        """
        Обработка объявления пина (pin declaration)
        """
        pin_name = None
        net_name = None
        has_net = False
        
        for i in range(pin_decl_node.getChildCount()):
            child = pin_decl_node.getChild(i)
            child_type = type(child).__name__
            
            if 'Pin_nameContext' in child_type:
                pin_name = self._get_node_text(child.getChild(0))
            elif 'Net_nameContext' in child_type:
                net_name = self._get_node_text(child.getChild(0))
                has_net = True
        
        if pin_name:
            pin_ast = self.ast.add_node(
                parent=parent_ast_node,
                node_type="pin_declaration",
                value=pin_name
            )

            pin_ast.attributes.update({
                "block": block_name,
                "net": net_name,
                "has_net": has_net
            })

    def _process_instance_decl(self, instance_decl_node, parent_ast_node, block_name):
        """
        Обработка объявления инстанса (instance declaration)
        """
        instance_name = None
        instance_type = None
        
        for i in range(instance_decl_node.getChildCount()):
            child = instance_decl_node.getChild(i)
            child_type = type(child).__name__
            
            if 'Instance_nameContext' in child_type:
                instance_name = self._get_node_text(child.getChild(0))
            elif 'Block_refContext' in child_type:
                instance_type = self._get_node_text(child.getChild(0))
        
        if instance_name and instance_type:
            instance_ast = self.ast.add_node(
                parent=parent_ast_node,
                node_type="instance_declaration",
                value=instance_name
            )
            instance_ast.attributes.update({
                "block": block_name,
                "instance_type": instance_type
            })

    def _process_net_decl(self, net_decl_node, parent_ast_node, block_name):
        """
        Обработка сети (net declaration)
        """
        net_name = None
        pin_ref_info = None
        
        for i in range(net_decl_node.getChildCount()):
            child = net_decl_node.getChild(i)
            child_type = type(child).__name__
            
            if 'Net_nameContext' in child_type:
                net_name = self._get_node_text(child.getChild(0))
            elif 'Pin_refContext' in child_type:
                pin_ref_info = self._process_pin_ref(child)
        
        if net_name and pin_ref_info:
            instance_name, pin_name = pin_ref_info
            full_pin_name = f"{instance_name + '.' if instance_name else ''}{pin_name}"
            
            connection_ast = self.ast.add_node(
                parent=parent_ast_node,
                node_type="connection",
                value=full_pin_name
            )
            connection_ast.attributes.update({
                "block": block_name,
                "instance": instance_name,
                "pin": pin_name,
                "net": net_name
            })

    def _process_pin_ref(self, pin_ref_node):
        """
        Обработка пина (pin reference)
        """
        instance_name = None
        pin_name = None
        
        # Извлекаем имя экземпляра (опционально) и имя пина
        for i in range(pin_ref_node.getChildCount()):
            child = pin_ref_node.getChild(i)
            child_type = type(child).__name__
            
            if 'Instance_nameContext' in child_type:
                instance_name = self._get_node_text(child.getChild(0))
            elif 'Pin_nameContext' in child_type:
                pin_name = self._get_node_text(child.getChild(0))
        
        return (instance_name, pin_name)

    def _get_node_text(self, parse_tree_node) -> str:
        """
        Вспомогательный метод для извлечения текста из узла ParseTre
        """
        if hasattr(parse_tree_node, 'getText'):
            text = parse_tree_node.getText()
            return text.strip()
        return ""
