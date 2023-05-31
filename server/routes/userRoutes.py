from flask import Blueprint, request
from models.User import User
from utils.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return {'error': 'Required fields are missing'}, 400

    # Check if username or email already exists
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()

    if existing_user:
        return {'error': 'Username or email already exists'}, 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return {'error': str(e)}, 500

    return {'message': 'User registered successfully'}, 201

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user_id = get_jwt_identity()  # Get the id of the current user from the access token
    if current_user_id != user_id:
        return {'error': 'Cannot update a different user'}, 401

    data = request.get_json()
    user = User.query.get(user_id)

    if not user:
        return {'error': 'User not found'}, 404

    # Update user fields from request data, if present
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    if 'password' in data:
        user.set_password(data['password'])

    db.session.commit()
    return {'message': 'User updated successfully'}, 200


@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    current_user_id = get_jwt_identity()  # Get the id of the current user from the access token
    if current_user_id != user_id:
        return {'error': 'Cannot delete a different user'}, 401

    user = User.query.get(user_id)

    if not user:
        return {'error': 'User not found'}, 404

    db.session.delete(user)
    db.session.commit()
    return {'message': 'User deleted successfully'}, 200