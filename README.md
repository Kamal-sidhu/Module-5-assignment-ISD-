# PiXELL River Financial – Banking System
Author: Kamaldeep Kaur  
Course: COMP-2327 – Intermediate Software Development  

---

## 📌 Project Overview

This project simulates a banking system that supports multiple account types, service charge strategies, observer notifications, a full event-driven GUI, data persistence, Sphinx documentation, and a Windows installer.

The system evolves across **Assignment 3, Assignment 4, and Assignment 5**, each building on the previous one.

---

# Assignment 3 – Strategy & Observer Patterns

## 🔷 Strategy Pattern

Each account uses a separate strategy class for calculating service charges:

| Account Type        | Strategy Class              |
|--------------------|-----------------------------|
| ChequingAccount    | OverdraftStrategy           |
| SavingsAccount     | MinimumBalanceStrategy      |
| InvestmentAccount  | ManagementFeeStrategy       |

---

## 🔷 Observer Pattern

The system uses the Observer Pattern for client notifications.

Clients receive notifications for:

- Large withdrawals/deposits  
- Low balances  

All generated messages are stored in:

```
output/observer_emails.txt
```

---

# Assignment 4 – Event-Driven GUI (PySide6)

A complete GUI application was developed using **PySide6**, featuring:

### ✔ Client Lookup Window  
- Enter a client number  
- Display all accounts  
- Select account to view details  

### ✔ Account Details Window  
- Deposit & withdraw  
- Service charge calculation  
- Emits `balance_updated` signal  

### ✔ Event-Driven Programming  
Fully reactive using events, slots, and custom signals.

---

# Assignment 5 – Filtering, Documentation & Installer

## 🔍 Filtering Feature
The Client Lookup Window now supports filtering by:

- Account Number  
- Balance  
- Date Created  
- Type  

---

## 📘 Sphinx Documentation

Documentation generated using:

```
sphinx-quickstart
make html
```

Output at:

```
build/html/index.html
```

---

## 🛠 Executable Build

Built using:

```
pyinstaller --add-data "data/*:data" pixell_river.py
```

Output in:

```
dist/pixell_river/pixell_river.exe
```

---

## 📦 Windows Installer
Created using Inno Setup with:

- License agreement  
- Pre-install instructions  
- Desktop & Start Menu shortcuts  

Installer file:

```
PixellAccountManager-installer.exe
```

---

# Running the Application

## ➡ From Source
```
pip install PySide6
python A04_main.py
```

## ➡ From Installer
Run installer → follow steps → launch via shortcut.

---

# Project Structure

```
A04_main.py
pixell_river.py
bank_account/
client/
patterns/
user_interface/
ui_superclasses/
data/
logs/
output/
docs/
dist/
installer/
```

---

# Git Version Control

- Multiple meaningful commits  
- Assignment branches  
- Merged to main  
- .git folder included  

---

# ✅ Final Status

All requirements for Assignments **3, 4, and 5** completed successfully.
