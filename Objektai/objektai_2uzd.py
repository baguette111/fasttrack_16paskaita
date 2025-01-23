"""
Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:
Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
Gražina, ar nurodytos sukakties metai buvo keliamieji
Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

"""
import datetime as datetime
import datetime as date
from datetime import timedelta


class Sukaktis:
    def __init__(self, metai=1999, menuo=5, diena=31, valanda=23, minute=45, sekunde=00):
        self.data = datetime.datetime(metai, menuo, diena, valanda, minute, sekunde)

    def praejo(self):
        dabar = datetime.datetime.now()
        praejo = dabar - self.data

        metai = praejo.days // 365
        menesiu = praejo.days % 365
        savaites = praejo.days // 7
        dienos = praejo.days
        valandos = praejo.seconds // 3600
        minutes = praejo.seconds // 60
        sekundes = praejo.seconds

        return dabar, praejo, metai, savaites, dienos, valandos, minutes, sekundes

    def ar_keliamieji(self):
        metai = self.data.year
        return (metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0))

    def atima_dienu(self, dienos):
        nauja_data_atima = self.data - datetime.timedelta(days=dienos)
        return nauja_data_atima

    def prideda_dienu(self, dienos):
        nauja_data_prideda = self.data + datetime.timedelta(days=dienos)
        return nauja_data_prideda


metai = input(f'iveskite metus: ')
metai = int(metai) if metai else 1999
menuo = input(f'iveskite menesi (skaitine israiska): ')
menuo = int(menuo) if menuo else 5
diena = input(f'iveskite diena: ')
diena = int(diena) if diena else 31
valandos = input(f'iveskite valanda: ')
valandos = int(valandos) if valandos else 23
minutes = input(f'iveskite minute: ')
minutes = int(minutes) if minutes else 45
sekundes = input(f'iveskite sekundes: ')
sekundes = int(sekundes) if sekundes else 0

sukaktis = Sukaktis(metai, menuo, diena, valandos, minutes, sekundes)

print(f"metai: {metai}, menesiu: {menuo}, dienu: {diena}, valandu: {valandos}, minuciu: {minutes}, sekundziu: {sekundes}")
print(f" ar metai keliamieji? {sukaktis.ar_keliamieji()}")

atimtos_dienos = int(input(f'kiek dienu atimti?: '))
pridetos_dienos = int(input(f'kiek dienu prideti?: '))
print(f"is sukakties, atimamos {atimtos_dienos} dienos, gaunasi: {sukaktis.atima_dienu(atimtos_dienos)}")
print(f"prie sukakties, pridedamos {pridetos_dienos} dienos, gaunasi: {sukaktis.prideda_dienu(pridetos_dienos)}")
