def translate_usql_to_sql(consulta_usql):
    consulta_sql = (
        consulta_usql.replace("TRAEME TODO", "SELECT *")
                     .replace("DE_LA_TABLA", "FROM")
                     .replace("DONDE", "WHERE")
                     .replace("METE_EN", "INSERT INTO")
                     .replace("LOS_VALORES", "VALUES")
                     .replace("ACTUALIZA", "UPDATE")
                     .replace("SETEA", "SET")
                     .replace("ORDENA POR", "ORDER BY")
                     .replace("COMO MUCHO", "LIMIT")
                     .replace("LOS_DISTINTOS", "SELECT DISTINCT")
                     .replace("CAMBIA_LA_TABLA", "ALTER TABLE")
                     .replace("AGREGA_LA_COLUMNA", "ADD COLUMN")
                     .replace("ELIMINA_LA_COLUMNA", "DROP COLUMN")
                     .replace("NO_NULO", "NOT NULL")
    )
    return consulta_sql.strip() + ";"

def translate_sql_to_usql(consulta_sql):
    consulta_usql = (
        consulta_sql.replace("SELECT *", "TRAEME TODO")
                     .replace("FROM", "DE_LA_TABLA")
                     .replace("WHERE", "DONDE")
                     .replace("INSERT INTO", "METE_EN")
                     .replace("VALUES", "LOS_VALORES")
                     .replace("UPDATE", "ACTUALIZA")
                     .replace("SET", "SETEA")
                     .replace("ORDER BY", "ORDENA POR")
                     .replace("LIMIT", "COMO MUCHO")
                     .replace("SELECT DISTINCT", "LOS_DISTINTOS")
                     .replace("ALTER TABLE", "CAMBIA_LA_TABLA")
                     .replace("ADD COLUMN", "AGREGA_LA_COLUMNA")
                     .replace("DROP COLUMN", "ELIMINA_LA_COLUMNA")
                     .replace("NOT NULL", "NO_NULO")
    )
    return consulta_usql.strip() + ";"
