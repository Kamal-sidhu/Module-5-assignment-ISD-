from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy


class InvestmentAccount(BankAccount):

    def __init__(self, account_number, client, date_opened, balance, management_fee, anniversary_date):
        """
        Assignment 3 InvestmentAccount (Strategy + Observer Ready)
        """

        super().__init__(account_number, client, date_opened, balance)

        # validate management fee
        try:
            self.management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.management_fee = 2.55

        # validate anniversary date
        self.anniversary_date = anniversary_date

        # Assign Strategy Pattern object
        self._service_strategy = ManagementFeeStrategy(self.management_fee, self.anniversary_date)

    def get_service_charges(self):
        """
        Uses Strategy Pattern to compute charges.
        """
        return self._service_strategy.calculate_service_charges(self)

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"Management Fee: ${self.management_fee:.2f}, "
            f"Anniversary Month: {self.anniversary_date.month}, "
            f"Account Type: Investment"
        )
