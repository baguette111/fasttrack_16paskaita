"""praleisti apie privatu metoda"""
import calendar
import datetime
import numpy as np

class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = float(valandos_ikainis)
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d").date()
        self.dirbtos_dienos = (datetime.date.today() - self.dirba_nuo).days
        print(f'vardas: {self.vardas}, valandos ikainis: {self.valandos_ikainis}, dirba nuo: {self.dirba_nuo}')

    def atlyginimmas(self, dirbtos_dienos, valandos_ikainis):
        self.dirbtos_dienos = dirbtos_dienos
        self.valandos_ikainis = valandos_ikainis

    def apskaiciuoti_dienas(self):
        print(datetime.date.today() - self.dirba_nuo)

    def apskaiciuoti_atlyginima(self):
        print(self.dirbtos_dienos * 8 * self.valandos_ikainis)

class NormalusDarbuotojas(Darbuotojas):
    def __init__ (self, vardas, valandos_ikainis, dirba_nuo):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)

    def apskaiciuoti_darbo_dienas(self, pradzia, pabaiga, sventines):
        self.pradzia = pradzia
        self.pabaiga = pabaiga
        self.dirbtos_dienos = np.busday_count(self.pradzia, self.pabaiga, holidays=sventines)
        print(self.dirbtos_dienos)



darbuotojas = Darbuotojas('Arnas', '7.15', '2024-12-07')
print(darbuotojas)

darbuotojas.apskaiciuoti_atlyginima()

normalus_darbuotojas = NormalusDarbuotojas('Arnas', '7.15', '2024-12-07')

normalus_darbuotojas.apskaiciuoti_darbo_dienas('2024-12-07', '2024-12-31',  ['2024-12-24', '2024-12-25', '2024-12-26'])

normalus_darbuotojas.apskaiciuoti_atlyginima()
