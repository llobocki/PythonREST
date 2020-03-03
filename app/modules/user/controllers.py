from app.modules.user.dao import UserDAO
from app.modules.user.namespace import api, response_user, user
from app.modules.user.schemas import UserSchema
from flask import request
from flask_restx import Resource

user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_Dao = UserDAO()


@api.route('/')
class UserList(Resource):

    @api.doc()
    @api.marshal_list_with(response_user)
    def get(self):
        entities = user_Dao.all()
        response = users_schema.dump(entities)
        return response

    @api.doc()
    @api.expect(user, validate=True)
    @api.marshal_with(response_user, code=201)
    def post(self):
        data = user_schema.load(request.get_json())
        entity = user_Dao.create(data)
        response = user_schema.dump(entity)
        return response, 201


@api.route('/<int:id>')
class User(Resource):

    @api.doc()
    @api.marshal_with(response_user)
    def get(self, id):
        entity = user_Dao.get(id)
        response = user_schema.dump(entity)
        return response

    @api.doc()
    @api.expect(user, validate=True)
    @api.marshal_with(response_user)
    def put(self, id):
        data = user_schema.load(request.get_json())
        entity = user_Dao.update(id, data)
        response = user_schema.dump(entity)
        return response

    @api.doc(responses={204: 'User deleted'})
    def delete(self, id):
        user_Dao.delete(id)
        return None, 204
