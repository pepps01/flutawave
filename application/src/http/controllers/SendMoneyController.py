from flask import (Blueprint,  request)
from application.services.ApiResource import ApiResource
from application.services.ValidationService import ValidationService
from application.src.repositories.SendMoneyRepository import SendMoneyRepository
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies
from application.services.MailService import MailService
from application.src.repositories.UserRepository import UserRepository

send_money = Blueprint('sendmoney', __name__, url_prefix='/send-money')

@send_money.route('/transfer', methods=['POST'])
def sendMoney():
    if request.method == 'POST':
        data = request.get_json()
        validated_data = ValidationService().validate_data(data)
        # if you dont have all the request response the errors 
        if validated_data:
            SendMoneyRepository().transfer(data)
            MailService.send(UserRepository().get_email_by_id(data['user_id']))
            return ApiResource.response(data="",message="Money Transfered Successfully")
        else:
            return ApiResource.errorResponse(message="Error response")

@send_money.route('/request_money', methods=['GET'])
def request_money():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")