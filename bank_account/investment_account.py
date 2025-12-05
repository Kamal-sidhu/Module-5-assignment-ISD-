from datetime import date, timedelta
from bank_account.bank_account import BankAccount, BASE_SERVICE_CHARGE


class InvestmentAccount(BankAccount):

    def __init__(self, account_number, balance,
                 date_created=None, management_fee=2.5):

        super().__init__(account_number, balance, date_created)

        self.management_fee = float(management_fee)

    def calculate_service_charge(self):
        age = (date.today() - self.date_created).days

        if age > 365 * 10:
            return BASE_SERVICE_CHARGE  # fee waived
        return BASE_SERVICE_CHARGE + self.management_fee

    def get_service_charges(self):
        return self.calculate_service_charge()

    def __str__(self):
        base = super().__str__()

        age = (date.today() - self.date_created).days
        if age > 365 * 10:
            fee_text = "Waived"
        else:
            fee_text = f"${self.management_fee:.2f}"

        return (
            f"{base}\n"
            f"Management Fee: {fee_text}, "
            f"Account Type: Investment"
        )
