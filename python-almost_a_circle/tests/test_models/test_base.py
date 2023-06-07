#!/usr/bin/python3
""" This module is a unittest for the Base class """

import unittest
import os
import io
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """ test class for Base class """
    # setup and teardown methods are called before and after each test
    def setUp(self):
        """Reset the __nb_objects counter.
        print test"""
        print("Base setUp")
        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        Base._Base__nb_objects = 0

        self.base = Base()

    def tearDown(self):
        print("Base tearDown")

        sys.stdout = sys.__stdout__

        del self.base
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_print(self):
        """ test print method """
        print("Hello, world!")
        self.assertEqual(self.capture_output.getvalue(), "Hello, world!\n")
        print("Hello, world!", file=sys.__stdout__)

    # test id assignment and if it increments correctly
    def test_id(self):
        """Test __init__ method:
        id assignment in the Base class. """
        self.assertEqual(self.base.id, 1)
        base2 = Base(50)
        self.assertEqual(base2.id, 50)
        base3 = Base()
        self.assertEqual(base3.id, 2)

    def test_too_many_args(self):
        """
        test too many args to init
        """
        # test too many args
        with self.assertRaises(TypeError):
            Base(1, 1, 1, 1, 1, 1, 1)

    def test_to_json_string(self):
        """ Test to_json_string method:
        returns the JSON string representation of list_directories
        """
        # test empty list
        self.assertEqual(Base.to_json_string([]), "[]")
        # test None
        self.assertEqual(Base.to_json_string(None), "[]")
        # test normal list
        list_directories = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
            ]
        expected_json = (
            '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, '
            '{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]')
        self.assertEqual(Base.to_json_string(list_directories), expected_json)

    def test_from_json_string(self):
        """ Test from_json_string method: returns the list of the JSON string
        representation json_string
        """
        # test empty string
        self.assertEqual(Base.from_json_string(""), [])

        # test empty list
        self.assertEqual(Base.from_json_string("[]"), [])

        # test None
        self.assertEqual(Base.from_json_string(None), [])

        # test normal list
        json_string = (
            '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, '
            '{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]')
        expected_list = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

        # test invalid json string
        with self.assertRaises(ValueError):
            Base.from_json_string("invalid")

    def test_save_to_file(self):
        """ Test save_to_file method: for Base class
        """
        # Test checks correct handling of None by creating an empty file
        Base.save_to_file(None)
        with open("Base.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")
        # Test correct handling of empty list to create empty file
        Base.save_to_file([])
        with open("Base.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == '__main__':
    unittest.main()
