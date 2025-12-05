from abc import ABC, abstractmethod
from patterns.observer.subject import Subject

# ---------------------------------------------------------
# REQUIRED CONSTANT for Assignment 5 (backward compatibility)
# ---------------------------------------------------------
BASE_SERVICE_CHARGE = 0.00


class BankAccount(Subject, ABC):
    """
    Base BankAccount class used by Chequing, Savings, Investment accounts.
    Assignment 5 Requirements:
    - Must include Observer Pattern (extends Subject)
    - Must define abstract calculate_service_charge()
    - Must notify on low balance + large transactions
    """

    LOW_BALANCE_LEVEL = 50.00
    LARGE_TRANSACTION_THRESHOLD = 5000.00

    def __init__(self, account_number, balance, date_created):
        super().__init__()

        self.account_number = account_number
        self.balance = float(balance)

        # tests expect this exact property name
        self.date_created = date_created

        # Strategy object will be set in subclasses
        self.service_charge_strategy = None

    # ---------------------------------------------------------
    # REQUIRED ABSTRACT METHOD (Strategy Pattern)
    # ---------------------------------------------------------
    @abstractmethod
    def calculate_service_charge(self):
        """
        Must be overridden by Chequing, Savings, and Investment accounts.
        """
        pass

    # ---------------------------------------------------------
    # Balance update + notifications
    # ---------------------------------------------------------
    def update_balance(self, amount):
        amount = float(amount)
        self.balance += amount

        # Low balance notification
        if self.balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.balance:,.2f}: on account {self.account_number}.")

        # Large transaction notification
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${abs(amount):,.2f}: on account {self.account_number}.")

    # ---------------------------------------------------------
    # Deposit
    # ---------------------------------------------------------
    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.update_balance(amount)

    # ---------------------------------------------------------
    # Withdraw
    # ---------------------------------------------------------
    def withdraw(self, amount):
        amount = float(amount)

        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.update_balance(-amount)

    # ---------------------------------------------------------
    # String representation
    # ---------------------------------------------------------
    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance:,.2f}"
