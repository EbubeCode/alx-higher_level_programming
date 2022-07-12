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
            square = Square(4, '0', 0, 7)
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

    def test_dic_rep(self):
        """test the dictionary representation of a Square"""
        square = Square(10, 2, 1, 1)
        dic_rep = square.to_dictionary()
        dic = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(dic_rep, dic)

    def test_save_to_file(self):
        """tests saving a list of Squares to file"""
        s1 = Square(4, id=3)
        s2 = Square(2, 3, 3, 4)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r", encoding='UTF-8') as f:
            lis = [{'id': 3, 'size': 4, 'x': 0, 'y': 0}]
            lis.append({'id': 4, 'size': 2, 'x': 3, 'y': 3})
            self.assertEqual(eval(f.read()), lis)

    def test_create(self):
        """test creation from the create method in the base class"""
        s1 = Square(5, 2, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)

        self.assertEqual(s1.id, s2.id)
        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.x, s2.x)

    def test_loadfromfile(self):
        """test loading a Rectangle from file"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        s3 = list_squares_output[0]
        s4 = list_squares_output[1]
 
        self.assertEqual(s1.id, s3.id)
        self.assertEqual(s1.size, s3.size)
        self.assertEqual(s1.y, s3.y)
        self.assertEqual(s1.x, s3.x)
 
        self.assertEqual(s4.id, s2.id)
        self.assertEqual(s4.width, s2.width)
        self.assertEqual(s4.y, s2.y)
        self.assertEqual(s4.x, s2.x)


if __name__ == "__main__":
    unittest.main()
