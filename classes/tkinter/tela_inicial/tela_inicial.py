from tkinter import ttk
import tkinter as tk

class Tela_Inicial:
    def __init__(self, frame_titulo, frame_2, frame_3):
        self.frame_titulo = frame_titulo
        self.frame_2 = frame_2
        self.frame_3 = frame_3

        btn = tk.Button(self.frame_2, text="Botão 1", background="yellow", foreground="black")
        btn.place(relx=0.10,rely=0.10,relheight=0.10, relwidth=0.25)

        

