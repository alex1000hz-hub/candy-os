import sys
import os
import subprocess
from pathlib import Path
import json

rutas = Path(__file__).resolve().parent.parent
bin = rutas / "bin"
session = rutas / "usr" / "session.json"
request = rutas / "system" / "request.json"
requester = rutas / "system" / "requested.py"

with open(session, "r", encoding="utf-8") as f:
    sesion = json.load(f)
    usuario = sesion.get("usuario")
    rol = sesion.get("rol")

args = sys.argv[1:]

if args:
    ruta = args[0]
    directorio = (rutas / ruta).resolve()

    # Evita salir del directorio raíz de Candy
    if not directorio.is_relative_to(rutas.resolve()):
        print("Acceso fuera de Candy OS denegado.")

    elif directorio.is_dir():

        while True:
            try:
                a = input(f"{ruta}>> ").strip()

                if not a:
                    continue

                if a in ("exit", "quit"):
                    break

                elif a == "list files":
                    for archivo in directorio.iterdir():
                        print(archivo.name)

                elif a == "pwd":
                    print(directorio)

                else:
                    # Solo acepta nombres simples de comandos
                    if not a.isidentifier():
                        print("Nombre de comando inválido.")
                        continue

                    archivo = bin / f"{a}.py"

                    if archivo.is_file():
                        with open(request, "w", encoding="utf-8") as f:
                            json.dump(
                                {
                                    "comando": a,
                                    "args": [],
                                    "usuario": usuario,
                                    "from": 0.002,
                                    "codigo": None,
                                },
                                f,
                            )

                        subprocess.run([sys.executable, str(requester)], check=False)
                    else:
                        print(f"Comando no encontrado: {a}")

            except (EOFError, KeyboardInterrupt):
                print()
                break

    else:
        print(f"No existe el directorio {ruta}")

else:
    print("No se especificó el directorio")
