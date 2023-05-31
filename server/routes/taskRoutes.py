from flask import Blueprint, request, jsonify
from models.Task import Task
from models.User import User
from utils.extensions import db

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/create-task', methods=['POST'])
def create_task():
    data = request.get_json()
    user_id = data.get('user_id')
    description = data.get('description')
    if not user_id or not description:
        return {'error': 'Required fields are missing'}, 400
    new_task = Task(user_id=user_id, description=description)
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400
    return {'message': 'Task created successfully'}, 201

# Retrieve all tasks for a specific user
@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    user_id = request.args.get('user_id')
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_dict() for task in tasks]), 200

# Retrieve a specific task by its ID
@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task:
        return jsonify(task.to_dict()), 200
    else:
        return {'error': 'Task not found'}, 404

# Update a specific task
@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get(task_id)
    if task:
        task.description = data.get('description', task.description)
        db.session.commit()
        return {'message': 'Task updated successfully'}, 200
    else:
        return {'error': 'Task not found'}, 404

# Delete a specific task
@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return {'message': 'Task deleted successfully'}, 200
    else:
        return {'error': 'Task not found'}, 404
