"""
Parašyti programą, kuri:
Leistų vartotojui įvesti sveiką skaičių.
Atspausdinti True, jei skaičius teigiamas
Atspausdinti False, jei skaičius neigiamas ar lygus 0
True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar_skaicius_teigiamas
Patarimas: naudoti input, boolean, if/else
Pakeisti 1 ir 3 užduotis taip, kad neteisingai įvedus duomenis ar įvykus klaidoms, programos mestų norimas klaidas lietuvių kalba (panaudoti try/except)

"""

try:
    s = input("Įveskite sveiką skaičių: ").replace(',', '')
    s = int(s)

except ValueError:
    print("Ivestas klaidingas skaicius")
    s = None
except Exception as e:
    print(f"Klaida: {e}")

if s is not None:
    if s <= 0:
        print(False)
    else:
        print(True)
