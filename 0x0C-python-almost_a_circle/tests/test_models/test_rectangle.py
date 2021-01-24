#!/usr/bin/python3
# test_rectangle.py
"""
Unittests for models/rectangle.py.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_class(self):
        """Tests Rectangle class type."""
        self.assertEqual(str(Rectangle),
                        "<class 'models.rectangle.Rectangle'>")

if __name__ == "__main__":
    unittest.main()
