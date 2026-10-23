import json, os, subprocess, time, sys

args = sys.argv[1:]
if args[0] == "-p" and args[1] == "path" and args[2] == "=":
    ruta = args[3]
    if os.path.exists(ruta):
        print("moving request")
        time.sleep(0.01)
        print(f"EXISTS FILE {ruta}")
else:
    print("moving request")
    time.sleep(0.01)
    print("no file")
