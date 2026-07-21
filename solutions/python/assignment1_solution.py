from __future__ import annotations


def make_patient() -> dict[str, object]:
    return {
        "full_name": "Jane Doe",
        "age": 45,
        "weight_kg": 70.5,
        "height_m": 1.65,
        "patient_id": "ID202305",
        "report": "The patient tested positive for strep throat.",
        "systolic_bp": 135,
        "diastolic_bp": 85,
    }


def describe_patient(patient: dict[str, object]) -> list[str]:
    return [f"Your {key} is {value}" for key, value in patient.items()]


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    if height_m <= 0:
        raise ValueError("height_m must be positive")
    return weight_kg / (height_m ** 2)


def summarize_report(report: str) -> dict[str, bool]:
    lower = report.lower()
    return {
        "mentions_positive": "positive" in lower,
        "mentions_strep": "strep" in lower,
        "needs_follow_up": "positive" in lower or "urgent" in lower,
    }


def blood_pressure_category(systolic: int, diastolic: int) -> str:
    if systolic >= 140 or diastolic >= 90:
        return "high"
    if systolic >= 130 or diastolic >= 80:
        return "elevated"
    return "normal"


def demo() -> dict[str, object]:
    patient = make_patient()
    return {
        "lines": describe_patient(patient),
        "bmi": round(calculate_bmi(float(patient["weight_kg"]), float(patient["height_m"])), 2),
        "report": summarize_report(str(patient["report"])),
        "blood_pressure": blood_pressure_category(int(patient["systolic_bp"]), int(patient["diastolic_bp"])),
    }


if __name__ == "__main__":
    result = demo()
    for line in result["lines"]:
        print(line)
    print(f"BMI: {result['bmi']}")
    print(f"Blood pressure: {result['blood_pressure']}")
