__author__ = "Kamaldeep Kaur"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount


class ClientLookupWindow(LookupWindow):

    def __init__(self):
        super().__init__()

        # Load client + account dictionaries
        self.client_listing, self.accounts = load_data()

        # Existing GUI connections
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)

        # NEW FOR ASSIGNMENT 5:
        self.filter_button.clicked.connect(self.on_filter_clicked)
        self.filter_button.setEnabled(False)     # Disabled until a client loads


    # --------------------------------------------------------
    # LOOKUP CLIENT BUTTON CLICKED
    # --------------------------------------------------------
    def on_lookup_client(self):
        # Reset display from parent class
        self.reset_display()

        # Reset filtering (NEW)
        self.toggle_filter(False)

        # Convert client number
        try:
            client_number = int(self.client_number_edit.text())
        except:
            QMessageBox.critical(self, "Invalid Client Number",
                                 "Client Number must be numeric.")
            return

        # Client not found
        if client_number not in self.client_listing:
            QMessageBox.information(self, "Client Not Found",
                                    f"Client Number {client_number} does not exist.")
            return

        # Client FOUND
        client = self.client_listing[client_number]
        self.client_info_label.setText(
            f"{client.last_name}, {client.first_name} [{client.client_number}]"
        )

        # Enable filtering (NEW)
        self.filter_button.setEnabled(True)

        # Populate the table with this client's accounts
        self.account_table.setRowCount(0)

        for acct in self.accounts.values():
            if acct.client_number == client_number:
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)

                acct_num_item = QTableWidgetItem(str(acct.account_number))
                acct_num_item.setTextAlignment(Qt.AlignCenter)

                bal_item = QTableWidgetItem(f"${acct.balance:,.2f}")
                bal_item.setTextAlignment(Qt.AlignRight)

                date_item = QTableWidgetItem(str(acct.date_created))
                date_item.setTextAlignment(Qt.AlignCenter)

                type_item = QTableWidgetItem(acct.__class__.__name__)
                type_item.setTextAlignment(Qt.AlignCenter)

                self.account_table.setItem(row, 0, acct_num_item)
                self.account_table.setItem(row, 1, bal_item)
                self.account_table.setItem(row, 2, date_item)
                self.account_table.setItem(row, 3, type_item)

        self.account_table.resizeColumnsToContents()


    # --------------------------------------------------------
    # FILTER BUTTON CLICKED (NEW - Assignment 5)
    # --------------------------------------------------------
    def on_filter_clicked(self):
        button_text = self.filter_button.text()

        if button_text == "Apply Filter":
            col_index = self.filter_combo_box.currentIndex()
            search_text = self.filter_edit.text().strip().lower()

            # Loop through rows and hide those that do not match
            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, col_index)

                if item is None or search_text not in item.text().lower():
                    self.account_table.setRowHidden(row, True)
                else:
                    self.account_table.setRowHidden(row, False)

            self.toggle_filter(True)

        else:
            # Reset to show all rows
            self.toggle_filter(False)


    # --------------------------------------------------------
    # TOGGLE FILTER (NEW - Assignment 5)
    # --------------------------------------------------------
    def toggle_filter(self, filter_on: bool):

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")

        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            # Show all rows again
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")


    # --------------------------------------------------------
    # TEXT CHANGED — CLEAR TABLE
    # --------------------------------------------------------
    def on_text_changed(self, text):
        self.account_table.setRowCount(0)
        self.filter_button.setEnabled(False)


    # --------------------------------------------------------
    # SELECT ACCOUNT FROM TABLE
    # --------------------------------------------------------
    @Slot(int, int)
    def on_select_account(self, row: int, column: int):
        item = self.account_table.item(row, 0)
        if item is None:
            QMessageBox.warning(self, "Invalid Selection", "Invalid account selection.")
            return

        account_number_text = item.text().strip()

        if account_number_text == "":
            QMessageBox.warning(self, "Invalid Selection", "Invalid account selection.")
            return

        account_number = int(account_number_text)

        if account_number not in self.accounts:
            QMessageBox.critical(self, "Account Error",
                                 f"Bank Account {account_number} does not exist.")
            return

        # Found the account — create details dialog
        account_obj = self.accounts[account_number]

        dialog = AccountDetailsWindow(account_obj)

        # connect signal
        dialog.balance_updated.connect(self.update_data)

        dialog.exec_()


    # --------------------------------------------------------
    # SLOT FOR RECEIVING SIGNAL FROM AccountDetailsWindow
    # --------------------------------------------------------
    def update_data(self, account: BankAccount):
        """Updates GUI table and accounts dictionary after transaction."""
        for row in range(self.account_table.rowCount()):
            acct_num = int(self.account_table.item(row, 0).text())
            if acct_num == account.account_number:
                self.account_table.item(row, 1).setText(f"${account.balance:,.2f}")

        self.accounts[account.account_number] = account
        update_data(account)
