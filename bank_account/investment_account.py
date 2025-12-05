from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy


class InvestmentAccount(BankAccount):

    def __init__(self, account_number, client, date_opened, balance,
                 management_fee, anniversary_date):

        super().__init__(account_number, client, date_opened, balance)

        try:
            self.management_fee = float(management_fee)
        except:
            self.management_fee = 2.55

        self.anniversary_date = anniversary_date

        self._service_strategy = ManagementFeeStrategy(
            self.management_fee,
            self.anniversary_date
        )

    # REQUIRED
    def calculate_service_charge(self):
        return self._service_strategy.calculate_service_charges(self)

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"Management Fee: ${self.management_fee:.2f}, "
            f"Anniversary Month: {self.anniversary_date.month}, "
            f"Account Type: Investment"
        )
