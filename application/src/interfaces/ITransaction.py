from abc import ABC, abstractmethod

class ITransaction:
    @abstractmethod
    def create(self, transactionData):
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
