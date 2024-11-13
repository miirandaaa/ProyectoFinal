

import unittest
from src.usql_parser import parse_usql

class TestUsqlParser(unittest.TestCase):

    def test_consulta_seleccion_todo(self):
        consulta = "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 18"
        resultado = parse_usql(consulta) 
        self.assertEqual(resultado, "SELECT * FROM usuarios WHERE edad > 18")

    def test_consulta_seleccion_distintos(self):
        consulta = "TRAEME LOS_DISTINTOS nombre DE_LA_TABLA clientes DONDE ciudad = 'Madrid'"
        resultado = parse_usql(consulta)
        self.assertEqual(resultado, "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid'")

    def test_consulta_insercion(self):
        consulta = "METE_EN usuarios (nombre, edad) LOS_VALORES ('Juan', 25)"
        resultado = parse_usql(consulta)
        self.assertEqual(resultado, "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)")

    def test_consulta_actualizacion(self):
        consulta = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero'"
        resultado = parse_usql(consulta)
        self.assertEqual(resultado, "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'")

    def test_consulta_alterar_agregar(self):
        consulta = "CAMBIA_LA_TABLA empleados AGREGA_LA_COLUMNA direccion VARCHAR NO_NULO"
        resultado = parse_usql(consulta)
        self.assertEqual(resultado, "ALTER TABLE empleados ADD COLUMN direccion VARCHAR NOT NULL")

    def test_consulta_alterar_eliminar(self):
        consulta = "CAMBIA_LA_TABLA empleados ELIMINA_LA_COLUMNA direccion"
        resultado = parse_usql(consulta)
        self.assertEqual(resultado, "ALTER TABLE empleados DROP COLUMN direccion")

if __name__ == '__main__':
    unittest.main()
