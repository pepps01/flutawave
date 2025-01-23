from flask import (Blueprint,  request)
from application.services.ApiResource import ApiResource
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies

charge = Blueprint('charge', __name__, url_prefix='/charge')

@charge.route('/edit-profile', methods=['PUT'])
def update():
    if request.method == 'PUT':
        return ApiResource.response(data=["122"],message="Solved")

@charge.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")

@charge.route('/', methods=['GET'])
def findAll():
    if request.method == 'GET':
        return ApiResource.response(data=["122"],message="Solved")

@charge.route('/<id>', methods=['GET'])
def findOne():
    if request.method == 'GET':
        return ApiResource.response(data=["122"],message="Solved")
    
@charge.route('/edit-profile', methods=['POST'])
def delete():
    if request.method == 'DELETE':
        return ApiResource.response(data=["122"],message="Solved")
