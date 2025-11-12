from typing import List
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ..resources import ExprLexer, ExprParser, ReportEntry, Error

class SyntaxErrorListener(ErrorListener):
    """
    Обработчик синтаксических ошибок
    """
    def __init__(self, reports: List[ReportEntry]):
        self.reports = reports
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Функция обрабатывает синтаксическую ошибку, обнаруженную парсером
        """
        self.reports.append(ReportEntry(
            error=Error.SYNTAX_ERROR,
            message=msg,
            location=f"line {line}:{column}",
            line=line
        ))

class FileToParseTreeConverter:
    """
    Конвертер из исходного файла в ParseTree
    """
    
    def convert(self, file_path: str, reports: List[ReportEntry]) -> ExprParser.ProgContext:
        """
        Основной метод конвертации файла в дерево разбора
        """
        input_stream = FileStream(file_path, encoding='utf-8')
        
        lexer = ExprLexer(input_stream)         # разбиваем текст на токены
        token_stream = CommonTokenStream(lexer)
        
        parser = ExprParser(token_stream)       # строим дерево разбора из токенов
        
        # заменяем стандартный обработчик ошибок
        error_listener = SyntaxErrorListener(reports)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        parse_tree = parser.prog()
        
        return parse_tree, reports

    def print_parse_tree(self, parse_tree: ExprParser.ProgContext, indent: int = 0):
        """
        Функция рекурсивно выводит дерево разбора в читаемом формате
        """
        if parse_tree is None:
            return
            
        if isinstance(parse_tree, TerminalNode):
            token = parse_tree.symbol
            token_type = token.type
            token_text = token.text.replace('\n', '\\n')
            token_name = ExprLexer.symbolicNames[token_type]
            print("  " * indent + f"TOKEN: {token_name} = '{token_text}'")
            return
        
        rule_name = ExprParser.ruleNames[parse_tree.getRuleIndex()]
        print("  " * indent + f"RULE: {rule_name}")
        
        for i in range(parse_tree.getChildCount()):
            child = parse_tree.getChild(i)
            self.print_parse_tree(child, indent + 1)