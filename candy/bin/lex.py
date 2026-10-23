import sys
from pathlib import Path

ruta = Path(__file__).resolve().parent.parent
temp = ruta / "temp"
args = sys.argv[1:]

if not args:
    print("no command provided")
    sys.exit(1)

if args[0] == "!":
    if len(args) < 2:
        print("missing command")
        sys.exit(1)

    comando = args[1]

    if comando == "printer" and len(args) >= 4 and args[2] == "func":
        archivo = temp / f"{args[3]}.json"

        if archivo.exists():
            with open(archivo, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print("no func available")

    elif comando == "save" and len(args) >= 4:
        guardar = args[2]
        archivo = temp / f"{guardar}.json"

        if archivo.exists():
            print("file already exists")
        else:
            temp.mkdir(parents=True, exist_ok=True)
            with open(archivo, "w", encoding="utf-8") as f:
                f.write(args[3])

            print("saved")

    else:
        print("unknown command")
