import pydoc
import sys
import argparse

# Añadir el directorio raíz del proyecto al path
sys.path.insert(0, "./")

def generar_documentacion(modulo, salida):
    # Genera la documentación del módulo especificado
    with open(salida, 'w') as archivo:
        archivo.write(pydoc.html.page(pydoc.render_doc(modulo, renderer=pydoc.plaintext)))
    print(f"Documentación generada para el módulo {modulo} en {salida}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar documentación HTML para un módulo.")
    parser.add_argument('--module', type=str, required=True, help="El módulo para documentar (e.g., USQL.src.main)")
    parser.add_argument('--output', type=str, required=True, help="Archivo de salida para la documentación HTML")

    args = parser.parse_args()
    generar_documentacion(args.module, args.output)
