from darbuotojas import Darbuotojas
from darbuotojas import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from tkinter import *

langas = Tk()


engine = create_engine('sqlite:///darbuotojai.db')

Session = sessionmaker(bind=engine)
session = Session()

pasirinkimas = Label(langas, text="Pasirikite veiksmą:")
button1 = Button(langas, text="pridėti darbuotoją")
button2 = Button(langas, text="pamatyti darbuotojų sąrašą")
button3 = Button(langas, text="pašalinti darbuotoją")
button4 = Button(langas, text="pakeisti darbuotojo informaciją")
button1.pack(side=BOTTOM, fill=X)
button2.pack(side=BOTTOM, fill=X)
button3.pack(side=BOTTOM, fill=X)
button4.pack(side=BOTTOM, fill=X)




name = Entry("Įveskite darbuotojo vardą: ")
surname = Entry("Įveskite darbuotojo pavardę: ")
position = Entry("Įveskite darbuotojo pareigas: ")
salary = float(Entry("Įveskite darbuotojo atlyginimą: "))
darbuotojas = Darbuotojas(name,surname, position, salary)
session.add(darbuotojas)
session.commit()
    
  
    
langas.mainloop()
