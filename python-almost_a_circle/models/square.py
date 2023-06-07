#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square attributes"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attr, val in zip(attributes, args):
                setattr(self, attr, val)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
