from abc import ABC
from patterns.observer.subject import Subject

# -------------------------------------------------------------------
# REQUIRED CONSTANT FOR backwards compatibility (Fix for Assignment 5)
# -------------------------------------------------------------------
BASE_SERVICE_CHARGE = 0.00


class BankAccount(Subject, ABC):

    LOW_BALANCE_LEVEL = 50.00
    LARGE_TRANSACTION_THRESHOLD = 5000.00

    def __init__(self, account_number, client, date_opened, balance=0.0):
        super().__init__()

        self.account_number = account_number
        self.client = client
        self.date_opened = date_opened

        try:
            self.balance = float(balance)
        except:
            self.balance = 0.0

    # ------------------------------------------------------------
    # Update balance + notify if thresholds are crossed
    # ------------------------------------------------------------
    def update_balance(self, amount):
        try:
            amount = float(amount)
        except:
            return

        self.balance += amount

        # Notify if low balance
        if self.balance < self.LOW_BALANCE_LEVEL:
            self.notify(
                f"Low balance warning ${self.balance:,.2f}: "
                f"on account {self.account_number}."
            )

        # Notify if large transaction
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(
                f"Large transaction ${abs(amount):,.2f}: "
                f"on account {self.account_number}."
            )

    # ------------------------------------------------------------
    # Deposit funds
    # ------------------------------------------------------------
    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.update_balance(amount)

    # ------------------------------------------------------------
    # Withdraw funds
    # ------------------------------------------------------------
    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.update_balance(-amount)

    # ------------------------------------------------------------
    # String Representation
    # ------------------------------------------------------------
    def __str__(self):
        return (
            f"Account Number: {self.account_number}, "
            f"Balance: ${self.balance:,.2f}"
        )
