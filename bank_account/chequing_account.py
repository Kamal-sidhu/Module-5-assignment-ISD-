ffrom bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):

    def __init__(self, account_number, client, date_opened, balance, overdraft_limit=-100, overdraft_fee=5.00):
        """
        Assignment 3 ChequingAccount (Strategy + Observer Ready)
        """

        super().__init__(account_number, client, date_opened, balance)

        # validate overdraft_limit
        try:
            self.overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.overdraft_limit = -100.0

        # validate overdraft_fee
        try:
            self.overdraft_fee = float(overdraft_fee)
        except (ValueError, TypeError):
            self.overdraft_fee = 5.00

        # Assign Strategy Pattern object
        self._service_strategy = OverdraftStrategy(self.overdraft_fee, self.overdraft_limit)

    def get_service_charges(self):
        """
        Now uses Strategy Pattern instead of inline logic.
        """
        return self._service_strategy.calculate_service_charges(self)

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"Overdraft Limit: ${self.overdraft_limit:.2f}, "
            f"Overdraft Fee: ${self.overdraft_fee:.2f}, "
            f"Account Type: Chequing"
        )
