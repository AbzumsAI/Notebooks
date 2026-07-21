from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "HW8.txt").read_text(encoding="utf-8")

required = [
    "kaggle.com/learn/data-visualization",
    "certification",
]

missing = [item for item in required if item not in TEXT]
if missing:
    print("Missing HW8 text: " + ", ".join(missing))
    raise SystemExit(1)

print("HW8 link check passed")
