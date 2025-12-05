from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime


class Client(Observer):
    """
    Client class now functions as an Observer.
    Receives notifications about unusual account activity.
    """

    def __init__(self, client_number, first_name, last_name, email):
        self.client_number = client_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def update(self, message):
        """
        Called by Subject.notify().
        Writes a simulated email to observer_emails.txt.
        """
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        body = (
            f"Notification for {self.client_number}: "
            f"{self.first_name} {self.last_name}: {message}"
        )

        simulate_send_email(subject, body)
