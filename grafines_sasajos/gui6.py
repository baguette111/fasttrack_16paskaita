from tkinter import *

langas = Tk()

def daryti():
    status['text'] = 'Dabar daro'
    
mygtukas = Button(langas, text='Daryti', command=daryti)
status = Label(langas, text='Nieko nedaro...', bd=1, relief=SUNKEN, anchor=W)
#status.pack(side=BOTTOM, fill=X)

status.grid(row=2, columnspan=3, sticky=W+E)
mygtukas.grid(row=1, column=1)

#mygtukas.pack()

langas.mainloop()
