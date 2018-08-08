# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------

from PyQt4 import QtCore, QtGui
import sys
import os
import subprocess
import time
import re
import sys
import os
import subprocess
import re
import time
import getpass
import shutil
import numpy as np
import threading
import matplotlib.pyplot as plt
import time
import pylab
import re
from pylab import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import animation
from subprocess import PIPE

# ----------------Дочерний поток для запуска процесса решения--------------------

class run_Thread(QtCore.QThread):
    def __init__(self, full_dir, parent, interface_lng_val):
        QtCore.QThread.__init__(self, parent)
        global f_d
        global int_lng
        global par
        f_d = full_dir
        int_lng = interface_lng_val
        par = parent
    def run(self):
        f = open(f_d + '/SOLVER_BASH', 'w')
        f.write('#!/bin/sh' + '\n' + '. /opt/openfoam4/etc/bashrc' + '\n' + par.new_app + '\n' + 'exit')
        f.close()
		
        if os.path.exists(f_d + "/out_run.log"):
            os.remove(f_d + "/out_run.log")
        self.emit(QtCore.SIGNAL("started(PyQt_PyObject, QString, QString)"), par, int_lng, f_d)
        
        file = open(f_d + "/out_run.log", "w")
        proc = subprocess.Popen(["bash " + f_d + "/SOLVER_BASH"], cwd = f_d, shell = True, stdout=file, stderr=file)

        while proc.poll() is None:	
            time.sleep(0.5)

        return_code = proc.returncode
			
        self.emit(QtCore.SIGNAL("finished(int, PyQt_PyObject, QString, QString)"), return_code, par, f_d, int_lng)
            

# ----------------Дочерний поток для останова процесса решения--------------------

class stop_Thread(QtCore.QThread):
    def __init__(self, full_dir, parent, interface_lng_val):
        QtCore.QThread.__init__(self, parent)
        global f_d
        global int_lng
        global par
        f_d = full_dir
        int_lng = interface_lng_val
        par = parent
    def run(self):
        import signal
		
        vspom = open(f_d+'/KILL_PROC_BASH', 'w')
        vspom.write('#!/bin/sh' + '\n' + '. /opt/openfoam4/etc/bashrc' + '\n' + 'pidof ' + par.new_app + '\n' + 'exit')
        vspom.close()

        vspom_file = open(f_d+"/out_kill.log", "w")
        vspom_proc = subprocess.Popen(["bash "+f_d+"/KILL_PROC_BASH"], cwd = f_d, shell = True, stdout=vspom_file, stderr=vspom_file)
        while vspom_proc.poll() is None:
            time.sleep(0.5)
			
        return_code = vspom_proc.returncode	
			
        self.emit(QtCore.SIGNAL("finished(int, PyQt_PyObject, QString, QString)"), return_code, par, f_d, int_lng)	

# ----------------Дочерний поток для запуска визуализации--------------------

class view_Thread(QtCore.QThread):
    def __init__(self, full_dir, parent, interface_lng_val):
        QtCore.QThread.__init__(self, parent)
        global f_d
        global int_lng
        global par
        f_d = full_dir
        int_lng = interface_lng_val
        par = parent
    def run(self):
        global view
		
        f = open(f_d+'/VIEW_BASH', 'w')
        f.write('#!/bin/sh' + '\n' + '. /opt/openfoam4/etc/bashrc' + '\n' + 'paraFoam' + '\n' + 'exit')
        f.close()
		
        view_file = open(f_d + "/case_visual_out.log", "w")
		
        view_proc = subprocess.Popen(["bash "+f_d+"/VIEW_BASH"], cwd = f_d, shell = True, stdout=view_file, stderr=view_file)
		
        self.emit(QtCore.SIGNAL("started(PyQt_PyObject, QString)"), par, int_lng)
		
        while view_proc.poll() is None:
            time.sleep(0.5)
			
        return_code = view_proc.returncode	
			
        self.emit(QtCore.SIGNAL("finished(int, PyQt_PyObject, QString, QString)"), return_code, par, f_d, int_lng)	
