#!/usr/bin/python3

"""Unit test for testing the Rectangle class."""
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO


class TestRectangle(unittest.TestCase):
    """A class for testing Rectangle class."""

    def setUp(self):
        """For testing the id."""
        Base._Base__nb_objects = 0

    def test_inheritence(self):
        """Test inheritence of Rectangle from Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id(self):
        """Tests the id of the rectangle class."""
        self.assertEqual(Rectangle(2, 2).id, 1)
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
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        r1 = Rectangle(1, 1, 1)
        self.assertEqual(r1.x, 1)
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.y, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1)

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

    def test_display(self):
        """Testng the display method in Rectangle."""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1, 1)
        r3 = Rectangle(1, 1, 1, 1)
        output = StringIO()

        recs = [r1, r2, r3]
        outputs = ['#\n', " #\n", "\n #\n"]
        for i in range(3):
            with patch("sys.stdout", new=output):
                recs[i].display()

            output_value = output.getvalue()
            self.assertEqual(outputs[i], output_value)
            output.truncate(0)
            output.seek(0)

    def test_to_dict(self):
        """Testing the conversion of rectangle to dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        same_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, same_dict)
