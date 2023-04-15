#!/usr/bin/python3

"""Unit testing for testing Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A class for testing Base class."""

    def test_id(self):
        """Testing id of the Base class."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(5).id, 5)
        self.assertEqual(Base().id, 3)
