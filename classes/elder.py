from tkinter import *

root = Tk()

class Elder:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text="Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Look at you... you clicked a button!!!")

Elder(root)

root.mainloop()