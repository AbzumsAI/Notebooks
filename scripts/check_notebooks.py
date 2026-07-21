from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]


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

    return errors


def main() -> int:
    notebooks = sorted(ROOT.glob("*.ipynb"))
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
