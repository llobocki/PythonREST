from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.database import Base, init_db
from app.extensions.api import blueprint as api
from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.register_blueprint(api)
    app.config.from_object(config)

    if app.debug is not True:
        import logging
        handler = logging.FileHandler('log.txt')
        handler.setLevel(logging.ERROR)
        app.logger.addHandler(handler)
    db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False, bind=db))

    Base.query = session.query_property()
    app.db_session = session
    init_db(db)
    return app
