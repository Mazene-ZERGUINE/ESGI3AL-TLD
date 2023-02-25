
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftorleftandnonassocEQUALSSUPleftPLUSMINUSleftTIMESDIVIDEDIVIDE EQUALS ET IF INFF ISEQUAL LACC LPAREN MINUS NAME NOTEQUAL NUMBER OU PLUS PRINT RACC RPAREN SEMI SUP THEN TIMES and orstart : bloc bloc : bloc statement\n    | statementstatement : NAME EQUALS expression SEMI   statement : IF expression THEN statement\n                  | IF expression THEN RACC bloc LACC  \n    \n    statement : PRINT LPAREN expression RPAREN SEMIexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression or expression\n                  | expression and expression\n                  | expression SUP expression\n                  | expression INFF expression\n                  | expression ISEQUAL expression\n                  | expression NOTEQUAL expression\n                  | expression ET expression\n                  | expression OU expression\n\n                  expression : MINUS expression expression : LPAREN expression RPARENexpression : NUMBERexpression : NAME'
    
_lr_action_items = {'NAME':([0,2,3,5,7,8,10,11,14,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,49,50,51,],[4,4,-3,13,-2,13,13,13,13,4,13,13,13,13,13,13,13,13,13,13,13,13,-4,-5,4,4,-7,-6,]),'IF':([0,2,3,7,16,32,33,34,49,50,51,],[5,5,-3,-2,5,-4,-5,5,5,-7,-6,]),'PRINT':([0,2,3,7,16,32,33,34,49,50,51,],[6,6,-3,-2,6,-4,-5,6,6,-7,-6,]),'$end':([1,2,3,7,32,33,50,51,],[0,-1,-3,-2,-4,-5,-7,-6,]),'LACC':([3,7,32,33,49,50,51,],[-3,-2,-4,-5,51,-7,-6,]),'EQUALS':([4,],[8,]),'MINUS':([5,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[10,10,18,10,10,-22,-23,10,18,10,10,10,10,10,10,10,10,10,10,10,10,-20,18,18,-8,-9,-10,-11,18,18,18,18,18,18,18,18,-21,]),'LPAREN':([5,6,8,10,11,14,17,18,19,20,21,22,23,24,25,26,27,28,],[11,14,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'NUMBER':([5,8,10,11,14,17,18,19,20,21,22,23,24,25,26,27,28,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'THEN':([9,12,13,29,35,36,37,38,39,40,41,42,43,44,45,46,47,],[16,-22,-23,-20,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,]),'PLUS':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[17,-22,-23,17,-20,17,17,-8,-9,-10,-11,17,17,17,17,17,17,17,17,-21,]),'TIMES':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[19,-22,-23,19,19,19,19,19,19,-10,-11,19,19,19,19,19,19,19,19,-21,]),'DIVIDE':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[20,-22,-23,20,20,20,20,20,20,-10,-11,20,20,20,20,20,20,20,20,-21,]),'or':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[21,-22,-23,21,-20,21,21,-8,-9,-10,-11,-12,-13,-14,21,21,21,21,21,-21,]),'and':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[22,-22,-23,22,-20,22,22,-8,-9,-10,-11,22,-13,-14,22,22,22,22,22,-21,]),'SUP':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[23,-22,-23,23,-20,23,23,-8,-9,-10,-11,23,23,None,23,23,23,23,23,-21,]),'INFF':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[24,-22,-23,24,-20,24,24,-8,-9,-10,-11,-12,-13,-14,24,24,24,24,24,-21,]),'ISEQUAL':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[25,-22,-23,25,-20,25,25,-8,-9,-10,-11,-12,-13,-14,25,25,25,25,25,-21,]),'NOTEQUAL':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[26,-22,-23,26,-20,26,26,-8,-9,-10,-11,-12,-13,-14,26,26,26,26,26,-21,]),'ET':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[27,-22,-23,27,-20,27,27,-8,-9,-10,-11,-12,-13,-14,27,27,27,27,27,-21,]),'OU':([9,12,13,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[28,-22,-23,28,-20,28,28,-8,-9,-10,-11,-12,-13,-14,28,28,28,28,28,-21,]),'SEMI':([12,13,15,29,35,36,37,38,39,40,41,42,43,44,45,46,47,48,],[-22,-23,32,-20,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,50,]),'RPAREN':([12,13,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-22,-23,-20,47,48,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-21,]),'RACC':([16,],[34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'bloc':([0,34,],[2,49,]),'statement':([0,2,16,34,49,],[3,7,33,3,7,]),'expression':([5,8,10,11,14,17,18,19,20,21,22,23,24,25,26,27,28,],[9,15,29,30,31,35,36,37,38,39,40,41,42,43,44,45,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> bloc','start',1,'p_start','calcMulrilignesVersAST.py',144),
  ('bloc -> bloc statement','bloc',2,'p_bloc','calcMulrilignesVersAST.py',151),
  ('bloc -> statement','bloc',1,'p_bloc','calcMulrilignesVersAST.py',152),
  ('statement -> NAME EQUALS expression SEMI','statement',4,'p_statement_assign','calcMulrilignesVersAST.py',160),
  ('statement -> IF expression THEN statement','statement',4,'p_if_els_statement','calcMulrilignesVersAST.py',165),
  ('statement -> IF expression THEN RACC bloc LACC','statement',6,'p_if_els_statement','calcMulrilignesVersAST.py',166),
  ('statement -> PRINT LPAREN expression RPAREN SEMI','statement',5,'p_statement_print','calcMulrilignesVersAST.py',176),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',181),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',182),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',183),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',184),
  ('expression -> expression or expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',185),
  ('expression -> expression and expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',186),
  ('expression -> expression SUP expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',187),
  ('expression -> expression INFF expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',188),
  ('expression -> expression ISEQUAL expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',189),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',190),
  ('expression -> expression ET expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',191),
  ('expression -> expression OU expression','expression',3,'p_expression_binop','calcMulrilignesVersAST.py',192),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','calcMulrilignesVersAST.py',199),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calcMulrilignesVersAST.py',203),
  ('expression -> NUMBER','expression',1,'p_expression_number','calcMulrilignesVersAST.py',207),
  ('expression -> NAME','expression',1,'p_expression_name','calcMulrilignesVersAST.py',211),
]
