#diccionario.py

#Traducciones de SQL a USQL
sql_usql = {
    "SELECT": "TRAEME",
    "*": "TODO",
    "FROM": "DE LA TABLA",
    "WHERE": "DONDE",
    "GROUP BY": "AGRUPANDO POR",
    "JOIN": "MEZCLANDO",
    "ON": "EN",
    "DISTINCT": "LOS DISTINTOS",
    "COUNT": "CONTANDO",
    "INSERT INTO": "METE EN",
    "VALUES": "LOS VALORES",
    "UPDATE": "ACTUALIZA",
    "SET": "SETEA",
    "DELETE FROM": "BORRA DE LA",
    "ORDER BY": "ORDENA POR",
    "LIMIT": "COMO MUCHO",
    "HAVING": "WHERE DEL GROUP BY",
    "EXISTS": "EXISTE",
    "IN": "EN ESTO:",
    "BETWEEN": "ENTRE",
    "LIKE": "PARECIDO A",
    "IS NULL": "ES NULO",
    "ALTER TABLE": "CAMBIA LA TABLA",
    "ADD COLUMN": "AGREGA LA COLUMNA",
    "DROP COLUMN": "ELIMINA LA COLUMNA",
    "CREATE TABLE": "CREA LA TABLA",
    "DROP TABLE": "TIRA LA TABLA",
    "DEFAULT": "POR DEFECTO",
    "UNIQUE": "UNICO",
    "PRIMARY KEY": "CLAVE PRIMA",
    "FOREIGN KEY": "CLAVE REFERENTE",
    "NOT NULL": "NO NULO",
    "CAST": "TRANSFORMA A",
}

#Traduccion de USQL a SQL
usql_sql_mapping = {v: k for k, v in sql_usql.items()}

sql_usql_mapping=sql_usql
