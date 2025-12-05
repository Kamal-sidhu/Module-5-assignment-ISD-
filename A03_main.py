"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "Kamaldeep Kaur"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount

#     Import date
from datetime import date

#     Import Client
from client.client import Client


def main():

    # -----------------------------------------------------------
    # 2. Create a Client object with data of your choice.
    # -----------------------------------------------------------
    client1 = Client(1001, "Kamaldeep", "kaur", "kamalsidhu2727@gmail.com")

    # -----------------------------------------------------------
    # 3a. Create a ChequingAccount object (linked to client1)
    # 3b. Create a SavingsAccount object (linked to client1)
    # -----------------------------------------------------------
    cheq1 = ChequingAccount(
        account_number=2001,
        client=client1,
        date_opened=date(2020, 5, 17),
        balance=100.00,
        overdraft_limit=-200,
        overdraft_fee=25.00
    )

    sav1 = SavingsAccount(
        account_number=3001,
        client=client1,
        date_opened=date(2019, 1, 1),
        balance=500.00,
        minimum_balance=100.00,
        premium_fee=10.00
    )

    # -----------------------------------------------------------
    # 4 Attach client1 as an Observer to both accounts
    # -----------------------------------------------------------
    cheq1.attach(client1)
    sav1.attach(client1)

    # -----------------------------------------------------------
    # 5a. Create second client
    # -----------------------------------------------------------
    client2 = Client(1002, "John", "Doe", "john@example.com")

    # -----------------------------------------------------------
    # 5b. Create SavingsAccount for second client
    # -----------------------------------------------------------
    sav2 = SavingsAccount(
        account_number=3002,
        client=client2,
        date_opened=date(2015, 3, 10),
        balance=1000.00,
        minimum_balance=200.00,
        premium_fee=15.00
    )

    # Attach second client to their own account
    sav2.attach(client2)

    # -----------------------------------------------------------
    # 6 Perform transactions causing notifications & normal actions
    # -----------------------------------------------------------

    print("\n--- Performing ChequingAccount transactions ---")
    for amount in [-50, -200, 6000]:  # triggers low/large alerts
        try:
            cheq1.withdraw(amount)
        except Exception as e:
            print(e)

    print("\n--- Performing SavingsAccount #1 transactions ---")
    for amount in [-450, -50, 200]:   # drop below minimum
        try:
            sav1.withdraw(amount)
        except Exception as e:
            print(e)

    print("\n--- Performing SavingsAccount #2 transactions ---")
    for amount in [6000, -850, 100]:
        try:
            if amount < 0:
                sav2.withdraw(abs(amount))
            else:
                sav2.deposit(amount)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
