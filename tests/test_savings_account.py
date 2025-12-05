import unittest
from bank_account import SavingsAccount, BASE_SERVICE_CHARGE

class TestSavingsAccount(unittest.TestCase):
    def test_service_charges_above_minimum(self):
        """Balance above minimum should return BASE_SERVICE_CHARGE."""
        acc = SavingsAccount("S001", 100, minimum_balance=50)
        self.assertEqual(BASE_SERVICE_CHARGE, round(acc.get_service_charges(), 2))

    
    def test_service_charges_below_minimum(self):
        """Balance below minimum should apply premium service charge."""
        acc = SavingsAccount("S002", 49.99, minimum_balance=50)
        self.assertEqual(BASE_SERVICE_CHARGE * 2, round(acc.get_service_charges(), 2))    

    def test_str_formatting(self):
        """Check __str__ formatting for SavingsAccount."""
        acc = SavingsAccount("S003", 200, minimum_balance=75)
        result = str(acc)
        self.assertIn("Account Type: Savings", result)
        self.assertIn("Minimum Balance: $75.00", result)

if __name__ == "__main__":
    unittest.main()

    
