"""
Padaryti minibiudžeto programą, kuri:
Leistų vartotojui įvesti pajamas
Leistų vartotojui įvesti išlaidas
Leistų vartotojui parodyti pajamų/išlaidų balansą
Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
Leistų vartotojui išeiti iš programos

Rekomendacija, kaip galima būtų padaryti:
Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
Programa turi turėti klasę Biudzetas, kurioje būtų:
Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
Metodas prideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
Metodas prideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
Metodas gauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
Metodas parodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).

"""

class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f'{self.tipas}: {self.suma}'

class Biudzetas:
    def __init__(self,):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        irasas = Irasas("Pajamos", suma)
        self.zurnalas.append(irasas)

    def prideti_islaidu_irasa(self, suma):
        irasas = Irasas("Islaidos", suma)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):
        pajamos = sum([irasas.suma for irasas in self.zurnalas if irasas.tipas == "Pajamos"])
        islaidos = sum([irasas.suma for irasas in self.zurnalas if irasas.tipas == "Islaidos"])
        return pajamos - islaidos

    def parodyti_ataskaita(self):
        if not self.zurnalas:
            print("Nera irasu")
        else:
            for irasas in self.zurnalas:
                print(irasas)

def valdyti_biudzeta():
    biudzetas = Biudzetas()

    while True:
        print("\n1. ivesti pajamas")
        print("2. ivesti islaidas")
        print("3. Parodyti pajamų/islaidu balansa")
        print("4. Parodyti biudzeto ataskaitą")
        print("5. Iseiti")

        pasirinkimas = input("Pasirinkite veiksma (1-5): ")

        if pasirinkimas == "1":
            suma = float(input("Įveskite pajamu suma: "))
            biudzetas.prideti_pajamu_irasa(suma)

        elif pasirinkimas == "2":
            suma = float(input("Įveskite islaidų suma: "))
            biudzetas.prideti_islaidu_irasa(suma)

        elif pasirinkimas == "3":
            balansas = biudzetas.gauti_balansa()
            print(f"Pajamų ir islaidu balansas: {balansas} eur")

        elif pasirinkimas == "4":
            print("\nBiudzeto ataskaita:")
            biudzetas.parodyti_ataskaita()

        elif pasirinkimas == "5":
            print("Iseinate is programos...")
            break

        else:
            print("Neteisingas pasirinkimas, bandykite dar karta.")

print(valdyti_biudzeta())