import sys, json, subprocess
from pathlib import Path

args = sys.argv[1:]


indent = 0
codigo = []

for arg in args:
    if arg == ":":
        indent += 1
        continue

    if arg == "end":
        indent -= 1
        continue
    codigo.append("    " * indent + arg)
    request = {
        "codigo": codigo,
        "usuario": "alexander",
        "from": 0.003,
    }
    rutas = Path(__file__).parent.parent
    requestpath = rutas / "system" / "request.json"
    with open(requestpath, "w", encoding="utf-8") as f:
        json.dump(request, f)
    subprocess.run([sys.executable, rutas / "system" / "requested.py"])
