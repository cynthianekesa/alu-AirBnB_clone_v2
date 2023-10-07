#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import os


class test_state(test_basemodel):
    """ states test class"""

    def _init_(self, *args, **kwargs):
        """ state test class init"""
        super()._init_(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ testing state name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
