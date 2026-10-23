import json
from pathlib import Path

ruta = Path(__file__).parent.parent
with open(ruta / "system" / "error.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    comando = data.get("error")
print(comando)
