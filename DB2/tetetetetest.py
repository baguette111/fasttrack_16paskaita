import tkinter as tk
from tkinter import *
from tkinter import ttk
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Sukuriame SQLAlchemy modelį
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = 'darbuotojai'
    
    id = Column(Integer, primary_key=True)
    vardas = Column(String, nullable=False)
    pavarde = Column(String, nullable=False)
    gimimo_data = Column(Date, nullable=False)
    pareigos = Column(String, nullable=False)
    atlyginimas = Column(Integer, nullable=False)
    pradzios_data = Column(Date, default=datetime.date.today)

# Sukuriame duomenų bazės variklį
engine = create_engine('sqlite:///darbuotojai.db', echo=True)

# Sukuriame lenteles, jei jos dar neegzistuoja
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Sukuriame Tkinter GUI langą
root = tk.Tk()
root.title("Darbuotojų Valdymas")
 # Jei turite ikoną, galite nurodyti kelią į ją

def prideti_darbuotoja():
    vardas = entry_vardas.get()
    pavarde = entry_pavarde.get()
    gimimo_data = entry_gimimo_data.get()
    pareigos = entry_pareigos.get()
    atlyginimas = entry_atlyginimas.get()

    if not vardas or not pavarde or not gimimo_data or not pareigos or not atlyginimas:
        messagebox.showerror("Klaida", "Visi laukai turi būti užpildyti!")
        return

    try:
        gimimo_data = datetime.datetime.strptime(gimimo_data, '%Y-%m-%d').date()
    except ValueError:
        messagebox.showerror("Klaida", "Netinkamas gimimo datos formatas. Naudokite YYYY-MM-DD.")
        return

    try:
        atlyginimas = int(atlyginimas)
    except ValueError:
        messagebox.showerror("Klaida", "Atlyginimas turi būti sveikasis skaičius.")
        return

    darbuotojas = Darbuotojas(vardas=vardas, pavarde=pavarde, gimimo_data=gimimo_data,
                             pareigos=pareigos, atlyginimas=atlyginimas)

    session.add(darbuotojas)
    session.commit()
    messagebox.showinfo("Pavyko", "Darbuotojas pridėtas!")
    perziureti_darbuotojus()

def perziureti_darbuotojus():
    for row in treeview.get_children():
        treeview.delete(row)

    darbuotojai = session.query(Darbuotojas).all()

    for darbuotojas in darbuotojai:
        treeview.insert("", "end", values=(darbuotojas.id, darbuotojas.vardas, darbuotojas.pavarde, 
                                          darbuotojas.gimimo_data, darbuotojas.pareigos, darbuotojas.atlyginimas))

def istrinti_darbuotoja():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror("Klaida", "Pasirinkite darbuotoją!")
        return

    darbuotojo_id = treeview.item(selected_item)['values'][0]
    darbuotojas = session.query(Darbuotojas).filter_by(id=darbuotojo_id).first()

    if darbuotojas:
        session.delete(darbuotojas)
        session.commit()
        messagebox.showinfo("Pavyko", "Darbuotojas ištrintas!")
        perziureti_darbuotojus()

def redaguoti_darbuotoja():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showerror("Klaida", "Pasirinkite darbuotoją!")
        return

    darbuotojo_id = treeview.item(selected_item)['values'][0]
    darbuotojas = session.query(Darbuotojas).filter_by(id=darbuotojo_id).first()

    if darbuotojas:
        entry_vardas.delete(0, tk.END)
        entry_vardas.insert(0, darbuotojas.vardas)
        entry_pavarde.delete(0, tk.END)
        entry_pavarde.insert(0, darbuotojas.pavarde)
        entry_gimimo_data.delete(0, tk.END)
        entry_gimimo_data.insert(0, darbuotojas.gimimo_data.strftime('%Y-%m-%d'))
        entry_pareigos.delete(0, tk.END)
        entry_pareigos.insert(0, darbuotojas.pareigos)
        entry_atlyginimas.delete(0, tk.END)
        entry_atlyginimas.insert(0, darbuotojas.atlyginimas)

        def atnaujinti():
            darbuotojas.vardas = entry_vardas.get()
            darbuotojas.pavarde = entry_pavarde.get()
            darbuotojas.gimimo_data = datetime.datetime.strptime(entry_gimimo_data.get(), '%Y-%m-%d').date()
            darbuotojas.pareigos = entry_pareigos.get()
            darbuotojas.atlyginimas = int(entry_atlyginimas.get())

            session.commit()
            messagebox.showinfo("Pavyko", "Darbuotojo duomenys atnaujinti!")
            perziureti_darbuotojus()

        atnaujinti_btn = tk.Button(root, text="Atnaujinti", command=atnaujinti)
        atnaujinti_btn.grid(row=6, column=1)

# GUI komponentai
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Laukai įvesti darbuotojo duomenis
tk.Label(frame, text="Vardas").grid(row=0, column=0)
entry_vardas = tk.Entry(frame)
entry_vardas.grid(row=0, column=1)

tk.Label(frame, text="Pavardė").grid(row=1, column=0)
entry_pavarde = tk.Entry(frame)
entry_pavarde.grid(row=1, column=1)

tk.Label(frame, text="Gimimo data (YYYY-MM-DD)").grid(row=2, column=0)
entry_gimimo_data = tk.Entry(frame)
entry_gimimo_data.grid(row=2, column=1)

tk.Label(frame, text="Pareigos").grid(row=3, column=0)
entry_pareigos = tk.Entry(frame)
entry_pareigos.grid(row=3, column=1)

tk.Label(frame, text="Atlyginimas").grid(row=4, column=0)
entry_atlyginimas = tk.Entry(frame)
entry_atlyginimas.grid(row=4, column=1)

# Mygtukai
prideti_btn = tk.Button(frame, text="Pridėti darbuotoją", command=prideti_darbuotoja)
prideti_btn.grid(row=5, columnspan=2)

# Sąrašas, kuriame rodomi darbuotojai
treeview = ttk.Treeview(root, columns=("ID", "Vardas", "Pavardė", "Gimimo data", "Pareigos", "Atlyginimas"), show="headings")
treeview.pack(padx=10, pady=10)

treeview.heading("ID", text="ID")
treeview.heading("Vardas", text="Vardas")
treeview.heading("Pavardė", text="Pavardė")
treeview.heading("Gimimo data", text="Gimimo data")
treeview.heading("Pareigos", text="Pareigos")
treeview.heading("Atlyginimas", text="Atlyginimas")

# Mygtukai valdyti darbuotojus
istrinti_btn = tk.Button(root, text="Ištrinti darbuotoją", command=istrinti_darbuotoja)
istrinti_btn.pack(padx=10, pady=10)

redaguoti_btn = tk.Button(root, text="Redaguoti darbuotoją", command=redaguoti_darbuotoja)
redaguoti_btn.pack(padx=10, pady=10)

# Inicializuojame darbuotojų sąrašą
perziureti_darbuotojus()

root.mainloop()
