class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(f'metai: {self.metai}, modelis: {self.modelis}, kuro tipas: {self.kuro_tipas}')

    def judeti(self):
        print('Vaziuoja')

    def stoveti(self):
        print('Priparkuota')

    def pildyti_degalu(self):
        print('Degalai ipilti')



class Elektromobilis(Automobilis):
    def __init__(self, metai, modelis, kuro_tipas):
        super().__init__(metai, modelis, kuro_tipas)

    def pildyti_degalu(self):
        print('Baterija ikrauta')

    def vaziuoja_autonomiskai(self):
        print('Vaziuoja autonomiskai')


automobilis1 = Automobilis("2007", "Volvo XC70", "Dyzelinas")
print(automobilis1)
automobilis1.judeti()
automobilis1.pildyti_degalu()
automobilis1.stoveti()

elektromobilis1 = Elektromobilis("2022", "Tesla model S", "Elektra")
print(elektromobilis1)
elektromobilis1.judeti()
elektromobilis1.stoveti()
elektromobilis1.pildyti_degalu()
elektromobilis1.vaziuoja_autonomiskai()