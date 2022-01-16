from abc import ABC,abstractmethod

class AbstractEngine(ABC):
    @abstractmethod
    def handle_message(self):
        pass


