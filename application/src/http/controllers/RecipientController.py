from flask import (Blueprint,  request)
from application.services.ApiResource import ApiResource
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies

from application.src.repositories.RecipientRepository import RecipientRepository

recipient = Blueprint('recipient', __name__, url_prefix='/recipient')

@recipient.route('/edit', methods=['PUT'])
def update():
    if request.method == 'PUT':
        return ApiResource.response(data=["122"],message="Solved")

@recipient.route('/', methods=['GET'])
def findAll():
    if request.method == "GET":
        return ApiResource.response(data={"key":"122"},message="Solved")

@recipient.route('/<id>', methods=['GET'])
def findOne():
    if request.method == "GET":
        return ApiResource.response(data={"key":"122"},message="Solved")

@recipient.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")
    
@recipient.route('/delete', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        return ApiResource.response(data=["122"],message="Solved")