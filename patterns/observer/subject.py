class Subject:
    """
    Subject base class for the Observer Pattern.
    Maintains a list of observers and notifies them of events.
    """

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """Add a new observer."""
        self._observers.append(observer)

    def detach(self, observer):
        """Remove an observer if it exists."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message):
        """Notify all observers with the given message."""
        for obs in self._observers:
            obs.update(message)
