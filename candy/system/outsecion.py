import json
import files  # type: ignore


def sesion():

    rutas = files.rutas()

    with open(rutas["secion"], "r", encoding="utf-8") as f:
        datos = json.load(f)

    return {
        "rol": datos.get("rol"),
        "particion": datos.get("particion"),
        "password": datos.get("password"),
        "nombre": datos.get("nombre"),
    }
