"""Unitfor Square class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests Square class
    """
    def test_size(self):
        """Square integer size"""
        Base._Base__nb_objects = 0
        s1 = Square(6)
        self.assertEqual(s1.size, 6)

    def test_size_zero(self):
        """zero"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
            self.assertEqual(e, "width must be > 0")

    def test_size_negative(self):
        """negative number"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(-3)
            self.assertEqual(e, "width must be > 0")

    def test_size_string(self):
        """string"""
        with self.assertRaises(TypeError) as e:
            s1 = Square("3m")
            self.assertEqual(e, "width must be an integer")

    def test_size_list(self):
        """list"""
        with self.assertRaises(TypeError) as e:
            s1 = Square([1, 2, 2, 5])
            self.assertEqual(e, "width must be an integer")

    def test_size_dict(self):
        """dictionary"""
        with self.assertRaises(TypeError) as e:
            s1 = Square({"n": 3, "b": 4})
            self.assertEqual(e, "width must be an integer")

    def test_size_tuple(self):
        """tuple"""
        with self.assertRaises(TypeError) as e:
            s1 = Square((3, 5, 2, 4))
            self.assertEqual(e, "width must be an integer")

    def test_size_float(self):
        """float"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(6.96)
            self.assertEqual(e, "width must be an integer")

    def test_size_nan(self):
        """not a number(nan)"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(float('nan'))
            self.assertEqual(e, "width must be an integer")

    def test_size_inf(self):
        """Infinity(inf)"""
        with self.assertRaises(TypeError) as e:
            s1 = Square(float('inf'))
            self.assertEqual(e, "width must be an integer")

    def test_printing_square(self):
        """string output of Square"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")

    def test_size_with_no_argument(self):
        """without supplied"""
        with self.assertRaises(TypeError) as e:
            s1 = Square()
            self.assertEqual(e, "__init__() missing 1 required \
                             positional argument: 'size'")

    def test_size_private(self):
        """Tests if size is an attribute of Square"""
        self.assertFalse(hasattr(Square, "_Square__size"))

    def test_area(self):
        """area of Square"""
        Base._Base__nb_objects = 0
        s1 = Square(6)
        self.assertEqual(s1.area(), 36)

    def test_with_id(self):
        """square string representation with id argument"""
        Base._Base__nb_objects = 0
        s1 = Square(6)
        s2 = Square(1)
        s3 = Square(3, 1, 3, 83)
        self.assertEqual(s3.__str__(), "[Square] (83) 1/3 - 3")

    def test_x_with_negative(self):
        """x: negative integer"""
        with self.assertRaises(ValueError) as e:
            s3 = Square(3, -5, 3, 83)
            self.assertEqual(e, "x must be >= 0")

    def test_x_with_string(self):
        """x: a string"""
        with self.assertRaises(TypeError) as e:
            s3 = Square(3, "8", 3, 83)
            self.assertEqual(e, "x must be an integer")

    def test_y_with_negative(self):
        """y: a negative integer"""
        with self.assertRaises(ValueError) as e:
            s3 = Square(3, 5, -3, 83)
            self.assertEqual(e, "y must be >= 0")

    def test_y_with_string(self):
        """y: a string"""
        with self.assertRaises(TypeError) as e:
            s3 = Square(3, 8, "3", 83)
            self.assertEqual(e, "y must be an integer")

    def test_update_id(self):
        """for update id"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")

    def test_update_size(self):
        """for update size"""
        s1 = Square(5)
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")

    def test_update_x(self):
        """for update x"""
        s1 = Square(5)
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")

    def test_update_y(self):
        """for update y"""
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_update_without_arg(self):
        """update square without any argument passed"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update()
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")

    def test_to_dictionary(self):
        """Square to dictionary output"""
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(type(s1_dictionary), dict)
        self.assertDictEqual(s1_dictionary, {'id': 1, 'size': 10,
                                             'x': 2, 'y': 1})

    def test_save_to_file_empty_list(self):
        """saving to file with an empty list"""
        Base._Base__nb_objects = 0
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            read = file.read()
            my_list = Base.from_json_string(read)
            self.assertListEqual(my_list, [])

    def test_kwarg_update_1(self):
        """update x with kwarg"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/0 - 5")

    def test_kwarg_update_2(self):
        """update size and x with kwarg"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/1 - 7")

    def test_kwarg_update_3(self):
        """update id, y and size with kwarg"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/1 - 7")

    def test_kwarg_update_4(self):
        """update all with kwarg"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(size=7, id=89, y=1, x=4)
        self.assertEqual(s1.__str__(), "[Square] (89) 4/1 - 7")

    def test_set_get_size(self):
        """setter and getter"""

        Base._Base__nb_objects = 0

        s1 = Square(4)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(s1.size, 4)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s3.size, 3)

    def test_setter_size_type(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, [2, 2])
        self.assertRaises(TypeError, Square, (3, 4))
        self.assertRaises(TypeError, Square, 1.3)
        self.assertRaises(TypeError, Square, {1, 2})
        self.assertRaises(TypeError, Square, float('inf'))
        self.assertRaises(TypeError, Square, float('NaN'))

    def test_setter_width_zero_neg(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -6)

    def test_setter_x_type(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Square, 2, [1, 2], 2)
        self.assertRaises(TypeError, Square, 2, (1, 2), 2)
        self.assertRaises(TypeError, Square, 2, 12.5, 2)
        self.assertRaises(TypeError, Square, 2, {1, 2}, 2)
        self.assertRaises(TypeError, Square, 2, float('inf'), 2)
        self.assertRaises(TypeError, Square, 2, float('NaN'), 2)

    def test_setter_x_neg(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Square, 2, -5, 2)

    def test_setter_y_type(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Square, 2, 2, [1, 2])
        self.assertRaises(TypeError, Square, 2, 2, (1, 2))
        self.assertRaises(TypeError, Square, 2, 2, 12.5)
        self.assertRaises(TypeError, Square, 2, 2, {1, 2})
        self.assertRaises(TypeError, Square, 2, 2, float('inf'))
        self.assertRaises(TypeError, Square, 2, 2, float('NaN'))

if __name__ == '__main__':
    unittest.main()
