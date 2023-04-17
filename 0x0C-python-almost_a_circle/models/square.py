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

    def __str__(self):
        """A str method"""

        sq = "[Square] "
        sq_id = "({}) ".format(self.id)
        sq_xy = "{}/{} ".format(self.x, self.y)
        sq_size = "- {}".format(self.size)

        return sq + sq_id + sq_xy + sq_size

    @property
    def size(self):
        """A size getter Method"""

        return self.width

    @size.setter
    def size(self, size):
        """A size setter Method"""

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """An Update Method"""

        if args is not None and len(args) != 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """A method that gets attributs and
        turn them to dictionary
        """

        attr = ['id', 'size', 'x', 'y']
        result = {}
        for i in attr:
            result[i] = getattr(self, i)

        return result
