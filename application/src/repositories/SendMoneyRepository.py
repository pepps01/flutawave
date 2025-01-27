from application.src.interfaces.ISendMoney import ISendMoney
from application.models import SendMoney, Transaction
from application import db
from application.services.HelperService import HelperService
from application.src.repositories.ChargeRepository import ChargeRepository

class SendMoneyRepository(ISendMoney):
    def __init__(self):
        super().__init__()

    def transfer(self,data):
        # charges to be deducted from the recievers amount
        sendMoney = SendMoney(
            user_id=data['user_id'],
            send_amount= data['send_amount'],
            reciever_amount=data['reciever_amount'],
            sender_currency = data['sender_currency'],
            reciever_currency = data['reciever_currency'],
            recipient_id = data['recipient_id'],
            exchange_rate = data['exchange_rate'],
            charge_fee= self.__add_charges(data['charge_fee']),
            delivery_method = data['delivery_method'],
            transfer_reference = HelperService.convert(),
        )

        db.session.add(sendMoney)
        db.session.commit()

        # testing send money
        transaction = Transaction(
            user_id = data['user_id'],
            send_money_id = sendMoney.id, 
        )

        db.session.add(transaction)
        db.session.commit()

        return True
    
        # what if there are issues 
    def __add_charges(self,data):
        return ChargeRepository().get_latest_charge() * data
    

