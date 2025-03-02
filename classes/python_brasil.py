from tkinter import *

class Janela():
    def __init__(self):
        self.root = Tk()

        self.root.title('Classes no tkinter')

        self.titulo = Label(self.root, text="Olá Mundo!", font="Verdana 30", bg=self.root.cget('bg'))
        self.titulo.pack(pady=100, padx=100)

        self.root.mainloop()

class Quadros(Janela):
    pass        

Quadros()
