from bank_account.bank_account import BankAccount, BASE_SERVICE_CHARGE
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):
    """
    ChequingAccount using Strategy Pattern (Assignment 3 & 5)
    """

    def __init__(self, account_number, client, date_opened, balance,
                 overdraft_limit=-100, overdraft_rate=0.05):

        super().__init__(account_number, client, date_opened, balance)

        # Validate overdraft limit
        try:
            self.overdraft_limit = float(overdraft_limit)
        except:
            self.overdraft_limit = -100.0

        # Validate overdraft rate
        try:
            self.overdraft_rate = float(overdraft_rate)
        except:
            self.overdraft_rate = 0.05

        # Strategy Pattern object
        self.service_charge_strategy = OverdraftStrategy(
            overdraft_limit=self.overdraft_limit,
            overdraft_rate=self.overdraft_rate
        )

    # ---------------------------------------------------------
    # REQUIRED BY ASSIGNMENT 5 — Strategy Pattern
    # ---------------------------------------------------------
    def calculate_service_charge(self):
        """Required override for abstract method"""
        return self.service_charge_strategy.calculate_service_charge(self)

    # ---------------------------------------------------------
    # Assignment-required wrapper
    # ---------------------------------------------------------
    def get_service_charges(self):
        return self.calculate_service_charge()

    def __str__(self):
        parent = super().__str__()
        return (
            f"{parent}\n"
            f"Overdraft Limit: ${self.overdraft_limit:.2f}, "
            f"Overdraft Rate: {self.overdraft_rate:.2f}, "
            f"Account Type: Chequing"
        )
