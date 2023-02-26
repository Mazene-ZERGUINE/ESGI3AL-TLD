import graphviz
from genereTreeGraphviz2 import printTreeGraph
import sys 

# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.
# -----------------------------------------------------------------------------

############################## reserved words #############################
reserved = {
    'print' : 'PRINT',
    'if' : 'IF' ,
    'OR' : 'or' ,
    'AND' : 'and',
    'if' : 'IF' , 
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'for' : 'FOR',
    'to' : 'TO'
}

############################## Tokens #############################

tokens = [
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS', "ISEQUAL", "NOTEQUAL",
    'LPAREN','RPAREN', 'SEMI', "ET" , "OU",'RACC' , 'LACC', 'THEN' , "COMMA",
    'SUP' , "INFF" ] + list(reserved.values())
# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMI    = r';'
t_SUP = r'>'
t_INFF = r'<'
t_ISEQUAL = r'=='
t_NOTEQUAL = r'!='
t_ET = r'&' 
t_OU = r'\|'
t_RACC = r'{'
t_LACC = r'}'
t_THEN = r'->'
t_COMMA = r',' 



def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

############################## lex #############################


import ply.lex as lex
lex.lex()


############################## evaluations #############################

precedence = (
 
    ('left','or'),
    ('left','and'),
    ('nonassoc','EQUALS','SUP'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
 
    )
 
names = {}

def evalInst(p):
    # Normalement faire que 
    print('EvalInst de ', p)

    if p == 'empty' : return 

    if type(p) != tuple : 
        print("inst non tuple")
        return 

    if p[0] == 'bloc':
        evalInst(p[1])
        evalInst(p[2])
        return 

    if p[0] == 'ASSIGN':names[p[1]] = evalExpr(p[2])
    if p[0] == 'PRINT':print("CALC >> ", evalExpr(p[1]))
    if p[0] == "IF": eval_if_elseif_else(p)
    if p[0] == "FOR" : eval_for_loop(p)

            

    return 'undifiend'

def evalExpr(p):
    if type(p) == int : return p
    if type(p) == str : return names[p]
    if type(p) == tuple:
        if p[0] == '+' : return evalExpr(p[1])+evalExpr(p[2])
        if p[0] == '-' : return evalExpr(p[1])-evalExpr(p[2])
        if p[0] == '*' : return evalExpr(p[1])*evalExpr(p[2])
        if p[0] == '/' : return evalExpr(p[1])/evalExpr(p[2])
        if p[0] == 'AND' : return evalExpr(p[1]) and evalExpr(p[2])
        if p[0] == 'OR' : return evalExpr(p[1]) or evalExpr(p[2])
        if p[0] == '>' : return evalExpr(p[1]) > evalExpr(p[2])
        if p[0] == '<' : return evalExpr(p[1]) < evalExpr(p[2])
        if(p[0] == "==") : return evalExpr(p[1]) == evalExpr(p[2])
        if(p[0] == "!=") : return evalExpr(p[1]) != evalExpr(p[2])
        if(p[0] == "&") : return evalExpr(p[1]) & evalExpr(p[2])
        if(p[0] == "|") : return evalExpr(p[1]) | evalExpr(p[2])


        
    return 'undifiedn'

def eval_for_loop(p):
    evalInst(p[1])
    if names[p[1][1]] < p[2] :
        while names[p[1][1]] <= p[2] :
            evalInst(p[4])
            evalInst(p[3])
    if names[p[1][1]] > p[2] :
        while names[p[1][1]] >= p[2] :
            evalInst(p[4])
            evalInst(p[3])    


def eval_if_elseif_else(p) : 
    if (len(p) == 3) : 
        if evalExpr(p[1]) == True : return evalInst(p[2])
    elif len(p) == 4:
        if evalExpr(p[1]) == True : return evalInst(p[2]) 
        else : return evalInst(p[3])
    else :
        if evalExpr(p[1]) == True : return evalInst(p[2])
        elif evalExpr(p[3]) == True : return evalInst(p[4]) 
        else : return evalInst(p[5])

############################## gramar and parsing #############################


def p_start(p):
    '''start : bloc '''
    p[0] = p[1]
    #printTreeGraph(p[1])
    evalInst(p[1])


def p_bloc(p):
    """bloc : bloc statement
    | statement"""
    if len(p) == 3:
        p[0] = ('bloc', p[1], p[2])
    else:
        p[0] = ('bloc', p[1], 'empty')


def p_statement_assign(p):
    '''statement : NAME EQUALS expression SEMI 
                 | NAME EQUALS expression '''
    p[0] = ('ASSIGN', p[1], p[3])


def p_for_loop(p):
    ''' statement : FOR LPAREN statement TO NUMBER COMMA statement RPAREN RACC bloc LACC '''
    p[0] = ('FOR' , p[3] , p[5] , p[7] , p[10])
        
        
def p_if_els_statement(p):
    ''' statement : IF expression THEN statement
                  | IF expression THEN RACC bloc LACC  
                  | IF expression THEN RACC bloc LACC ELSEIF expression THEN RACC bloc LACC ELSE RACC bloc LACC 
                  | IF expression THEN RACC bloc LACC ELSE RACC bloc LACC 
    
    '''
    if len(p) == 5 : p[0] = ('IF' , p[2] , p[4]) 
    if len(p) == 7 : p[0] = ('IF' , p[2], p[5]) 
    if len(p) == 17 : p[0] = ('IF' , p[2] , p[5] , p[8] , p[11] , p[15])
    if len(p) == 11 : p[0] = ('IF' , p[2] , p[5] , p[9])
        
def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN SEMI'
    p[0] = ('PRINT', p[3])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression or expression
                  | expression and expression
                  | expression SUP expression
                  | expression INFF expression
                  | expression ISEQUAL expression
                  | expression NOTEQUAL expression
                  | expression ET expression
                  | expression OU expression

                  '''
    p[0] = (p[2], p[1] , p[3])


def p_expression_uminus(p):
    'expression : MINUS expression '
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : NAME'
    p[0] = p[1]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

import ply.yacc as yacc
yacc.yacc()


############################## output #############################


file = open(sys.argv[1] , "r")
s = file.read() 
yacc.parse(s)
# s = ''
# while 1 :

#     s = input('calc >>> ')
#     if s == "exit" :
#         exit()
#     elif s == "" :
#         pass
#     #s='print(1+2);x=4;x=x+1;'
#     #s='x=4;x=x+1;print(x+1);'
#     yacc.parse(s)


# 2h arret cours 