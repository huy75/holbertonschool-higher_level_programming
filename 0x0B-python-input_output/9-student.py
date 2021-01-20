#!/usr/bin/python3
# 9-student.py
"""
Defines a Student class."""


class Student:
    """
    Student class.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary description of the instance.
        """
        return self.__dict__
