#!/usr/bin/python3
"""
Test module to base.Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base Class Test"""

    def test_creation(self):
        """check if an instance can be created"""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_correctId(self):
        """check if id is correctly assigned"""
        base = Base(2)
        self.assertEqual(base.id, 2)

    def test_stringid(self):
        """check if id can be a string"""
        base = Base('my_id')
        self.assertEqual(base.id, 'my_id')

    def test_from_json_string(self):
        """tests the static method from_json_string"""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        list_str = str(list_input)
        self.assertEqual(list_input, Base.from_json_string(list_str))


if __name__ == "__main__":
    unittest.main()
