# Generated from parser/resources/antlr/grammar/Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from io import TextIO

def serializedATN():
    return [
        4,1,10,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        5,0,29,8,0,10,0,12,0,32,9,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,3,5,3,44,8,3,10,3,12,3,47,9,3,1,4,1,4,3,4,51,8,4,1,4,1,4,3,4,55,
        8,4,1,4,1,4,3,4,59,8,4,3,4,61,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,70,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        3,8,86,8,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,0,0,13,0,2,
        4,6,8,10,12,14,16,18,20,22,24,0,0,91,0,26,1,0,0,0,2,33,1,0,0,0,4,
        37,1,0,0,0,6,45,1,0,0,0,8,60,1,0,0,0,10,69,1,0,0,0,12,71,1,0,0,0,
        14,76,1,0,0,0,16,85,1,0,0,0,18,87,1,0,0,0,20,89,1,0,0,0,22,91,1,
        0,0,0,24,93,1,0,0,0,26,30,3,2,1,0,27,29,3,4,2,0,28,27,1,0,0,0,29,
        32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,1,1,0,0,0,32,30,1,0,0,
        0,33,34,5,1,0,0,34,35,5,8,0,0,35,36,3,6,3,0,36,3,1,0,0,0,37,38,5,
        7,0,0,38,39,5,6,0,0,39,40,5,8,0,0,40,41,3,6,3,0,41,5,1,0,0,0,42,
        44,3,8,4,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,
        0,46,7,1,0,0,0,47,45,1,0,0,0,48,50,3,10,5,0,49,51,5,8,0,0,50,49,
        1,0,0,0,50,51,1,0,0,0,51,61,1,0,0,0,52,54,3,12,6,0,53,55,5,8,0,0,
        54,53,1,0,0,0,54,55,1,0,0,0,55,61,1,0,0,0,56,58,3,14,7,0,57,59,5,
        8,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,48,1,0,0,0,60,
        52,1,0,0,0,60,56,1,0,0,0,61,9,1,0,0,0,62,63,5,2,0,0,63,70,3,22,11,
        0,64,65,5,2,0,0,65,66,3,22,11,0,66,67,5,5,0,0,67,68,3,24,12,0,68,
        70,1,0,0,0,69,62,1,0,0,0,69,64,1,0,0,0,70,11,1,0,0,0,71,72,5,3,0,
        0,72,73,3,20,10,0,73,74,5,6,0,0,74,75,3,18,9,0,75,13,1,0,0,0,76,
        77,3,16,8,0,77,78,5,5,0,0,78,79,3,24,12,0,79,15,1,0,0,0,80,86,3,
        22,11,0,81,82,3,20,10,0,82,83,5,4,0,0,83,84,3,22,11,0,84,86,1,0,
        0,0,85,80,1,0,0,0,85,81,1,0,0,0,86,17,1,0,0,0,87,88,5,7,0,0,88,19,
        1,0,0,0,89,90,5,7,0,0,90,21,1,0,0,0,91,92,5,7,0,0,92,23,1,0,0,0,
        93,94,5,7,0,0,94,25,1,0,0,0,8,30,45,50,54,58,60,69,85
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main:'", "'pin'", "'instance'", "'.'", 
                     "'-'", "':'" ]

    symbolicNames = [ "<INVALID>", "MAIN", "PIN", "INSTANCE", "DOT", "DASH", 
                      "COLON", "IDENTIFIER", "NEWLINE", "WS", "LINE_COMMENT" ]

    RULE_prog = 0
    RULE_main_block = 1
    RULE_named_block = 2
    RULE_block_content = 3
    RULE_element = 4
    RULE_pin_decl = 5
    RULE_instance_decl = 6
    RULE_net_decl = 7
    RULE_pin_ref = 8
    RULE_block_ref = 9
    RULE_instance_name = 10
    RULE_pin_name = 11
    RULE_net_name = 12

    ruleNames =  [ "prog", "main_block", "named_block", "block_content", 
                   "element", "pin_decl", "instance_decl", "net_decl", "pin_ref", 
                   "block_ref", "instance_name", "pin_name", "net_name" ]

    EOF = Token.EOF
    MAIN=1
    PIN=2
    INSTANCE=3
    DOT=4
    DASH=5
    COLON=6
    IDENTIFIER=7
    NEWLINE=8
    WS=9
    LINE_COMMENT=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_block(self):
            return self.getTypedRuleContext(ExprParser.Main_blockContext,0)


        def named_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Named_blockContext)
            else:
                return self.getTypedRuleContext(ExprParser.Named_blockContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.main_block()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 27
                self.named_block()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(ExprParser.MAIN, 0)

        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def block_content(self):
            return self.getTypedRuleContext(ExprParser.Block_contentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_main_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_block" ):
                listener.enterMain_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_block" ):
                listener.exitMain_block(self)




    def main_block(self):

        localctx = ExprParser.Main_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(ExprParser.MAIN)
            self.state = 34
            self.match(ExprParser.NEWLINE)
            self.state = 35
            self.block_content()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Named_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def block_content(self):
            return self.getTypedRuleContext(ExprParser.Block_contentContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_named_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamed_block" ):
                listener.enterNamed_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamed_block" ):
                listener.exitNamed_block(self)




    def named_block(self):

        localctx = ExprParser.Named_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_named_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ExprParser.IDENTIFIER)
            self.state = 38
            self.match(ExprParser.COLON)
            self.state = 39
            self.match(ExprParser.NEWLINE)
            self.state = 40
            self.block_content()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ElementContext)
            else:
                return self.getTypedRuleContext(ExprParser.ElementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_content" ):
                listener.enterBlock_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_content" ):
                listener.exitBlock_content(self)




    def block_content(self):

        localctx = ExprParser.Block_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 42
                    self.element() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pin_decl(self):
            return self.getTypedRuleContext(ExprParser.Pin_declContext,0)


        def NEWLINE(self):
            return self.getToken(ExprParser.NEWLINE, 0)

        def instance_decl(self):
            return self.getTypedRuleContext(ExprParser.Instance_declContext,0)


        def net_decl(self):
            return self.getTypedRuleContext(ExprParser.Net_declContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = ExprParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.pin_decl()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 49
                    self.match(ExprParser.NEWLINE)


                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.instance_decl()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 53
                    self.match(ExprParser.NEWLINE)


                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.net_decl()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 57
                    self.match(ExprParser.NEWLINE)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pin_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIN(self):
            return self.getToken(ExprParser.PIN, 0)

        def pin_name(self):
            return self.getTypedRuleContext(ExprParser.Pin_nameContext,0)


        def DASH(self):
            return self.getToken(ExprParser.DASH, 0)

        def net_name(self):
            return self.getTypedRuleContext(ExprParser.Net_nameContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_pin_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPin_decl" ):
                listener.enterPin_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPin_decl" ):
                listener.exitPin_decl(self)




    def pin_decl(self):

        localctx = ExprParser.Pin_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pin_decl)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(ExprParser.PIN)
                self.state = 63
                self.pin_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(ExprParser.PIN)
                self.state = 65
                self.pin_name()
                self.state = 66
                self.match(ExprParser.DASH)
                self.state = 67
                self.net_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANCE(self):
            return self.getToken(ExprParser.INSTANCE, 0)

        def instance_name(self):
            return self.getTypedRuleContext(ExprParser.Instance_nameContext,0)


        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def block_ref(self):
            return self.getTypedRuleContext(ExprParser.Block_refContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_instance_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_decl" ):
                listener.enterInstance_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_decl" ):
                listener.exitInstance_decl(self)




    def instance_decl(self):

        localctx = ExprParser.Instance_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_instance_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ExprParser.INSTANCE)
            self.state = 72
            self.instance_name()
            self.state = 73
            self.match(ExprParser.COLON)
            self.state = 74
            self.block_ref()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Net_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pin_ref(self):
            return self.getTypedRuleContext(ExprParser.Pin_refContext,0)


        def DASH(self):
            return self.getToken(ExprParser.DASH, 0)

        def net_name(self):
            return self.getTypedRuleContext(ExprParser.Net_nameContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_net_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNet_decl" ):
                listener.enterNet_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNet_decl" ):
                listener.exitNet_decl(self)




    def net_decl(self):

        localctx = ExprParser.Net_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_net_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.pin_ref()
            self.state = 77
            self.match(ExprParser.DASH)
            self.state = 78
            self.net_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pin_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pin_name(self):
            return self.getTypedRuleContext(ExprParser.Pin_nameContext,0)


        def instance_name(self):
            return self.getTypedRuleContext(ExprParser.Instance_nameContext,0)


        def DOT(self):
            return self.getToken(ExprParser.DOT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_pin_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPin_ref" ):
                listener.enterPin_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPin_ref" ):
                listener.exitPin_ref(self)




    def pin_ref(self):

        localctx = ExprParser.Pin_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pin_ref)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.pin_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.instance_name()
                self.state = 82
                self.match(ExprParser.DOT)
                self.state = 83
                self.pin_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_block_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_ref" ):
                listener.enterBlock_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_ref" ):
                listener.exitBlock_ref(self)




    def block_ref(self):

        localctx = ExprParser.Block_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ExprParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_instance_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_name" ):
                listener.enterInstance_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_name" ):
                listener.exitInstance_name(self)




    def instance_name(self):

        localctx = ExprParser.Instance_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_instance_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ExprParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pin_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_pin_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPin_name" ):
                listener.enterPin_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPin_name" ):
                listener.exitPin_name(self)




    def pin_name(self):

        localctx = ExprParser.Pin_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pin_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(ExprParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Net_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_net_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNet_name" ):
                listener.enterNet_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNet_name" ):
                listener.exitNet_name(self)




    def net_name(self):

        localctx = ExprParser.Net_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_net_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ExprParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





