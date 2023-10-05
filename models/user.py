#!/usr/bin/python3
<<<<<<< HEAD
""" User Module for HBNB project """

=======
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
>>>>>>> parent of 06df725 (models)
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
<<<<<<< HEAD
    """ User class """
    __tablename__ = 'users'

=======
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
>>>>>>> parent of 06df725 (models)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
<<<<<<< HEAD
    reviews = relationship("Review", backref="user", cascade="all, delete")
=======
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
>>>>>>> parent of 06df725 (models)
