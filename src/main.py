from tkinter import *
from tkinter import ttk

root = Tk()

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
plotframe = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=800, height=700)
w1_lbl = ttk.Label(mainframe, text="Primer peso")
w1 = ttk.Entry(mainframe, width=6)
w2_lbl = ttk.Label(mainframe, text="Segundo peso")
w2 = ttk.Entry(mainframe, width=6)
bias_lbl = ttk.Label(mainframe, text="Bias")
bias = ttk.Entry(mainframe, width=6)

submit = ttk.Button(mainframe, text="Clasificar")

mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
w1_lbl.grid(column=0, row=0, sticky=E)
w1.grid(column=1, row=0, sticky=W)
w2_lbl.grid(column=2, row=0, sticky=E)
w2.grid(column=3, row=0, sticky=W)
bias_lbl.grid(column=4, row=0, sticky=E)
bias.grid(column=5, row=0, sticky=W)
submit.grid(column=6, row=0, sticky=(E, W))
plotframe.grid(column=0, row=1, columnspan=7, sticky=(N, S, E, W))

for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
