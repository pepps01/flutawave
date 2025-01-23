from flask import (Blueprint,  request)
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, current_user, create_refresh_token, set_access_cookies
from application.services.ApiResource import ApiResource
from werkzeug.security import check_password_hash, generate_password_hash
from application.services.ValidationService import ValidationService
from flask_cors import CORS, cross_origin
from application.src.repositories.UserRepository import UserRepository
from application import app, cross_origin

auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route('/register', methods=('GET', 'POST'))
@cross_origin(origins=["*"])
def register():
    if request.method == "POST":
        data = request.get_json()
        
        validated_data = ValidationService().validate_data(data)

        if(validated_data):
            UserRepository.create(validated_data)
            return ApiResource.response(data={validated_data},message="Email Registered Successfully")
        else:
            return ApiResource.errorResponse(data={},message="", error=True)

@auth.route('/login', methods=('GET', 'POST'))
@cross_origin(origins=["*"])
def login():
    if request.method == 'POST':
        data= request.get_json()
        user = UserRepository.getUserByEmailandPassword(data['email'], data['password'])

        if user is None:
            return ApiResource.errorResponse(message="User is not recognised", data={"error": "Unauthorised"}, status="error")
        else:
            access_token = create_access_token(identity=user.email)
            refresh_token = create_refresh_token(identity=user.email)
            app.logger.info("Program running correctly")

            response = ApiResource.errorResponse(message="Token validated Successfully", 
                data={
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user":user
                },
            )
            return response

@auth.route('/pin', methods=('GET', 'POST'))
def create_pin():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")
    
@auth.route('/otp', methods=('GET', 'POST'))
def sendOtp():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")

@auth.route('/resend-otp', methods=('GET', 'POST'))
def resendOtp():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")
    
@auth.route('/reset-request', methods=('GET', 'POST'))
def resetRequest():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")

    
@auth.route('/reset-password', methods=('GET', 'POST'))
def resetPassword():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")
    
@auth.route('/me', methods=('GET', 'POST'))
def get_user_id_by_token():
    if request.method == 'GET':
        return ApiResource.response(data=["122"],message="Solved")