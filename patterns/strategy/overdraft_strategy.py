from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):

    def __init__(self, overdraft_fee, overdraft_limit):
        self._overdraft_fee = overdraft_fee
        self._overdraft_limit = overdraft_limit

    def calculate_service_charges(self, account):
        charges = self.BASE_SERVICE_CHARGE

        if account.balance < 0:
            charges += self._overdraft_fee

        if account.balance < self._overdraft_limit:
            charges += 5.00

        return charges
