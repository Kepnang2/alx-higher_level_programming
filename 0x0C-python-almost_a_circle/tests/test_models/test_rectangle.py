for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests ractangle class"""
    def width_height_integers(self):
        """Tests for width and height as integers"""
        Base._Base.__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def with_arguments_01(self):
        """with all valid arguments"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_private_x(self):
        """x as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__x"))

    def test_private_y(self):
        """y as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__y"))

    def test_private_width(self):
        """for width as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__width"))

    def test_private_height(self):
        """height as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__height"))

    def width_setter_getter_01(self):
        """width setter and getter with integers"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        r3.width = 5
        self.assertEqual(r3.width, 5)

    def height_setter_getter_02(self):
        """height setter and getter with integers"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        r3.height = 5
        self.assertEqual(r3.height, 5)

    def height_setter_getter_03(self):
        """height setter and geter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r3.height = "5"

    def width_setter_getter_04(self):
        """width setter and geter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r3.width = "5"

    def width_str(self):
        """width with string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle("4", 3)

    def width_neg(self):
        """width with negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(-3, 3)

    def width_zero(self):
        "width with zero"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 5)

    def height_str(self):
        """height setter and geter with other data type"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(3, "3")

    def height_neg(self):
        """height with seter and getter with negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(8, -2)

    def height_zero(self):
        "setter and getter with zero"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 2)

    def test_without_arg(self):
        """no argument supplied"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle()

    def x_with_str(self):
        """x string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, "98", 4)

    def x_with_neg(self):
        """x negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(3, 4, -9, 4)

    def y_with_string(self):
        """y with string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 4, 5, "8")

    def y_with_negative(self):
        """y negative"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(3, 6, 4, -4)

    def width_with_tupple(self):
        """width tuple"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle((6, 8), 3, 4, 5)

    def width_with_dictionary(self):
        """width with dictionary"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle({"name": "alex", "other_name": "steve"}, 3, 5, 4)

    def width_with_float(self):
        """width float"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(8.86, 3, 5, 4)

    def width_with_list(self):
        """width list"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle([5, 2, 6], 3, 5, 4)

    def width_with_nan(self):
        """width nan"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(float('nan'), 3, 5, 4)

    def width_with_inf(self):
        """width inf"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(float('inf'), 3, 5, 4)

    def height_with_tupple(self):
        """height tuple"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(3, (4, 6), 5, 4)

    def height_with_dictionary(self):
        """height dictionary"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(4, {"name": "alex", "other_name": "steve"}, 5, 4)

    def height_with_float(self):
        """height float"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(6, 3.642, 5, 4)

    def height_with_list(self):
        """height list"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, [1, 2, 3], 4, 5)

    def height_with_nan(self):
        """height with nan"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(4, float('nan'), 2, 3)

    def height_with_inf(self):
        """height inf"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(3, float('inf'), 2, 3)

    def x_setter_getter_with_other_type(self):
        """x setter and geter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3, 4, 6)
        with self.assertRaises(TypeError):
            r3.x = "5"

    def y_setter_getter_with_other_type(self):
        """y setter and geter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3, 7, 8)
        with self.assertRaises(TypeError):
            r3.y = "5"

    def test_for_area(self):
        """area"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_for_str_with_id(self):
        """output class to string with id"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_for_str_without_id(self):
        """output class to string without id"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/1 - 4/6")

    def test_update_id(self):
        """update id"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_width(self):
        """update width"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_height(self):
        """update height"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_x(self):
        """update x"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_y(self):
        """update y"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        """Rectangle to dictionary output"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)
        self.assertDictEqual(r1_dictionary, {'id': 1, 'width': 10,
                                             'height': 2, 'x': 1, 'y': 9})

    def test_kwarg_update_1(self):
        """width and x with kwarg"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/10")

    def test_kwarg_update_2(self):
        """update y, x, width, id with kwarg"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/10")

    def test_kwarg_update_3(self):
        """update x, height, y and width with kwarg"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/3 - 4/2")

    def test_kwarg_update_4(self):
        """update height with kwarg"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")

    def test_setter_width_type(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, [1, 2], 2)
        self.assertRaises(TypeError, Rectangle, (1, 2), 2)
        self.assertRaises(TypeError, Rectangle, 12.5, 2)
        self.assertRaises(TypeError, Rectangle, {1, 2}, 2)
        self.assertRaises(TypeError, Rectangle, float('inf'), 2)
        self.assertRaises(TypeError, Rectangle, float('NaN'), 2)

    def test_setter_width_zero_neg(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 0, 12)
        self.assertRaises(ValueError, Rectangle, -5, 12)

    def test_setter_height_type(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 2, (1, 2))
        self.assertRaises(TypeError, Rectangle, 2, 12.5)
        self.assertRaises(TypeError, Rectangle, 2, {1, 2})
        self.assertRaises(TypeError, Rectangle, 2, float('inf'))
        self.assertRaises(TypeError, Rectangle, 2, float('NaN'))

    def test_setter_height_zero_neg(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 12, 0)
        self.assertRaises(ValueError, Rectangle, 12, -5)

    def test_setter_x_type(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 1, 2, [1, 2], 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, (1, 2), 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, 12.5, 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, {1, 2}, 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, float('inf'), 2)
        self.assertRaises(TypeError, Rectangle, 1, 2, float('NaN'), 2)

    def test_setter_x_neg(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(ValueError, Rectangle, 1, 2, -5, 2)

    def test_setter_y_type(self):
        """errors from setter"""

        Base._Base__nb_objects = 0

        self.assertRaises(TypeError, Rectangle, 1, 2, 2, [1, 2])
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, (1, 2))
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, 12.5)
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, {1, 2})
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, float('inf'))
        self.assertRaises(TypeError, Rectangle, 1, 2, 2, float('NaN'))

if __name__ == '__main__':
    unittest.main()
