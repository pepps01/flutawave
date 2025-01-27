from flask import (Blueprint,  request)
from application.services.ApiResource import ApiResource
from werkzeug.security import check_password_hash, generate_password_hash
from application import get_jwt_identity, jwt_required
from application.src.repositories.ProfileRepository import ProfileRepository
# from application import app, cross_origin, jwt_required,  get_jwt_identity,jwt

profile = Blueprint('profile', __name__, url_prefix='/profile')

@profile.route('/edit-profile', methods=['PUT'])
@jwt_required()
def editprofile():
    if request.method == 'PUT':
        data= request.get_json()
        ProfileRepository.create(data)
        return ApiResource.response(data="Profile updated successfully",message="Profile updated successfully")

@profile.route('/', methods=['GET'])
@jwt_required()
def get():
    if request.method == "GET":
        return ApiResource.response(data="",message="Profile retrieved successfully")
    
@profile.route('/', methods=['POST'])
@jwt_required()
def create():
    if request.method == "GET":
        return ApiResource.response(data=[],message="Profile created successfully")
    
