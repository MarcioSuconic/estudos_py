from tkinter import *



class frames_principais:
    def __init__ (self):
        self.janela = Tk()
        self.frame_1 = Frame(self.janela, bg="black")
        self.frame_1.place(relx=0.10,rely=0.10,relheight=0.20,relwidth=0.80)
        self.frame_2 = Frame(self.janela, bg="red")
        self.frame_2.place(relx=0.10,rely=0.30,relheight=0.60,relwidth=0.40)
        self.frame_3 = Frame(self.janela, bg="black")
        self.frame_3.place(relx=0.50,rely=0.30,relheight=0.60,relwidth=0.40)
        tela_inicial()
        self.janela.mainloop()
        

class tela_inicial(frames_principais):
    def __init__(self):
        super().__init__()

        # self.entry_ini = Entry(self.frame_1, bg="yellow")
        # self.entry_ini.place(relx=0.10,rely=0.10,relheight=0.50,relwidth=0.80)       
        
        self.frame_1.configure(bg="green")

tela_inicial()



