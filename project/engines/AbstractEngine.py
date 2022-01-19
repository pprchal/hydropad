from abc import ABC,abstractmethod

class AbstractEngine(ABC):
    @abstractmethod
    def handle_message(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
    


