# coding=utf-8

from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np
import time

from classifier import Perceptron


class Gui:
    def __init__(self, root):
        root.title("Práctica Perceptrón")
        self.coord = []
        self.coord_class = []
        self.weights = np.random.rand(1, 3)
        
        self.w1 = StringVar()
        self.w2 = StringVar()
        self.bias = StringVar()
        self.epoch = StringVar()
        self.lr = StringVar()
        
        # create plot
        self.fig = Figure(figsize=(8, 8), dpi=100)
        self.ax = self.fig.add_subplot()
        self._config_plot()

        self._create_widgets()
        
    def start(self):
        X = np.asarray(self.coord)
        d = np.asarray(self.coord_class)
        w_1, w_2, bias, epoch, lr = self._retrieve_values()
        W = np.asarray([bias, w_1, w_2])

        for _ in range(epoch):
            p = Perceptron(W, d, lr)
            p.train(X)
            Y = p.activation(X)
            W = p.W

            self.ax.cla()       # clean the points on canvas
            self._config_plot() # set plot configs

            self._set_fields(W)

            # draw the points
            self._draw_classified_points(Y, X)

            # draw line
            self._draw_line(W[1:], W[0])

            self.fig.canvas.draw()
            time.sleep(1)


    def _draw_classified_points(self, Y, X):
        for i in range(Y.shape[0]):
            if Y[i] == 1:
                self.ax.plot(X[i][0], X[i][1], 'ro')
            elif Y[i] == -1:
                self.ax.plot(X[i][0], X[i][1], 'go')

    def _retrieve_values(self):
        w_1 = 0
        w_2 = 0
        bias = 0
        epoch = 0
        lr = 0
        
        try:
            w_1   = float(self.w1.get())
            w_2   = float(self.w2.get())
            bias  = float(self.bias.get())
            epoch = int(self.epoch.get())
            lr    = float(self.lr.get())
        except:
            pass

        return w_1, w_2, bias, epoch, lr

    def _draw_line(self, W, bias):
        for i in np.linspace(-1, 1):
            m = -(W[0] / W[1])
            b = (bias / W[1])

            y = (m * i) + b

            self.ax.plot(i, y, 'bo')

    def _set_fields(self, W):
        print(W)
        self.w1.set(W[1].item())
        self.w2.set(W[2].item())
        self.bias.set(W[0].item())
    
    def onclick(self, event):
        RIGHT_BUTTON = 3
        LEFT_BUTTON  = 1
        try:
            x = event.xdata
            y = event.ydata

            if x is not None and y is not None:
                if event.button == LEFT_BUTTON:
                    self.ax.plot(x, y, 'go')
                    self.coord_class.append(-1)
                elif event.button == RIGHT_BUTTON:
                    self.ax.plot(x, y, 'ro')
                    self.coord_class.append(1)

                self.coord.append([x, y])
        except:
            pass
        
        self.fig.canvas.draw()
    
    def _config_plot(self):
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_xticks([-1, 0, 1])
        self.ax.set_yticks([-1, 1])

    def _create_widgets(self):
        # set application mainframe
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
        
        # set plot frame
        plotframe = ttk.Frame(mainframe, borderwidth=5,
                              relief="ridge", width=900, height=900)
        plotframe.grid(column=0, row=1, columnspan=7, rowspan=7,sticky=(N, S, E, W))
        
        # set entry for first weight
        ttk.Label(mainframe, text="Primer peso").grid(column=9,
                                                      row=1, sticky=E)
        w1_entry = ttk.Entry(mainframe, width=20, textvariable=self.w1,
                                state="disabled")
        w1_entry.grid(column=10, row=1, sticky=W)
        self.w1.set(self.weights[:, 1].item())

        # set entry for second weight
        ttk.Label(mainframe, text="Segundo peso").grid(column=9,
                                                       row=2, sticky=E)
        w2_entry = ttk.Entry(mainframe, width=20, textvariable=self.w2,
                                state="disabled")
        w2_entry.grid(column=10, row=2, sticky=W)
        self.w2.set(self.weights[:, 2].item())
        
        # set entry for bias
        ttk.Label(mainframe, text="Bias").grid(column=9, row=3, sticky=E)
        bias_entry = ttk.Entry(mainframe, width=20, textvariable=self.bias,
                                state="disabled")
        bias_entry.grid(column=10, row=3, sticky=W)
        self.bias.set(self.weights[:, 0].item())

        # set entry for epoch
        ttk.Label(mainframe, text="Épocas").grid(column=9, row=4, sticky=E)
        bias_entry = ttk.Entry(mainframe, width=6, textvariable=self.epoch)
        bias_entry.grid(column=10, row=4, sticky=W)

        # set entry for learning rate (lr)
        ttk.Label(mainframe, text="Learning Rate").grid(column=9, row=5, sticky=E)
        bias_entry = ttk.Entry(mainframe, width=6, textvariable=self.lr)
        bias_entry.grid(column=10, row=5, sticky=W)

        # set start button
        ttk.Button(mainframe, text="Clasificar", command=self.start).grid(
            column=10, row=6, sticky=(E, W))

        canvas = FigureCanvasTkAgg(self.fig, master=plotframe)
        canvas.draw()

        canvas.mpl_connect("button_press_event", self.onclick)
        canvas.get_tk_widget().grid(row=0, column=0)


root = Tk()
Gui(root)
root.mainloop()
