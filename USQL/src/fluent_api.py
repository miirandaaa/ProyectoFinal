class USQLQuery:
    def __init__(self):
        self.query = ""

    # Selección
    def traeme(self):
        self.query += "TRAEME "
        return self

    def todo(self):
        self.query += "TODO "
        return self

    def los_distintos(self, column):
        self.query += f"LOS DISTINTOS {column} "
        return self

    def de_la_tabla(self, table):
        self.query += f"DE LA TABLA {table} "
        return self

    def donde(self, condition):
        self.query += f"DONDE {condition} "
        return self

    # Inserción
    def mete_en(self, table, fields):
        self.query = f"METE EN {table} ({fields}) "
        return self

    def los_valores(self, values):
        self.query += f"LOS VALORES ({values}) "
        return self

    # Actualización
    def actualiza(self, table):
        self.query = f"ACTUALIZA {table} "
        return self

    def setea(self, condition):
        self.query += f"SETEA {condition} "
        return self

    # Alteración de tabla
    def cambia_la_tabla(self, table):
        self.query = f"CAMBIA LA TABLA {table} "
        return self

    def agrega_la_columna(self, column, column_type, constraint=""):
        self.query += f"AGREGA LA COLUMNA {column} {column_type} {constraint} "
        return self

    def elimina_la_columna(self, column):
        self.query += f"ELIMINA LA COLUMNA {column} "
        return self

    # Orden y Límite
    def ordena_por(self, column):
        self.query += f"ORDENA POR {column} "
        return self

    def limit(self, number):
        self.query += f"COMO MUCHO {number} "
        return self

    # Construcción final de la consulta
    def build(self):
        return self.query.strip() + ";"

# Prueba del Fluent API para cada tipo de consulta
if __name__ == '__main__':
    # Ejemplo de consulta de selección simple
    query1 = USQLQuery().traeme().todo().de_la_tabla("usuarios").donde("edad > 18").build()
    print(query1)  # "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"

    # Ejemplo de consulta de selección con "DISTINCT"
    query2 = USQLQuery().traeme().los_distintos("nombre").de_la_tabla("clientes").donde("ciudad = 'Madrid'").build()
    print(query2)  # "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"

    # Ejemplo de consulta de inserción
    query3 = USQLQuery().mete_en("usuarios", "nombre, edad").los_valores("'Juan', 25").build()
    print(query3)  # "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"

    # Ejemplo de consulta de actualización
    query4 = USQLQuery().actualiza("empleados").setea("salario = 3000").donde("puesto = 'ingeniero'").build()
    print(query4)  # "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"

    # Ejemplo de consulta de alteración para agregar una columna
    query5 = USQLQuery().cambia_la_tabla("empleados").agrega_la_columna("direccion", "VARCHAR", "NO NULO").build()
    print(query5)  # "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR NO NULO;"

    # Ejemplo de consulta de alteración para eliminar una columna
    query6 = USQLQuery().cambia_la_tabla("empleados").elimina_la_columna("direccion").build()
    print(query6)  # "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
