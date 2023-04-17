#!/usr/bin/python3

"""Defines a Square class the inherits from Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A simple Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance by using the
        Rectangle class initializer.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Overriding the str method in Rectangle class
        which returns the str representation of Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Updates the Square instance with args or kwargs."""
        if len(args) == 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v
            return
        attrs = ['id', 'size', 'x', 'y']
        for i in range(len(args)):
            k = attrs[i]
            v = args[i]
            if k == 'id':
                self.id = v
            if k == 'size':
                self.size = v
            if k == 'x':
                self.x = v
            if k == 'y':
                self.y = v

    def to_dictionary(self):
        """Returns dictionary representation of the class."""
        return {"id": self.id, "size": self.size, 'x': self.x, 'y': self.y}
