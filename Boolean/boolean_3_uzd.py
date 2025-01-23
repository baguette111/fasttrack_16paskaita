"""
Parašyti programą, kuri:
Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
Metų
Mėnesių
Dienų
Valandų
Minučių
Sekundžių
Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
Patarimas: naudoti datetime, .days, .total_seconds()
Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):
skaicius = 4.66
print(round(skaicius))
"""
import datetime
from datetime import timedelta

now = datetime.datetime.now()

while True:
    try:
        ivesta_data = input("Iveskite savo gimtadieni (YYYY mm dd): ")
        data = datetime.datetime.strptime(ivesta_data, "%Y %m %d")

        break
    except ValueError:
        print("ivestas klaidingas datos formatas. Pabandykite is naujo.")
        data = None
    except TypeError:
        print("ivestas klaidingas datos formatas. Pabandykite is naujo.")
        data = None

if data:
    skirtumas = now - data

    metai = round(skirtumas.days // 365, 1)
    menesiai = round(skirtumas.days // 30.415, 1)
    dienos = skirtumas.days
    valandos = round(skirtumas.total_seconds() // 3600, 1)
    minutes = round(skirtumas.total_seconds() // 60, 1)
    sekundes = round(skirtumas.total_seconds(), 1)

    print(ivesta_data)
    print(f"Praejo metu: ", metai)
    print(f"Praejo menesiu: ", menesiai)
    print(f"Praejo dienu: ", dienos)
    print(f"Praejo valandu: ", valandos)
    print(f"Praejo minuciu: ", minutes)
    print(f"Praejo sekundziu: ", sekundes)
