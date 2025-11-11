class ASTNode:
    def __init__(self, node_type: str, value: str = None, line_number: int = -1):
        self.node_type = node_type
        self.value = value
        self.line_number = line_number
        self.children = []
        self.parent = None
        self.attributes = {}

    def add_child(self, child_node: 'ASTNode') -> None:
        if child_node not in self.children:
            self.children.append(child_node)
            child_node.parent = self

    def remove_child(self, child_node: 'ASTNode') -> None:
        if child_node in self.children:
            self.children.remove(child_node)
            child_node.parent = None

    def get_siblings(self) -> list:
        if self.parent is None:
            return []
        return [child for child in self.parent.children if child != self]

    def __str__(self) -> str:
        attrs = ""
        if self.attributes:
            attrs = f" {self.attributes}"
        return f"{self.node_type}: {self.value}{attrs}"

    def __repr__(self) -> str:
        return self.__str__()


class AST:
    """
    Абстрактное синтаксическое дерево (AST)
    """
    def __init__(self):
        self.root = None
        self.nodes = []

    def add_node(self, parent: ASTNode = None, node_type: str = "", value: str = None, line_number: int = -1) -> ASTNode:
        new_node = ASTNode(node_type, value, line_number)
        
        if parent is None:
            if self.root is None:
                self.root = new_node
        else:
            parent.add_child(new_node)
        
        self.nodes.append(new_node)
        return new_node

    def find_nodes(self, node_type: str) -> list:
        return [node for node in self.nodes if node.node_type == node_type]

    def get_children(self, node: ASTNode) -> list:
        return node.children.copy()

    def get_parent(self, node: ASTNode) -> ASTNode:
        return node.parent

    def traverse(self, callback, node: ASTNode = None):
        if node is None:
            if self.root is None:
                return
            node = self.root
        
        callback(node)
        
        for child in node.children:
            self.traverse(callback, child)

    def print_tree(self, node: ASTNode = None, level: int = 0):
        if node is None:
            if self.root is None:
                print("Empty AST")
                return
            node = self.root
        
        indent = "  " * level
        print(f"{indent}{node}")
        
        for child in node.children:
            self.print_tree(child, level + 1)
