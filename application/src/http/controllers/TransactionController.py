from flask import (Blueprint,  request)
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies

from application.services.ValidationService import ValidationService
from application.src.repositories.TransactionRepository import TransactionRepository

transaction = Blueprint('transaction', __name__, url_prefix='/transaction')

@transaction.route('/', methods=('GET', 'POST'))
def retrieve_transactions():
    if request.method == 'POST':
        print("ran the application")
    
    if request.method == "GET":
        print("we found it")

@transaction.route('/user-transaction', methods=('GET', 'POST'))
def retrieve_single_user_transactions():
    if request.method == 'POST':
        print("ran the application")
    
    if request.method == "GET":
        print("we found it")

@transaction.route('/banks', methods=('GET', 'POST'))
def banks_transactions():
    if request.method == "GET":
        print("banks")