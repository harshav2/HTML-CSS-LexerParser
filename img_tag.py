import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'OTAG',
    'ETAG',
    'TAG_TEXT',
)

t_OTAG = r'<img'
t_ETAG = r'>'
t_TAG_TEXT = r'''[a-zA-Z_]+\s*=\s*["']\w+["']'''

t_ignore_COMMENT = r'\#.*'
t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

def p_check(p):
    '''check : OTAG TAG_TEXT ETAG'''
    print("HTML syntax is valid")

def p_error(p):
    print("HTML syntax is invalid")

parser = yacc.yacc()

valid = '<img src="img.png" width="200px" >'
print("Valid string:", valid)
parser.parse(valid, lexer=lexer)
print('Lexer output:')
lexer.input(valid)
for i in lexer:
    print(i)

print('\n'*2)

invalid = '<img src "img.png" width="200px" '
print("Invalid string:", invalid)
parser.parse(invalid, lexer=lexer)
print('Lexer output:')
lexer.input(invalid)
for i in lexer:
    print(i)


