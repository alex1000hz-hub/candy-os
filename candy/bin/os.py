import subprocess
from pathlib import Path

rutas = Path(__file__).parent.parent
inputs = rutas / "system" / "inputs.py"
subprocess.run(["python", inputs])
