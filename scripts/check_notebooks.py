from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TEXT_SYMBOLS = {chr(0x03C0), chr(0x20AC)}
BLOCKED_SYMBOLS = {
    chr(0x2013): "en dash",
    chr(0x2014): "em dash",
}


def check_notebook(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path.name}: invalid JSON at line {exc.lineno}"]

    cells = data.get("cells")
    if not isinstance(cells, list) or not cells:
        errors.append(f"{path.name}: missing cells")

    for index, cell in enumerate(cells or [], start=1):
        if cell.get("cell_type") not in {"code", "markdown", "raw"}:
            errors.append(f"{path.name}: cell {index} has an unknown type")
        if "source" not in cell:
            errors.append(f"{path.name}: cell {index} has no source")
        text = "".join(cell.get("source", []))
        for symbol, label in BLOCKED_SYMBOLS.items():
            if symbol in text:
                errors.append(f"{path.name}: cell {index} has {label}")
        for char in text:
            if ord(char) > 127 and char not in ALLOWED_TEXT_SYMBOLS:
                code = f"U+{ord(char):04X}"
                errors.append(f"{path.name}: cell {index} has {code}")
                break

    return errors


def main() -> int:
    notebooks = [
        path
        for path in sorted(ROOT.rglob("*.ipynb"))
        if ".ipynb_checkpoints" not in path.parts
    ]
    errors: list[str] = []
    for notebook in notebooks:
        errors.extend(check_notebook(notebook))

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Checked {len(notebooks)} notebooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
