from abc import ABC, abstractmethod

class IRecipient:
    @abstractmethod
    def create(self, userData):
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
