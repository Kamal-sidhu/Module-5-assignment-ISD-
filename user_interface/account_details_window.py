__author__ = "Kamaldeep kaur"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy


class AccountDetailsWindow(DetailsWindow):

    # ------------------------------------------------------------
    # SIGNAL for notifying ClientLookupWindow that balance changed
    # ------------------------------------------------------------
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes the AccountDetailsWindow with the given account.
        """
        super().__init__()

        # Validate received account
        if isinstance(account, BankAccount):
            # Make a COPY so changes do not affect original until confirmed
            self.account = copy.copy(account)

            # Show initial data
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # Connect buttons
            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)

        else:
            # Invalid object passed
            self.reject()

    # ------------------------------------------------------------
    # APPLY TRANSACTION (DEPOSIT OR WITHDRAW)
    # ------------------------------------------------------------
    @Slot()
    def on_apply_transaction(self):
        """Handles deposit and withdrawal actions."""

        # 1. Convert amount
        try:
            amount = float(self.transaction_amount_edit.text())
        except:
            QMessageBox.critical(
                self,
                "Transaction Failed",
                "Amount must be numeric."
            )
            self.transaction_amount_edit.setFocus()
            return

        # 2. Determine which button was pressed
        sender = self.sender()

        try:
            # Deposit
            if sender == self.deposit_button:
                action = "Deposit"
                self.account.deposit(amount)

            # Withdraw
            elif sender == self.withdraw_button:
                action = "Withdraw"
                self.account.withdraw(amount)

            # Update balance label
            self.balance_label.setText(f"${self.account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

            # EMIT SIGNAL — notify ClientLookupWindow
            self.balance_updated.emit(self.account)

        except Exception as ex:
            QMessageBox.critical(
                self,
                f"{action} Failed",
                f"{action} failed: {ex}"
            )
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    # ------------------------------------------------------------
    # EXIT BUTTON
    # ------------------------------------------------------------
    @Slot()
    def on_exit(self):
        """Closes window and returns to lookup window."""
        self.close()
