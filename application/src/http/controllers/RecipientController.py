from flask import (Blueprint,  request)
from application.services.ApiResource import ApiResource
from werkzeug.security import check_password_hash, generate_password_hash
# from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies
from application.src.repositories.RecipientRepository import RecipientRepository
from application import jwt_required, get_jwt_identity
from application.src.repositories.UserRepository import UserRepository

recipient = Blueprint('recipient', __name__, url_prefix='/recipient')


@recipient.route('/edit', methods=['PUT'])
@jwt_required()
def update():
    if request.method == 'PUT':
        data=request.get_json()
        recipients = RecipientRepository().update(1,data)
        return ApiResource.response(data=[],message="Recipient Updated successfully")

@recipient.route('/', methods=['GET'])
@jwt_required()
def findAll():
    if request.method == "GET":
        # the data would be gotten from jwt
        data =6 
        recipients = RecipientRepository().findAll(data)
        return ApiResource.response(data={"recipients":recipients},message="Recipients retrieved successfully")

@recipient.route('/<id>', methods=['GET'])
@jwt_required()
def findOne():
    if request.method == "GET":
        id =6 
        recipients = RecipientRepository().findOne(id)
        return ApiResource.response(data={"recipients":recipients},message="Recipients retrieved successfully")

@recipient.route('/create', methods=['POST'])
@jwt_required()
def create():
    if request.method == 'POST':
        data = request.get_json()
        RecipientRepository().create(data)
        return ApiResource.response(data="Recipient Created Successfully",message="Recipient Created Successfully")
    
@recipient.route('/delete', methods=['DELETE'])
@jwt_required()
def delete():
    if request.method == 'DELETE':
        return ApiResource.response(data=["122"],message="Recipient deleted Successfully")
