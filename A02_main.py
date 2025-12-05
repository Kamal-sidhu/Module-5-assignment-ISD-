"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "kamaldeep kaur"
__version__ = "1.0.0"
__credits__ = ""

# 1. Import all BankAccount types using the bank_account package
from bank_account import *
from datetime import date, timedelta

print("===================================================")
# 2. Create a ChequingAccount with balance below overdraft limit
cheq_acc = ChequingAccount("C1001", -200, overdraft_limit=-100, overdraft_rate=0.05)

# 3. Print the ChequingAccount and service charges
print(cheq_acc)
print(f"Service Charges: ${cheq_acc.get_service_charges():.2f}")

# 4a. Deposit money to avoid overdraft fees
cheq_acc.deposit(200)  # Assuming deposit method exists
# 4b. Print updated ChequingAccount and service charges
print(cheq_acc)
print(f"Service Charges: ${cheq_acc.get_service_charges():.2f}")

print("===================================================")
# 5. Create a SavingsAccount with balance above minimum
sav_acc = SavingsAccount("S1001", 100, minimum_balance=50)

# 6. Print SavingsAccount and service charges
print(sav_acc)
print(f"Service Charges: ${sav_acc.get_service_charges():.2f}")

# 7a. Withdraw to fall below minimum
sav_acc.withdraw(60)  # Assuming withdraw method exists
# 7b. Print updated SavingsAccount and service charges
print(sav_acc)
print(f"Service Charges: ${sav_acc.get_service_charges():.2f}")

print("===================================================")
# 8. Create InvestmentAccount with date within last 10 years
recent_date = date.today() - timedelta(days=365*5)
inv_acc_recent = InvestmentAccount("I1001", 1000, date_created=recent_date, management_fee=2.5)

# 9a. Print InvestmentAccount and service charges
print(inv_acc_recent)
print(f"Service Charges: ${inv_acc_recent.get_service_charges():.2f}")

# 10. Create InvestmentAccount with date older than 10 years
old_date = date.today() - timedelta(days=365*11)
inv_acc_old = InvestmentAccount("I1002", 1000, date_created=old_date, management_fee=2.5)

# 11a. Print InvestmentAccount and service charges
print(inv_acc_old)
print(f"Service Charges: ${inv_acc_old.get_service_charges():.2f}")

print("===================================================")
# 12. Withdraw service charges from each account
for acc in [cheq_acc, sav_acc, inv_acc_recent, inv_acc_old]:
    acc.withdraw(acc.get_service_charges())

# 13. Print each account after service charges applied
for acc in [cheq_acc, sav_acc, inv_acc_recent, inv_acc_old]:
    print(acc)
