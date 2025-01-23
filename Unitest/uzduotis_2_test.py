"""Pasiimti anksčiau sukurtą programos kodą (iš Teams)
Teste sukurti setUp() metodą, kuriame būtų inicijuotas klasės objektas
Funkcijas perdaryti taip, kad jos gražintų duomenis
Sukurti UNIT testą visoms funkcijoms
Kiekvienai funkcijai turi būti mažiausiai 3 patikrinimai
Maksimaliai patobulinti kodą, nuolatos leidžiant sukurtą UNIT testą
"""

import unittest
from uzduotis_2 import *

class TestStringTriukai(unittest.TestCase):
    def setUp(self):
        self.objektas1 = StringTriukai(("Labas vakaras, studentai"))
        self.objektas2 = StringTriukai(("Labasvakaras, studentai"))
        self.objektas3 = StringTriukai(("Labasvakarasstudentai"))
        
    def test_pirmas_zodis(self):
        self.assertEqual("Labas", self.objektas1.pirmas_zodis())
        self.assertEqual("Labasvakaras,", self.objektas2.pirmas_zodis())
        self.assertEqual("Labasvakarasstudentai", self.objektas3.pirmas_zodis())
        
    def test_paskutinis_zodis(self):
        self.assertEqual("studentai", self.objektas1.paskutinis_zodis())
        self.assertEqual("studentai", self.objektas2.paskutinis_zodis())
        self.assertEqual("Labasvakarasstudentai", self.objektas3.paskutinis_zodis())
        

        
        
        
if __name__ == '__main__':
    unittest.main()