from pathlib import Path

ls = Path(__file__).parent.parent
import os

ruta = ls / "bin"
nombres = os.listdir(ruta)
for nombre in os.listdir(ruta):
    if nombre in ["candylib.py"] or nombre == "__pycache__":
        continue

    if nombre.endswith(".py"):
        print(nombre.removesuffix(".py"))
