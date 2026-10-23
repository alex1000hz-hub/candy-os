import os
import subprocess
import sys
import json
from pathlib import Path

rutas = Path(__file__).resolve().parent.parent
requester = rutas / "system" / "request.system"
logerr = rutas / "system" / "logger.py"
bin = rutas / "bin"
error = rutas / "system" / "error.json"


def request():
    error_solicitud = None

    if not requester.is_file():
        return

    try:
        with open(requester, "r", encoding="utf-8") as f:
            solicitud = json.load(f)

        if not isinstance(solicitud, dict):
            raise ValueError("la solicitud debe ser un objeto JSON")

        comando = solicitud.get("comando")
        args = solicitud.get("args", [])
        usuario = solicitud.get("usuario")
        origen = solicitud.get("from")
        codigo = solicitud.get("codigo")

        comando2 = solicitud.get("comando2")
        args2 = solicitud.get("args2", [])

        if not isinstance(args, list) or not all(isinstance(arg, str) for arg in args):
            raise ValueError("args debe ser una lista de cadenas")

        if comando is not None and not isinstance(comando, str):
            raise ValueError("comando inválido")

        if origen == 0.001:
            app = rutas / "apps" / f"{comando}.py"

            if not app.is_file():
                error_solicitud = {"error": f"no found command {comando}"}
            else:
                subprocess.run(
                    [sys.executable, str(app), *args],
                    check=False,
                )

        elif origen == 0.002:
            if not comando:
                raise ValueError("comando vacío")

            archivo = bin / f"{comando}.py"

            if not archivo.is_file():
                error_solicitud = {"error": f"no found command {comando}"}

            elif comando2 is not None:
                if not isinstance(comando2, str) or not comando2:
                    raise ValueError("segundo comando inválido")

                if not isinstance(args2, list) or not all(
                    isinstance(arg, str) for arg in args2
                ):
                    raise ValueError("args2 debe ser una lista de cadenas")

                archivo2 = bin / f"{comando2}.py"

                if not archivo2.is_file():
                    error_solicitud = {"error": f"no found command {comando2}"}
                else:
                    proceso1 = subprocess.run(
                        [sys.executable, str(archivo), *args],
                        capture_output=True,
                        text=True,
                        check=False,
                    )

                    if proceso1.returncode != 0:
                        error_solicitud = {
                            "error": proceso1.stderr,
                            "comando": comando,
                        }
                    else:
                        proceso2 = subprocess.run(
                            [sys.executable, str(archivo2), *args2],
                            input=proceso1.stdout,
                            capture_output=True,
                            text=True,
                            check=False,
                        )

                        if proceso2.returncode != 0:
                            error_solicitud = {
                                "error": proceso2.stderr,
                                "comando": comando2,
                            }
                        else:
                            print(proceso2.stdout, end="")
                            if proceso2.stderr:
                                print(
                                    proceso2.stderr,
                                    file=sys.stderr,
                                    end="",
                                )

            else:
                resultado = subprocess.run(
                    [sys.executable, str(archivo), *args],
                    check=False,
                )

                if resultado.returncode != 0:
                    error_solicitud = {
                        "error": f"el comando terminó con código "
                        f"{resultado.returncode}",
                        "comando": comando,
                    }

        elif origen == 0.003:
            if not isinstance(codigo, list) or not all(
                isinstance(linea, str) for linea in codigo
            ):
                raise ValueError("código inválido")

            exec(
                "\n".join(codigo),
                {"__builtins__": __builtins__},
            )

        else:
            error_solicitud = {"error": f"origen no válido: {origen}"}

    except (
        ValueError,
        TypeError,
        json.JSONDecodeError,
        OSError,
    ) as e:
        error_solicitud = {"error": str(e)}
        subprocess.run([sys.executable, error.py])
    finally:
        # El logger debe ejecutarse antes de borrar la solicitud.
        try:
            if error_solicitud is not None:
                with open(error, "w", encoding="utf-8") as f:
                    json.dump(
                        error_solicitud,
                        f,
                        ensure_ascii=False,
                        indent=4,
                    )

                subprocess.run(
                    [sys.executable, str(logerr)],
                    check=False,
                )
        finally:
            if requester.exists():
                requester.unlink()


request()
