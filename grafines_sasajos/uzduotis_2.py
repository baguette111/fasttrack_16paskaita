from tkinter import *
langas = Tk()

def patvirtinti():
    vardas = vardas_entry.get()
    sveikinimas_label.config(text=f'Labas, {vardas}!')

    
vardas_label = Label(langas, text='Iveskite varda')
vardas_label.pack()

vardas_entry = Entry(langas)
vardas_entry.pack()
    
mygtukas = Button(langas, text='Patvirtinti', command=patvirtinti)
langas.bind('<Return>', lambda event: patvirtinti())
mygtukas.pack()


sveikinimas_label = Label(langas, text='')
sveikinimas_label.pack()

langas.mainloop()