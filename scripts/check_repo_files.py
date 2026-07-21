from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "SUBMISSION.md",
    "Notebook1.ipynb",
    "HW2.ipynb",
    "HW3.ipynb",
    "HW4(Project1).ipynb",
    "HW5.ipynb",
    "HW6.ipynb",
    "HW7.ipynb",
    "HW8.txt",
]

missing = [name for name in required if not (ROOT / name).exists()]
if missing:
    print("Missing files: " + ", ".join(missing))
    raise SystemExit(1)

print("Notebook repo files are present")
