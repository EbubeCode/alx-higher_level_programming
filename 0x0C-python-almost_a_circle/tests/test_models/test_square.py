#!/usr/bin/python3
"""
Test module to square.Square
"""
import unittest
import io
import sys
from models.square import Square


class TestBase(unittest.TestCase):
    """Square Class Test"""

    def test_creation(self):
        """check if an instance can be created"""
        square = Square(3)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.size, 3)

    def test_corsquareId(self):
        """check if id is corsquarely assigned"""
        square = Square(3, id=6)
        self.assertEqual(square.id, 6)

    def test_stringid(self):
        """check if id can be a string"""
        square = Square(3, id='my_id')
        self.assertEqual(square.id, 'my_id')

    def test_full_arguement(self):
        """pass full arguments"""
        square = Square(5, 2, 3, 17)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 17)

    def test_invalidsize(self):
        """invalid width"""
        with self.assertRaises(TypeError):
            square = Square('4')
        with self.assertRaises(ValueError):
            square = Square(-4)
        square = Square(4, 6)
        with self.assertRaises(TypeError):
            square.size = '5'
        with self.assertRaises(ValueError):
            square.size = -7

    def test_invalidx(self):
        """invalid x"""
        with self.assertRaises(TypeError):
            square = Square(4,'0', 0, 7)
        with self.assertRaises(ValueError):
            square = Square(4, -7, 6, 9)
        square = Square(4)
        with self.assertRaises(TypeError):
            square.x = '5'
        with self.assertRaises(ValueError):
            square.x = -7

    def test_invalidy(self):
        """invalid y"""
        with self.assertRaises(TypeError):
            square = Square(4, 6, '0', 7)
        with self.assertRaises(ValueError):
            square = Square(4, 7, -6, 9)
        square = Square(4)
        with self.assertRaises(TypeError):
            square.y = '5'
        with self.assertRaises(ValueError):
            square.y = -7

    def test_area(self):
        """test area"""
        square = Square(4)
        self.assertEqual(square.area(), 16)

        square = Square(7, 5, 0, 13)
        self.assertEqual(square.area(), 7 * 7)

    def test_display_origin(self):
        """test display from origin x=0 y=0"""
        square = Square(4)
        op = io.StringIO()
        sys.stdout = op
        square.display()
        sys.stdout = sys.__stdout__
        expected = (('#' * 4) + '\n') * 4
        self.assertEqual(expected, op.getvalue())

    def test_display(self):
        """test display from other points"""
        square = Square(4, 3, 3)
        op = io.StringIO()
        sys.stdout = op
        square.display()
        sys.stdout = sys.__stdout__
        ex = ('\n' * 3) + ('   ' + '#' * 4 + '\n') * 4
        self.assertEqual(ex, op.getvalue())

    def test_printsquare(self):
        """test string representation of the squareangle"""
        square = Square(4, id=6)
        op = io.StringIO()
        sys.stdout = op
        print(square)
        sys.stdout = sys.__stdout__
        expected = '[Square] (6) 0/0 - 4\n'
        self.assertEqual(expected, op.getvalue())

    def test_converttostr(self):
        """test string representation of the squareangle using str()"""
        square = Square(7, 1, 7, 9)
        square_str = str(square)
        expected = '[Square] (9) 1/7 - 7'
        self.assertEqual(square_str, expected)

    def test_update(self):
        """test update with just *args"""
        square = Square(10, 10, 10)
        square_str = str(square)
        expected = f'[Square] ({square.id}) 10/10 - 10'
        self.assertEqual(square_str, expected)

        square.update(89)
        square_str = str(square)
        expected = '[Square] (89) 10/10 - 10'
        self.assertEqual(square_str, expected)

        square.update(89, 2)
        square_str = str(square)
        expected = '[Square] (89) 10/10 - 2'
        self.assertEqual(square_str, expected)

        square.update(89, 2, 4)
        square_str = str(square)
        expected = '[Square] (89) 4/10 - 2'
        self.assertEqual(square_str, expected)

        square.update(89, 2, 4, 5)
        square_str = str(square)
        expected = '[Square] (89) 4/5 - 2'
        self.assertEqual(square_str, expected)

    def test_key_update(self):
        """test the update method using named attributes"""
        square = Square(10, 10, 10, 4)
        square_str = str(square)
        expected = f'[Square] ({square.id}) 10/10 - 10'
        self.assertEqual(square_str, expected)

        square.update(size=1)
        square_str = str(square)
        expected = '[Square] (4) 10/10 - 1'
        self.assertEqual(square_str, expected)

        square.update(size=1, id=5)
        square_str = str(square)
        expected = '[Square] (5) 10/10 - 1'
        self.assertEqual(square_str, expected)

        square.update(x=81, y=4)
        square_str = str(square)
        expected = '[Square] (5) 81/4 - 1'
        self.assertEqual(square_str, expected)

        square.update(8, size=5)
        square_str = str(square)
        expected = '[Square] (8) 81/4 - 1'
        self.assertEqual(square_str, expected)


if __name__ == "__main__":
    unittest.main()
