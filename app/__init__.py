from flask import Flask
from pathlib import Path
from config import Config
from flask_restx import Api

from app.category.categoryResource import CategoryResource, CategoriesResource, category_ns, categories_ns

from app.producto.productoResource import ProductResource, producto_ns


app = Flask(__name__)
app.config.from_object(Config)

authorizations = {
        'Bearer Auth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
        }
}

api = Api(app, 
        title='Pachaqtec Blog',
        version='v1',
        description='RESTApi Blog',
        prefix='/api/', doc='/swagger/',
        contact='Jeancarlos De la cruz',
        security='Bearer Auth',
        authorizations=authorizations,
        contact_url='https://www.linkedin.com/in/jeancarlosdelacruz/')

api.add_namespace(category_ns)
category_ns.add_resource(CategoryResource, '/<int:id>')

api.add_namespace(categories_ns)
categories_ns.add_resource(CategoriesResource, '')


api.add_namespace(producto_ns)
producto_ns.add_resource(ProductResource,'')



from app.category import categoryModel
from app.producto import productoModel

