"""
Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:
Gražina tekstą atbulai
Gražina tekstą mažosiomis raidėmis
Gražina tekstą didžiosiomis raidėmis
Gražina žodį pagal nurodytą eilės numerį
Gražina, kiek tekste yra nurodytų simbolių arba žodžių
Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
Susikurti kelis klasės objektus ir išbandyti visus metodus
"""


class Sakinys:
    def __init__(self, tekstas="Zen of Phyton"):
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
            print('tokio zodzio nera')  # padejo internetas

    def nurodyti_simboliai(self):
        return self.tekstas.split()

    def pakeisti_simboliai(self, senas, naujas):
        return self.tekstas.replace(senas, naujas)

    def zodziu_skaicius(self):
        zodziai = self.tekstas.split()
        return len(zodziai)

    def kiekis_skaiciu(self):
        return sum(1 for a in self.tekstas if a.isdigit())

tekstas = Sakinys(input("Ivesite sakini, kuri norite koreguoti: "))



print(tekstas.atbulai())
print(tekstas.mazosios_raides())
print(tekstas.didziosios_raides())
print(tekstas.eiles_numeris(3))
print(tekstas.nurodyti_simboliai())
print(tekstas.pakeisti_simboliai("sventes", "laisvas dienas"))
print(tekstas.zodziu_skaicius())
print(tekstas.kiekis_skaiciu())
