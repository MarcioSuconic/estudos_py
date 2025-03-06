import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):
        
        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}+{size[2]}+{size[3]}')
        self.minsize(size[0], size[1])

        # widgets
        self.frame_1 = Frame_1(self)
        self.frame_2 = Frame_2(self)
        self.frame_3 = Frame_3(self)

        # run
        self.mainloop()

class Frame_1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        cor_fundo_frame_1 = "#6e44ff"
        ttk.Label(self, background=cor_fundo_frame_1).pack(expand=True, fill= 'both')
        self.place(relx=0, rely=0.00, relheight=0.06, relwidth=1)

class Frame_2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        cor_fundo_frame_2 = "#ea526f"
        ttk.Label(self, background=cor_fundo_frame_2).pack(expand=True, fill= 'both')
        self.place(relx=0, rely=0.06, relheight=0.94, relwidth=0.55)

class Frame_3(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        cor_fundo_frame_3 = "#d2f1e4"
        ttk.Label(self, background=cor_fundo_frame_3).pack(expand=True, fill= 'both')
        self.place(relx=0.55, rely=0.06, relheight=0.94, relwidth=0.45)


App('Cervejaria MVB',[1043,600,10,10])
