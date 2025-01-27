from application.src.interfaces.IRecipient import IRecipient
from application.models import Recipient
from application import db
from application.models import User

class RecipientRepository(IRecipient):
    def __init__(self):
        super().__init__()

    def create(self, data):
        recipient = Recipient(
            recipient_country= data['recipient_country'],
            delivery_method= data['delivery_method'],
            email= data['email'],
            bank_name = data['bank_name'],
            account_number = data['account_number'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            beneficiary_address = data['beneficiary_address'],
            city = data['city'],
            state = data['state'],
            postal_code = data['postal_code'],
            user_id = data["user_id"]
        )

        db.session.add(recipient)
        db.session.commit()
        return True

    def findOne(self, id):
        recipient = Recipient.query.filter(id=id).first()
        # transform the data from recipient
        recipientData = {
            "recipient_country": recipient.recipient_country,
            "delivery_method":  recipient.delivery_method,
            "email": recipient.email,
            "bank_name": recipient.bank_name,
            "account_number": recipient.account_number,
            "firstname": recipient.firstname,
            "lastname": recipient.lastname,
            "beneficiary_address":recipient.beneficiary_address,
            "city":recipient.city,
            "state": recipient.state,
            "postal_code": recipient.postal_code,
            "user_id" : recipient.user_id
        }
        
        return recipient

    def findAll(self, user_id):
        recipients = Recipient.query.filter_by(user_id=user_id).all()
        recipientData = []
            
        for recipient in recipients:
            recipientData.append(
                {
                "id": recipient.id,
                "firstname": recipient.firstname,
                "lastname": recipient.lastname,
                "email": recipient.email,
                "account_number": recipient.account_number,
                "beneficiary_address": recipient.beneficiary_address,
                "delivery_method": recipient.delivery_method,
                "bank_name": recipient.bank_name,
                "recipient_country": recipient.recipient_country,
                "state": recipient.state,
                "postal_code": recipient.postal_code,
                "email" : User.query.filter_by(id=recipient.user_id).first().email
            }
        )
            
        if recipientData is None:
            return True
        return recipientData

    def findAllById(self, user_id):
        recipients = Recipient.query.filter(email=user_id).get()
        # get the needed data from the db

        # transform the data from recipient resource
        return recipients

    def update(self,id, userDetails):
        recipient = Recipient.query.filter_by(id=id).first()

        if userDetails['bank_name']:
            recipient.bank_name = userDetails['bank_name']
            # test with the others

            db.session.update(recipient)
            db.session.commit()
        return True
        # what happens when if we see

    def delete(self, id):
        recipient =  Recipient.query.get(id=id)
        if not recipient:
            return {"message": "Recipient not found"}
        # delete the user 
        db.session.delete(recipient)
        db.session.commit()
        return {'message': "recipient deleted successfully"}
