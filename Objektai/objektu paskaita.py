class Kate:
    uodega = True
    def __init__(self, ivestas_vardas='Rainius', ivestas_kojos=5):
        self.vardas = ivestas_vardas
        self.kojos = ivestas_kojos


    def miaukseti(self):
        print(f'Sveiki as esu {self.vardas}')

kate1 = Kate(ivestas_vardas='Pilka')
kate2 = Kate(ivestas_vardas='Juoda', ivestas_kojos=4)

print(kate1.vardas)
kate1.vardas = 'JuodaJuoda'
print(kate1.vardas)

"""
"""


class Apskritimas:
    def __init__(self, spindulys):
        self.pi = 3.14
        self.spindulys = spindulys

    def plotas(self, pi):
        return self.spindulys + self.spindulys * self.pi


apskritimas1 = Apskritimas(spindulys=5)
apskritimas2 = Apskritimas(spindulys=6)

print(apskritimas1(plotas))


class Kate:
    def __init__(self, spalva, kojos):
        self.spalva = spalva
        self.kojos = kojos


kates = []

kate1 = Kate(spalva='juoda', kojos=4)
kate2 = Kate(spalva='pilka', kojos=4)
kate3 = Kate(spalva='balta', kojos=4)

kates.append(kate1)
kates.append(kate2)
kates.append(kate3)

for kate in kates:
    print(kate.kojos)




class Preke:
    def __init__(self, pavadinimas, savikaina):
        self.pavadinimas = pavadinimas
        self.savikaina = savikaina

def nuskaityti_prekes(failo_vieta):
    pass #kazkada bus implementuota
    return [{'pavadinimas': 'telefonas', 'savikaina': 5, 'pavadinimas': 'tele', 'savikaina': 100}]

prekiu_sarasas = nuskaityti_prekes('c:/documents/prekes.csv')
prekes = []
for eilute in prekiu_sarasas:
    prekes_pavadinimas_failo = eilute['pavadinimas']
    prekes_savikaina_failo = eilute['savikaina']
    preke_failo = Preke(pavadinimas=prekes_pavadinimas_failo, savikaina=prekes_savikaina_failo)
    prekes.append(preke_failo)


class Preke:  # rasyt didziaja raide
    def __init__(self, pavadinimas=None, savikaina=None):
        self.pavadinimas = pavadinimas
        self.savikaina = savikaina

    def __str__(
            self):  # ner prasmes sita naudot, galima aprasinet, bet nebutina, konstruktoriui visas reikalas matosi
        return f"Spausdinam is str"

    def __repr__(self):
        return f"Spausdinam is repr"

    preke1 = Preke(pavadinimas='Jonas', savikaina=10)
    print()


class Preke:  # rasyt didziaja raide
    def __init__(self, pavadinimas=None, savikaina=None):
        self.pavadinimas = pavadinimas
        self.savikaina = savikaina

    def __str__(self):  # ner prasmes sita naudot, galima aprasinet, bet nebutina, konstruktoriui visas reikalas matosi
        return f"Spausdinam is str"


    def atspausdinti_informacija(self):
        print(self.pavadinimas)


preke1 = Preke()
print(preke1)
preke1.atspausdinti_informacija()




