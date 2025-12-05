from datetime import date, timedelta
from bank_account.bank_account import BankAccount, BASE_SERVICE_CHARGE


class InvestmentAccount(BankAccount):

    def __init__(self, account_number, balance,
                 date_created=None, management_fee=2.5):

        super().__init__(account_number, balance, date_created)
        self.management_fee = float(management_fee)

    def calculate_service_charge(self):
        age_years = (date.today() - self.date_created).days / 365
        return BASE_SERVICE_CHARGE if age_years > 10 else self.management_fee

    def __str__(self):
        return (super().__str__() +
                f"\nManagement Fee: ${self.management_fee:.2f}, "
                f"Account Type: Investment")
