import sys
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import TextArea, Footer, Header

CANDY = Path(__file__).resolve().parent.parent


class Editor(App):
    BINDINGS = [
        ("ctrl+s", "guardar", "Guardar"),
        ("ctrl+q", "quit", "Salir"),
    ]

    def __init__(self, archivo: Path):
        super().__init__()
        self.archivo = archivo

    def compose(self) -> ComposeResult:
        yield Header()

        codigo = self.archivo.read_text(encoding="utf-8")
        yield TextArea(
            codigo,
            language="python",
            theme="monokai",
            soft_wrap=False,
        )

        yield Footer()

    def action_guardar(self):
        editor = self.query_one(TextArea)
        self.archivo.write_text(editor.text, encoding="utf-8")
        self.notify("Archivo guardado correctamente")


def main():
    args = sys.argv[1:]

    if len(args) != 3 or args[:2] != ["modify", "print"]:
        print('Uso: modify print path = "system/bin/terminal.py"')
        return

    ruta = args[2]

    archivo = (CANDY / ruta).resolve()

    if not archivo.is_relative_to(CANDY.resolve()):
        print("Error: ruta fuera de Candy OS")
        return

    if not archivo.is_file():
        print(f"Error: archivo no encontrado: {ruta}")
        return

    Editor(archivo).run()


if __name__ == "__main__":
    main()