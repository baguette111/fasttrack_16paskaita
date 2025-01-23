"""
Sukurti minibiudžeto programą, kuri:
Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
Atvaizduotų jau įvestas pajamas ir išlaidas
Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)

Patarimas:
import pickle
"""
import pickle


class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma
    
    def __str__(self):
        return f'{self.tipas}: {self.suma}' 

class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def pridedamas_pajamu_irasas(self, suma):
        irasas = Irasas("Pajamos", suma)
        self.zurnalas.append(irasas)

    def pridedamas_islaidu_irasas(self, suma):
        irasas = Irasas("Islaidos", suma)
        self.zurnalas.append(irasas)
    
    def gauti_balansa(self):
        pajamos = sum([irasas.suma for irasas in self.zurnalas if irasas.tipas == "Pajamos"])
        islaidos = sum([irasas.suma for irasas in self.zurnalas if irasas.tipas == "Islaidos"])
        return pajamos - islaidos

biudzetas = Biudzetas()

pajamos = int(input("Iveskite pajamas: "))
islaidos = int(input("Iveskite islaidas (su minuso zenklu): "))

biudzetas.pridedamas_pajamu_irasas(pajamos)
biudzetas.pridedamas_islaidu_irasas(islaidos)

with open("zurnalas.pkl", "wb") as file:
    pickle.dump(biudzetas, file)

with open("zurnalas.pkl", "rb") as file:
    naujas_biudzetas = pickle.load(file)

for irasas in naujas_biudzetas.zurnalas:
    print(irasas)
  
print("Balanas:", naujas_biudzetas.gauti_balansa())