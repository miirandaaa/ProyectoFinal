import pydoc
import sys
sys.path.insert(0, "./")  # Añadir el directorio raíz del proyecto al path
pydoc.writedoc('USQL.src.main')
