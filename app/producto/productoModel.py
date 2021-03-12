from app.db import db
from slugify import slugify

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True, default=None)
    price = db.Column(db.Float, index=True, default=1)
    stock = db.Column(db.Integer, index=True, default =1)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    status = db.Column(db.Integer, index=True, default=1)
    slug = db.Column(db.String(120), index=True, default=None)
    prodcuto_img=db.Column(db.String(200), default=None)
    #
    category = db.relationship('Category', )


    def __repr__(self):
        return f'Product: {self.name}'
        
    def slug_create(self):
        self.slug = slugify(self.name)



