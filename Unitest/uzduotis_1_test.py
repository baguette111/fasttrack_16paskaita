"""Pasiimti anksčiau sukurtą programos kodą (iš Teams)
Funkcijas perdaryti taip, kad jos gražintų duomenis
Sukurti UNIT testą visoms funkcijoms
Kiekvienai funkcijai turi būti mažiausiai 3 patikrinimai
Maksimaliai patobulinti kodą, nuolatos leidžiant sukurtą UNIT testą
"""

import unittest
from uzduotis_1 import *

class TestSkaiciuSuma(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(3, skaiciu_suma(0,3))
        self.assertEqual(5, skaiciu_suma(2,3))

    def test_didziausias_skaicius(self):
        self.assertEqual(3, didziausias_skaicius(0, 3))
        self.assertEqual(3, didziausias_skaicius(2, 3))
        self.assertEqual(3, didziausias_skaicius(1, 3))

    def test_sakinys_atvirksciai(self):
        self.assertEqual('pridėjo? tiek plytų čia kas atėjo, pavasaris Jau', sakinys_atvirksciai('Jau pavasaris atėjo, kas čia plytų tiek pridėjo?'))
        self.assertEqual('1 d c b a', sakinys_atvirksciai('a b c d 1'))
        self.assertEqual('d c b a', sakinys_atvirksciai('a b c d'))

    def test_ar_yra(self):
        self.assertEqual(True, ar_yra(5, [5, 6, 7, 9, 10, 15, 45, 100]))
        #self.assertEqual(False, ar_yra([1, 2, a, b]))
    

if __name__ == '__main__':
    unittest.main()