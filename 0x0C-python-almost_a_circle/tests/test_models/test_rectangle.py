#!/usr/bin/python3
""" rectangle test module """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ rectangle test case class """

    def test_constructor(self):
        rectangle = Rectangle(5, 4)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_area(self):
        rectangle = Rectangle(3, 7)
        self.assertEqual(rectangle.area(), 21)

    def test_display(self):
        rectangle = Rectangle(5, 4, 2, 1)
        rectangle.display()

    def test_str_representation(self):
        rectangle = Rectangle(5, 4, 2, 1, id=10)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 2/1 - 5/4")

    def test_width_setter_raises_type_error(self):
        rectangle = Rectangle(5, 4)
        with self.assertRaises(TypeError):
            rectangle.width = "hello"

    def test_width_setter_raises_value_error(self):
        rectangle = Rectangle(5, 4)
        with self.assertRaises(ValueError):
            rectangle.width = 0

if __name__ == "__main__":
    unittest.main()
