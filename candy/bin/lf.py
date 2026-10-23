import sys
from pathlib import Path

ruta = Path(__file__).parent.parent
args = sys.argv[1:]

# Sin argumentos: listar toda la raíz de Candy
if not args:
    ruta2 = ruta
else:
    ruta2 = ruta / args[0]

if ruta2.is_dir():
    for archivo in ruta2.iterdir():
        print(archivo.name)
else:
    print(f"No existe la ruta: {ruta2}")
