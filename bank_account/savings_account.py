from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy


class SavingsAccount(BankAccount):

    def __init__(self, account_number, client, date_opened, balance, minimum_balance, premium_fee):
        """
        Assignment 3 SavingsAccount using Strategy Pattern
        """

        super().__init__(account_number, client, date_opened, balance)

        # validate minimum balance
        try:
            self.minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.minimum_balance = 50.0

        # validate premium fee
        try:
            self.premium_fee = float(premium_fee)
        except (ValueError, TypeError):
            self.premium_fee = 2.0

        # Strategy Pattern setup
        self._service_strategy = MinimumBalanceStrategy(self.minimum_balance, self.premium_fee)

    def get_service_charges(self):
        """
        Uses Strategy Pattern instead of inline logic.
        """
        return self._service_strategy.calculate_service_charges(self)

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"Minimum Balance: ${self.minimum_balance:.2f}, "
            f"Premium Fee: ${self.premium_fee:.2f}, "
            f"Account Type: Savings"
        )
