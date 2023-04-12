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

    def to_json(self, attrs=None):
        """A Method that returns
        a dictionary format of an
        objcet
        """

        obj = self.__dict__
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return obj

            new_dic = {}
            for j in attrs:
                for k in obj:
                    if(k == j):
                        new_dic[j] = obj[j]
            return new_dic

        return obj
