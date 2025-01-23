from abc import ABC, abstractmethod

# Defining User with Abstract Classes
class IUser(ABC):
    @abstractmethod
    def create(self, userData):
        return NotImplemented()
    
    @abstractmethod
    def createPin(self, code):
        return NotImplemented()
    
    @abstractmethod
    def confimPin(self, code):
        return NotImplemented()
    
    @abstractmethod
    def findAll(self):
        return NotImplemented()
    
    @abstractmethod
    def findOne(self, id):
        return NotImplemented()
    
    @abstractmethod
    def update(self, id,userData=[]):
        return NotImplemented()
    
    @abstractmethod
    def delete(self, id):
        return NotImplemented()
    
    @abstractmethod
    def getUserByEmail(self, userEmail):
        return NotImplemented()