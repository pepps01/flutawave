from application.src.interfaces.IRecipient import IRecipient
from application.models import Recipient
from application import db

class RecipientRepository(IRecipient):
    def __init__(self):
        super().__init__()

    def create(self, data):
        recipient = Recipient(
            # subject to change
            recipient_country=data['country'],
            deliveryMethod=data['delivery_method'],
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

    def findOne(self):
        recipient = Recipient.query.filter(id=id).first()
        # transform the data from recipient
        return recipient


    def findAll(self, email):
        recipients = Recipient.query.filter(email=email).get()
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
