from application import db, bycrypt
import datetime
from hmac import compare_digest

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=True)
    lastname = db.Column(db.String(20), nullable=True)
    pin = db.Column(db.String(20),nullable=True)
    is_logged = db.Column(db.Boolean)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    date_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    profile = db.relationship("Profile", backref="profiles", lazy=True)
    transactions = db.relationship("Transaction", backref="transactions", lazy=True)
    send_money = db.relationship("SendMoney", backref="send_money", lazy=True)

    def __repr__(self):
        return "<User %r>" % self.firstname
    
    def check_password(self, password):
        return compare_digest(bycrypt.generate_password_hash(password), "password")


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    date_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    user = db.relationship('User', back_populates='recipients')

    def __repr__(self):
        return "<Profile %r>" % self.phone


# Address the foreigh key issues with the profile
# use enums
class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    transaction_name = db.Column(db.String(20), nullable=True)
    status = db.Column(db.String(20), nullable=True)
    transaction_reference = db.Column(db.String(20), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    send_money_id = db.Column(db.Integer, db.ForeignKey("send_money.id"), nullable=True)
    transaction_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    date_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return "<Transaction %r>" % self.status


class Charge(db.Model):
    __tablename__ = "charges"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return "<Charge %r>" % self.name


class SendMoney(db.Model):
    __tablename__ = "send_money"

    id = db.Column(db.Integer, primary_key=True)
    send_amount = db.Column(db.Float, nullable=True)
    reciever_amount = db.Column(db.Float, nullable=True)
    sender_currency = db.Column(db.String(100), nullable=True)
    reciever_currency = db.Column(db.String(100), nullable=True)
    recipient_id = db.Column(db.Integer, db.ForeignKey('recipients.id'), nullable=True)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'),nullable=True)
    exchange_rate = db.Column(db.Float, nullable=True)
    charge_fee = db.Column(db.Float, nullable=True)
    delivery_method = db.Column(db.String(100), nullable=True)
    transfer_reference = db.Column(db.String(100), nullable=True)

    # Relationship: A user has many posts
    recipient = db.relationship('Recipient', back_populates='recipients')
    user = db.relationship('User', back_populates='users')
    
    def __repr__(self):
        return "<SendMoney %r>" % self.transfer_reference
    

class Gateway(db.Model):
    __tablename__ = "gateways"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    code = db.Column(db.String(20), nullable=True)
    api_key = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return "<SendMoney %r>" % self.name


class Recipient(db.Model):
    __tablename__ = "recipients"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=True)
    lastname = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(50),  nullable=False)
    account_number = db.Column(db.String(50),nullable=True)
    beneficiary_address = db.Column(db.String(125),nullable=True)
    delivery_method = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(150),nullable=True)
    bank_name = db.Column(db.String(150),nullable=True)
    recipient_country = db.Column(db.String(150),nullable=True)
    state = db.Column(db.String(150),nullable=True)
    postal_code = db.Column(db.String(150),nullable=True)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'),nullable=True)

    user = db.relationship("User", backref="users", lazy=True)
    sendMoney = db.relationship('SendMoney', back_populates='send_money')

    def __repr__(self):
        return "<Recipient %r>" % self.name
    
class Payment(db.Model):
    __tablename__ = "selectors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return "<Payment %r>" % self.name