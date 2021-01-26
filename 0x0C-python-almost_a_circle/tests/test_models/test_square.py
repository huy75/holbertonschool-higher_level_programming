#!/usr/bin/python3
# test_square.py
"""
Unittests for models/square.py.
"""
import io
import sys
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Unit tests for the Square class.
    """

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

# ---------- task 2 ---------------------------------------------

    def test_1_inheritance(self):
        """Tests if Square inherits Base & Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_2_isinstance(self):
        """make instance"""
        s = Square(2)
        self.assertTrue(isinstance(s, Base))
        self.assertTrue(isinstance(s, Rectangle))

    def test_3_class(self):
        """Tests Square class type."""
        self.assertEqual(str(Square),
                        "<class 'models.square.Square'>")
