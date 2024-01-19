#!/usr/bin/python3
""" base test module """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ test cases for base class """

    def test_auto_id_assignment(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id_assignment_with_given_val(self):
        base = Base(id=89)
        self.assertEqual(base.id, 89)

    def test_to_json_str_with_none(self):
        self.assertIsNone(Base.to_json_string(None))

    def test_to_json_str_with_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_str_with_list_of_dicts(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_to_json_str_returns_str(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
