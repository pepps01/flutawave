from flask import (Blueprint,  request)
from application.services.ApiResource import ApiResource
from werkzeug.security import check_password_hash, generate_password_hash

gateway = Blueprint('gateway', __name__, url_prefix='/')

@gateway.route('/edit-profile', methods=['PUT'])
def update():
    if request.method == 'PUT':
        return ApiResource.response(data=["122"],message="Solved")

@gateway.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        return ApiResource.response(data=["122"],message="Solved")

@gateway.route('/', methods=['GET'])
def findAll():
    if request.method == 'GET':
        return ApiResource.response(data=["122"],message="Solved")

@gateway.route('/<id>', methods=['GET'])
def findOne(id):
    if request.method == 'GET':
        return ApiResource.response(data=["122"],message="Solved")
    
@gateway.route('/edit-profile', methods=['POST'])
def delete():
    if request.method == 'DELETE':
        return ApiResource.response(data=["122"],message="Solved")
