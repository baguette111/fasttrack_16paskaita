class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def mazosios_raides(self):
        return self.tekstas.lower()

    def didziosios_raides(self):
        return self.tekstas.upper()

    def eiles_numeris(self, numeris):
        zodziai = self.tekstas.split()
        if 1 <= numeris <= len(zodziai):
            return zodziai[numeris - 1]
        else:
            return 'Tokio zodzio nera'

    def nurodyti_simboliai(self):
        return self.tekstas.split()

    def pakeisti_simboliai(self, senas=None, naujas=None, numeris=None):
        zodziai = self.tekstas.split()

        if numeris is not None:
            # Check if the word index exists in the list of words
            if 1 <= numeris <= len(zodziai):
                zodziai[numeris - 1] = naujas  # Replace the word at the specified index
            else:
                return "Zodis tokiu numeriu nerastas"  # If the index is out of range
        elif senas and naujas:
            # The original behavior, replacing a specific word
            zodziai = [naujas if word == senas else word for word in zodziai]

        return ' '.join(zodziai)

    def zodziu_skaicius(self):
        zodziai = self.tekstas.split()
        return len(zodziai)

    def kiekis_skaiciu(self):
        return sum(1 for a in self.tekstas if a.isdigit())

# Get the input
tekstas_input = input("Įveskite tekstą bent iš 5 žodžių: ")

# Create an instance of Sakinys
tekstas = Sakinys(tekstas_input)

# Check if the input is empty
if not tekstas.tekstas.strip():
    import this  # Show Zen of Python if no input

    # Perform all the method calls with empty input
    print("Atbulai:", tekstas.atbulai())
    print("Mazosioms raidems:", tekstas.mazosios_raides())
    print("Didziosioms raidems:", tekstas.didziosios_raides())
    print("Trecias zodis:", tekstas.eiles_numeris(3))
    print("Simboliai:", tekstas.nurodyti_simboliai())
    print("Pakeisti simboliai (5th word):", tekstas.pakeisti_simboliai(numeris=2, naujas="laisvas dienas"))
    print("Zodziu skaicius:", tekstas.zodziu_skaicius())
    print("Kiek skaiciu:", tekstas.kiekis_skaiciu())
else:
    # If there is input, just perform the operations
    print("Atbulai:", tekstas.atbulai())
    print("Mazosioms raidems:", tekstas.mazosios_raides())
    print("Didziosioms raidems:", tekstas.didziosios_raides())
    print("Trecias zodis:", tekstas.eiles_numeris(3))
    print("Simboliai:", tekstas.nurodyti_simboliai())
    print("Pakeisti simboliai (5th word):", tekstas.pakeisti_simboliai(numeris=2, naujas="laisvas dienas"))
    print("Zodziu skaicius:", tekstas.zodziu_skaicius())
    print("Kiek skaiciu:", tekstas.kiekis_skaiciu())
