from tkinter import *

langas = Tk()   

def spausdinti():
    print('Spausdinam...')
    
mygtukas = Button(langas, text='Spausdinti', command=spausdinti)
mygtukas.pack()
langas.mainloop()