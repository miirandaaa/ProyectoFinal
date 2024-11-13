from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    modules = ["USQL", "SistemaPedidos", "Trivia"]
    print("Rendering index.html with modules:", modules)  # Línea de depuración
    return render_template("index.html", modules=modules)

# Ruta para cada módulo que carga su documentación principal
@app.route('/module/<name>')
def module(name):
    # Definir el archivo de documentación principal para cada módulo
    doc_files = {
        "USQL": "Documentacion/DocumentacionUSQL/diccionario.html",
        "SistemaPedidos": "Documentacion/DocumentacionSistemaPedidos/index.html",
        "Trivia": "Documentacion/DocumentacionTrivia/trivia.html"
    }

    # Obtener la ruta del archivo HTML del módulo
    doc_path = doc_files.get(name)
    if doc_path and os.path.exists(doc_path):
        with open(doc_path, 'r', encoding='utf-8') as f:
            info = f.read()
    else:
        info = "No se encontró la documentación para este módulo."
    
    return render_template("module.html", name=name, info=info)

if __name__ == "__main__":
    app.run(debug=True)


