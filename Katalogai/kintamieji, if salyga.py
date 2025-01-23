"""
Parašyti programą, kuri:
Leistų įvesti skaičius a ir b (int arba float)
Išvestų į ekraną „a mažesnis už b“, jei taip yra
Išvestų į ekraną „a lygu b“, jei taip yra
Išvestų į ekraną „a didesnis už b“, jei taip yra
Patarimas: naudoti if, elif, else sąlygas
"""
a = int(input("iveskite sveika skaiciu:"))
b = float(input("iveskite skaiciu:"))
if a < b:
    print("pirmas skaicius mazesnis uz antraji skaiciu")
elif a == b:
    print("abu skaiciai lygus")
else:
    print("antras skaicius didesnis uz pirmaji")

"""
Parašyti programą, kuri su eilute "Zen of Python" darytų šiuos veiksmus:
Atspausdintų paskutinį antro žodžio simbolį
Atspausdintų pirmą trečio žodžio simbolį
Atspausdintų tik pirmą žodį
Atspausdintų tik paskutinį žodį
Atspausdintų visą frazę atbulai
Atskirtų žodžius ir juos atspausdintų
Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį
Patarimas: naudoti string karpymo įrankius, funkcijas split(), replace()
The Zen of Python:
"""
sakinys = str("Zen of Python")
print(sakinys [5])
print(sakinys[7])
print(sakinys[0 : 3])
print(sakinys[7 : 13])
print(sakinys[:: -1])
print(sakinys.split())
print(sakinys.replace('Python', 'Programming'))
print(sakinys)
print(sakinys.upper())
print(sakinys.lower())
print(sakinys.title())
print(sakinys.casefold())
print(sakinys.count('o'))
print(sakinys.count('z'))
print(sakinys.find('o')) #kodel rado 4?


"""
Programoje išbandyti daugiau string funkcijų:
upper()
casefold()
capitalize()
count()
find()
ir t.t.
Visas jas galite rasti čia: https://www.w3schools.com/python/python_ref_string.asp

"""


"""
Parašyti programą, kuri:
Leistų įvesti pirmą skaičių
Leistų įvesti antrą skaičių
Paklaustų, kokį matematinį veiksmą reiktų atliktų
Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.
Patarimas: naudoti input(), if, print
"""

a = int(input("iveskite pirma skaiciu:"))
b = int(input("iveskite antra skaiciu:"))
veiksmas = str(input("iveskite, koki matematini veiksma norite atlikti(daugyba, sudetis, dalyba, atimtis):"))
if veiksmas == 'daugyba':
    daugyba = (a * b)
    print(daugyba)
if veiksmas == 'dalyba':
    dalyba = (a / b)
    print(dalyba)
if veiksmas == 'sudetis':
    sudetis = (a + b)
    print(sudetis)
if veiksmas == 'atimtis':
    atimtis = (a - b)
    print(atimtis)



