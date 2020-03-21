from app.modules.user.dao import UserDAO
from app.modules.user.namespace import api, user
from flask import request
from flask_restx import Resource

user_Dao = UserDAO()


@api.route('/')
class UserList(Resource):

    @api.doc()
    @api.marshal_list_with(user)
    def get(self):
        return user_Dao.all()

    @api.doc()
    @api.expect(user, validate=True)
    @api.marshal_with(user, code=201)
    def post(self):
        return user_Dao.create(api.payload), 201


@api.route('/<int:id>')
class User(Resource):

    @api.doc()
    @api.marshal_with(user)
    def get(self, id):
        return user_Dao.get(id)

    @api.doc()
    @api.expect(user, validate=True)
    @api.marshal_with(user)
    def put(self, id):
        return user_Dao.update(id, api.payload)

    @api.doc(responses={204: 'User deleted'})
    def delete(self, id):
        user_Dao.delete(id)
        return None, 204
