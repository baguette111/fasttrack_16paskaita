import unittest
from keliamieji import *

class TestKeliammieji(unittest.TestCase):
    def test_ar_keliamieji(self):
        self.assertEqual("Nekeliamieji", ar_keliamieji(2041))

    def test_dalyba(self):
        self.assertEqual(2,5, dalyba(5, 2))
        self.assertEqual(3.333, dalyba(10.3))
        self.assertEqual(5, dalyba(10, 2))


def test_dalyba (a, b):
    return a // b

