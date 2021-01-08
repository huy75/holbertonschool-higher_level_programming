#!/usr/bin/python3
"""
Unittest for max_integer([..])
python3 -m unittest tests.6-max_integer_test
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

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

    def test_equal_values(self):
        '''
            Testing with all the list values equal to each other
        '''
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

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

if __name__ == '__main__':
    unittest.main()
