from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.database import Base, init_db
from app.extensions.api import blueprint as api
from flask import Blueprint, Flask
from flask_restplus import Api, apidoc


# import config


def create_app(config):
    app = Flask(__name__)
    app.register_blueprint(api)
    app.config.from_object(config)

    # @app.errorhandler(500)
    # def internal_server_error(error):
    #     app.logger.error('Server Error: %s', (error))
    #     return {}, 500
    #
    # @app.errorhandler(Exception)
    # def unhandled_exception(e):
    #     app.logger.error('Unhandled Exception: %s', (e))

    if app.debug is not True:
        import logging
        # errors logged to this file
        handler = logging.FileHandler('log.txt')
        handler.setLevel(logging.ERROR)  # only log errors and above
        app.logger.addHandler(handler)
    db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False, bind=db))

    Base.query = session.query_property()
    app.db_session = session
    init_db(db)
    return app
