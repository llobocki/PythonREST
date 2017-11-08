from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(db):
    import app.modules.user.models
    Base.metadata.create_all(db)
