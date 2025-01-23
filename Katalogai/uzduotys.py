import datetime
from datetime import timedelta

class Sukaktis:
    def __init__(self, metai, menuo, diena, valanda, minute, sekunde):
        # Sukuriame datą naudodami datetime
        self.data = datetime.datetime(metai, menuo, diena, valanda, minute, sekunde)

    def praejo(self):
        dabar = datetime.datetime.now()
        praejo = dabar - self.data

        metai = praejo.days // 365
        savaites = praejo.days // 7
        dienos = praejo.days
        valandos = praejo.seconds // 3600
        minutes = praejo.seconds // 60
        sekundes = praejo.seconds

        return praejo, metai, savaites, dienos, valandos, minutes, sekundes

    def ar_keliamieji(self):
        # Patikriname, ar metai yra keliamieji
        metai = self.data.year
        return (metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0))

    def atima_dienu(self, dienos_atimti):
        # Atimame dienas nuo datos
        nauja_data_atima = self.data - timedelta(days=dienos_atimti)
        return nauja_data_atima

    def prideda_dienu(self, dienos_prideti):
        # Pridedame dienas prie datos
        nauja_data_prideda = self.data + timedelta(days=dienos_prideti)
        return nauja_data_prideda


# Vartotojo įvestis
metai = int(input(f'Įveskite metus: '))
menuo = int(input(f'Įveskite mėnesį (skaitinė išraiška): '))
diena = int(input(f'Įveskite dieną (skaitinė išraiška): '))
valandos = int(input(f'Įveskite valandą (skaitinė išraiška): '))
minutes = int(input(f'Įveskite minutę (skaitinė išraiška): '))
sekundes = int(input(f'Įveskite sekundes (skaitinė išraiška): '))

# Sukuriame Sukakties objektą
sukaktis = Sukaktis(metai, menuo, diena, valandos, minutes, sekundes)

# Atspausdiname praeitą laiką
praejo, metai, savaites, dienos, valandos, minutes, sekundes = sukaktis.praejo()
print(f"Praėjo laikas: {praejo}")
print(f"Metai: {metai}, Savaitės: {savaites}, Dienos: {dienos}, Valandos: {valandos}, Minutės: {minutes}, Sekundės: {sekundes}")

# Pavyzdžiui, patikrinkime, ar metai keliamieji
print(f"Ar metai keliamieji? {sukaktis.ar_keliamieji()}")

# Pavyzdys: atimti arba pridėti dienas
dienos_atimti = int(input(f'Įveskite dienų skaičių, kurį norite atimti: '))
dienos_prideti = int(input(f'Įveskite dienų skaičių, kurį norite pridėti: '))

print(f"Po {dienos_atimti} dienų atėmimo data bus: {sukaktis.atima_dienu(dienos_atimti)}")
print(f"Po {dienos_prideti} dienų pridėjimo data bus: {sukaktis.prideda_dienu(dienos_prideti)}")





