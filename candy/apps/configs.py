import json
import sys
from pathlib import Path
import subprocess
import os


def configs_menu():
    rutas = Path(__file__).parent.parent
    archivo = rutas / "#system" / "configs.json"

    while True:
        print()
        print("=== CANDY CONFIGS ===")
        print("advanced => True / False")
        print("return   => volver")
        print("delete   => borrar configuración")
        print()

        opcion = input("configs => ").strip()

        if opcion == "True":
            configuracion = {"advanced": True}

            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(configuracion, f, indent=4)

            print("ADVANCED -> ENABLED")

        elif opcion == "False":
            configuracion = {"advanced": False}

            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(configuracion, f, indent=4)

            print("ADVANCED -> DISABLED")

        elif opcion == "delete":
            if archivo.exists():
                os.remove(archivo)
                print("CONFIGURATION -> DELETED")
            else:
                print("CONFIGURATION -> NOT FOUND")

        elif opcion == "return":
            subprocess.run([sys.executable, str(rutas / "system" / "inputs.py")])
            return

        else:
            print("UNKNOWN CONFIG")


configs_menu()
