"""
Sukurti programą, kuri:
•	Leistų vartotojui įvesti metus
•	Atspausdintų „Keliamieji metai“, jei taip yra
•	Atspausdintų „Nekeliamieji metai“, jei taip yra
Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų
"""

metai = int(input('iveskite metus: '))

if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
    print('keliamieji metai')
else:
    print('nekelemieji metai')

"""
Perdaryti 5 užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų
"""
for metai in range(1900, 2101):
    if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
        print(metai, ' yra keliamieji metai')


