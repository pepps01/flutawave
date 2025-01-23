from application.src.interfaces.IUser import IUser
from application.models import User, Profile
from application import db

class UserRepository(IUser):
    def __init__(self):
        pass

    def create(self, data):
        db.session.commit()
        return True
    
    def createPin(self, data):
        email =  data["email"]
        code =  data["code"]

        user=  User.query.filter_by(email=email).first()
        user.code = int(code)
        return True
    
    def createPin(self, data):
        email =  data["email"]
        code =  data["code"]

        user=  User.query.filter( code = code).first()
        user.code = int(code)
        return True
    
    def findAll(self):
        # db.session.execute()
        users = User.query.all()
        userData = []
        for user in users:
            userData.push(user.firstname)
        
        return userData
    
    def findOne(self, id):
        user = User.query.filter_by(id=id).first()
        return user
    
    def update(self, id, userData=...):
        user= User.query.filter_by(id=id).first()
        if userData['firstname']:
            user.firstName =  userData['firstname']
        if userData['lastname']:
            user.lastname = userData['lastname']
        
        db.sesssion.commit()
        return True
    
    def delete(self, id):
        user =  User.query.get(id=id)
        if not user:
            return {"message": "User not found"}
        # delete the user 
        db.session.delete(user)
        db.session.commit()
        return {'message': "user deleted successfully"}
        
    def getUserByEmail(self, userEmail):
         user = User.query.filter_by(email=userEmail).first()
         return user
    
    def getUserByEmailandPassword(self, userEmail, password):
         user = User.query.filter_by(email=userEmail).first()

         if not user:
             return None
         return user

