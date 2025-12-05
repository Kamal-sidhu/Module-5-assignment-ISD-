import unittest
from datetime import date, timedelta
from bank_account import InvestmentAccount, BASE_SERVICE_CHARGE

class TestInvestmentAccount(unittest.TestCase):
    def test_service_charges_old_account(self):
        """Accounts older than 10 years should waive management fee."""
        old_date = date.today() - timedelta(days=365*11)
        acc = InvestmentAccount("I001", 1000, date_created=old_date, management_fee=2.5)
        self.assertEqual(BASE_SERVICE_CHARGE, round(acc.get_service_charges(), 2))

    def test_service_charges_recent_account(self):
        """Accounts 10 years old or less should include management fee."""
        recent_date = date.today()
        acc = InvestmentAccount("I002", 1000, date_created=recent_date, management_fee=2.5)
        self.assertEqual(BASE_SERVICE_CHARGE + 2.5, round(acc.get_service_charges(), 2))    

    def test_str_formatting(self):
        """Check __str__ formatting for recent and old accounts."""
        recent_date = date.today()
        old_date = date.today() - timedelta(days=365*11)
        recent_acc = InvestmentAccount("I003", 500, date_created=recent_date, management_fee=3)
        old_acc = InvestmentAccount("I004", 500, date_created=old_date, management_fee=3)
        self.assertIn("Management Fee: $3.00", str(recent_acc))
        self.assertIn("Management Fee: Waived", str(old_acc))

if __name__ == "__main__":
    unittest.main()    