from sqlalchemy import Column, Integer, String

from app.database import Base
from app.model import BaseModel


class User(Base, BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
