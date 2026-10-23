import sys
import os
args = sys.argv[1:]
if args[0] == "create" and args[1] == "new" and args[2] == "file":
    ruta = args[3]
    nombre = args[4]
    if os.path.exists(ruta + "/" + nombre).lstrip("/"):
        print("ruta existente")
    else:
        os.mkdir(ruta + "/" + nombre).lstrip