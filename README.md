# PiXELL River Financial – Banking System  
Author: Kamaldeep Kaur  
Course: COMP-2327 – Intermediate Software Development  

---

## Assignment 3 – Strategy & Observer Patterns

### Strategy Pattern
The service charge calculation for each account type is handled using the Strategy Design Pattern:

- ChequingAccount → OverdraftStrategy  
- SavingsAccount → MinimumBalanceStrategy  
- InvestmentAccount → ManagementFeeStrategy  

This keeps the calculation logic separate, flexible, and easy to update.

### Observer Pattern
The Observer Pattern is used to notify clients when:

- A large transaction occurs  
- Their balance becomes low  

The BankAccount acts as the Subject, and Client acts as the Observer.  
Notifications are written to `output/observer_emails.txt`.

---

## Assignment 4 – Event-Driven GUI (PySide6)

This assignment adds a GUI that allows:

- Looking up clients by client number  
- Viewing all their bank accounts  
- Selecting an account  
- Depositing or withdrawing money  
- Automatically updating balances in both windows  
- Saving updated balances back to `accounts.csv`

### Event-Driven Programming
The program reacts to user actions such as:

- Button clicks  
- Text changes  
- Table row selections  
- Custom signals from the Account Details window  

The AccountDetailsWindow emits a `balance_updated` signal, and the ClientLookupWindow receives it to update the table and save changes.

---

## Running the Application

Install PySide6:

```
pip install PySide6
```

Run the program:

```
python A04_main.py
```

---

## Project Structure (Simplified)

```
A04_main.py
bank_account/
client/
user_interface/
ui_superclasses/
data/
logs/
output/
```

---

## Version Control

This project includes:

- Multiple commits  
- Assignment branch merged into main  
- .git folder included as required  
