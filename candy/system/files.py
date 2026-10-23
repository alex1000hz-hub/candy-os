from pathlib import Path


def rutas():
    ruta = Path(__file__).resolve().parent.parent

    return {
        "kernel": ruta / "inputs.py",
        "users": ruta / "usr",
        "apps": ruta / "apps",
        "binary": ruta / "bin",
        "logs": ruta / "#system" / "logs.json",
        "secion": ruta / "usr" / "session.session",
    }
