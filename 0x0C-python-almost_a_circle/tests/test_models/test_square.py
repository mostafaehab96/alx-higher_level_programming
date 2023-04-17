#!/usr/bin/python3

"""Unit testing for the Square class."""
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestSquare(unittest.TestCase):
    """A class for testing Square class."""

    def test_inheritence(self):
        """Testing Square inherits from Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_id(self):
        """Testing the id of the Square instance."""
        last_id = Base().id
        self.assertEqual(Square(2).id, last_id + 1)
        self.assertEqual(Square(2, 0, 0, 89).id, 89)

    def test_init(self):
        """Testing initializer of the Square class."""
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, "s",
                          msg="width must be an integer")
        self.assertRaises(TypeError, Square, True,
                          msg="width must be an integer")
        self.assertRaises(TypeError, Square, [1],
                          msg="width must be an integer")
        self.assertRaises(TypeError, Square, (1,),
                          msg="width must be an integer")
        self.assertRaises(TypeError, Square, 1.5,
                          msg="width must be an integer")
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(TypeError, Square, 1, "s")
        self.assertRaises(TypeError, Square, 1, True)
        self.assertRaises(TypeError, Square, 1, 1.5)
        self.assertRaises(TypeError, Square, 1, (1,))
        self.assertRaises(TypeError, Square, 1, [1])
        self.assertRaises(TypeError, Square, 1, 1.5)
        self.assertRaises(TypeError, Square, 1, 1, True)
        self.assertRaises(TypeError, Square, 1, 1, (1,))
        self.assertRaises(TypeError, Square, 1, 1, [1])
        self.assertRaises(TypeError, Square, 1, 1, 1.5)
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaises(ValueError, Square, 1, 0, -1)
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_area(self):
        """Testing area of the Square."""
        self.assertEqual(Square(5).area(), 25)

    def test_str(self):
        """Testing the str method in Square class."""
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

    def test_update(self):
        """Tesint Square update method."""
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        s1.update(11, id=89, size=10, x=0, y=0)
        self.assertEqual(s1.id, 11)
        self.assertEqual(s1.size, 2)
        s1.update(id=89, size=10, x=0, y=0)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertRaises(TypeError, s1.update, size="5")
        self.assertRaises(TypeError, s1.update, x="5")
        self.assertRaises(TypeError, s1.update, y="5")
        self.assertRaises(ValueError, s1.update, size=0)
        self.assertRaises(ValueError, s1.update, x=-1)
        self.assertRaises(ValueError, s1.update, y=-1)
