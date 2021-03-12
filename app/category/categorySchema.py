from app.ma import ma
from app.category.categoryModel import Category
from app.producto.productoSchema import ProductSchema


class CategorySchema(ma.SQLAlchemyAutoSchema):
    productos = ma.Nested(ProductSchema, many=True)

    class Meta:
        model = Category
        load_instance = True
        include_fk = True
