from tkinter import *
from tkinter import ttk

import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

figure = Figure(figsize=(8, 8), dpi=100)
plot = figure.add_subplot(1, 1, 1)
plot.spines['left'].set_position('center')
plot.spines['bottom'].set_position('center')

plot.plot(0.5, 0.3, color="red", marker="o", linestyle="")

x = [0.1, 0.2, 0.3]
y = [-0.1, -0.2, -0.3]
plot.plot(x, y, color="blue", marker="x", linestyle="")

canvas = FigureCanvasTkAgg(figure, plotframe)
canvas.get_tk_widget().grid(row=0, column=0)

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
