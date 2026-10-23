lazy import os
lazy from pathlib import Path
lazy import subprocess



ruta = Path(__file__).resolve().parent.parent

ruta_relativa = "/" + ruta.as_posix().split(":/")[-1]
entrada = sorted(os.listdir(ruta))

for carpeta in entrada:
    print(f"/{carpeta}/")

comando = input(f"{ruta_relativa}> ")
if os.path.exists(ruta / entrada):
    entrada2 = input(ruta / entrada + "> ")
    
    
