from pathlib import Path
import time
import subprocess
import sqlite3
import random
import string
import sys

# ============================================================
# RUTAS
# ============================================================
CANDY = Path(__file__).resolve().parent.parent

DATABASE = CANDY / "usr" / "candy.db"
INSTALACION = CANDY / "instalacion.py"
INICIO = CANDY / "inicio" / "inicio.py"
# ============================================================
# CONFIGURACIÓN
# ============================================================

ROLES_VALIDOS = ["dev", "root", "invitado", "tester"]

PASSWORDS_PROHIBIDAS = ["qwerty", "12345", "(salir)", "123", "1234", "12", "1"]


# ============================================================
# CREAR USUARIO
# ============================================================


def crear():

    print("¿Qué nombre de usuario creará?")
    nombre = input("name>> ").strip()

    print(f"¿Rol? Opciones: {ROLES_VALIDOS}")

    while True:

        rol = input("rol> ").strip()

        if rol not in ROLES_VALIDOS:
            print("Escoja un rol válido.")
            continue

        break

    print(f"Perfecto. Nombre: {nombre} | Rol: {rol}")

    time.sleep(2)

    print("¿Letra del particionado? " 'Ejemplo: C (se completará como "C:/>")')

    while True:

        letra = input("partition letter> ").strip()

        if len(letra) != 1:
            print("Solo un carácter, bro.")
            continue

        break

    print("Seleccionando partición...")
    time.sleep(2)

    print("Creando usuario...")
    time.sleep(2)

    print(f"""
    Usuario creado con los siguientes datos:
        Rol:    {rol}
        Nombre: {nombre}
        Letra:  {letra}
    """)

    password(rol, nombre, letra)


# ============================================================
# PASSWORD
# ============================================================


def password(rol, nombre, letra):

    print("Bienvenido al apartado de passwords.")

    print(f"Evite contraseñas como: " f"{PASSWORDS_PROHIBIDAS}")

    print('O escriba "sugerir" ' "para generar una automáticamente.")

    while True:

        pw = input(": ").strip()

        if pw in PASSWORDS_PROHIBIDAS:

            print(f'"{pw}" está prohibida. ' "Intente otra.")

            continue

        if pw == "sugerir":

            pw = "".join(random.choices(string.ascii_lowercase, k=4))

            print(f"Contraseña sugerida: {pw}")

        print(f"¿Confirma la contraseña " f"'{pw}'? (s/n)")

        confirmacion = input("s/n: ").strip().lower()

        if confirmacion == "s":

            _guardar_usuario(rol, nombre, letra, pw)

            return

        elif confirmacion == "n":

            print("Retornando...")

            continue


# ============================================================
# GUARDAR USUARIO
# ============================================================


def _guardar_usuario(rol, nombre, letra, pw):

    # Crear carpetas necesarias
    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    db = sqlite3.connect(DATABASE)

    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rol TEXT,
            nombre TEXT,
            letra TEXT,
            password TEXT
        )
    """)

    cursor.execute(
        """
        INSERT INTO users (
            rol,
            nombre,
            letra,
            password
        )
        VALUES (?, ?, ?, ?)
    """,
        (rol, nombre, letra, pw),
    )

    db.commit()
    db.close()

    print("Usuario guardado correctamente.")

    time.sleep(2)

    # Ejecutar instalacion.py
    subprocess.run([sys.executable, str(INICIO)])


# ============================================================
# INICIO
# ============================================================

crear()
