
lazy import sys
lazy import os, json, time
lazy from pathlib import Path
lazy from subprocess import run


def rutas():
    root = Path(__file__).resolve().parent.parent
    request = root / "system" / "requested.py"
    secion = root / "usr" / "session.session"
    ruta_solicitud = root / "system" / "request.json"
    configs = root / "#system" / "configs.json"
    transformer = root / "system" / "transformador.py"

    if os.path.exists(configs):
        with open(configs, "r", encoding="utf-8") as f:
            configuracion = json.load(f)
            advanced = configuracion.get("advanced")

            if advanced is True:
                printear = "all"
            else:
                printear = "none"
    else:
        printear = None

    with open(secion, "r", encoding="utf-8") as f:
        sesion = json.load(f)
        usuario = sesion.get("usuario")
        rol = sesion.get("rol")

    return rol, usuario, ruta_solicitud, request, printear, transformer


def entrada(rol, usuario, ruta_solicitud, request, printear, transformer):

    while True:
        entrada_usuario = input(f"{usuario}¨¨-CANDY-¨¨{rol}->")

        if not entrada_usuario.strip():
            continue

        if "|" in entrada_usuario:
            partes = entrada_usuario.split("|", 1)
            comando_base = partes[0].strip().split()
            comando2 = partes[1].strip().split()

            if not comando_base or not comando2:
                print("Error: faltan comandos.")
                continue

            solicitud = {
                "comando": comando_base[0],
                "args": comando_base[1:],
                "usuario": usuario,
                "from": 0.002,
                "codigo": None,
                "comando2": comando2[0],
                "args2": comando2[1:]
            }

        else:
            partes = entrada_usuario.split()
            comando_base = partes[0]
            args = partes[1:]

            solicitud = {
                "comando": comando_base,
                "args": args,
                "usuario": usuario,
                "from": 0.002,
                "codigo": None,
            }

        if printear == "all":
            mensajes = [
                "REQUESTING SEND TO KERNEL",
                "INITIALIZING KERNEL REQUEST",
                "CHECKING SYSTEM STATUS",
                "LOADING KERNEL CONFIG",
                "VERIFYING KERNEL INTEGRITY",
                "ACCESSING /system/requested",
                "REQUEST SENT -> KERNEL",
                "WAITING FOR KERNEL RESPONSE",
                "CHECKING VFS",
                "LOADING SYSTEM MODULES",
                "CHECKING PERMISSIONS",
                "VERIFYING USER SESSION",
                "SESSION FOUND",
                f"USER: {usuario}",
                f"ROLE: {rol}",
                "REQUEST AUTHORIZED",
                "KERNEL CHANNEL -> ONLINE",
                "PROCESSING REQUEST",
            ]

            for mensaje in mensajes:
                print(mensaje)
                time.sleep(0.01)

        with open(ruta_solicitud, "w", encoding="utf-8") as f:
            json.dump(solicitud, f, indent=4)

        run([sys.executable, str(transformer)], check=True)

        if os.path.exists(ruta_solicitud): 
            run([sys.executable, str(request)], check=True)


rol, usuario, ruta_solicitud, request, printear, transformer = rutas()
entrada(rol, usuario, ruta_solicitud, request, printear, transformer)
