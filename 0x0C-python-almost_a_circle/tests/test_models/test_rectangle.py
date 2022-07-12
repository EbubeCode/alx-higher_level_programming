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
        """invalid x"""
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
        """invalid y"""
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
        """test area"""
        rect = Rectangle(4, 6)
        self.assertEqual(rect.area(), 24)

        rect = Rectangle(7, 90, 5, 0, 13)
        self.assertEqual(rect.area(), 7 * 90)

    def test_display_origin(self):
        """test display from origin x=0 y=0"""
        rect = Rectangle(4, 3)
        op = io.StringIO()
        sys.stdout = op
        rect.display()
        sys.stdout = sys.__stdout__
        expected = (('#' * 4) + '\n') * 3
        self.assertEqual(expected, op.getvalue())

    def test_display(self):
        """test display from other points"""
        rect = Rectangle(4, 3, 3, 3)
        op = io.StringIO()
        sys.stdout = op
        rect.display()
        sys.stdout = sys.__stdout__
        ex = ('\n' * 3) + ('   ' + '#' * 4 + '\n') * 3
        self.assertEqual(ex, op.getvalue())

    def test_printrect(self):
        """test string representation of the rectangle"""
        rect = Rectangle(4, 3, id=6)
        op = io.StringIO()
        sys.stdout = op
        print(rect)
        sys.stdout = sys.__stdout__
        expected = '[Rectangle] (6) 0/0 - 4/3\n'
        self.assertEqual(expected, op.getvalue())

    def test_converttostr(self):
        """test string representation of the rectangle using str()"""
        rect = Rectangle(7, 9, 1, 7, 9)
        rect_str = str(rect)
        expected = '[Rectangle] (9) 1/7 - 7/9'
        self.assertEqual(rect_str, expected)

    def test_update(self):
        """test update with just *args"""
        rect = Rectangle(10, 10, 10, 10)
        rect_str = str(rect)
        expected = f'[Rectangle] ({rect.id}) 10/10 - 10/10'
        self.assertEqual(rect_str, expected)

        rect.update(89)
        rect_str = str(rect)
        expected = '[Rectangle] (89) 10/10 - 10/10'
        self.assertEqual(rect_str, expected)

        rect.update(89, 2)
        rect_str = str(rect)
        expected = '[Rectangle] (89) 10/10 - 2/10'
        self.assertEqual(rect_str, expected)

        rect.update(89, 2, 3)
        rect_str = str(rect)
        expected = '[Rectangle] (89) 10/10 - 2/3'
        self.assertEqual(rect_str, expected)

        rect.update(89, 2, 3, 4)
        rect_str = str(rect)
        expected = '[Rectangle] (89) 4/10 - 2/3'
        self.assertEqual(rect_str, expected)

        rect.update(89, 2, 3, 4, 5)
        rect_str = str(rect)
        expected = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(rect_str, expected)

    def test_key_update(self):
        """test the update method using named attributes"""
        rect = Rectangle(10, 10, 10, 10, 4)
        rect_str = str(rect)
        expected = f'[Rectangle] ({rect.id}) 10/10 - 10/10'
        self.assertEqual(rect_str, expected)

        rect.update(height=1)
        rect_str = str(rect)
        expected = '[Rectangle] (4) 10/10 - 10/1'
        self.assertEqual(rect_str, expected)

        rect.update(height=1, id=5, width=6)
        rect_str = str(rect)
        expected = '[Rectangle] (5) 10/10 - 6/1'
        self.assertEqual(rect_str, expected)

        rect.update(x=81, y=4)
        rect_str = str(rect)
        expected = '[Rectangle] (5) 81/4 - 6/1'
        self.assertEqual(rect_str, expected)

        rect.update(8, height=5)
        rect_str = str(rect)
        expected = '[Rectangle] (8) 81/4 - 6/1'
        self.assertEqual(rect_str, expected)


if __name__ == "__main__":
    unittest.main()
