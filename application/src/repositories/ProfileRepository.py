from application.src.interfaces.IProfile import IProfile
from application.models import Profile

class ProfileRepository(IProfile):
    def __init__(self):
        pass

    def create(self, profileDetail):
        return NotImplemented()
    
    def updateProfile(self, id, profileDetails):
        return NotImplemented()
    
    def findOne(self, id):
        return NotImplemented()