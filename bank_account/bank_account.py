from abc import ABC, abstractmethod
from patterns.observer.subject import Subject

# ---------------------------------------------------------
# REQUIRED CONSTANT (Backward compatibility for Assignment 5)
# ---------------------------------------------------------
BASE_SERVICE_CHARGE = 0.00


class BankAccount(Subject, ABC):
    """
    Abstract BankAccount class used as the parent for
    ChequingAccount, SavingsAccount, and InvestmentAccount.

    Assignment 5 Requirements:
    - Must inherit from Subject (Observer Pattern)
    - Must define an abstract calculate_service_charge() (Strategy Pattern)
    - Must trigger notifications on low balance + large transactions
    """

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

        # Strategy placeholder — will be overridden in subclasses
        self.service_charge_strategy = None

    # ---------------------------------------------------------
    # REQUIRED BY ASSIGNMENT 5 — STRATEGY PATTERN
    # ---------------------------------------------------------
    @abstractmethod
    def calculate_service_charge(self):
        """
        Each account type MUST override this.
        Chequing, Savings, Investment accounts will apply their own strategy.
        """
        pass

    # ---------------------------------------------------------
    # Update balance + notify observers
    # ---------------------------------------------------------
    def update_balance(self, amount):
        try:
            amount = float(amount)
        except:
            return

        self.balance += amount

        # Low balance notification
        if self.balance < self.LOW_BALANCE_LEVEL:
            self.notify(
                f"Low balance warning ${self.balance:,.2f}: "
                f"on account {self.account_number}."
            )

        # Large transaction notification
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(
                f"Large transaction ${abs(amount):,.2f}: "
                f"on account {self.account_number}."
            )

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
        return (
            f"Account Number: {self.account_number}, "
            f"Balance: ${self.balance:,.2f}"
        )
