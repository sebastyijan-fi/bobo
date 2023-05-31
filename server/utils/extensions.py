# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
