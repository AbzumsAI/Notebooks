from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "SUBMISSION.md",
    "HW1.ipynb",
    "HW2.ipynb",
    "HW3.ipynb",
    "HW4(Project1).ipynb",
    "HW5.ipynb",
    "HW6.ipynb",
    "HW7.ipynb",
    "HW8.txt",
    "sessions/python/session-02-variables.ipynb",
    "sessions/python/session-03-control-flow.ipynb",
    "sessions/python/session-04-functions.ipynb",
    "projects/clinic-appointment-guide.ipynb",
    "masterclasses/numpy-masterclass.ipynb",
    "masterclasses/pandas-masterclass.ipynb",
    "docs/solution-index.md",
    "solutions/README.md",
    "solutions/python/assignment1_solution.py",
    "solutions/python/assignment2_solution.py",
    "solutions/python/assignment3_solution.py",
    "solutions/python/assignment4_solution.py",
    "solutions/python/assignment5_solution.py",
    "solutions/python/assignment6_solution.py",
    "solutions/python/assignment7_solution.py",
    "solutions/notebooks/assignment1_solution.ipynb",
    "solutions/notebooks/assignment2_solution.ipynb",
    "solutions/notebooks/assignment3_solution.ipynb",
    "solutions/notebooks/assignment4_solution.ipynb",
    "solutions/notebooks/assignment5_solution.ipynb",
    "solutions/notebooks/assignment6_solution.ipynb",
    "solutions/notebooks/assignment7_solution.ipynb",
    "scripts/check_solution_files.py",
]

missing = [name for name in required if not (ROOT / name).exists()]
if missing:
    print("Missing files: " + ", ".join(missing))
    raise SystemExit(1)

print("Notebook repo files are present")
