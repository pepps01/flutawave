from flask import (Blueprint,  request)
from application.services.ApiResource import ApiResource
from application.services.ValidationService import ValidationService
from application.src.repositories.SendMoneyRepository import SendMoneyRepository
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies

send_money = Blueprint('sendmoney', __name__, url_prefix='/send-money')

@send_money.route('/send-money', methods=['POST'])
def sendMoney():
    if request.method == 'POST':
        data = request.get_json()

        validated_data = ValidationService()

        if validated_data:
            return ApiResource.response(data=["122"],message="Solved")

@send_money.route('/request_money', methods=['GET'])
def request_money():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")
