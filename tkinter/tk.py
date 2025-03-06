from tkinter import *

class Janela:
    def __init__(self):
        self.root = Tk()
        self.root.title('Estudos classes com tkinter')
        self.frame_1 = Frame(self.root, bg="black")
        self.frame_1.place(relx=0.10, rely=0.10, relwidth=0.80, relheight=0.20)
        self.frame_2 = Frame(self.root, bg="red")
        self.frame_2.place(relx=0.10, rely=0.20, relwidth=0.40, relheight=0.60)
        self.frame_3 = Frame(self.root, bg="yellow")
        self.frame_3.place(relx=0.50, rely=0.20, relwidth=0.40, relheight=0.60)
        self.root.mainloop()

class Quadros(Janela):
    def __init__(self):
        super().__init__()

    print('quadros')
    label = Label(self.frame_1)

Janela()