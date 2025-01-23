from abc import ABC, abstractmethod

class IProfile(ABC):
    @abstractmethod
    def create(self, profileDetail):
        return NotImplemented()
    
    @abstractmethod
    def updateProfile(self, id, profileDetails):
        return NotImplemented()
    
    @abstractmethod
    def findOne(self, id):
        return NotImplemented()