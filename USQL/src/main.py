# from USQL.src.usql_parser import usql_parser

from USQL.src.fluent_api import USQLQuery

if __name__ == '__main__':
    # Probar el parser
    resultado = parser.parse("TRAEME TODO DE LA TABLA usuarios DONDE edad > 18")
    print("Resultado del parser:", resultado)

    # Probar el Fluent API
    query = USQLQuery().traeme().de_la_tabla("usuarios").donde("edad > 18").build()
    print("Resultado del Fluent API:", query)

    sql_query = "SELECT * FROM usuarios WHERE edad > 18"
    resultado = parser.parse(sql_query)
    print(resultado) 
