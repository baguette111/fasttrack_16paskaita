from tkinter import *
import webbrowser


def callback(url):
    webbrowser.open(url)
    
root = Tk()
link1 = Label(root, text="Google", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://www.google.com"))

link2 = Label(root, text="Ecosia", fg="blue", cursor="hand1")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("https://www.ecosia.org"))

root.mainloop()