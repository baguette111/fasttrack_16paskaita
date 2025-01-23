from darbuotojas import Darbuotojas
from darbuotojas import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///darbuotojai.db')

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("""Pasirikite veiksmą:
    1 - pridėti darbuotoją
    2 - pamatyti darbuotojų sąrašą
    3 - pašalinti darbuotoją
    4 - pakeisti darbuotojo informaciją
    """))
    
    if pasirinkimas == 1:
        name = input("Įveskite darbuotojo vardą: ")
        surname = input("Įveskite darbuotojo pavardę: ")
        position = input("Įveskite darbuotojo pareigas: ")
        salary = float(input("Įveskite darbuotojo atlyginimą: "))
        darbuotojas = Darbuotojas(name,surname, position, salary)
        session.add(darbuotojas)
        session.commit()
    
    if pasirinkimas == 2:
        darbuotojai = session.query(Darbuotojas).all()
        print("---------------------------")
        for darbuotojas in darbuotojai:
            print(darbuotojas)
        print("---------------------------")
    
    
    if pasirinkimas == 3:
        darbuotojai = session.query(Darbuotojas).all()
        print("---------------------------")
        for darbuotojas in darbuotojai:
            print(darbuotojas)
        print("---------------------------")
        trinamo_id = int(input("Pasirinkite norimo ištrinti darbuotojo ID: "))
        trinamas_darbuotojas = session.query(Darbuotojas).filter_by(id=trinamo_id).one()
        session.delete(trinamas_darbuotojas)
        session.commit()
    
    
    if pasirinkimas == 4:
        darbuotojai = session.query(Darbuotojas).all()
        print("---------------------------")
        for darbuotojas in darbuotojai:
            print(darbuotojas)
        print("---------------------------")
        keiciamo_id = int(input("Pasirinkite norimo pakeisti darbuotojo ID: "))
        keiciamas_darbuotojas = session.query(Darbuotojas).get(keiciamo_id)
        pakeitimas = int(input("""Ką norite pakeisti:
        1 - vardą
        2 - pavardę
        3 - pareigas
        4 - atlyginimą
                               """))
        if pakeitimas == 1:
            keiciamas_darbuotojas.name = input("Įveskite naują darbuotojo vardą: ")
        if pakeitimas == 2:
            keiciamas_darbuotojas.surname = input("Įveskite naują darbuotojo pavardę: ")
        if pakeitimas == 3:
            keiciamas_darbuotojas.surname = input("Įveskite naujas darbuotojo pareigas: ")
        if pakeitimas == 4:
            keiciamas_darbuotojas.surname = float(input("Įveskite naują darbuotojo atlyginimą: "))
        session.commit()