from app import app
from app.db import db
from app.ma import ma
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

migrate = Migrate(app, db)
jwt = JWTManager(app)

db.init_app(app)
ma.init_app(app)
