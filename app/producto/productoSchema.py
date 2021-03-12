from app.ma import ma
from app.producto.productoModel import Product
from app.category.categoryModel import Category

class ProductSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Product
        load_instance = True
        load_only = ("category",)
        include_fk = True
        #ordered = True
        #fields = ("id","name","price","stock","category_id",)
