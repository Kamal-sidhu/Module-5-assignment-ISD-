"""
Description: Main entry point for Assignment 4 GUI application.
Launches the Client Lookup Window for PiXELL-River Financial.
"""

__author__ = "Kamaldeep Kaur"
__version__ = "1.0.0"
__credits__ = "ACE Faculty"

from PySide6.QtWidgets import QApplication
from user_interface.client_lookup_window import ClientLookupWindow
import sys


def main():
    """Start the Qt application and open the Client Lookup Window."""
    app = QApplication(sys.argv)

    window = ClientLookupWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
