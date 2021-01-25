#!/usr/bin/python3
# test_base.py
"""
Unittest for Base
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

# ---------- task 1 ----------------------------------------------

    def test_1_nb_objects_private(self):
        """nb_objects == private class attribute"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_2_nb_objects_initialized(self):
        """nb_objects initializes to 0"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_3_id_synced(self):
        """tests class and instance id"""
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_4_instantiation(self):
        """Tests Base() instantiation"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_5_type(self):
        """Testing for instance type"""
        b = Base()
        self.assertTrue(type(b) == Base)

    def test_6_id_keyword(self):
        """id as keyword arg"""
        i = 98
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_7_id(self):
        """Prints out the id"""
        b = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b.id, b3.id - 1)

    def test_8_id_string(self):
        """Passing string"""
        self.assertEqual(Base("Hello").id, "Hello")

    def test_9_id_None(self):
        """Passing None"""
        self.assertEqual(Base(None).id, 1)

    def test_10_id_float(self):
        """Passing float"""
        self.assertEqual(Base(1.2).id, 1.2)

    def test_11_id_bool(self):
        self.assertEqual(Base(True).id, True)

    def test_12_id_list(self):
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_id_13_tuple(self):
        self.assertEqual(Base((1, 2)).id, (1, 2))

    def test_14_two_args(self):
        with self.assertRaises(TypeError) as e:
            b = Base(1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

# ---------- task 15 --------------------------------------------

    def test_15_to_json_string_none(self):
        """ Test when to_json_string is passed None"""

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_16_to_json_string_empty(self):
        """Test to_json_string with empty"""
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d), "[{}, {}]")

    def test_17_to_json_string_len(self):
        """Test to_json_string len"""
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 2, 'y': 4, 'width': 6, 'id': 8, 'height': 10}]

        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        self.assertTrue(type(Base.to_json_string(d)), dict)

    def test_18_to_json_string_rect(self):
        """Test to_json_string with Rectangle class"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        r3 = Rectangle(12, 12, 13, 14, 15)

        dict_r = [r1.to_dictionary(), r2.to_dictionary(), r3.to_dictionary()]
        jd = Base.to_json_string(dict_r)
        self.assertTrue(type(jd) is str)
        dict_r = str(dict_r)
        dict_r = dict_r.replace("'", '"')
        self.assertEqual(dict_r, jd)

    def test_19_to_json_string_sqr(self):
        """Test to_json_string with Square class"""
        s1 = Square(1, 2, 3)
        s2 = Square(4, 5, 6)
        s3 = Square(7, 8, 9)

        dict_s = [s1.to_dictionary(), s2.to_dictionary(), s3.to_dictionary()]
        jd = Base.to_json_string(dict_s)
        self.assertTrue(type(jd) is str)
        dict_s = str(dict_s)
        dict_s = dict_s.replace("'", '"')
        self.assertEqual(dict_s, jd)

# ---------- task 17 -------------------------------------------

    def test_20_from_json_string_none(self):
        """ Test when json_string is passed None"""

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_21_to_json_string_empty(self):
        """Test to_json_string with empty"""
        d = [{}, {}]
        s = '[{}, {}]'
        self.assertEqual(Base.from_json_string(s), d)

    def test_22_from_json_string_Rout(self):
        """Test from_json_string output Rectangle"""
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 2, 'y': 4, 'width': 6, 'id': 8, 'height': 10}]

        out = Rectangle.from_json_string(Rectangle.to_json_string(d))

        self.assertEqual(d, out)
        self.assertTrue(type(out) is list)
        self.assertEqual(len(out), 2)
        self.assertTrue(type(out[0]) is dict)
        self.assertTrue(type(out[1]) is dict)

    def test_23_from_json_string_Sout(self):
        """Test from_json_string output Square"""
        d = [{'id': 1, 'size': 3},
             {'id': 2, 'size': 4}]

        out = Square.from_json_string(Square.to_json_string(d))

        self.assertEqual(d, out)
        self.assertTrue(type(out) is list)
        self.assertEqual(len(out), 2)
        self.assertTrue(type(out[0]) is dict)
        self.assertTrue(type(out[1]) is dict)

# ---------- task 16 -------------------------------------------

    def test_24_save_to_file(self):
        """Tests save_to_file() method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 105)
        os.remove("Rectangle.json")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 38)
        os.remove("Square.json")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

# ---------- task 18 -------------------------------------------

    def test_25_create(self):
        """Tests create() method."""
        r1 = Rectangle(1, 2, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

if __name__ == '__main__':
    unittest.main()
