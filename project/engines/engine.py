from abc import ABC,abstractmethod
from config import config

class AbstractEngine(ABC):
    @abstractmethod
    def handleMessage(self):
        pass


