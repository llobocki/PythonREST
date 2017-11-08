import sqlalchemy as sa

from app.modules.user import models
from app.modules.user.namespace import api, response_user, user
from app.modules.user.schemas import UserSchema
from flask import current_app, request
from flask_restplus import Resource

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@api.route('/')
class UserList(Resource):

    @api.doc()
    @api.marshal_list_with(response_user)
    def get(self):
        entities = current_app.db_session.query(models.User).all()
        response = users_schema.dump(entities).data
        return response

    @api.doc()
    @api.expect(user, validate=True)
    @api.marshal_with(response_user, code=201)
    def post(self):
        data, errors = user_schema.load(request.get_json())
        entity = models.User(**data)
        current_app.db_session.add(entity)
        current_app.db_session.commit()
        response = user_schema.dump(entity).data
        return response, 201


@api.route('/<int:id>')
class User(Resource):

    @api.doc()
    @api.marshal_with(response_user)
    def get(self, id):
        entity = current_app.db_session.query(models.User).filter(
            models.User.id == id).one_or_none()
        if not entity:
            api.abort(404)
        response = user_schema.dump(entity).data
        return response

    @api.doc()
    @api.expect(user, validate=True)
    @api.marshal_with(response_user)
    def put(self, id):
        entity = current_app.db_session.query(models.User).filter(
            models.User.id == id).one_or_none()
        if not entity:
            api.abort(404)
        data, errors = user_schema.load(request.get_json())
        entity.update(data)
        current_app.db_session.commit()
        response = user_schema.dump(entity).data
        return response

    @api.doc(responses={204: 'User deleted'})
    def delete(self, id):
        entity = current_app.db_session.query(models.User).filter(
            models.User.id == id).first()
        try:
            current_app.db_session.delete(entity)
        except sa.orm.exc.UnmappedInstanceError:
            api.abort(404)
        current_app.db_session.commit()
        return None, 204
