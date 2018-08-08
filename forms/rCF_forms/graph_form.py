from PyQt4 import QtGui
import re
import numpy as np

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as GOCCanvas
from matplotlib.figure import Figure

#----------------Холст--------------#
class Graph_Canvas(GOCCanvas):
    def __init__(self, parent=None):
        GBox = Figure()
        self.axes = GBox.add_subplot(111)
        GOCCanvas.__init__(self, GBox)
		
#------------Класс с функциями получения данных для графика------------#		
class Graphs_Data(Graph_Canvas):
    def getting_initial_data(self, f_d):
        global data, reg_prs
        orf = open(f_d + "/out_run.log", "r")
        data = orf.read()
        orf.close()
        reg_prs = re.compile(r"(?<=[ ])\S*(?=[,])")
		
    def t_making(self):
        global t
        t_reg = re.compile(r"Time\s=\s\S*\n")
        t_mas = t_reg.findall(data)
        fr_t_mas = []

        fr_t = np.array([])
        for g in range(len(t_mas)):
            t_div = t_mas[g].split(" ")
            fr_t_mas.append(t_div[2])
        t = np.append(fr_t, fr_t_mas)
    
    def Ux_making(self):
        global Ux
        Ux_reg = re.compile(r"\srhoUx,\sInitial\sresidual\s=\s\S*,\sFinal\sresidual\s=\s\S*")
        Ux_mas = Ux_reg.findall(data)
        fr_Ux_mas = []
        fr_Ux = np.array([])
        for g in range(len(Ux_mas)):
            Ux_prs_mas = reg_prs.findall(Ux_mas[g])
            fr_Ux_mas.append(Ux_prs_mas[2]) 
        Ux = np.append(fr_Ux, fr_Ux_mas)

    def Uy_making(self):
        global Uy
        Uy_reg = re.compile(r"\srhoUy,\sInitial\sresidual\s=\s\S*,\sFinal\sresidual\s=\s\S*")
        Uy_mas = Uy_reg.findall(data)
        fr_Uy_mas = []
        fr_Uy = np.array([])
        for g in range(len(Uy_mas)):
            Uy_prs_mas = reg_prs.findall(Uy_mas[g])
            fr_Uy_mas.append(Uy_prs_mas[2])
        Uy = np.append(fr_Uy, fr_Uy_mas)

    def E_making(self):
        global E
        E_reg = re.compile(r"\srhoE,\sInitial\sresidual\s=\s\S*,\sFinal\sresidual\s=\s\S*")
        E_mas = E_reg.findall(data)
        fr_E_mas = []
        fr_E = np.array([])
        for g in range(len(E_mas)):
            E_prs_mas = reg_prs.findall(E_mas[g])
            fr_E_mas.append(E_prs_mas[2])
        E = np.append(fr_E, fr_E_mas)

    def graphs_making(self):
        self.axes.plot(t, Ux)
        self.axes.plot(t, Uy)
        self.axes.plot(t, E)
        self.axes.grid(True)
        self.axes.set_xlabel("Time")
        self.axes.set_ylabel("Koeff")
        self.legend_lbls = ['rhoUx', 'rhoUy', 'rhoE']
        self.axes.legend(self.legend_lbls)

#----------------Класс, в котором создается экземпляр класса-графика--------------#
class graph_form_class(QtGui.QWidget):
    def __init__(self, f_d, parent=None):
        QtGui.QWidget.__init__(self, parent)

        GD = Graphs_Data()
        GD.getting_initial_data(f_d)
        GD.t_making()
        GD.Ux_making()
        GD.Uy_making()
        GD.E_making()
        GD.graphs_making()

        GW_hbox = QtGui.QHBoxLayout()
        GW_hbox.addWidget(GD)
        GW_form = QtGui.QFormLayout()
        GW_form.addRow(GW_hbox)
        self.setLayout(GW_form)