import json, sys
from pathlib import Path
import sqlite3

rutas = Path(__file__).parent.parent
secion = rutas / "usr" / "session.json"
args = sys.argv[1:]
if args[0] == "-j":
    with open(secion, "r", encoding="utf-8") as f:
        sesion = json.load(f)
        nombre = sesion.get("usuario")
        id = sesion.get("rol")
        particion = sesion.get("particion")
        print(nombre)
        print("==========================")
        print(f"rol: {id}")
        print(f"particion: {particion}")
        print("==========================")
elif args[0] == "whoami" and args[1] == "-d":
    # aca se enumera todo el dataset
    con = sqlite3.connect(rutas / "usr" / "dandy.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM data")
    for row in cursor:
        print(row)
    con.close()
