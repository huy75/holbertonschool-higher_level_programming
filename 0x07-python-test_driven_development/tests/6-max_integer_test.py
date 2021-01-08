#!/usr/bin/python3
"""
Unittest for max_integer([..])
python3 -m unittest tests.6-max_integer_test
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_none_value(self):
        '''
            Testing when the paratemerter None is passed
        '''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_none(self):
        '''
            Testing with None in the list
        '''
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])

    def test_right_output(self):
        '''
            Testing when passing and argument that is expected to succeed
        '''
        self.assertEqual(max_integer([1, 6, 100, 4, 0, -1, 10]), 100)

    def test_string(self):
        '''
            Testing with string
        '''
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_numeric_string(self):
        '''
            Testing with numeric string
        '''
        self.assertEqual(max_integer("192834754"), "9")

    def test_lists(self):
        '''
            Testing with a list of different lengths
        '''
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_empty_list(self):
        '''
            Testing an empty list parameter
        '''
        self.assertIsNone(max_integer([]))

    def test_no_param(self):
        '''
            Testing no parameter
        '''
        self.assertIsNone(max_integer())

    def test_equal_values(self):
        '''
            Testing with all the list values equal to each other
        '''
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_no_ints(self):
        '''
            Testing with values in the list that are not integers
        '''
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 2, 3])

    def test_only_negatives(self):
        '''
            Testing with negative numbers
        '''
        self.assertEqual(max_integer([-10, -100, -6, -3, -1]), -1)

    def test_begining(self):
        '''
            Testing with the max int at the beginning
        '''
        self.assertEqual(max_integer([100, 1, 1, 1]), 100)

    def test_mid(self):
        '''
            Testing with the max int in the middle
        '''
        self.assertEqual(max_integer([1, 4, 3]), 4)

    def test_one(self):
        '''
            Testing with all the list values equal to each other
        '''
        self.assertEqual(max_integer([1]), 1)

    def test_int(self):
        '''
            Testing with an int
        '''
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        '''
            Testing with a float
        '''
        with self.assertRaises(TypeError):
            max_integer(9.8)

if __name__ == '__main__':
    unittest.main()
