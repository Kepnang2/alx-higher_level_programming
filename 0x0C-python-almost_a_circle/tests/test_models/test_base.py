"""Unittest for the Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
""" Base = Base
to_json_string = Base.to_json_string
save_to_file = Base.save_to_file
from_json_string = Base.from_json_string
create = Base.create
load_from_file = Base.load_from_file
 """
class TestBase(unittest.TestCase):



    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Base.__doc__) > 0)

    def test_class_doc(self):
        """documentation"""

        self.assertTrue(len(Base.__doc__) > 0)

    def test_json_string_doc(self):
        """documentation"""

        self.assertTrue(len(Base.to_json_string.__doc__) > 0)

    def test_save_file(self):
        """documentation"""

        self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    def test_from_json(self):
        """documentation"""

        self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    def test_create(self):
        """documentation"""

        self.assertTrue(len(Base.create.__doc__) > 0)

    def test_load_file(self):
        """documentation"""

        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    """Base class test cases"""
    def test_arg_01(self):
        """no argument passed to object"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_arg_02(self):
        """with one object created but with argument"""
        Base._Base__nb_objects = 0
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(98)
        self.assertEqual(b4.id, 98)
        b5 = Base(-8)
        self.assertEqual(b5.id, -8)
        b6 = Base(9)
        self.assertEqual(b6.id, 9)

    def test_arg_03(self):
        """multiple objects without argument
        and one with one argument"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b5.id, 3)

    def test_arg_04(self):
        """multiple objects without argument
        and one with one argument"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_arg_04(self):
        """2 test with arguments"""
        Base._Base__nb_objects = 0
        b3 = Base(6)
        b4 = Base(98)
        self.assertEqual(b4.id, 98)

    def test_04_01(self):
        """for type and instance."""
        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(isinstance(b6, Base))

    def test_arg_05(self):
        """ for multiple object with arguments then one last
        doesn't have any argument"""
        Base._Base__nb_objects = 0
        b3 = Base(5)
        b4 = Base(12)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_private_attribute(self):
        """Check if attribute exists in object"""
        self.assertFalse(hasattr(Base, '__nb_objects'))

    def test_save_file_Rectangle(self):
        """ saving JSON to file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])
            self.assertDictEqual(r2.to_dictionary(), my_list[1])

    def test_save_Rectangle_none(self):
        """saving to file with none"""
        Base._Base__nb_objects = 0
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def test_save_Rectangle_empty_list(self):
        """saving to file with none"""
        Base._Base__nb_objects = 0
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def test_save_rectangle_only(self):
        """ saving of json representation of objects to file
        for Rectangle only"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])

    def test_save_Square(self):
        """ savingjson representation to file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        s2 = Square(2)
        Square.save_to_file([r1, s2])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(r1.to_dictionary(), my_list[0])
            self.assertDictEqual(s2.to_dictionary(), my_list[1])

    def test_save_Square_none(self):
        """saving to file with none"""
        Base._Base__nb_objects = 0
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def test_save_Square_only_square(self):
        """saving to file with only Square"""
        Base._Base__nb_objects = 0
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertDictEqual(s1.to_dictionary(), my_list[0])

    def test_create_Rectangle(self):
        """Rectangle new instance"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertDictEqual(r1_dictionary, r2.to_dictionary())

    def test_create_Square(self):
        """creating of new Square instance"""
        Base._Base__nb_objects = 0
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertDictEqual(s1_dictionary, s2.to_dictionary())

    def test_load_file_rectangle(self):
        """loading from file for Rectangle"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_input[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_input[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")
        self.assertEqual(list_rectangles_output[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")

    def test_load_file_square(self):
        """loading from file for Square"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_input[0].__str__(),
                         "[Square] (5) 0/0 - 5")
        self.assertEqual(list_squares_output[0].__str__(),
                         "[Square] (5) 0/0 - 5")
        self.assertEqual(list_squares_input[1].__str__(),
                         "[Square] (6) 9/1 - 7")
        self.assertEqual(list_squares_output[1].__str__(),
                         "[Square] (6) 9/1 - 7")

    def test_json_string(self):
        """to_json_string with wrong args."""

        s1 = ("to_json_string() missing 1 required positional argument: " +
              "'list_dictionaries'")
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(s1, str(x.exception))
        s2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(s2, str(x.exception))

    def test_to_json_string(self):
        """json string"""
        a = Base()
        b = a.__dict__
        self.assertTrue(type(b) is dict)
        c = Base.to_json_string([b])
        self.assertTrue(type(c) is str)

    def test_from_json_string(self):
        """json string"""
        a = Base(12)
        b = a.__dict__
        c = Base.to_json_string([b])
        d = Base.from_json_string(c)
        self.assertTrue(type(c) is str)
        self.assertTrue(type(d) is list)


if __name__ == "__main__":
    unittest.main()
