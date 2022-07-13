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

    def test_dic_rep(self):
        """test the dictionary representation of a rectangle"""
        rect = Rectangle(10, 2, 1, 9, 5)
        dic_rep = rect.to_dictionary()
        dic = {'id': 5, 'x': 1, 'y': 9, 'width': 10, 'height': 2}
        self.assertEqual(dic_rep, dic)

    def test_save_to_file(self):
        """test saving a list of Rectangles to file"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=2)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r", encoding='UTF-8') as file:
            lis = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}]
            lis.append({"y": 0, "x": 0, "id": 2, "width": 2, "height": 4})
            self.assertEqual(eval(file.read()), lis)

    def test_create(self):
        """test creation from the create method in the base class"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.x, r2.x)

    def test_loadfromfile(self):
        """test loading a Rectangle from file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        r3 = list_rectangles_output[0]
        r4 = list_rectangles_output[1]

        self.assertEqual(r1.id, r3.id)
        self.assertEqual(r1.height, r3.height)
        self.assertEqual(r1.width, r3.width)
        self.assertEqual(r1.y, r3.y)
        self.assertEqual(r1.x, r3.x)

        self.assertEqual(r4.id, r2.id)
        self.assertEqual(r4.height, r2.height)
        self.assertEqual(r4.width, r2.width)
        self.assertEqual(r4.y, r2.y)
        self.assertEqual(r4.x, r2.x)


if __name__ == "__main__":
    unittest.main()
