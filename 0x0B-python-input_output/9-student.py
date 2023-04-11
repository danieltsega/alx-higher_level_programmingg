#!/usr/bin/python3
"""A Student Module"""


class Student:
    """A class that defines a
    student
    """

    def __init__(self, first_name, last_name, age):
        """A function that is called
        everytime an object is created
        from this file
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A Method that returns
        a dictionary format of an
        objcet
        """

        return self.__dict__
