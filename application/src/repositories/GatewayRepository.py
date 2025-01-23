from application.src.interfaces.IGateway import IGateway
from application.models import Gateway
from application import db

class GatewayRepository(IGateway):
    def __init__(self):
        pass

    def create(self, data):
        gateway = Gateway(
            api_key=data['api_key'],
            name= data['name'],
            code= data['code']
        )
        db.session.add(gateway)
        db.session.commit()

        return True
        



