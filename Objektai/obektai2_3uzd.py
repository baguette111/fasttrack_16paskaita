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


class Irasas:
    def __init__(self, suma):
        self.suma = suma
        print(f'Suma:, {self.suma}')

class PajamuIrasas(Irasas):
    def __init__(self, suma):
        super().__init__(suma)

    def siuntejas(self):
        print(input('Siuntejas: '))

    def papildoma_informacija(self):
        print(input('Papildoma informacija: '))

class IslaiduIrasas(Irasas):
    def __init__(self, suma):
        super().__init__(suma)

    def atsiskaitymo_budas(self):
        print(input('Atsiskaitymo budas: '))

    def isigyta_preke_paslauga(self):
        print(input('Isigyta preke paslauga: '))

