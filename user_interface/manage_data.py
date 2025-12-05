from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount
from datetime import datetime, date
import logging
import csv

def load_data() -> tuple[dict, dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """

    client_listing = {}
    accounts = {}

    # ============================
    # READ CLIENT DATA
    # ============================
    try:
        with open(clients_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for record in reader:
                try:
                    client_number = int(record["client_number"])
                    first_name = record["first_name"]
                    last_name = record["last_name"]
                    email = record["email_address"]

                    client_obj = Client(client_number, first_name, last_name, email)
                    client_listing[client_number] = client_obj

                except Exception as e:
                    logging.error(f"Unable to create client: {e}")
    except Exception as e:
        logging.error(f"Unable to open clients.csv: {e}")

    # ============================
    # READ ACCOUNT DATA
    # ============================
    try:
        with open(accounts_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for record in reader:
                try:
                    # Convert raw values
                    account_number = int(record["account_number"])
                    client_number = int(record["client_number"])
                    balance = float(record["balance"])

                    # Convert date_created
                    try:
                        date_created = datetime.strptime(record["date_created"], "%Y-%m-%d").date()
                    except:
                        raise ValueError("Invalid date format")

                    account_type = record["account_type"]

                    # Extract optional fields with Null handling
                    overdraft_limit = record["overdraft_limit"]
                    overdraft_rate = record["overdraft_rate"]
                    minimum_balance = record["minimum_balance"]
                    management_fee = record["management_fee"]

                    # Replace "Null" with Python None
                    overdraft_limit = None if overdraft_limit == "Null" else float(overdraft_limit)
                    overdraft_rate = None if overdraft_rate == "Null" else float(overdraft_rate)
                    minimum_balance = None if minimum_balance == "Null" else float(minimum_balance)
                    management_fee = None if management_fee == "Null" else float(management_fee)

                    # Create the correct BankAccount subclass
                    if account_type == "ChequingAccount":
                        acct = ChequingAccount(
                            account_number,
                            client_number,
                            date_created,
                            balance,
                            overdraft_limit,
                            overdraft_rate
                        )

                    elif account_type == "SavingsAccount":
                        acct = SavingsAccount(
                            account_number,
                            client_number,
                            date_created,
                            balance,
                            minimum_balance,
                            2.0  # premium fee default
                        )

                    elif account_type == "InvestmentAccount":
                        acct = InvestmentAccount(
                            account_number,
                            client_number,
                            date_created,
                            balance,
                            management_fee,
                            date_created  # anniversary date = date created
                        )

                    else:
                        raise ValueError("Not a valid account type.")

                    # Check if client exists before adding account
                    if client_number in client_listing:
                        accounts[account_number] = acct
                    else:
                        logging.error(
                            f"Bank Account: {account_number} contains invalid Client Number: {client_number}"
                        )

                except Exception as e:
                    logging.error(f"Unable to create bank account: {e}")

    except Exception as e:
        logging.error(f"Unable to open accounts.csv: {e}")

    # ============================
    # RETURN STATEMENT
    # ============================
    return client_listing, accounts
