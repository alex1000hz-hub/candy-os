lazy from pathlib import Path
lazy import sqlite3
lazy import json
lazy import time
lazy import subprocess
lazy import sys
lazy import os
def rutas():

    root = Path(__file__).resolve().parent.parent

    ruta_usuario = root / "usr" / "candy.db"
    session = root / "usr" / "session.json"
    system = root / "system"

    return {
        "root": root,
        "ruta_usuario": ruta_usuario,
        "session": session,
        "system": system,
    }


def sacarSQL(salidarutas):

    conexion = sqlite3.connect(salidarutas["ruta_usuario"])
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM users")

    datos = cursor.fetchall()

    conexion.close()

    return datos


def entrada_inicio(datos, salidarutas):

    print("\n=== USUARIOS DISPONIBLES ===")

    for numero, usuario in enumerate(datos, start=1):
        print(f"[{numero}] {usuario[2]}")

    while True:

        try:

            seleccion = int(input("\nSeleccione el usuario: "))

            if 1 <= seleccion <= len(datos):
                break

            print("Usuario inexistente.")

        except ValueError:

            print("Introduzca un número válido.")

    usuario = datos[seleccion - 1]

    # users:
    # id | rol | nombre | letra | password

    usuario_id = usuario[0]
    rol = usuario[1]
    nombre = usuario[2]
    particion = usuario[3]
    password = usuario[4]

    print(f"\nUsuario seleccionado: {nombre}")

    contraseña = input("Contraseña: ")

    if contraseña != password:

        print("Contraseña incorrecta.")

        return False

    print("Inicio de sesión correcto.")
    time.sleep(3)
    escritura(salidarutas, nombre, particion, rol)

    iniciar_kernel(salidarutas)

    return True


def escritura(salidarutas, nombre, particion, rol):

    datos = {"usuario": nombre, "particion": particion, "rol": rol, "unix": time.time()}

    with open(salidarutas["session"], "w", encoding="utf-8") as archivo:

        json.dump(datos, archivo, indent=4)
    subprocess.run([sys.executable, salidarutas["system"] / "transformador.py"])

def iniciar_kernel(salidarutas):

    kernel = salidarutas["system"] / "inputs.py"
    
    subprocess.run([sys.executable, str(kernel)])


salidarutas = rutas()

datos = sacarSQL(salidarutas)

entrada_inicio(datos, salidarutas)
