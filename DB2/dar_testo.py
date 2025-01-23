from darbuotojas import Darbuotojas
from darbuotojas import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from tkinter import *

# Sukuriame pagrindinį langą
langas = Tk()

# Sukuriame ryšį su duomenų baze
engine = create_engine('sqlite:///darbuotojai.db')
Session = sessionmaker(bind=engine)
session = Session()

# Funkcija, kuri pridės darbuotoją
def prideti_darbuotoja():
    name = entry_name.get()
    surname = entry_surname.get()
    position = entry_position.get()
    try:
        salary = float(entry_salary.get())
        if salary <= 0:
            raise ValueError("Atlyginimas turi būti teigiamas")
    except ValueError as ve:
        print(f"Įvedėte neteisingą atlyginimo vertę: {ve}")
        return

    darbuotojas = Darbuotojas(name=name, surname=surname, position=position, salary=salary)
    session.add(darbuotojas)
    session.commit()
    print(f"Darbuotojas {name} {surname} pridėtas!")

# Sukuriame įvesties laukus ir mygtukus
pasirinkimas = Label(langas, text="Pasirinkite veiksmą:")
pasirinkimas.pack()

button1 = Button(langas, text="Pridėti darbuotoją", command=prideti_darbuotoja)
button1.pack(side=TOP, fill=X)

# Etiketės ir įvesties laukai
label_name = Label(langas, text="Vardas:")
label_name.pack()

entry_name = Entry(langas)
entry_name.pack()

label_surname = Label(langas, text="Pavardė:")
label_surname.pack()

entry_surname = Entry(langas)
entry_surname.pack()

label_position = Label(langas, text="Pareigos:")
label_position.pack()

entry_position = Entry(langas)
entry_position.pack()

label_salary = Label(langas, text="Atlyginimas:")
label_salary.pack()

entry_salary = Entry(langas)
entry_salary.pack()

# Paleidžiam GUI langą
langas.mainloop()
