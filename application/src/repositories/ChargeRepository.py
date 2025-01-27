from application.src.interfaces.ICharge import ICharge
from application.models import Charge

class ChargeRepository(ICharge):
    DEFAULT_CHARGE=0.05
    def __init__(self):
        pass
    
    def get_latest_charge():
        return ChargeRepository.DEFAULT_CHARGE
    
    def update(self):
        pass

    def delete(self):
        pass
    
    def create(self, userData):
        pass
    
    def findAll(self):
        pass
    
    def findOne(self, id):
        pass

        