from tkinter import *
langas = Tk()

langas.geometry('200x50')

def patvirtinti():
    vardas = vardas_entry.get()
    sveikinimas_label.config(text=f'Labas, {vardas}!')

    
vardas_label = Label(langas, text='Iveskite varda')
vardas_label.grid(row=0, column=0)

vardas_entry = Entry(langas)
vardas_entry.grid(row=0, column=1)
    
mygtukas = Button(langas, text='Patvirtinti', command=patvirtinti)
langas.bind('<Return>', lambda event: patvirtinti())
mygtukas.grid(row=0, columnspan=3, sticky=E)

sveikinimas_label = Label(langas, text='')
sveikinimas_label.grid(row=2, columnspan=2)


langas.mainloop()