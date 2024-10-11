import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'OTAG',
    'ETAG',
    'TAG_TEXT',
)

t_OTAG = r'<p>'
t_ETAG = r'</p>'
t_TAG_TEXT = r'([a-zA-Z_][a-zA-Z_0-9]*|\d+|\s+)+'

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

valid = '<p>This is a paragraph</p>'
print("Valid string:", valid)
parser.parse(valid, lexer=lexer)
print('Lexer output:')
lexer.input(valid)
for i in lexer:
    print(i)

print('\n'*2)

invalid = '<p>This is a paragraph/p>'
print("Invalid string:", invalid)
parser.parse(invalid, lexer=lexer)
print('Lexer output:')
lexer.input(invalid)
for i in lexer:
    print(i)


