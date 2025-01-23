import unittest
from keliamieji2 import *

class TestKeliammieji(unittest.TestCase):
    def test_ar_keliamieji2(self):
        ###self.assertEqual(False, ar_keliamieji2(2041))
        self.assertTrue(ar_keliamieji2(2004))
        self.assertFalse(ar_keliamieji2(2100))

if __name__ == "__main__":
    unittest.main()
