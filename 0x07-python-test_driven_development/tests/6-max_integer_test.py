#!/usr/bin/python3
"""
Test module for 6-max_integer module
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class that houses test methods"""

    def test_max_integer(self):
        self.assertEqual(max_int([1, 3, 4, 2]), 4)
        self.assertEqual(max_int([1, 3, 4, 2, 6, 0, 77, 4]), 77)

    def test_none(self):
        self.assertEqual(max_int([]), None)


if __name__ == '__main__':
    unittest.main()
