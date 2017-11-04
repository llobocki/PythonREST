from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# from app.extensions.api import api


Base = declarative_base()
# db = create_engine(SQLALCHEMY_DATABASE_URI)
# session = scoped_session(sessionmaker(autocommit=False,
#                                       autoflush=False, bind=db))
#
# Base.query = session.query_property()


def init_db(db):
    import app.modules.user.models
    Base.metadata.create_all(db)
