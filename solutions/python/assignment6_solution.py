from __future__ import annotations


class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_holder = account_holder
        self.balance = float(initial_balance)
        self.transactions: list[str] = [f"Opened account with ${self.balance:.2f}"]

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            self.transactions.append("Rejected deposit")
            return False
        self.balance += amount
        self.transactions.append(f"Deposited ${amount:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.balance:
            self.transactions.append("Rejected withdrawal")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount:.2f}")
        return True

    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        if not new_name.strip():
            raise ValueError("Bank name cannot be empty")
        cls.bank_name = new_name

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount > 0

    def show_transactions(self) -> list[str]:
        return list(self.transactions)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01) -> None:
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> float:
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Added interest ${interest:.2f}")
        return interest


def demo() -> dict[str, object]:
    checking = BankAccount("Sara", 200)
    checking.deposit(50)
    checking.withdraw(30)
    savings = SavingsAccount("Ali", 1000, 0.05)
    savings.add_interest()
    BankAccount.change_bank_name("Abzums Bank")
    return {
        "checking": str(checking),
        "savings": str(savings),
        "bank": BankAccount.bank_name,
        "transactions": checking.show_transactions(),
    }


if __name__ == "__main__":
    print(demo())
