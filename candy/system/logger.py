import json, time
from pathlib import Path

rutas = Path(__file__).parent.parent

requester = rutas / "system" / "request.json"

sytema_log = rutas / "#system" / "logmax.json"
with open(requester, "r", encoding="utf-8") as f:
    solicitud = json.load(f)
    comando = solicitud.get("comando")
    args = solicitud.get("args")
    usuario = solicitud.get("usuario")
    origen = solicitud.get("from")
    codigo = solicitud.get("codigo")
try:
    if "root" in comando:
        with open(sytema_log, "r", encoding="utf-8") as f:
            log = json.load(f)

        log.append(
            {
                "comando": comando,
                "args": args,
                "usuario": usuario,
                "from": origen,
                "codigo": codigo,
            }
        )

        with open(sytema_log, "w", encoding="utf-8") as f:
            json.dump(log, f, indent=4)
except Exception as e:
    import time
    import psutil

    print("KERNEL PANIC: CANDY ERROR")
    time.sleep(0.1)

    for proceso in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            nombre = proceso.info["name"] or ""

            if "python" in nombre.lower():
                print(
                    f"Python PID {proceso.info['pid']} | "
                    f"{' '.join(proceso.info['cmdline'] or [])}"
                )

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    errno = getattr(e, "errno2", None)

    if errno is not None:
        print(f"candy panic = {errno}")
