import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'LBRACK',
    'RBRACK',
    'CSS_SEL',
    'CSS_CONT',
)

t_LBRACK=r'\{'
t_RBRACK=r'\}'
t_CSS_SEL=r'(((\.[a-zA-Z0-9_-]+)|(\#[a-zA-Z0-9_-]+))| \*)+ '
t_CSS_CONT=r'(([a-zA-Z]+):[a-zA-Z0-9_-]+ \,)* ([a-zA-Z]+):([a-zA-Z0-9_-]+);'

t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

def p_check(p):
    '''check : CSS_SEL int'''
    pass
def p_check1(p):
    '''int : LBRACK CSS_CONT RBRACK'''
    print("CSS syntax is valid")
def p_error(p):
    print("CSS syntax is invalid")

parser = yacc.yacc()

valid = '.class {color:red;}'
print("Valid string:", valid)
parser.parse(valid, lexer=lexer)
print('Lexer output:')
lexer.input(valid)
for i in lexer:
    print(i)

print('\n'*2)

invalid = '.class {color:red}'
print("Invalid string:", invalid)
parser.parse(invalid, lexer=lexer)
print('Lexer output:')
lexer.input(invalid)
for i in lexer:
    print(i)


