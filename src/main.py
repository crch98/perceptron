# coding=utf-8

from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

from classifier import Perceptron


class Gui:
    def __init__(self, root):
        root.title("Práctica Perceptrón")
        self.coord = []
        
        # set application mainframe
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
        
        # set plot frame
        plotframe = ttk.Frame(mainframe, borderwidth=5,
                              relief="ridge", width=900, height=900)
        plotframe.grid(column=0, row=1, columnspan=7, sticky=(N, S, E, W))
        
        # set entry for first weight
        self.w1 = StringVar()
        ttk.Label(mainframe, text="Primer peso").grid(column=0,
                                                      row=0, sticky=E)
        w1_entry = ttk.Entry(mainframe, width=6, textvariable=self.w1)
        w1_entry.grid(column=1, row=0, sticky=W)
        
        # set entry for second weight
        self.w2 = StringVar()
        ttk.Label(mainframe, text="Segundo peso").grid(column=2,
                                                       row=0, sticky=E)
        w2_entry = ttk.Entry(mainframe, width=6, textvariable=self.w2)
        w2_entry.grid(column=3, row=0, sticky=W)
        
        # set entry for bias
        self.bias = StringVar()
        ttk.Label(mainframe, text="Bias").grid(column=4, row=0, sticky=E)
        bias_entry = ttk.Entry(mainframe, width=6, textvariable=self.bias)
        bias_entry.grid(column=5, row=0, sticky=W)
        
        # set start button
        ttk.Button(mainframe, text="Clasificar", command=self.start).grid(
            column=6, row=0, sticky=(E, W))
        
        # create plot
        self.fig = Figure(figsize=(8, 8), dpi=100)
        self.ax = self.fig.add_subplot()
        self._config_plot()
        
        canvas = FigureCanvasTkAgg(self.fig, master=plotframe)
        canvas.draw()

        canvas.mpl_connect("button_press_event", self.onclick)
        canvas.get_tk_widget().grid(row=0, column=0)

    def _config_plot(self):
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_xticks([-1, 0, 1])
        self.ax.set_yticks([-1, 1])
        
    def start(self):
        w_1 = 0
        w_2 = 0
        bias = 0
        
        try:
            w_1 = float(self.w1.get())
            w_2 = float(self.w2.get())
            bias = float(self.bias.get())
        except:
            pass            
    
        X = np.asarray(self.coord)
        W = [w_1, w_2]
        p = Perceptron(X, W, bias)
        Y = p.activation()
        type_a = np.empty([0, 2])
        type_b = np.empty([0, 2])
    
        self.ax.cla()
        self._config_plot()

        for i in range(Y.shape[0]):
            if Y[i] == 1:
                #type_a = np.append(type_a, [X[i]], axis=0)
                a = X[i]
                self.ax.plot(a[0], a[1], 'ro')
            elif Y[i] == 0:
                #type_b = np.append(type_b, [X[i]], axis=0)
                a = X[i]
                self.ax.plot(a[0], a[1], 'go')

        # draw line
        self._draw_line(W, bias)

        #self.ax.plot(type_a, 'ro')
        #self.ax.plot(type_b, 'bo')
        self.fig.canvas.draw()

    def _draw_line(self, W, bias):
        for i in np.linspace(-1, 1):
            m = -(W[0] / W[1])
            b = (bias / W[1])

            y = (m * i) + b

            self.ax.plot(i, y, 'bo')
    
    def onclick(self, event):
        try:
            x = event.xdata
            y = event.ydata

            if x is not None and y is not None:
                self.coord.append([x, y])
                self.ax.plot(x, y, 'ko')
        except:
            pass
        
        self.fig.canvas.draw()
        
        
root = Tk()
Gui(root)
root.mainloop()