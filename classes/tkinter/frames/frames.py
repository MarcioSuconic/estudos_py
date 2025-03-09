from tkinter import ttk

class Frame_0(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)        
        ttk.Label(self, background='lightblue').pack(expand=True, fill='both')
        self.place(relx=0.0,rely=0.0,relwidth=1,relheight=1)


class Frame_1(ttk.Frame):
    def __init__(self, parent, titulo):
        super().__init__(parent)        
        ttk.Label(self, background='gold', text=titulo, foreground='black', justify='center', anchor='center').pack(expand=True, fill='both')
        self.place(relx=0.10,rely=0.05,relwidth=0.80,relheight=0.075)


class Frame_nav(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)        
        ttk.Label(self, background='black').pack(expand=True, fill='both')
        self.place(relx=0.10,rely=0.125,relwidth=0.80,relheight=0.075)


class Frame_2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)        
        ttk.Label(self, background='blue').pack(expand=True, fill='both')
        self.place(relx=0.10,rely=0.20,relwidth=0.40,relheight=0.70)


class Frame_3(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)        
        ttk.Label(self, background='white').pack(expand=True, fill='both')
        self.place(relx=0.50,rely=0.20,relwidth=0.40,relheight=0.70)
