
lazy import os
lazy from pathlib import Path as path

def rutas():
    ruta = path(__file__).resolve().parent.parent
    usuario = ruta / "usr"

    return {
        "session": usuario / "session.json",
        "request": ruta / "system" / "request.json"
    }

def convierte(session, request):
    session = path(session)
    request = path(request)

    if session.exists():
        session.replace(session.with_suffix(".session"))

    if request.exists():
        request.replace(request.with_suffix(".system"))
if __name__ == "__main__":
    convierte(**rutas())
