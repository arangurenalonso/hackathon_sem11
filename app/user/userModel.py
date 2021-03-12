from app.db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(150))
    rol_id = db.Column(db.Integer, index=True)
    #
    posts = db.relationship('Post', lazy='dynamic', primaryjoin='User.id == Post.user_id')

    def __repr__(self):
        return f'User: {self.username}'

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
