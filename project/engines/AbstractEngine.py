from abc import ABC,abstractmethod
from project.Config import config

class AbstractEngine(ABC):
    @abstractmethod
    def handleMessage(self):
        pass


