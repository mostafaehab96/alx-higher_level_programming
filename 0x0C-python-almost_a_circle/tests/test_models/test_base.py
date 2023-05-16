#!/usr/bin/python3

"""Unit testing for testing Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """A class for testing Base class."""

    def setUp(self):
        """For testing the id."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Testing id of the Base class."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(5).id, 5)
        self.assertEqual(Base().id, 3)

    def test_to_json_string(self):
        """Testing the json string representation."""
        pass
