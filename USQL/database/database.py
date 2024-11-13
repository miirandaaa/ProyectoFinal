import sqlite3
from utils import translate_usql_to_sql, translate_sql_to_usql

#crea la base de datos
conn = sqlite3.connect('database_test_prog.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

#datos de prueba
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Bob', 22)")
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Charlie', 17)")

conn.commit()

conn.close()