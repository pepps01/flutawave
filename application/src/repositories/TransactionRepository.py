from application.src.interfaces.ITransaction import ITransaction
from application.models import Transaction
from application import db

class TransactionRepository(ITransaction):
    def create(self, transactionData):
        
        transaction = Transaction(
            user_id = transactionData['user_id'],
            send_money_id = transactionData['send_money_id'],
            status="processing",
            transaction_reference='processing',
            transaction_name="Transaction"
        )
        db.session.add(transaction)
        db.session.commit()

        return True
    
    def findAll(self):
        transactions = Transaction.query.all()
        transactionsData = []

        # transpose data
        for user in transactions:
            transactionsData.push(user.firstname)
        return transactionsData
    
    def findOne(self, id):
        transaction = Transaction.query.filter_by(id=id).first()
        return transaction
    
    def update(self, id,transactionData=[]):
        transaction= Transaction.query.filter_by(id=id).first()
        if transactionData['firstname']:
            transaction.firstName =  transactionData['firstname']
        if transactionData['lastname']:
            transaction.lastname = transactionData['lastname']
        
        db.sesssion.commit()
        return True
    
    
    def delete(self, id):
        transaction =  Transaction.query.get(id=id)
        if not transaction:
            return {"message": "User not found"}
        # delete the user 
        db.session.delete(transaction)
        db.session.commit()

        return {'message': "user deleted successfully"}