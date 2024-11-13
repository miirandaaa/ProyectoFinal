import sqlite3
from src.utils import translate_usql_to_sql, translate_sql_to_usql

class Database:
    def __init__(self, db_name='database_test_prog.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def ejecutar_consulta_usql(self, consulta_usql):
        """Traduce USQL a SQL y ejecuta la consulta en la base de datos."""
        consulta_sql = translate_usql_to_sql(consulta_usql)
        print(f"Ejecutando SQL: {consulta_sql}")
        self.cursor.execute(consulta_sql)
        if consulta_sql.strip().upper().startswith("SELECT"):
            return self.cursor.fetchall()
        self.conn.commit()
        return None

    def ejecutar_consulta_sql(self, consulta_sql):
        """Ejecuta directamente una consulta SQL en la base de datos."""
        print(f"Ejecutando SQL: {consulta_sql}")
        self.cursor.execute(consulta_sql)
        if consulta_sql.strip().upper().startswith("SELECT"):
            return self.cursor.fetchall()
        self.conn.commit()
        return None

    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos."""
        self.conn.close()

# Ejemplo de uso
if __name__ == '__main__':
    db = Database()

    # Ejecuta una consulta USQL
    consulta_usql = "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 18"
    resultados = db.ejecutar_consulta_usql(consulta_usql)
    for usuario in resultados:
        print(f'ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}')

    db.cerrar_conexion()

