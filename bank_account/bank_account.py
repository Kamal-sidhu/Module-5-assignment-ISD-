from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject

BASE_SERVICE_CHARGE = 0.00


class BankAccount(Subject, ABC):

    def __init__(self, account_number, balance, date_created=None):
        super().__init__()

        self.account_number = account_number
        self.balance = float(balance)

        # Tests expect automatic fallback to today's date
        if isinstance(date_created, date):
            self.date_created = date_created
        else:
            self.date_created = date.today()

        # Strategy placeholder assigned in subclasses
        self.service_charge_strategy = None

    @abstractmethod
    def calculate_service_charge(self):
        pass

    def update_balance(self, amount):
        amount = float(amount)
        self.balance += amount

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.update_balance(-amount)

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}"
