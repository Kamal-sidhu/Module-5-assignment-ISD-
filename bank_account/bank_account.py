from abc import ABC
from patterns.observer.subject import Subject

# -------------------------------------------------------------------
# REQUIRED CONSTANT (Assignment 5)
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
        # STRATEGY PATTERN – service charge strategy placeholder
        # ------------------------------------------------------------
        self.service_charge_strategy = None

    # ------------------------------------------------------------
    # Assign a strategy at runtime
    # ------------------------------------------------------------
    def set_strategy(self, strategy):
        """
        Sets the service charge strategy dynamically.
        """
        self.service_charge_strategy = strategy

    # ------------------------------------------------------------
    # Apply the selected strategy
    # ------------------------------------------------------------
    def apply_service_charge(self):
        """
        Calls the chosen service charge strategy and deducts from balance.
        """
        if self.service_charge_strategy is None:
            return BASE_SERVICE_CHARGE

        charge_amount = self.service_charge_strategy.calculate_charge(self)

        # Deduct charge
        self.update_balance(-abs(charge_amount))

        return charge_amount

    # ------------------------------------------------------------
    # Update balance + notify observer based on thresholds
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

        # Apply Service Charge (Strategy)
        self.apply_service_charge()

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

        # Apply Service Charge (Strategy)
        self.apply_service_charge()

    # ------------------------------------------------------------
    # String Representation
    # ------------------------------------------------------------
    def __str__(self):
        return (
            f"Account Number: {self.account_number}, "
            f"Balance: ${self.balance:,.2f}"
        )
