from flask_restx import Resource, fields, Namespace,reqparse
from flask import request
from flask_jwt_extended import jwt_required
from app.category.categoryModel import Category
from app.category.categorySchema import CategorySchema
from app.db import db
from werkzeug.datastructures import FileStorage




category_ns = Namespace('category', description='Category Endpoints')
categories_ns = Namespace('categories', description='Categories Endpoints')

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('file', location='files',type=FileStorage, required=True)


insert_category_data = category_ns.model(
    "Insert_category_data",
    {
        "name": fields.String(description="category name", required=True),
        "status": fields.Integer(description="category status", required=True)
    },
)


class CategoryResource(Resource):
    #@jwt_required()
    def get(self, id):
        category_data = Category.find_by_id(id)
        if category_data:
            #category_data['mensaje']='Lista'
            return category_schema.dump(category_data)
        return {'message': 'Category not found'}, 501

    def delete(self, id):
        try:
            category_data = Category.query.filter_by(id=id)
            if category_data:
                category_data = category_data.delete()
                db.session.commit()
                return {'message': 'Se elimino la categoria con exito'}, 200
            return {'message': 'Category not found'}, 501
        except Exception as e:
            return {
                'error': f'Ocurrio un error -> {str(e)}'
            },500
    @category_ns.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']
 
class CategoriesResource(Resource):
    #@jwt_required()
    def get(self): 
        return categories_schema.dump(Category.find_all()), 200

    @categories_ns.expect(insert_category_data)
    def post(self):
        try:
            json_data = request.json
            name = json_data['name']
            status = json_data['status']
            category = Category(name=name,status=status)
            category.slug_create()
            db.session.add(category)
            db.session.commit()
            return category_schema.dump(category)
        except Exception as e:
            return {
                'error': f'Ocurrio un error -> {str(e)}'
            },500