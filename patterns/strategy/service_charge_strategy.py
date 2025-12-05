from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):

    BASE_SERVICE_CHARGE = 1.00

    @abstractmethod
    def calculate_service_charges(self, account):
        pass
