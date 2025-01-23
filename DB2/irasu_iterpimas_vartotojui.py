from projektas import engine, Projektas
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("""Pasirikite veiksmą:
    1 - atvaizduoti projektus
    2 - sukurti projektą
    3 - pakeisti projektą
    4 - ištrinti projektą
    """))
    
    if pasirinkimas == 1:
        projektai = session.query(Projektas).all()
        print("++++++++++++++++++++++++++")
        for projektas in projektai:
            print(projektas)
        print("**************************")
    
    if pasirinkimas == 2:
        name = input("Įveskite projekto pavadinimą: ")
        price = float(input("Įveskite projekto kainą: "))
        projektas = Projektas(name,price)
        session.add(projektas)
        session.commit()
        
    if pasirinkimas == 3:
        projektai = session.query(Projektas).all()
        print("++++++++++++++++++++++++++")
        for projektas in projektai:
            print(projektas)
        print("**************************")
        keiciamo_id = int(input("Pasirinkite norimo pakeisti projekto ID: "))
        keiciamas_projektas = session.query(Projektas).get(keiciamo_id)
        pakeitimas = int(input("""Ką norite pakeisti: 1 - pavadinimą, 2 - kainą
                               """))
        if pakeitimas == 1:
            keiciamas_projektas.name = input("Įveskite naują projekto pavadinimą: ")
        if pakeitimas == 2:
            keiciamas_projektas.price = float(input("Įveskite naują projekto kainą: "))
        session.commit()
        
    if pasirinkimas == 4:
        projektai = session.query(Projektas).all()
        print("++++++++++++++++++++++++++")
        for projektas in projektai:
            print(projektas)
        print("**************************")
        trinamo_id = int(input("Pasirinkite norimo ištrinti projekto ID: "))
        trinamas_projektas = session.query(Projektas).get(trinamo_id)
        session.delete(trinamas_projektas)
        session.commit()