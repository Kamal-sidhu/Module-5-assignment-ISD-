from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):
    """
    ChequingAccount with Overdraft Strategy (Assignment 3 & 5 Requirement)
    """

    def __init__(self, account_number, client, date_opened, balance,
                 overdraft_limit=-100, overdraft_fee=5.00):

        super().__init__(account_number, client, date_opened, balance)

        # ---------------------------
        # VALIDATION FOR PARAMETERS
        # ---------------------------
        try:
            self.overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.overdraft_limit = -100.0

        try:
            self.overdraft_fee = float(overdraft_fee)
        except (ValueError, TypeError):
            self.overdraft_fee = 5.00

        # ---------------------------
        # STRATEGY PATTERN OBJECT
        # ---------------------------
        self._service_strategy = OverdraftStrategy(
            fee=self.overdraft_fee,
            limit=self.overdraft_limit
        )

    # ------------------------------------------------------------
    # SERVICE CHARGE CALCULATION (STRATEGY PATTERN)
    # ------------------------------------------------------------
    def get_service_charges(self):
        return self._service_strategy.calculate_service_charges(self)

    # ------------------------------------------------------------
    # STRING DISPLAY
    # ------------------------------------------------------------
    def __str__(self):
        parent = super().__str__()
        return (
            f"{parent}\n"
            f"Overdraft Limit: ${self.overdraft_limit:.2f}, "
            f"Overdraft Fee: ${self.overdraft_fee:.2f}, "
            f"Account Type: Chequing"
        )
