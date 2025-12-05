from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer base class for Assignment 3.
    All observers must implement the update() method.
    """

    @abstractmethod
    def update(self, message):
        pass
