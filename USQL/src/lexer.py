# lexer.py
import ply.lex as lex
from USQL.src.diccionario import sql_usql, usql_sql_mapping, sql_usql_mapping

# Tokens en base al diccionario
tokens = [key.replace(" ", "_").replace("(", "").replace(")", "") for key in sql_usql.keys() if key != "*"]

# Tokens específicos
tokens.extend([
    'ASTERISK', 'ID', 'NUMBER', 'GT', 'GE', 'LT', 'LE', 'EQUAL', 'SEMICOLON',
    'LPAREN', 'RPAREN', 'COMMA', 'AND', 'LOS_DISTINTOS', 'AGRUPANDO_POR', 'BORRA_DE_LA', 'CAMBIA_LA_TABLA',
    'AGREGA_LA_COLUMNA', 'ELIMINA_LA_COLUMNA', 'NO_NULO', 'STRING', 'OR', 'FLOAT', 'DATE', 'VARCHAR', 'INT', 'MEZCLANDO', 'ENTRE', 'EN', 'DOT'
])

# Tokens adicionales específicos
tokens.extend(['TRAEME', 'TODO', 'DE_LA_TABLA', 'DONDE', 'CONTANDO', 'METE_EN', 'LOS_VALORES', 'ACTUALIZA', 'SETEA'])

# Expresiones regulares
t_TRAEME = r'TRAEME'
t_EN = r'EN'
t_TODO = r'TODO'
t_DE_LA_TABLA = r'DE_LA_TABLA'
t_DONDE = r'DONDE'
t_CONTANDO = r'CONTANDO'
t_METE_EN = r'METE_EN'
t_LOS_VALORES = r'LOS_VALORES'
t_ACTUALIZA = r'ACTUALIZA'
t_SETEA = r'SETEA'
t_MEZCLANDO = r'MEZCLANDO'
t_ENTRE = r'ENTRE'

# Expresiones regulares
t_LOS_DISTINTOS = r'LOS_DISTINTOS'
t_AGRUPANDO_POR = r'AGRUPANDO_POR'
t_BORRA_DE_LA = r'BORRA_DE_LA'
t_CAMBIA_LA_TABLA = r'CAMBIA_LA_TABLA'
t_AGREGA_LA_COLUMNA = r'AGREGA_LA_COLUMNA'
t_ELIMINA_LA_COLUMNA = r'ELIMINA_LA_COLUMNA'
t_NO_NULO = r'NO_NULO'

# Definimos los patrones de los tokens basados en el diccionario, excepto "*"
for key in sql_usql.keys():
    token_name = key.replace(" ", "_").replace("(", "").replace(")", "")
    if key != "*":  # Excluir "*"
        globals()[f't_{token_name}'] = r'\b' + key + r'\b'

# Tokens adicionales simbolos
t_INT = r'INT'
t_VARCHAR = r'VARCHAR'
t_FLOAT = r'FLOAT'
t_DATE = r'DATE'
t_ASTERISK = r'\*'
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_EQUAL = r'='
t_SEMICOLON = r';'
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_AND = r'AND'
t_OR = r'OR'


t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in tokens:  
        t.type = t.value.upper()
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    return t

def t_STRING(t):
    r'\'([^\\\']|\\.)*\'|"([^\\\"]|\\.)*"' 
    t.value = t.value[1:-1]  
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter no válido: '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

def t_eof(t):
    return None


lexer = lex.lex()

if __name__ == '__main__':
    data = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18"
    lexer.input(data)
    for tok in lexer:
        print(tok)
