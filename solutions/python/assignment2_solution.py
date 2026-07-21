from __future__ import annotations


def temperature_message(temperature: int) -> str:
    if temperature > 30:
        return "It's a hot day."
    if temperature > 20:
        return "It's a nice day."
    if temperature > 10:
        return "It's a bit cold."
    return "It's cold."


def concert_message(age: int, has_ticket: bool) -> str:
    if age >= 18:
        if has_ticket:
            return "You can enter the concert."
        return "You need a ticket to enter."
    return "You must be at least 18 to enter."


def fruit_lines(fruits: list[str]) -> list[str]:
    fruit_output = [f"I like {fruit}" for fruit in fruits]
    letters = [letter for letter in "Python"]
    return fruit_output + letters


def numbers_and_sum() -> tuple[list[int], int]:
    numbers = list(range(1, 11))
    return numbers, sum(numbers)


def controlled_count() -> list[int]:
    count = 0
    printed: list[int] = []
    while True:
        count += 1
        if count == 3:
            continue
        if count == 7:
            break
        printed.append(count)
    return printed


def demo() -> dict[str, object]:
    numbers, total = numbers_and_sum()
    return {
        "weather": temperature_message(24),
        "concert": concert_message(20, True),
        "fruits": fruit_lines(["apple", "banana", "orange", "grape", "melon"]),
        "numbers": numbers,
        "sum": total,
        "count": controlled_count(),
    }


if __name__ == "__main__":
    print(demo())
