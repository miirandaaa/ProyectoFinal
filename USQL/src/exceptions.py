class InvalidQueryError(Exception):
    pass

def validar_query(query):
    if not query:
        raise InvalidQueryError("La consulta no puede estar vacía")

# Probar la validación
if __name__ == '__main__':
    try:
        validar_query("")
    except InvalidQueryError as e:
        print(e)  # Debería imprimir: La consulta no puede estar vacía
