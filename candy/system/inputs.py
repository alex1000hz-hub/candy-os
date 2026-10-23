import subprocess
import sys, json
from pathlib import Path
from outsecion import sesion  # type: ignore


def main():

    datos = sesion()

    rol = datos["rol"]
    particion = datos["particion"]
    password = datos["password"]
    nombre = datos["nombre"]
    ruta = Path(__file__).parent.parent
    system = ruta / "system"
    requested = system / "requested.py"
    request = system / "request.json"
    while True:

        entrada = input(particion + ":>/")
        app = Path(__file__).parent.parent / "apps"
        archivo = app / entrada
        ruta = Path(__file__).parent.parent
        with open(request, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "comando": entrada,
                    "args": [],
                    "usuario": nombre,
                    "from": 0.001,
                    "codigo": None,
                },
                f,
            )
        subprocess.run([sys.executable, requested])


main()
