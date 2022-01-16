from abc import ABC,abstractmethod

class AbstractEngine(ABC):
    @abstractmethod
    def handleMessage(self):
        pass


