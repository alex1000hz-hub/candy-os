from pathlib import Path

apps = Path(__file__).parent.parent / "apps"

for archivo in sorted(apps.iterdir()):
    if archivo.is_file() and archivo.suffix == ".py":
        print(
            archivo.stem + ".candy   <- Commands containing .candy cannot be executed."
        )
