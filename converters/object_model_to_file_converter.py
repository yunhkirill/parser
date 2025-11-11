from ..resources import NetlistProject, Block, PinRef, Instance

class ObjectModelToFileConverter:
    """
    Конвертер из объектной модели в исходный текстовый формат
    """
    def convert(self, project: NetlistProject) -> str:        
        file_content = []
        
        main_block = next((b for b in project.blocks.values() if b.name == "main"), None)
        
        if main_block:
            file_content.extend(self._convert_main_block(main_block))
        
        other_blocks = [b for b in project.blocks.values() if b.name != "main"]
        for block in other_blocks:
            if file_content and file_content[-1] != "":
                file_content.append("")
            file_content.extend(self._convert_named_block(block))
        
        return "\n".join(file_content)

    def _convert_main_block(self, block: Block) -> list[str]:
        lines = ["main:"]
        lines.extend(self._convert_block_content(block))
        return lines

    def _convert_named_block(self, block: Block) -> list[str]:
        lines = [f"{block.name}:"]
        lines.extend(self._convert_block_content(block))
        return lines

    def _convert_block_content(self, block: Block) -> list[str]:
        lines = []
        
        for pin_ref in block.interface_pins.values():
            connected_net = self._find_net_for_pin(block, pin_ref)
            if connected_net:
                lines.append(f"pin {pin_ref.name} - {connected_net.name}")
            else:
                lines.append(f"pin {pin_ref.name}")
        
        if block.interface_pins and block.instances:
            lines.append("")
        
        for instance in block.instances.values():
            lines.append(f"instance {instance.name}: {instance.type.name}")
        
        if block.instances and any(block.nets.values()):
            lines.append("")
        
        connections = []
        for net in block.nets.values():
            for pin_ref in net.pins.values():
                if pin_ref in block.interface_pins.values():
                    continue
                pin_ref_str = self._format_pin_ref(pin_ref)
                connections.append(f"{pin_ref_str} - {net.name}")
        
        lines.extend(connections)
        
        return lines

    def _find_net_for_pin(self, block: Block, pin_ref: PinRef):
        for net in block.nets.values():
            if pin_ref in net.pins.values():
                return net
        return None

    def _format_pin_ref(self, pin_ref: PinRef) -> str:
        parent = pin_ref.ref_parent
        
        if isinstance(parent, Block):
            return pin_ref.name
        elif isinstance(parent, Instance):
            return f"{parent.name}.{pin_ref.name}"
        else:
            if hasattr(pin_ref, 'name'):
                return pin_ref.name
            return "UNKNOWN_PIN"