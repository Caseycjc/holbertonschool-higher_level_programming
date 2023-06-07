#!/usr/bin/python3
""" This module is a unittest for the Rectangle class """

import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle class """
    def setUp(self):
        """Set up test method"""
        print("Rectangle setUp")

        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        self.rectangle = Rectangle(1, 1)

        # reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0
        # print(f"Base.__nb_objects after reset: {Base._Base__nb_objects}")

    def tearDown(self):
        """Tear down test method"""
        print("Rectangle tearDown")

        sys.stdout = sys.__stdout__

        del self.rectangle
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    # test id assignment and if it increments correctly
    def test_id(self):
        """Test __init__ method:
        id assignment in the Rectangle class.
        """
        print(f"Actual id: {self.rectangle.id}")
        self.assertEqual(self.rectangle.id, 1)
        rectangle2 = Rectangle(50, 50)
        print(f"Actual id: {rectangle2.id}")
        self.assertEqual(rectangle2.id, 1)
        rectangle3 = Rectangle(1, 1)
        print(f"Actual id: {rectangle3.id}")
        self.assertEqual(rectangle3.id, 2)

    # test to many args to init method
    def test_too_many_args(self):
        """
        test too many args to init
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1, 1)

    def test_rectangle_creation(self):
        """ Test Rectangle creation """
        # basic rectangle
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        # rectangle with x
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

        # rectangle with y
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

        # rectangle with id
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

        # rectangle with negative width
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4, 5)

        # rectangle with negative height
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4, 5)

        # rectangle with negative x
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4, 5)

        # rectangle with negative y
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4, 5)

        # rectangle with zero width
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2, 3, 4, 5)

        # rectangle with zero height
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 3, 4, 5)

        # rectangle with string width
        with self.assertRaises(TypeError):
            r = Rectangle("string", 2, 3, 4, 5)

        # rectangle with string height
        with self.assertRaises(TypeError):
            r = Rectangle(1, "string", 3, 4, 5)

        # rectangle with string x
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "string", 4, 5)

        # rectangle with string y
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "string", 5)

    def test_width(self):
        """ Test width getter and setter:
        width must be an integer, positive and non-zero """
        # test width getter
        self.assertEqual(self.rectangle.width, 1)
        # test width setter
        self.rectangle.width = 50
        # test width getter after setter
        self.assertEqual(self.rectangle.width, 50)
        # test width setter with negative value
        with self.assertRaises(ValueError):
            self.rectangle.width = -1
        # test width setter with zero
        with self.assertRaises(ValueError):
            self.rectangle.width = 0
        # test width setter with string
        with self.assertRaises(TypeError):
            self.rectangle.width = "string"
        # test width setter with list
        with self.assertRaises(TypeError):
            self.rectangle.width = [1, 2, 3]
        # test width setter with tuple
        with self.assertRaises(TypeError):
            self.rectangle.width = (1, 2, 3)
        # test width setter with dict
        with self.assertRaises(TypeError):
            self.rectangle.width = {"key": 1, "key2": 2}

    def test_height(self):
        """ Test height getter and setter:
        height must be an integer, positive and non-zero """
        # test height getter
        self.assertEqual(self.rectangle.height, 1)
        # test height setter
        self.rectangle.height = 50
        # test height getter after setter
        self.assertEqual(self.rectangle.height, 50)

        # test height setter with negative value
        with self.assertRaises(ValueError):
            self.rectangle.height = -1
        # test height setter with zero
        with self.assertRaises(ValueError):
            self.rectangle.height = 0
        # test height setter with string
        with self.assertRaises(TypeError):
            self.rectangle.height = "string"
        # test height setter with list
        with self.assertRaises(TypeError):
            self.rectangle.height = [1, 2, 3]
        # test height setter with tuple
        with self.assertRaises(TypeError):
            self.rectangle.height = (1, 2, 3)
        # test height setter with dict
        with self.assertRaises(TypeError):
            self.rectangle.height = {"key": 1, "key2": 2}

    def test_x(self):
        """ test x getter and setter:
        x must be an integer, positive and zero """
        # test x getter
        self.assertEqual(self.rectangle.x, 0)
        # test x setter
        self.rectangle.x = 50
        # test x getter after setter
        self.assertEqual(self.rectangle.x, 50)

        # test x setter with negative value
        with self.assertRaises(ValueError):
            self.rectangle.x = -1
        # test x setter with string
        with self.assertRaises(TypeError):
            self.rectangle.x = "string"
        # test x setter with list
        with self.assertRaises(TypeError):
            self.rectangle.x = [1, 2, 3]
        # test x setter with tuple
        with self.assertRaises(TypeError):
            self.rectangle.x = (1, 2, 3)
        # test x setter with dict
        with self.assertRaises(TypeError):
            self.rectangle.x = {"key": 1, "key2": 2}

    def test_y(self):
        """ Test y getter and setter:
        y must be an integer, positive and zero """
        # test y getter
        self.assertEqual(self.rectangle.y, 0)
        # test y setter
        self.rectangle.y = 50
        # test y getter after setter
        self.assertEqual(self.rectangle.y, 50)

        # test y setter with negative value
        with self.assertRaises(ValueError):
            self.rectangle.y = -1
        # test y setter with string
        with self.assertRaises(TypeError):
            self.rectangle.y = 'string'
        # test y setter with list
        with self.assertRaises(TypeError):
            self.rectangle.y = [1, 2, 3]
        # test y setter with tuple
        with self.assertRaises(TypeError):
            self.rectangle.y = (1, 2, 3)
        # test y setter with dict
        with self.assertRaises(TypeError):
            self.rectangle.y = {"key": 1, "key2": 2}

    def test_area(self):
        """ Test area method:
        area = width * height, always positive """
        # test area
        self.assertEqual(self.rectangle.area(), 1)
        # test area with width setter
        self.rectangle.width = 50
        self.assertEqual(self.rectangle.area(), 50)
        # test area with height setter
        self.rectangle.height = 50
        self.assertEqual(self.rectangle.area(), 2500)

        # test area with negative width
        with self.assertRaises(ValueError):
            self.rectangle.width = -1
            self.rectangle.area()
        # test area with negative height
        with self.assertRaises(ValueError):
            self.rectangle.height = -1
            self.rectangle.area()

    def test_str(self):
        """ Test __str__ method:
        check if instance of the class matches
        the expected string representation.
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        self.rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.rectangle.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        """ Test display method:
        print the Rectangle instance to stdout """
        # Test display
        self.rectangle = Rectangle(2, 2)
        self.rectangle.display()
        self.assertEqual(self.capture_output.getvalue(), "##\n##\n")

    def test_display_with_x(self):
        # Test display with x
        self.rectangle = Rectangle(2, 2, 2)
        self.rectangle.display()
        self.assertEqual(self.capture_output.getvalue(), "  ##\n  ##\n")

    def test_display_with_y(self):
        # Test display with x and y
        self.rectangle = Rectangle(2, 2, 2, 2)
        self.rectangle.display()
        self.assertEqual(self.capture_output.getvalue(), "\n\n  ##\n  ##\n")

    def to_dictionary(self):
        """ Test to_dictionary method:
        Returns a dictionary representation of a Rectangle """
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))

        # test to_dictionary
        self.rectangle = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def test_update_positional_args(self):
        """ test update method:
        assigns an argument to each attribute
        """
        # test update id
        self.rectangle.update(10)
        self.assertEqual(self.rectangle.id, 10)
        # test update width
        self.rectangle.update(10, 20)
        self.assertEqual(self.rectangle.width, 20)
        # test update height
        self.rectangle.update(10, 20, 30)
        self.assertEqual(self.rectangle.height, 30)
        # test update x
        self.rectangle.update(10, 20, 30, 40)
        self.assertEqual(self.rectangle.x, 40)
        # test update y
        self.rectangle.update(10, 20, 30, 40, 50)
        self.assertEqual(self.rectangle.y, 50)

    def test_update_kw_args(self):
        """Test updating attributes with keyword arguments"""
        rectangle = Rectangle(1, 1, 1, 1, 1)
        rectangle.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_update_args_and_kwargs(self):
        """ test update method:
        assigns an argument to each attribute using *args and **kwargs
        """
        rectangle = Rectangle(1, 1, 1, 1, 1)
        rectangle.update(2, 3, 4, 5, 6, id=7, width=8, height=9, x=10, y=11)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_create_with_attributes(self):
        """ Test if create method sets attributes correctly """
        attributes = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        rectangle = Rectangle.create(**attributes)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_save_to_file_none(self):
        """ Test save_to_file method:
        writes the JSON string representation of None to a file
        """
        # test save_to_file with None
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """ Test save_to_file method:
        writes the JSON string representation of empty list to a file
        """
        # test save_to_file with empty list
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_normal_list(self):
        """Test if save_to_file method saves a list with a single
        Rectangle to file"""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_json = \
                '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]'
            self.assertEqual(content, expected_json)

    def test_load_from_file_file_not_exist(self):
        """Test load_from_file method when the file doesn't exist"""
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file_file_exists(self):
        """Test load_from_file method when the file exists"""
        # Create a dummy file with sample JSON content
        with open("Rectangle.json", "w") as file:
            file.write('[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]')

        rectangles = Rectangle.load_from_file()
        expected_rectangles = [Rectangle(2, 3, 4, 5, 1)]

        # Compare the attributes of the objects
        self.assertEqual(rectangles[0].id, expected_rectangles[0].id)
        self.assertEqual(rectangles[0].width, expected_rectangles[0].width)
        self.assertEqual(rectangles[0].height, expected_rectangles[0].height)
        self.assertEqual(rectangles[0].x, expected_rectangles[0].x)
        self.assertEqual(rectangles[0].y, expected_rectangles[0].y)


if __name__ == '__main__':
    unittest.main()
