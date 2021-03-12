from flask_restx import Resource, fields, Namespace,reqparse
from flask import request, current_app
from flask_jwt_extended import jwt_required
from os import path
from app.db import db
#from app import app
from app.producto.productoModel import Product
from app.producto.productoSchema import ProductSchema
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from uuid import uuid4

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('img', location='files',type=FileStorage, required=True)
upload_parser.add_argument('name', type=str, required=True)
upload_parser.add_argument('stock', type=int, required=True)
upload_parser.add_argument('price', type=float, required=True)
upload_parser.add_argument('category_id', type=int, required=True)


producto_ns = Namespace('producto', description='producto end point')


producto_schema = ProductSchema()
producto_schema_many=ProductSchema(many=True)


#content type json
insert_product_data = producto_ns.model(
    "Insert_product_data",
    {
        "name": fields.String(description="Nombre del producto", required=True),
        "stock": fields.Integer(description="Cantidad en Stock", required=True),
        "price": fields.Float(description="Precio del producto", required=True),
        "category_id": fields.Integer(description="id de la categoría relacionada", required=True),
    },
)


class ProductResource(Resource):
    #@jwt_required()
    def get(self): 
        try:
            producto=Product.query.all()
            return producto_schema_many.dump(producto), 200

        except Exception as e:
            return {
                'error': f'Ocurrio un error -> {str(e)}'
            },500 

    def put(self):
        try:
            producto_id = request.form['id']
            name = request.form['name']
            price = request.form['price']
            stock = request.form['stock']
            category_id = request.form['category_id']
            prodcuto_img = request.files['img']
            
            producto = Product.query.filter_by(id=producto_id).first()
            
            if prodcuto_img.filename is not None and prodcuto_img.filename != '':
                prodcuto_img.filename = producto.prodcuto_img
                filename = secure_filename(prodcuto_img.filename)
                destination = path.join(current_app.config['UPLOAD_FOLDER'], filename)
                prodcuto_img.save(destination)

            
            producto.name=name
            producto.price=price
            producto.stock=stock
            producto.category_id=category_id
            producto.prodcuto_img=prodcuto_img.filename

            producto.slug_create()

            db.session.commit()
            return producto_schema.dump(producto)
        except Exception as e:
            return {
                'error': f'Ocurrio un error -> {str(e)}'
            },500
    
    def post(self):
        try:
            name = request.form['name']
            price = request.form['price']
            stock = request.form['stock']
            category_id = request.form['category_id']
            prodcuto_img = request.files['img']
            
            if prodcuto_img.filename is not None and prodcuto_img.filename != '':
                random = uuid4().hex[:8]
                prodcuto_img.filename = f'{random}.jpg'
                filename = secure_filename(prodcuto_img.filename)
                destination = path.join(current_app.config['UPLOAD_FOLDER'], filename)
                prodcuto_img.save(destination)

            producto = Product(name=name,
                                price=price,
                                stock=stock,
                                category_id=category_id,
                                prodcuto_img=prodcuto_img.filename
                                )
            producto.slug_create()
            
            db.session.add(producto)
            db.session.commit()
            
            return producto_schema.dump(producto)
        except Exception as e:
            return {
                'error': f'Ocurrio un error -> {str(e)}'
            },500

#############################################################################################
    
#    @producto_ns.expect(upload_parser)
#    def post(self):
#        try:
#            args = upload_parser.parse_args()
#            name = args['name']
#            price = args['stock']
#            stock = args['price']
#            category_id = args['category_id']
#            uploaded_file = args['img']
#            
#            producto = Product(name=name,
#                                price=price,
#                                stock=stock,
#                                category_id=category_id,
#                                )
#            producto.slug_create()
#            db.session.add(producto)
#            db.session.commit()
#            if uploaded_file.filename is not None and uploaded_file.filename != '':
#                filename = secure_filename(uploaded_file.filename)
#                print(filename)
#                destination = path.join(current_app.config['UPLOAD_FOLDER'], filename)
#                uploaded_file.save(destination)
#            return producto_schema.dump(producto)
#        except Exception as e:
#            return {
#                'error': f'Ocurrio un error -> {str(e)}'
#            },500

###############################################################################################

#    @producto_ns.expect(Insert_product_data)
#    def post(self):
#        try:
#            #content type json
#               
#            json_data = request.json
#            name = json_data['name']
#            stock = json_data['stock']
#            price = json_data['price']
#            category_id = json_data['category_id']
#            
#            producto = Product(name=name,
#                                price=price,
#                                stock=stock,
#                                category_id=category_id,
#                                )
#            producto.slug_create()
#            db.session.add(producto)
#            db.session.commit()
#
#            return producto_schema.dump(producto)
#        except Exception as e:
#            return {
#                'error': f'Ocurrio un error -> {str(e)}'
#            },500

