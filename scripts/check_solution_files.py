from __future__ import annotations

from pathlib import Path
import importlib.util
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOLUTION_ROOT = ROOT / "solutions" / "python"


def load_module(name: str):
    path = SOLUTION_ROOT / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_assignment_one() -> None:
    module = load_module("assignment1_solution")
    assert round(module.calculate_bmi(70.5, 1.65), 2) == 25.9
    assert module.blood_pressure_category(135, 85) == "elevated"
    assert module.summarize_report("positive test")["mentions_positive"] is True


def check_assignment_two() -> None:
    module = load_module("assignment2_solution")
    assert module.temperature_message(31) == "It's a hot day."
    assert module.concert_message(20, True).startswith("You can")
    assert module.numbers_and_sum()[1] == 55
    assert module.controlled_count() == [1, 2, 4, 5, 6]


def check_assignment_three() -> None:
    module = load_module("assignment3_solution")
    assert module.greet("Ali") == "Hello, Ali!"
    assert module.find_a_b(10, 4) == (7, 3)
    assert module.safe_divide(3, 0) is None
    assert module.first_names(["Ada Lovelace"])[0] == "Ada"


def check_assignment_four() -> None:
    module = load_module("assignment4_solution")
    result = module.play_turns([1, 4, 2, 5, 3])
    assert result["winner"] == "X"
    assert module.is_tie(["X", "O", "X", "X", "O", "O", "O", "X", "X"]) is True


def check_assignment_five() -> None:
    module = load_module("assignment5_solution")
    with tempfile.TemporaryDirectory() as folder:
        data = module.demo(Path(folder))
    assert data["squares"][3] == 9
    assert data["cubes"][5] == 125
    assert data["evens"][-1] == 20
    assert data["people"][0]["Name"] == "Alice"


def check_assignment_six() -> None:
    module = load_module("assignment6_solution")
    account = module.BankAccount("Mina", 100)
    assert account.deposit(50) is True
    assert account.withdraw(20) is True
    assert account.balance == 130
    savings = module.SavingsAccount("Reza", 200, 0.1)
    assert savings.add_interest() == 20


def check_assignment_seven() -> None:
    module = load_module("assignment7_solution")
    client = module.MastermindClient(post=module.fake_post)
    assert client.start_game() == "demo-game"
    result = client.send_guess("1234")
    assert result["status"] == "won"


def main() -> int:
    checks = [
        check_assignment_one,
        check_assignment_two,
        check_assignment_three,
        check_assignment_four,
        check_assignment_five,
        check_assignment_six,
        check_assignment_seven,
    ]
    for check in checks:
        check()
    print(f"Checked {len(checks)} solution groups")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
