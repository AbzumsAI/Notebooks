from __future__ import annotations

import csv
import json
import math
import random
from datetime import date
from pathlib import Path


def write_sample_text(folder: Path) -> Path:
    path = folder / "sample.txt"
    path.write_text("Hello from a sample text file.\n", encoding="utf-8")
    return path


def read_sample_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_people_csv(folder: Path) -> Path:
    path = folder / "data.csv"
    rows = [
        {"Name": "Alice", "Age": 30, "Occupation": "Engineer"},
        {"Name": "Bob", "Age": 25, "Occupation": "Designer"},
        {"Name": "Charlie", "Age": 35, "Occupation": "Teacher"},
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Name", "Age", "Occupation"])
        writer.writeheader()
        writer.writerows(rows)
    return path


def read_people_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_config(folder: Path) -> Path:
    path = folder / "config.json"
    config = {"theme": "light", "language": "Python", "version": 1}
    path.write_text(json.dumps(config, indent=2), encoding="utf-8")
    return path


def read_config(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def squares() -> list[int]:
    return [number ** 2 for number in range(10)]


def cubes() -> dict[int, int]:
    return {number: number ** 3 for number in range(1, 6)}


def evens() -> list[int]:
    return [number for number in range(21) if number % 2 == 0]


def square_root_of_sixteen() -> float:
    return math.sqrt(16)


def random_between_one_and_ten(seed: int = 7) -> int:
    generator = random.Random(seed)
    return generator.randint(1, 10)


def greet(name: str) -> str:
    return f"Hello, {name}!"


def today_iso() -> str:
    return date.today().isoformat()


def demo(folder: Path) -> dict[str, object]:
    text_path = write_sample_text(folder)
    csv_path = write_people_csv(folder)
    config_path = write_config(folder)
    return {
        "text": read_sample_text(text_path).strip(),
        "people": read_people_csv(csv_path),
        "config": read_config(config_path),
        "squares": squares(),
        "cubes": cubes(),
        "evens": evens(),
        "sqrt": square_root_of_sixteen(),
        "random": random_between_one_and_ten(),
        "greeting": greet("Ali"),
        "date": today_iso(),
    }


if __name__ == "__main__":
    print("Run demo with a folder path from another script.")
