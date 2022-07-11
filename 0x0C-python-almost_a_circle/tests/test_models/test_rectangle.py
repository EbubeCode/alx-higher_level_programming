#!/usr/bin/python3
"""
Test module to rectangle.Rectangle
"""
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Rectangle Class Test"""

    def test_creation(self):
        """check if an instance can be created"""
        rect = Rectangle(3, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)

    def test_correctId(self):
        """check if id is correctly assigned"""
        rect = Rectangle(3, 2, id=6)
        self.assertEqual(rect.id, 6)

    def test_stringid(self):
        """check if id can be a string"""
        rect = Rectangle(3, 2, id='my_id')
        self.assertEqual(rect.id, 'my_id')

    def test_full_arguement(self):
        """pass full arguments"""
        rect = Rectangle(5, 6, 2, 3, 17)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 17)

    def test_invalidwidth(self):
        """invalid width"""
        with self.assertRaises(TypeError):
            rect = Rectangle('4', 6)
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 6)
        rect = Rectangle(4, 6)
        with self.assertRaises(TypeError):
            rect.width = '5'
        with self.assertRaises(ValueError):
            rect.width = -7

    def test_invalidheight(self):
        """invalid height"""
        with self.assertRaises(TypeError):
            rect = Rectangle(4, '6')
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -6)
        rect = Rectangle(4, 6)
        with self.assertRaises(TypeError):
            rect.height = '5'
        with self.assertRaises(ValueError):
            rect.height = -7

    def test_invalidx(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 6, '0', 0, 7)
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 6, -7, 6, 9)
        rect = Rectangle(4, 6)
        with self.assertRaises(TypeError):
            rect.x = '5'
        with self.assertRaises(ValueError):
            rect.x = -7

    def test_invalidy(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 6, 6, '0', 7)
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 6, 7, -6, 9)
        rect = Rectangle(4, 6)
        with self.assertRaises(TypeError):
            rect.y = '5'
        with self.assertRaises(ValueError):
            rect.y = -7

    def test_area(self):
        rect = Rectangle(4, 6)
        self.assertEqual(rect.area(), 24)

        rect = Rectangle(7, 90, 5, 0, 13)
        self.assertEqual(rect.area(), 7 * 90)

    def test_display(self):
        rect = Rectangle(4, 3)
        op = io.StringIO()
        sys.stdout = op
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual('####\n####\n####\n', op.getvalue())


if __name__ == "__main__":
    unittest.main()
