import sqlalchemy as sa
from app.modules.user import models
from app.modules.user.namespace import api
from flask import current_app


class UserDAO(object):

    def all(self):
        entities = current_app.db_session.query(models.User).all()
        return entities

    def get(self, id):
        entity = current_app.db_session.query(models.User).filter(
            models.User.id == id).one_or_none()
        if entity:
            return entity
        else:
            api.abort(404)

    def create(self, data):
        entity = models.User(**data)
        current_app.db_session.add(entity)
        current_app.db_session.commit()
        return entity

    def update(self, id, data):
        entity = current_app.db_session.query(models.User).filter(
            models.User.id == id).one_or_none()
        if not entity:
            api.abort(404)
        entity.update(data)
        current_app.db_session.commit()
        return entity

    def delete(self, id):
        entity = current_app.db_session.query(models.User).filter(
            models.User.id == id).first()
        try:
            current_app.db_session.delete(entity)
        except sa.orm.exc.UnmappedInstanceError:
            api.abort(404)
        current_app.db_session.commit()
