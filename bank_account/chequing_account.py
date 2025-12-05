from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):

    def __init__(self, account_number, client, date_opened, balance,
                 overdraft_limit=-100, overdraft_fee=5.00):

        super().__init__(account_number, client, date_opened, balance)

        try:
            self.overdraft_limit = float(overdraft_limit)
        except:
            self.overdraft_limit = -100.0

        try:
            self.overdraft_fee = float(overdraft_fee)
        except:
            self.overdraft_fee = 5.00

        self._service_strategy = OverdraftStrategy(
            fee=self.overdraft_fee,
            limit=self.overdraft_limit
        )

    # REQUIRED BY ASSIGNMENT 5
    def calculate_service_charge(self):
        return self._service_strategy.calculate_service_charges(self)

    def __str__(self):
        parent = super().__str__()
        return (
            f"{parent}\n"
            f"Overdraft Limit: ${self.overdraft_limit:.2f}, "
            f"Overdraft Fee: ${self.overdraft_fee:.2f}, "
            f"Account Type: Chequing"
        )
