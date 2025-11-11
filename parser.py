from typing import List
from .converters import ASTToObjectModelConverter, FileToParseTreeConverter, ObjectModelToFileConverter, ParseTreeToASTConverter
from .resources import NetlistProject, AST, ReportEntry


class Parser:
    def __init__(self):
        self._file_to_ps_converter = FileToParseTreeConverter()
        self._pt_to_ast_converter = ParseTreeToASTConverter()
        self._ast_to_om_converter = ASTToObjectModelConverter()
        self._om_to_file_converter = ObjectModelToFileConverter()
        
    def load_netlist_from_file(self, file_path: str) -> tuple[NetlistProject, List[ReportEntry]]:
        reports = []

        parse_tree, reports = self._get_parse_tree_from_file(file_path, reports)
        ast = self._get_ast_from_parse_tree(parse_tree)
        project, reports = self._get_object_model_from_ast(ast, file_path, reports)
        return project, reports


    def save_netlist_to_file(self, file_path: str, netlist: NetlistProject) -> bool:
        try:
            file_content = self._convert_object_model_to_file(netlist)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
            return True
        except Exception as e:
            return False
    
    def _get_parse_tree_from_file(self, file_path: str, reports: list):
        return self._file_to_ps_converter.convert(file_path, reports)
    
    def _get_ast_from_parse_tree(self, parse_tree):
        return self._pt_to_ast_converter.convert(parse_tree)
    
    def _get_object_model_from_ast(self, ast: AST, file_path: str, reports: list):
        project_name = file_path.split('/')[-1].split('\\')[-1]
        return self._ast_to_om_converter.convert(ast, project_name, reports)

    def _convert_object_model_to_file(self, project: NetlistProject) -> str:
        return self._om_to_file_converter.convert(project)