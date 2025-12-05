from datetime import date, timedelta
from .service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee, anniversary_date):
        self._management_fee = management_fee
        self._anniversary_date = anniversary_date

    def calculate_service_charges(self, account):
        charges = self.BASE_SERVICE_CHARGE

        if account.date_opened < self.TEN_YEARS_AGO:
            charges += self._management_fee

        if account.date_opened.month == self._anniversary_date.month:
            charges += 2.00

        return charges
