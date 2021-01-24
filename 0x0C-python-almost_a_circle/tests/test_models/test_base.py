#!/usr/bin/python3
# test_v=base.py
"""
Unittest for Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Base class unit tests
    """

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_nb_objects_private(self):
        """nb_objects == private class attribute"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_initialized(self):
        """nb_objects initializes to 0"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_id_synced(self):
        """tests class and instance id"""
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_instantiation(self):
        """Tests Base() instantiation"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_type(self):
        """Testing for instance type"""
        b = Base()
        self.assertTrue(type(b) == Base)

    def test_id_keyword(self):
        """id as keyword arg"""
        i = 98
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_id(self):
        """Prints out the id"""
        b = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b.id, b3.id - 1)

    def test_id_string(self):
        """Passing string"""
        self.assertEqual(Base("Hello").id, "Hello")

    def test_id_None(self):
        """Passing None"""
        self.assertEqual(Base(None).id, 1)

    def test_id_float(self):
        """Passing float"""
        self.assertEqual(Base(1.2).id, 1.2)

    def test_id_bool(self):
        self.assertEqual(Base(True).id, True)

    def test_id_list(self):
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_id_tuple(self):
        self.assertEqual(Base((1, 2)).id, (1, 2))

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == '__main__':
    unittest.main()
