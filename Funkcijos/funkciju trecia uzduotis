"""
Sukurti funkciją, kuri grąžintų True reikšmę, jei įvesto skaičiaus pirma skaitmenų pusė yra lygi antrąjai, priešingu atveju grąžintų False.
Parašyti funkciją, kuri grąžintų, kiekvieno elemento gretimą skaičių. Pvz:
 Input: 5678
 Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79
"""

# pirma dalis
def patikrinti_puses_lyguma(skaicius):
    skaicius_str = str(skaicius)  # Paverčiame skaičių į eilutę
    n = len(skaicius_str)

    # Patikriname, ar skaičius turi lygų skaitmenų kiekį
    if n % 2 != 0:
        return False

    # Padaliname į dvi dalis
    pirmoji_puse = skaicius_str[:n // 2]
    antroji_puse = skaicius_str[n // 2:]

    # Grąžiname True, jei pusės lygios, priešingu atveju False
    return pirmoji_puse == antroji_puse

# Testavimas
print(patikrinti_puses_lyguma(123321))  # False
print(patikrinti_puses_lyguma(112211))  # True
print(patikrinti_puses_lyguma(1234))    # False
print(patikrinti_puses_lyguma(123123))  # True

#antra dalis
def gretimi_skaiciai(skaicius):
    skaicius_str = str(skaicius)
    rezultatas = []


    for i in range(len(skaicius_str) - 1):
        pirmas = skaicius_str[i]
        antras = skaicius_str[i + 1]
        rezultatas.append(f"{pirmas} - {pirmas + antras}")


    rezultatas.append(f"{skaicius_str[-1]} - {int(skaicius_str[-1]) + 1}")

    return ", ".join(rezultatas)

print(gretimi_skaiciai(5678))  # 5 - 46, 6 - 57, 7 - 68, 8 - 79