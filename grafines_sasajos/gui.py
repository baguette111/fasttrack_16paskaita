from tkinter import *
langas = Tk()

def spausdinti():
    ivesta = laukas1.get()
    rezultatas['text'] = ivesta
    
uzrasas1 = Label(langas, text='Irasykite zodi')    
laukas1 = Entry(langas)
mygtukas = Button(langas, text='Spausdinti', command=spausdinti)
rezultatas = Label(langas, text='')

uzrasas1.grid(row=0, column=0)
laukas1.grid(row=0, column=1)
mygtukas.grid(row=1, columnspan=2)
rezultatas.grid(row=2, columnspan=2)
langas.mainloop()


