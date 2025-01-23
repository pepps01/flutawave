from abc import ABC, abstractmethod

class ISendMoney(ABC):
    @abstractmethod
    def transfer(self):
        return NotImplemented()