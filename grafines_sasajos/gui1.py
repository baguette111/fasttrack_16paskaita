from tkinter import *

langas = Tk()

virsutinis = Frame(langas)
apatinis = Frame(langas)

mygtukas1 = Button(virsutinis, text='Mygtukas 1')
mygtukas2 = Button(virsutinis, text='Mygtukas 2')
mygtukas3 = Button(virsutinis, text='Mygtukas 3')
mygtukas4 = Button(apatinis, text='Mygtukas 4')

virsutinis.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=BOTTOM, fill=Y)




langas.mainloop()