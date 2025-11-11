# Generated from parser/resources/antlr/grammar/Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#main_block.
    def enterMain_block(self, ctx:ExprParser.Main_blockContext):
        pass

    # Exit a parse tree produced by ExprParser#main_block.
    def exitMain_block(self, ctx:ExprParser.Main_blockContext):
        pass


    # Enter a parse tree produced by ExprParser#named_block.
    def enterNamed_block(self, ctx:ExprParser.Named_blockContext):
        pass

    # Exit a parse tree produced by ExprParser#named_block.
    def exitNamed_block(self, ctx:ExprParser.Named_blockContext):
        pass


    # Enter a parse tree produced by ExprParser#block_content.
    def enterBlock_content(self, ctx:ExprParser.Block_contentContext):
        pass

    # Exit a parse tree produced by ExprParser#block_content.
    def exitBlock_content(self, ctx:ExprParser.Block_contentContext):
        pass


    # Enter a parse tree produced by ExprParser#element.
    def enterElement(self, ctx:ExprParser.ElementContext):
        pass

    # Exit a parse tree produced by ExprParser#element.
    def exitElement(self, ctx:ExprParser.ElementContext):
        pass


    # Enter a parse tree produced by ExprParser#pin_decl.
    def enterPin_decl(self, ctx:ExprParser.Pin_declContext):
        pass

    # Exit a parse tree produced by ExprParser#pin_decl.
    def exitPin_decl(self, ctx:ExprParser.Pin_declContext):
        pass


    # Enter a parse tree produced by ExprParser#instance_decl.
    def enterInstance_decl(self, ctx:ExprParser.Instance_declContext):
        pass

    # Exit a parse tree produced by ExprParser#instance_decl.
    def exitInstance_decl(self, ctx:ExprParser.Instance_declContext):
        pass


    # Enter a parse tree produced by ExprParser#net_decl.
    def enterNet_decl(self, ctx:ExprParser.Net_declContext):
        pass

    # Exit a parse tree produced by ExprParser#net_decl.
    def exitNet_decl(self, ctx:ExprParser.Net_declContext):
        pass


    # Enter a parse tree produced by ExprParser#pin_ref.
    def enterPin_ref(self, ctx:ExprParser.Pin_refContext):
        pass

    # Exit a parse tree produced by ExprParser#pin_ref.
    def exitPin_ref(self, ctx:ExprParser.Pin_refContext):
        pass


    # Enter a parse tree produced by ExprParser#block_ref.
    def enterBlock_ref(self, ctx:ExprParser.Block_refContext):
        pass

    # Exit a parse tree produced by ExprParser#block_ref.
    def exitBlock_ref(self, ctx:ExprParser.Block_refContext):
        pass


    # Enter a parse tree produced by ExprParser#instance_name.
    def enterInstance_name(self, ctx:ExprParser.Instance_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#instance_name.
    def exitInstance_name(self, ctx:ExprParser.Instance_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#pin_name.
    def enterPin_name(self, ctx:ExprParser.Pin_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#pin_name.
    def exitPin_name(self, ctx:ExprParser.Pin_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#net_name.
    def enterNet_name(self, ctx:ExprParser.Net_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#net_name.
    def exitNet_name(self, ctx:ExprParser.Net_nameContext):
        pass



del ExprParser