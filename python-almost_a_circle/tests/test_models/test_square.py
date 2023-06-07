#!/usr/bin/python3
""" This module is a unittest for the Square class """

import unittest
import os
import io
import sys

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test class for Square class """
    def setUp(self):
        """Set up test method"""
        # reset __nb_objects to 0 before each test
        print("Square setUp")

        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        self.square = Square(1)

        # reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tear down test method"""
        print("Square tearDown")

        sys.stdout = sys.__stdout__

        del self.square
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_square_inheritance(self):
        """ Test if Square inherits from Rectangle """
        self.assertIsInstance(self.square, Rectangle)

    def test_square_inheritance_base(self):
        """ Test if Square inherits from Base """
        self.assertIsInstance(self.square, Base)

    def test_square_id(self):
        """ Test if Square id increments correctly """
        # Test auto-increment id
        square = Square(5, 5, 5)
        print(f"Actual id: {square.id}")
        self.assertEqual(square.id, 1)
        # Test auto-increment id
        square1 = Square(5, 5, 0, 50)
        print(f"Actual id: {square1.id}")
        self.assertEqual(square1.id, 50)
        # Test auto-increment id
        square1 = Square(5, 5, 5)
        print(f"Actual id: {square1.id}")
        self.assertEqual(square1.id, 2)
        # Test auto-increment id
        square2 = Square(5, 5, 5)
        print(f"Actual id: {square2.id}")
        self.assertEqual(square2.id, 3)

    def test_square_id_assignment(self):
        """ Test if Square id is assigned correctly """
        # Test explicit id assignment positive number
        square4 = Square(6, 0, 0, 12)
        self.assertEqual(square4.id, 12)

        # Test auto-increment id after explicit assignment
        square5 = Square(5, 0, 0, None)
        self.assertEqual(square5.id, 1)

        # Test explicit id assignment with negative number
        square6 = Square(4, 0, 0, -12)
        self.assertEqual(square6.id, -12)

        # Test explicit id assignment with zero
        square7 = Square(5, 0, 0, 0)
        self.assertEqual(square7.id, 0)

    def test_too_few_args(self):
        """
        test too few args to init
        """
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """
        test too many args to init
        """
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1, 1, 1)

    def test_square_getter(self):
        """ Test if Square getter works """
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_square_setter(self):
        """ Test if Square setter works """
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_square_creation_pos(self):
        """ Test if Square is created correctly """
        # basic square with size
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        self.assertIsInstance(s1, Square)

        # square with size and x
        s2 = Square(5, 10)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 10)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 2)

        # square with size, x and y
        s3 = Square(5, 10, 15)
        self.assertEqual(s3.size, 5)
        self.assertEqual(s3.x, 10)
        self.assertEqual(s3.y, 15)
        self.assertEqual(s3.id, 3)

    def test_square_init_type(self):
        """ Test if Square is initialized correctly """
        # Test if size is a string
        with self.assertRaises(TypeError):
            Square("1")
        # Test if x is an string
        with self.assertRaises(TypeError):
            Square(1, "2")
        # Test if y is an string
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        # Test with negative size
        with self.assertRaises(ValueError):
            Square(-1)
        # Test with negative x
        with self.assertRaises(ValueError):
            Square(1, -2)
        # Test with negative y
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        # Test with zero size
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_method(self):
        """ Test is __str__ method works """
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.__str__(), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        """ Test if to_dictionary method works """
        square = Square(1, 2, 3, 4)
        dictionary = square.to_dictionary()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary["id"], 4)
        self.assertEqual(dictionary["size"], 1)
        self.assertEqual(dictionary["x"], 2)
        self.assertEqual(dictionary["y"], 3)

    def test_update_args(self):
        """ Test if update method works with *args """
        square = Square(1, 2, 3, 4)
        square.update(10, 20, 30, 40)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_update_kwargs(self):
        """ Test if update method works with **kwargs """
        square = Square(1, 2, 3, 4)
        square.update(id=10, size=20, x=30, y=40)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_update_args_kwargs(self):
        """ Test if update method works with *args and **kwargs """
        square = Square(1, 2, 3, 4)
        square.update(10, 20, id=30, size=40)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_create(self):
        """ Test if create method works """
        # create square id
        square = Square.create(**{"id": 10})
        self.assertEqual(square.id, 10)
        # create square size
        square = Square.create(**{"size": 10})
        self.assertEqual(square.size, 10)
        # create square x
        square = Square.create(**{"x": 10})
        self.assertEqual(square.x, 10)
        # create square y
        square = Square.create(**{"y": 10})
        self.assertEqual(square.y, 10)
        # create square size and x
        square = Square.create(**{"size": 10, "x": 20})
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 20)
        # create square size and y
        square = Square.create(**{"size": 10, "y": 20})
        self.assertEqual(square.size, 10)
        self.assertEqual(square.y, 20)
        # create square x and y
        square = Square.create(**{"x": 10, "y": 20})
        self.assertEqual(square.x, 10)
        self.assertEqual(square.y, 20)
        # create square id, size and x
        square = Square.create(**{"id": 10, "size": 20, "x": 30})
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        # create square id, size and y
        square = Square.create(**{"id": 10, "size": 20, "y": 30})
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.y, 30)
        # create square id, x and y
        square = Square.create(**{"id": 10, "x": 20, "y": 30})
        self.assertEqual(square.id, 10)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)
        # create square id, size, x and y
        square = Square.create(**{"id": 10, "size": 20, "x": 30, "y": 40})
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_save_to_file_none(self):
        """ Test if save_to_file method works """
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        """ Test if save_to_file method works """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file(self):
        """ Test if save_to_file method works """
        Square.save_to_file([Square(1)])
        expected_output = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), expected_output)

    def test_load_from_json_file_none(self):
        """ Test if load_from_json_file method works """
        list_sqr_output = Square.load_from_file()
        self.assertEqual(list_sqr_output, [])

    def test_load_from_file_existent(self):
        """Test load_from_file method when file exists"""
        # Create a list of squares
        list_sqr_input = [Square(10, 7, 9, 5), Square(2, 4, 6, 8)]
        Square.save_to_file(list_sqr_input)

        # Load squares from file
        list_sqr_output = Square.load_from_file()

        for i in range(len(list_sqr_input)):
            # Compare if they are the same instance.
            self.assertEqual(str(list_sqr_input[i]), str(list_sqr_output[i]))


if __name__ == '__main__':
    unittest.main()
