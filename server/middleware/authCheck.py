from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models.User import User

def auth_check(func):
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return func(*args, **kwargs)
    return wrapper
