from flask import (Blueprint,  request)
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies

from application.services.ValidationService import ValidationService
from application.src.repositories.TransactionRepository import TransactionRepository
from application.src.repositories.ChargeRepository import ChargeRepository
from application.services.ApiResource import ApiResource
from application.src.repositories.UserRepository import UserRepository

transaction = Blueprint('transaction', __name__, url_prefix='/transaction')

@transaction.route('/', methods=('GET', 'POST'))
@jwt_required()
def retrieve_transactions():
    if request.method == 'POST':
        charge= ChargeRepository.get_latest_charge()
        return ApiResource.response(data={"charge": charge}, message="Charge retrieved")