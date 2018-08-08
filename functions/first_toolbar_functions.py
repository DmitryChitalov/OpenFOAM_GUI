# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil
import re
import signal

from windows.prj_window import prj_window_class

from threads.case_threads import run_Thread
from threads.case_threads import stop_Thread
from threads.case_threads import view_Thread

from windows.lng_window import lng_form_class

from functions.case_functions import case_functions_class

class first_toolbar_functions_class():
	
	#.......................Функция открытия окна выбора директории проекта...................
	
    def on_proj_open(par):
        proj_win = prj_window_class(par)
        if par.interface_lng_val == 'Russian':
            proj_win.setWindowTitle('Окно выбора директории проекта')
        elif par.interface_lng_val == 'English':
            proj_win.setWindowTitle('Window for selecting project directory')
        proj_win.show()
		
	#...........................Функция запуска процесса решения задачи МСС.....................
        
    def on_task_open(par):
        par.t1 = run_Thread(par.full_dir, par, par.interface_lng_val)
        par.connect(par.t1, QtCore.SIGNAL("started(PyQt_PyObject, QString, QString)"), case_functions_class.on_case_run_started)
        par.connect(par.t1, QtCore.SIGNAL("finished(int, PyQt_PyObject, QString, QString)"), case_functions_class.on_case_run_finished)
        par.t1.start()
		
	#...........................Функция запуска останова процесса решения...........................

    def on_task_close(par):
        par.t2 = stop_Thread(par.full_dir, par, par.interface_lng_val)
        par.connect(par.t2, QtCore.SIGNAL("finished(int, PyQt_PyObject, QString, QString)"), case_functions_class.on_case_close_finished)
        par.t2.start()
		
	#-----------------------------Функция запуска визуализации результатов решения задачи МСС----------------------------------

    def on_view_open(par):
        par.t3 = view_Thread(par.full_dir, par, par.interface_lng_val)
        par.connect(par.t3, QtCore.SIGNAL("started(PyQt_PyObject, QString)"), case_functions_class.on_case_visual_started)
        par.connect(par.t3, QtCore.SIGNAL("finished(int, PyQt_PyObject, QString, QString)"), case_functions_class.on_case_visual_finished)
        par.t3.start()
		
    #........................Функция открытия окна выбора интерфейса программы...................
        
    def on_lng_chs(par):
        lng_win = lng_form_class(par)
        if par.interface_lng_val == 'Russian':
            lng_win.setWindowTitle('Окно выбора языка интерфейса')
        elif par.interface_lng_val == 'English':
            lng_win.setWindowTitle('Interface language selection window')
        lng_win.show()