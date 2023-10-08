from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    __tablename__ = 'users'
    
    places = relationship("Place", backref="user", cascade="all, delete-orphan")
