from bank_account.bank_account import BankAccount, BASE_SERVICE_CHARGE


class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance,
                 date_created=None, minimum_balance=50, premium_fee=2):

        super().__init__(account_number, balance, date_created)

        self.minimum_balance = float(minimum_balance)
        self.premium_fee = float(premium_fee)

    def calculate_service_charge(self):
        if self.balance >= self.minimum_balance:
            return BASE_SERVICE_CHARGE
        else:
            return BASE_SERVICE_CHARGE * self.premium_fee

    def get_service_charges(self):
        return self.calculate_service_charge()

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"Minimum Balance: ${self.minimum_balance:.2f}, "
            f"Premium Fee: ${self.premium_fee:.2f}, "
            f"Account Type: Savings"
        )
