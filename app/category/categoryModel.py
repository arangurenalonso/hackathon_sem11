from app.db import db
from sqlalchemy.sql import func
from slugify import slugify


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True, default=None)
    status = db.Column(db.Integer, index=True, default=1)
    slug = db.Column(db.String(120), index=True, default=None)
    #
    productos = db.relationship('Product', lazy='dynamic', primaryjoin='Category.id == Product.category_id')

    def __repr__(self):
        return f'Category: {self.name}'

    def slug_create(self):
        self.slug = slugify(self.name)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
