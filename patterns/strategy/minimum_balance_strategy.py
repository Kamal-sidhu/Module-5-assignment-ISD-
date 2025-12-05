from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):

    def __init__(self, minimum_balance, premium_fee):
        self._minimum_balance = minimum_balance
        self._premium_fee = premium_fee

    def calculate_service_charges(self, account):
        charges = self.BASE_SERVICE_CHARGE

        if account.balance < self._minimum_balance:
            charges += self._premium_fee

        return charges
