# Entregable 1
# Maria Agustina Diaz 5424735-9
# Miranda Martinez 5338886-7

import csv
import random
from functools import reduce, wraps
import time
from itertools import chain

def tiempo_respuesta(func):
    """
    Decorador que mide el tiempo de respuesta de una función.
    Args:
        func (function): La función a la que se aplicará el decorador.
    Returns:
        function: La función envuelta con la medición de tiempo.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de respuesta: {end_time - start_time:.2f} segundos")
        return result
    return wrapper

def leer_preguntas(archivo_csv):
    """
    Generador que lee las preguntas desde un archivo CSV.
    Args:
        archivo_csv (str): El nombre del archivo CSV que contiene las preguntas.
    Yields:
        dict: Un diccionario con los datos de cada pregunta.
    """
    with open(archivo_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        yield from reader

def seleccionar_preguntas(preguntas, n=5):
    """
    Selecciona un número específico de preguntas aleatorias de una lista de preguntas.
    Args:
        preguntas (list): Lista de diccionarios que contienen las preguntas.
        n (int): Número de preguntas a seleccionar (por defecto es 5).
    
    Returns:
        list: Lista de preguntas seleccionadas aleatoriamente.
    """
    return random.sample(preguntas, n)

@tiempo_respuesta
def procesar_respuesta(pregunta, opciones):
    """
    Procesa la respuesta del usuario para una pregunta.
    Args:
        pregunta (dict): Un diccionario con los datos de la pregunta.
        opciones (list): Lista de opciones de respuesta para la pregunta.
    Returns:
        int: Puntaje obtenido por la respuesta (10 puntos por respuesta correcta, 0 por incorrecta).
    """
    respuesta = input(f"\nPregunta: {pregunta['Pregunta']}\n" + 
                      "\n".join([f"{i+1}. {op}" for i, op in enumerate(opciones)]) + 
                      "\nSelecciona la opción correcta (1, 2 o 3): ") 
    respuesta_correcta = opciones[int(respuesta) - 1]
    if respuesta_correcta == pregunta['Correcta']:
        print(f"¡Correcto!")
        return 10
    else:
        print(f"Incorrecto. La respuesta correcta era: {pregunta['Correcta']}.")
        return 0

def jugar(preguntas):
    """
    Controla el flujo del juego, procesando las respuestas del usuario y calculando el puntaje final.
    Args:
        preguntas (list): Lista de preguntas seleccionadas para el juego.
    Returns:
        int: Puntaje total obtenido en el juego.
    """
    opciones = lambda pregunta: [pregunta[f'Respuesta{i+1}'] for i in range(3)]
    respuestas = map(lambda p: procesar_respuesta(p, opciones(p)), preguntas)
    return reduce(lambda acc, x: acc + x, respuestas, 0) #acc : acumulador del puntaje

def main():
    """
    Función principal que maneja el juego.
    """
    preguntas = list(leer_preguntas('preguntas.csv'))
    preguntas_seleccionadas = seleccionar_preguntas(preguntas)
    puntaje_final = jugar(preguntas_seleccionadas)
    print(f"\nTu puntaje final es: {puntaje_final}")
    nuevo_juego = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    if nuevo_juego == 's':
        main()  # Llamada recursiva para volver a jugar
    else:
        print("¡Gracias por jugar!")
        print("\n")
        print("Se imprime la documentacion:")
        imprimir_documentacion([tiempo_respuesta, leer_preguntas, seleccionar_preguntas, procesar_respuesta, jugar, main, imprimir_documentacion])

def imprimir_documentacion(funciones):
    """
    Imprime el nombre y la documentación de una lista de funciones.
    Args:
        funciones (list): Lista de funciones a documentar.
    """
    def format_info(func):
        nombre = func.__name__
        docstring = func.__doc__
        return f"\nNombre: {nombre}\nDocumentación: {docstring}"
    
    documentacion = map(format_info, funciones)
    print('\n'.join(documentacion))

if __name__ == "__main__":
    main()
