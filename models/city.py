#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
=======
"""This is the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
>>>>>>> parent of 06df725 (models)
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
<<<<<<< HEAD
    """ City class """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="city", cascade="all, delete")
=======
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
>>>>>>> parent of 06df725 (models)
