import tkinter as tk

root = tk.Tk()
root.title('Listbox com Scrollbar')
frame = tk.Frame(root)
frame.pack(padx=10,pady=10)

listbox= tk.Listbox(frame, width=40, height=2)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)

for n in range(1,25):
    listbox.insert(n,f'item_{n}')

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

listbox.selection_set(10)

root.mainloop()


