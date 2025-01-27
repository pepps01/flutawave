from application.src.interfaces.IUser import IUser
from application.models import User, Profile
from application import db
from werkzeug.security import check_password_hash, generate_password_hash
from application import get_jwt_identity
class UserRepository(IUser):
    def __init__(self):
        pass

    def create(self, data):
        usercase = User.query.filter_by(email=data['email']).first()

        if usercase:
            usercase = {"email": usercase.email, "checked":True }
            return usercase 

        user = User(
            email= data['email'],
            password= generate_password_hash(data['password']),
            pin= data['pin']
        )

        db.session.add(user)
        db.session.commit()

        last_created_user = User.query.order_by(User.date_added.desc()).first()
        profile = Profile(
            user_id=last_created_user.id
        )
        db.session.add(profile)
        db.session.commit()

        userData={
            "email": last_created_user.email,
            "checked":False
        }
        return userData
    
    def createPin(self, data):
        email =  data["email"]
        pin =  data["pin"]

        print("data sets",data)

        user=  User.query.filter_by(email=email).first()
        if user:
            user.pin = pin
            db.session.commit()
            print(f"user pin updated {user.pin}")
            return True
        else:
            print("User not found")

    
    def confirmPin(self, data):
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
    
    
    def get_email_by_id(self, id):
         user = User.query.filter_by(id=id).first()
         return user
    
    def getUserByEmailandPassword(self, userEmail, password):
         user = User.query.filter_by(email=userEmail).first()
         userData = {
                "id": user.id,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "email": user.email,
                "is_logged": user.is_logged,
                "date_added": user.date_added,
                "date_updated": user.date_updated,
         }
         if not user:
             return None
         return userData


    def get_current_user_id(self):
        user_email = get_jwt_identity()
        user= User.query.filter_by(email=user_email).first()
        return user.id



