from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.User import User
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401


    token = create_access_token(identity=user.id)
    return jsonify(access_token=token), 200
