"""
Sukurkite ir išsibandykite funkcijas, kurios:
Gražinti trijų paduotų skaičių sumą.
Gražintų paduoto sąrašo iš skaičių, sumą.
Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
Gražintų paduotą stringą atbulai.
Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
Gražintų, ar paduotas skaičius yra pirminis.
Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
Gražina, ar paduoti metai yra keliamieji, ar ne.
Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių
"""
import math
from zoneinfo import reset_tzpath


# pirmoji dalis
def skaiciu_suma(sk1=5, sk2=2, sk3=15):
    suma = sk1 + sk2 + sk3
    return suma


print(skaiciu_suma())

#antroji dalis
def skaiciu_saraso_suma(sarasas):
    suma_saraso = sum(sarasas)
    return suma_saraso


sarasas = [6, 15, 20, 6]
print(skaiciu_saraso_suma(sarasas))


# trecioji dalis
def didziausias_skaicius(*args):
    return max(args)


print(didziausias_skaicius(5, 19, 6, 4, 5))

# ketvirta dalis
def zodziai_atbulai(str):
    return str[::-1]


print(zodziai_atbulai('NAME'))


# penkta dalis
def stringo_informacija(stringas):
    zodziu_skaicius = 0
    didziosios_raides = 0
    mazosios_raides = 0
    skaiciu_kiekis = 0

    zodziu_skaicius = len(stringas.split())

    for simbolis in stringas:
        if simbolis.isupper():
            didziosios_raides += 1
        elif simbolis.islower():
            mazosios_raides += 1
        elif simbolis.isdigit():
            skaiciu_kiekis += 1
            return zodziu_skaicius, didziosios_raides, mazosios_raides, skaiciu_kiekis

stringas = "sunkiai SEKASI 1 uzduotis su 10 Daliu"
print(stringo_informacija(stringas))

#6 uzduotis


# 7 uzduotis
def skaicius_pirminis(skaicius):
    if skaicius <= 1:
        return False
    if skaicius == 2:
        return True
    if skaicius % 2 == 0:
        return False


    for i in range(3, int(math.sqrt(skaicius)) + 1, 2):
        if skaicius % i == 0:
            return False

    return True

print(skaicius_pirminis(15))
print(skaicius_pirminis(20))
print(skaicius_pirminis(11))
print(skaicius_pirminis(5))

# 8 dalis
def stringo_zodziai_atbulai(stringas):
    zodziai = stringas.split()
    return ' '.join(zodziai[::-1])


stringas = "NAME namas gelda audra"
print(stringo_zodziai_atbulai(stringas))

# 9 dalis
def keliamieji_metai(metai):
    if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
        return True
    else:
        return False
print(keliamieji_metai(1995))
print(keliamieji_metai(2000))
print(keliamieji_metai(2020))

# 10 dalis
from datetime import datetime


def kiek_praeje_metu(data):
    data = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
    dabar = datetime.now()
    skirtumas = dabar - data

    metai = skirtumas.days // 365
    menesiai = (skirtumas.days % 365) // 30
    dienos = skirtumas.days % 30
    valandos = skirtumas.seconds // 3600
    minutes = (skirtumas.seconds % 3600) // 60
    sekundes = skirtumas.seconds % 60
    return f'Praejo: {metai} metai, {menesiai} menesiai, {dienos} dienos, {valandos} valandos, {minutes} minutes, {sekundes} sekundes.'

data = "1957-03-07 15:16:13"
print(kiek_praeje_metu(data))
