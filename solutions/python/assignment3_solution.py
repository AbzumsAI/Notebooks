from __future__ import annotations


def greet(name: str) -> str:
    return f"Hello, {name}!"


def analyze_numbers(first: float, second: float) -> dict[str, float]:
    return {
        "first": first,
        "second": second,
        "sum": first + second,
        "difference": first - second,
        "product": first * second,
        "average": (first + second) / 2,
    }


def find_a_b(total: float, difference: float) -> tuple[float, float]:
    first = (total + difference) / 2
    second = total - first
    return first, second


def calculate_discounted_price(price: float, discount: float = 10, tax: float = 5) -> float:
    discount_amount = price * (discount / 100)
    price_after_discount = price - discount_amount
    tax_amount = price_after_discount * (tax / 100)
    return price_after_discount + tax_amount


def first_names(full_names: list[str]) -> list[str]:
    return list(map(lambda full_name: full_name.split()[0], full_names))


def active_adults(users: list[dict[str, object]]) -> list[dict[str, object]]:
    return list(filter(lambda user: bool(user["active"]) and int(user["age"]) >= 18, users))


def safe_divide(numerator: float, denominator: float) -> float | None:
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None


def demo() -> dict[str, object]:
    users = [
        {"name": "Ali", "age": 17, "active": True},
        {"name": "Sara", "age": 22, "active": False},
        {"name": "Reza", "age": 19, "active": True},
    ]
    return {
        "greeting": greet("Iman"),
        "numbers": analyze_numbers(8, 2),
        "pair": find_a_b(10, 4),
        "price": round(calculate_discounted_price(100), 2),
        "names": first_names(["Alexander Fleming", "Elizabeth Blackwell"]),
        "active_adults": active_adults(users),
        "division": safe_divide(10, 2),
    }


if __name__ == "__main__":
    print(demo())
