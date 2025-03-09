import tkinter as tk
from frames.frames import Frame_0,Frame_nav,Frame_1,Frame_2,Frame_3
from tela_inicial.tela_inicial import Tela_Inicial 

class App(tk.Tk):
    def __init__(self, titulo: str, tamanho_tela: list):
        
        # main setup
        super().__init__()
        self.title(titulo)
        self.geometry(f'{tamanho_tela[0]}x{tamanho_tela[1]}+{tamanho_tela[2]}+{tamanho_tela[3]}')
        self.minsize(tamanho_tela[0],tamanho_tela[1])
      
        # frames_iniciais
        self.frame_fundo = Frame_0(self)
        self.frame_nav = Frame_nav(self)
        self.frame_titulo = Frame_1(self, titulo)
        self.frame_2 = Frame_2(self)
        self.frame_3 = Frame_3(self)

        # tela inicial
        Tela_Inicial(self.frame_titulo, self.frame_2, self.frame_3)

        # run
        self.mainloop()


titulo = 'Cervejaria MVB'
tamanho_tela = [600,600,10,10]
App(titulo, tamanho_tela)