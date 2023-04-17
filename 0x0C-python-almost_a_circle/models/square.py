#!/usr/bin/pyhton3
"""The Square Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A square Class that inherits
    a Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """A constructor method"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """A size getter Method"""

        return self.width

    @size.setter
    def size(self, size):
        """A size setter Method"""

        self.width = size
        self.height = size
