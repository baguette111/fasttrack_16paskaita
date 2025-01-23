from tkinter import *

langas = Tk()

def spausdinti(event):
    print('Paspaustas kairts peles mygtukas')
    
def spausdinti2(event):
    print('Paspaustas desinys peles mygtukas')
    
def spausdinti3(event):
    print('Paspaustas ENTER')
    
mygtukas = Button(langas, text='Spausdinti')
mygtukas.bind('<Button-1>', spausdinti)
mygtukas.bind('<Button-3>', spausdinti2)
langas.bind('<Return>', spausdinti3)
mygtukas.pack()

langas.mainloop()