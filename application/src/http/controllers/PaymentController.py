from flask import (Blueprint,  request)
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies
from application import jwt_required
from application.src.repositories.UserRepository import UserRepository

payment_route = Blueprint('payment', __name__, url_prefix='/payment')

@payment_route.route('/payment', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        print("ran the application")
    
    if request.method == "GET":
        print("we found it")