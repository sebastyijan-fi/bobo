# server.py
from flask import Flask
from flask_jwt_extended import JWTManager
from utils.extensions import db, cors, migrate
from routes.userRoutes import user_bp
from routes.taskRoutes import task_bp
from routes.auth import auth_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Enable CORS
    cors.init_app(app)

    # Set the configuration for SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = os.getenv('SECRET_KEY')




    # Initialize SQLAlchemy and Flask-Migrate
    db.init_app(app)
    migrate.init_app(app, db)

    jwt = JWTManager(app)

    # Register the blueprints for our routes
    app.register_blueprint(user_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=2222)
