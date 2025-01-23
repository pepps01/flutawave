from abc import ABC, abstractmethod

class ICharge(ABC):
    @abstractmethod
    def create(self, userData):
        return NotImplemented()
    
    @abstractmethod
    def findAll(self):
        return NotImplemented()
    
    @abstractmethod
    def findOne(self, id):
        return NotImplemented()