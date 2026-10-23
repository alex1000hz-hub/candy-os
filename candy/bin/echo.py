import sys
import os
from pathlib import Path

ruta_base = Path(__file__).parent.parent
args = sys.argv[1:]

for argumento in args:
    ruta = Path(argumento)

    if ruta.exists() and ruta.is_dir():
        print(*os.listdir(ruta), sep="\n")
    else:
        print()

print(*args)
