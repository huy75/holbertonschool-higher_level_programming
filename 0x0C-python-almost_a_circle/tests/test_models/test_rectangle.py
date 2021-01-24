#!/usr/bin/python3
# test_rectangle.py
"""
Unittests for models/rectangle.py.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class.
    """

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_1_id(self):
        """Prints out the id"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 4)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertTrue(type(r3), Rectangle)


    def test_2_inheritance(self):
        """Tests if Rectangle inherits Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_3_no_args(self):
        """Tests no arguments."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_4_many_args(self):
        """Tests many arguments."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(e.exception), s)

    def test_5_one_args(self):
        """Tests one argument."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_6_isinstance(self):
        """make instance"""
        r = Rectangle(1, 2)
        self.assertTrue(isinstance(r, Base))

    def test_7_type_int(self):
        """Arguments of type integer"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_8_instantiation(self):
        """Tests positional instantiation."""
        r = Rectangle(1, 2, 3, 4)
        d = {'_Rectangle__height': 2, '_Rectangle__width': 1,
            '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Rectangle(1, 2, 3, 4, 5)
        d = {'_Rectangle__height': 2, '_Rectangle__width': 1,
             '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 5}
        self.assertEqual(r.__dict__, d)

    def test_9_keyword(self):
        """Tests positional instantiation."""
        r = Rectangle(1, 2, id=3, y=4, x=5)
        d = {'_Rectangle__height': 2, '_Rectangle__width': 1,
             '_Rectangle__x': 5, '_Rectangle__y': 4, 'id': 3}
        self.assertEqual(r.__dict__, d)

    def test_10_id_inherited(self):
        """Tests if id is inherited from Base."""
        Base._Base__nb_objects = 98
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 99)

    def test_11_properties(self):
        """Tests property getters/setters."""
        r = Rectangle(5, 9)
        r.width = 1
        r.height = 2
        r.x = 3
        r.y = 4
        d = {'_Rectangle__height': 2, '_Rectangle__width': 1,
            '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

if __name__ == "__main__":
    unittest.main()
