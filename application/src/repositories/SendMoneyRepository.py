from application.src.interfaces.ISendMoney import ISendMoney
from application.models import SendMoney, Transaction
from application import db

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
            reciever_currency = data['reciver_currency'],
            recipient_id = data['recipient_id'],
            exchange_rate = data['exchange_rate'],
            charge_fee= data['charge_fee'],
            delivery_method = data['delivery_method'],
            transfer_reference = data['transfer_reference'],
        )

        db.session.add(sendMoney)
        db.session.commit()

        # testing send money
        transaction =Transaction(
            user_id = data['user_id'],
            send_money_id = sendMoney.id
        )

        db.session.add(transaction)
        db.session.commit()

        return True
    
        # what if there are issues 
    

