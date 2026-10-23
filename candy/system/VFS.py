from pathlib import Path

CANDY = Path(__file__).resolve().parent.parent


def ruta(path):
    return CANDY / path.removeprefix("/candy/").lstrip("/")
