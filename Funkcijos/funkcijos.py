
def kvadratu(sk):
    return sk ** 2

kvadratu = lambda x: x ** 2
"""
Lambda neturetu turet pavadinimo. geriau to nerasyti
"""

sarasas = [1,2,3,4,5]

sarasas_kvadratu = []
    for skaicius in sarasas:
        pakelta_kvrdatu = kvadratu(skaicius)
        sarasas_kvadratu.append(sarasas)

sarasas_kvadratu_p = list(map(lambda a: a ** 2, sarasas))
sarasas_kvadratu_2 = [skaicius **2 for skaicius in sarasas]

print(sarasas_kvadratu_2)
"""
map yra funkcija, tik vienas kintamas funkcija, kitas sarasas. lambda taikoma prie map ir apply
12 ir 13 eilute is esmes vienoda
13 yra list comprehension, reik naudooooot
"""