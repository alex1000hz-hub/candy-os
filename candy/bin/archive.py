
lazy import sys
lazy import os
lazy from pathlib import Path
lazy from rich.console import Console
lazy from rich.syntax import Syntax

path = Path(__file__).parent.parent
args = sys.argv[1:]
console = Console()

if len(args) < 4:
    print('Uso: code path = "archivo.py"')
    raise SystemExit(1)

if args[0] == "code" and args[1] == "path" and args[2] == "=":
    ruta = args[3]

    if ruta == "None":
        print("non path")
        raise SystemExit(1)

    archivo = path / ruta

    if archivo.is_file():
        sintaxis = Syntax.from_path(
            str(archivo),
            line_numbers=True,
            theme="monokai",
            word_wrap=True
        )

        console.print(sintaxis)
    else:
        print(f"Archivo no encontrado: {archivo}")
else:
    print("Sintaxis incorrecta")
