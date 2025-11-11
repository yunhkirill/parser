grammar Expr;

prog: main_block (named_block)*;

main_block: MAIN NEWLINE block_content;
named_block: IDENTIFIER COLON NEWLINE block_content;

block_content: (element)*;

element: 
    pin_decl NEWLINE?
    | instance_decl NEWLINE?  
    | net_decl NEWLINE?
    ;

pin_decl: 
    PIN pin_name
    | PIN pin_name DASH net_name
    ;

instance_decl: INSTANCE instance_name COLON block_ref;

net_decl: pin_ref DASH net_name;

pin_ref: 
    pin_name
    | instance_name DOT pin_name
    ;

block_ref: IDENTIFIER;
instance_name: IDENTIFIER;
pin_name: IDENTIFIER;
net_name: IDENTIFIER;

// Ключевые слова
MAIN: 'main:';
PIN: 'pin';
INSTANCE: 'instance';
DOT: '.';
DASH: '-';
COLON: ':';

// Лексер
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NEWLINE: [\r\n]+;
WS: [ \t\r]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;