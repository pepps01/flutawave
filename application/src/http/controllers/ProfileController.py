from flask import (Blueprint,  request)
from application.services.ApiResource import ApiResource
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies

profile = Blueprint('profile', __name__, url_prefix='/profile')

@profile.route('/edit-profile', methods=['PUT'])
def editprofile():
    if request.method == 'PUT':
        return ApiResource.response(data=["122"],message="Solved")

@profile.route('/', methods=['GET'])
def get():
    if request.method == "GET":
        return ApiResource.response(data={"key":"122"},message="Solved")
    
@profile.route('/', methods=['POST'])
def create():
    if request.method == "GET":
        return ApiResource.response(data={"key":"122"},message="Solved")
    
