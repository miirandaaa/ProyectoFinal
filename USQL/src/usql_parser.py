import ply.yacc as yacc
from USQL.src.lexer import tokens
from USQL.src.diccionario import sql_usql_mapping


def p_consulta(p):
    '''consulta : consulta_seleccion
                | consulta_insercion
                | consulta_borrar
                | consulta_actualizar
                | consulta_alterar'''
    p[0] = p[1]

def p_consulta_seleccion(p):
    '''consulta_seleccion : TRAEME TODO DE_LA_TABLA nombre_tabla DONDE condicion
                          | TRAEME LOS_DISTINTOS nombre_columna DE_LA_TABLA nombre_tabla DONDE condicion
                          | TRAEME CONTANDO LPAREN TODO RPAREN DE_LA_TABLA nombre_tabla AGRUPANDO_POR nombre_columna HAVING condicion
                          | TRAEME TODO DE_LA_TABLA nombre_tabla MEZCLANDO nombre_tabla EN nombre_columna EQUAL nombre_columna DONDE condicion'''
    if len(p) == 7: 
        p[0] = f"SELECT * FROM {p[4]} WHERE {p[6]}"
    elif len(p) == 8:  
        p[0] = f"SELECT DISTINCT {p[3]} FROM {p[5]} WHERE {p[7]}"
    elif len(p) == 12:  
        p[0] = f"SELECT COUNT(*) FROM {p[7]} GROUP BY {p[9]} HAVING {p[11]}"
    elif len(p) == 10:  
        p[0] = f"SELECT * FROM {p[4]} JOIN {p[6]} ON {p[8]} WHERE {p[10]}"

def p_consulta_insercion(p):
    '''consulta_insercion : METE_EN nombre_tabla LPAREN lista_columna RPAREN LOS_VALORES LPAREN lista_valores RPAREN'''
    p[0] = f"INSERT INTO {p[2]} ({p[4]}) VALUES ({p[8]})"

def p_consulta_borrar(p):
    '''consulta_borrar : BORRA_DE_LA nombre_tabla DONDE condicion'''
    p[0] = f"DELETE FROM {p[2]} WHERE {p[4]}"

def p_consulta_actualizar(p):
    '''consulta_actualizar : ACTUALIZA nombre_tabla SETEA nombre_columna EQUAL valor DONDE condicion'''
    p[0] = f"UPDATE {p[2]} SET {p[4]} = {p[6]} WHERE {p[8]}"

def p_consulta_alterar(p):
    '''consulta_alterar : CAMBIA_LA_TABLA nombre_tabla AGREGA_LA_COLUMNA nombre_columna tipo_dato NO_NULO
                        | CAMBIA_LA_TABLA nombre_tabla ELIMINA_LA_COLUMNA nombre_columna'''
    if len(p) == 7:  
        p[0] = f"ALTER TABLE {p[2]} ADD COLUMN {p[4]} {p[5]} NOT NULL"
    else:  
        p[0] = f"ALTER TABLE {p[2]} DROP COLUMN {p[4]}"

def p_tipo_dato(p):
    '''tipo_dato : INT
                 | VARCHAR
                 | FLOAT
                 | DATE
                 | STRING'''  
    p[0] = p[1]

def p_elementos(p):
    '''elementos : TODO
                 | LOS_DISTINTOS nombre_columna
                 | CONTANDO LPAREN TODO RPAREN'''
    if p[1] == "TODO":
        p[0] = '*'
    elif p[1] == "LOS_DISTINTOS":
        p[0] = f'DISTINCT {p[2]}'
    elif p[1] == "CONTANDO":
        p[0] = 'COUNT(*)'

def p_nombre_tabla(p):
    '''nombre_tabla : ID'''
    p[0] = p[1]

def p_lista_columna(p):
    '''lista_columna : nombre_columna COMMA lista_columna
                     | nombre_columna'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"

def p_lista_valores(p):
    '''lista_valores : valor COMMA lista_valores
                     | valor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"

def p_valores(p):
    '''valores : STRING
               | NUMBER'''
    if isinstance(p[1], str):
        p[0] = f"'{p[1]}'" 
    else:
        p[0] = p[1]

def p_nombre_columna(p):
    '''nombre_columna : ID
                      | ID DOT ID'''  
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}.{p[3]}"

def p_condicion(p):
    ''' condicion : expresion 
                  | expresion AND condicion '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f'{p[1]} AND {p[3]}'

def p_expresion(p):
    '''expresion : nombre_columna comparador valor
                 | nombre_columna ENTRE valor AND valor'''
    if len(p) == 4:
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    else:
        p[0] = f"{p[1]} BETWEEN {p[3]} AND {p[5]}"

def p_comparador(p):
    '''comparador : GT
                  | LT
                  | EQUAL
                  | GE
                  | LE'''
    p[0] = p[1]

def p_valor(p):
    '''valor : NUMBER
             | STRING'''
    if isinstance(p[1], str):
        p[0] = f"'{p[1]}'" 
    else:
        p[0] = p[1]

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}', línea {p.lineno}")
    else:
        print("Error de sintaxis al final de la entrada")

parser = yacc.yacc(debug=True)

def parse_usql(consulta):
    resultado = parser.parse(consulta)
    return resultado

def parse_sql(consulta):
    for sql, usql in sql_usql_mapping.items():
        consulta = consulta.replace(sql, usql)
    return consulta

if __name__ == '__main__':
    consultas = [
        "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 18",
        "TRAEME LOS_DISTINTOS nombre DE_LA_TABLA usuarios DONDE pais = 'Uruguay'",
        "METE_EN usuarios (nombre, edad) LOS_VALORES ('Juan', 25)",
        "BORRA_DE_LA usuarios DONDE edad < 18",
        "ACTUALIZA usuarios SETEA nombre = 'Maria' DONDE id = 1",
        "CAMBIA_LA_TABLA usuarios AGREGA_LA_COLUMNA nombre STRING NO_NULO",
        "CAMBIA_LA_TABLA usuarios ELIMINA_LA_COLUMNA edad",
        "BORRA_DE_LA clientes DONDE edad ENTRE 18 AND 25",
        "TRAEME CONTANDO(TODO) DE_LA_TABLA ventas AGRUPANDO_POR producto DONDE COUNT(*) > 5",
        "TRAEME TODO DE_LA_TABLA pedidos MEZCLANDO clientes EN pedidos.cliente = clientes.id DONDE clientes.ciudad = 'Barcelona'"
    ]

    for consulta in consultas:
        resultado = parse_usql(consulta)
        print(f"Consulta: {consulta} \nResultado: {resultado}\n")
