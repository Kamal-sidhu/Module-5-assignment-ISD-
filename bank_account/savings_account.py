from bank_account.bank_account import BankAccount, BASE_SERVICE_CHARGE


class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance,
                 date_created=None, minimum_balance=50, premium_fee=2):

        super().__init__(account_number, balance, date_created)

        self.minimum_balance = float(minimum_balance)
        self.premium_fee = float(premium_fee)

    def calculate_service_charge(self):
        return BASE_SERVICE_CHARGE if self.balance >= self.minimum_balance else self.premium_fee

    def __str__(self):
        return (super().__str__() +
                f"\nMinimum Balance: ${self.minimum_balance:.2f}, "
                f"Premium Fee: ${self.premium_fee:.2f}, "
                f"Account Type: Savings")
