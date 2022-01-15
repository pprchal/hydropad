from abc import ABC,abstractmethod

class AbstractEngine(ABC):
    @abstractmethod
    def executeCommand(self):
        pass

