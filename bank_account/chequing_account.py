from bank_account.bank_account import BankAccount, BASE_SERVICE_CHARGE


class ChequingAccount(BankAccount):

    def __init__(self, account_number, balance,
                 date_created=None, overdraft_limit=-100, overdraft_rate=0.05):

        super().__init__(account_number, balance, date_created)

        self.overdraft_limit = float(overdraft_limit)
        self.overdraft_rate = float(overdraft_rate)

    def calculate_service_charge(self):
        if self.balance >= self.overdraft_limit:
            return BASE_SERVICE_CHARGE
        else:
            diff = self.overdraft_limit - self.balance
            return BASE_SERVICE_CHARGE + diff * self.overdraft_rate

    def get_service_charges(self):
        return self.calculate_service_charge()

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f"Overdraft Limit: ${self.overdraft_limit:.2f}, "
            f"Overdraft Rate: {self.overdraft_rate*100:.2f}%, "
            f"Account Type: Chequing"
        )
