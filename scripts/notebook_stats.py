from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

for path in sorted(ROOT.glob("*.ipynb")):
    data = json.loads(path.read_text(encoding="utf-8"))
    cells = data.get("cells", [])
    code = sum(1 for cell in cells if cell.get("cell_type") == "code")
    markdown = sum(1 for cell in cells if cell.get("cell_type") == "markdown")
    print(f"{path.name}\t{len(cells)} cells\t{code} code\t{markdown} markdown")
