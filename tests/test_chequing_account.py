import unittest
from bank_account import ChequingAccount, BASE_SERVICE_CHARGE

class TestChequingAccount(unittest.TestCase):
    def test_service_charges_above_overdraft(self):
        """Balance above overdraft limit should return BASE_SERVICE_CHARGE."""
        acc = ChequingAccount("C001", 0, overdraft_limit=-100, overdraft_rate=0.05)
        self.assertEqual(BASE_SERVICE_CHARGE, round(acc.get_service_charges(), 2))
    
    def test_service_charges_below_overdraft(self):
        """Balance below overdraft limit should include overdraft fees."""
        acc = ChequingAccount("C002", -200, overdraft_limit=-100, overdraft_rate=0.05)
        expected = BASE_SERVICE_CHARGE + (-100 - -200) * 0.05
        self.assertEqual(expected, round(acc.get_service_charges(), 2))

    def test_str_formatting(self):
        """Check __str__ formatting for ChequingAccount."""
        acc = ChequingAccount("C003", 500, overdraft_limit=-150, overdraft_rate=0.1)
        result = str(acc)
        self.assertIn("Account Type: Chequing", result)
        self.assertIn("Overdraft Limit: $-150.00", result)
        self.assertIn("Overdraft Rate: 10.00%", result)

if __name__ == "__main__":
    unittest.main()