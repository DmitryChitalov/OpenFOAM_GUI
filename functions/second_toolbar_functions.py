# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil
import re
import signal

from windows.msh_window import msh_window_class

from threads.msh_threads import msh_generation_thread
from threads.msh_threads import msh_visualisation_thread

from functions.msh_functions import msh_functions_class


class second_toolbar_functions_class():
	    
	#.......................Функция открытия окна выбора директории расчетной сетки.......................

    def on_msh_open(par):
        msh_win = msh_window_class(par)
        if par.interface_lng_val == 'Russian':
            msh_win.setWindowTitle('Окно выбора директории расчетной сетки')
        elif par.interface_lng_val == 'English':
            msh_win.setWindowTitle('Mesh directory selection window')
        msh_win.show()
		
    #...........................Функция запуска генерации расчетной сетки........................

    def on_msh_run(prj_path_val, mesh_name_txt_val, pp_dir, par, interface_lng_val, msh_type): 
		
        bm = msh_generation_thread(prj_path_val, mesh_name_txt_val, pp_dir, par, interface_lng_val, msh_type)
        par.connect(bm, QtCore.SIGNAL("finished(int, QString, QString, PyQt_PyObject, QString, QString)"), msh_functions_class.on_msh_finished)
        bm.start()
		
    #...........................Функция запуска визуализации расчетной сетки.....................         

    def on_visual_msh_run(prj_path_val, mesh_name_txt_val, pp_dir, par, interface_lng_val):

        par.mv = msh_visualisation_thread(prj_path_val, mesh_name_txt_val, pp_dir, par, interface_lng_val)
        par.connect(par.mv, QtCore.SIGNAL("started(PyQt_PyObject, QString)"), msh_functions_class.on_msh_visual_run)
        par.connect(par.mv, QtCore.SIGNAL("finished(int, QString, QString, PyQt_PyObject, QString)"), msh_functions_class.on_msh_visual_finished)
        par.mv.start()
	