import unittest
from datetime import date
from bank_account import ChequingAccount

class TestBankAccount(unittest.TestCase):
    def test_date_created_with_valid_date(self):
        """If a valid date is passed, date_created should match it."""
        valid_date = date(2024, 1, 1)
        acc = ChequingAccount("B001", 1000, date_created=valid_date)
        self.assertEqual(acc.date_created, valid_date)

    def test_date_created_with_invalid_date(self):
        """Validate date_created defaults to today if invalid date is passed."""
        invalid_date = "2024-01-01"  # string instead of date
        acc = ChequingAccount("B002", 1000, date_created=invalid_date)
        self.assertEqual(acc.date_created, date.today())

if __name__ == "__main__":
    unittest.main()    

    