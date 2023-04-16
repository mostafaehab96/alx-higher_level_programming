#!/usr/bin/python3

"""Unit test for testing the Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """A class for testing Rectangle class."""

    def test_inheritence(self):
        """Test inheritence of Rectangle from Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id(self):
        """Tests the id of the rectangle class."""
        last_id = Base().id
        self.assertEqual(Rectangle(2, 2).id, last_id + 1)
        self.assertEqual(Rectangle(2, 10, 0, 0, 12).id, 12)

    def test_attributes(self):
        """Tests the attributes validations and errors."""
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, "s", 1)
        self.assertRaises(TypeError, Rectangle, 1, "s")
        self.assertRaises(TypeError, Rectangle, True, 1)
        self.assertRaises(TypeError, Rectangle, [1], 1)
        self.assertRaises(TypeError, Rectangle, (1,), 1)
        self.assertRaises(TypeError, Rectangle, 1, [1])
        self.assertRaises(TypeError, Rectangle, 1, (1,))
        self.assertRaises(TypeError, Rectangle, 1, True)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)
        self.assertRaises(TypeError, Rectangle, 1, 1, "s")
        self.assertRaises(TypeError, Rectangle, 1, 1, True)
        self.assertRaises(TypeError, Rectangle, 1, 1, (1,))
        self.assertRaises(TypeError, Rectangle, 1, 1, [1])
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, "s")
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, True)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, (1,))
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, [1])
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)

    def test_area(self):
        """Testing area function in Rectangle class."""
        self.assertEqual(Rectangle(2, 3).area(), 6)

    def test_str(self):
        """Testing the str return or Rectangle."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Testing update function in Rectangle class."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        r1.update(89, height=1)
        self.assertEqual(r1.height, 3)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)
        self.assertRaises(TypeError, r1.update, 89, "s")
        self.assertRaises(TypeError, r1.update, 89, (1,))
        self.assertRaises(TypeError, r1.update, 89, 1, True)
        self.assertRaises(TypeError, r1.update, 89, 1, 1, "s")
        self.assertRaises(ValueError, r1.update, 89, 0)
        self.assertRaises(ValueError, r1.update, 89, 1, 0)
        self.assertRaises(ValueError, r1.update, 89, 1, 1, -1)
        self.assertRaises(ValueError, r1.update, 89, 1, 1, -1, -1)
