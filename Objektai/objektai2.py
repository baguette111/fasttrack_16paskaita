class Gyvunas:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print('begu')

class Suo:
    def __init__(self, vardas):
        self.vardas = vardas

class Kate(Gyvunas):
    def __init__(self, vardas, spalva):
        super().__init__(vardas, spalva)

    def miaukseti(self):
        print('miau')

kate = Kate('Muza', 'Pilka')


class Vezlys(Gyvunas):
    def __init__(self, vardas, spalva):
        super().__init__(vardas, spalva)
        self.begti()
        """none - kai tevines klases specifikacijos neturi"""

    def begti(self):
        print('einu')

vezlys = Vezlys('Bagis', 'Zalsvas')
vezlys.begti()


print(isinstance(vezlys, Suo))
"""klausia, ar Suo yra tevine klase"""




