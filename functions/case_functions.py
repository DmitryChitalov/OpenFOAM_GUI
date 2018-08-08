# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil
import re
import signal

from forms.rCF_forms.graph_form import graph_form_class

class case_functions_class():
	
    def on_case_run_started(par, int_lng, f_d):

        if int_lng == 'Russian':
            msg = "Выполняется процесс решения..."
        elif int_lng == 'English':
            msg = "The decision process is being implemented"
		
        par.treeview.setEnabled(False)
        par.task_close.setEnabled(True)
		
        par.listWidget.clear()
        par.item = QtGui.QListWidgetItem(msg, par.listWidget)
        color = QtGui.QColor("blue")
        par.item.setTextColor(color)
        par.listWidget.addItem(par.item)
		
    def on_case_run_finished(return_code, par, f_d, int_lng):
        if return_code == 0:
            if int_lng == 'Russian':
                msg = "Процесс решения успешно завершен"
                par.ffw_label.setText("График сходимости решения задачи " + "<font color='peru'>" + par.prj_name + "</font>")
            elif int_lng == 'English':
                msg = "Solution process successfully completed"
                par.ffw_label.setText("The graph of problem solution convergence " + "<font color='peru'>" + par.prj_name + "</font>")
            color = QtGui.QColor("green")
			
            par.treeview.setEnabled(True)
            par.task_close.setEnabled(False)
            par.view_open.setEnabled(True)
			
            par.outf_scroll.setFixedSize(350, 660)
            par.cdw_frame.setFixedSize(350, 35)
            par.cdw.setWidget(par.outf_scroll)
            par.cdw.setTitleBarWidget(par.cdw_frame)

            if int_lng == 'Russian':
                par.outf_lbl.setText('Результаты решения задачи ' + "<font color='peru'>" + par.prj_name + "</font>") 
            elif int_lng == 'English':
                par.outf_lbl.setText('Case solving results ' + "<font color='peru'>" + par.prj_name + "</font>") 
			
            f = open(f_d + '/out_run.log')
            data = f.read()     
            par.outf_edit.setText(data)	
			
            par.listWidget.clear()
            par.item = QtGui.QListWidgetItem(msg, par.listWidget)
            par.item.setTextColor(color)
            par.listWidget.addItem(par.item)
						 
            par.ffw_label.setStyleSheet("border-style: none;" "font-size: 9pt;")
            par.ffw.setTitleBarWidget(par.ffw_frame)
            par.ffw_frame.setFixedSize(838, 44)  
			
            graph_form = graph_form_class(f_d)
            par.ffw.setWidget(graph_form)
            par.setCentralWidget(par.ffw)
			
        elif return_code != 0 and return_code != 137:
            if int_lng == 'Russian':
                msg = "Процесс решения завершен c ошибками"
            elif int_lng == 'English':
                msg = "The decision process is completed with errors"
            color = QtGui.QColor("red")
			
            par.treeview.setEnabled(True)
            par.task_close.setEnabled(False)
			
            par.outf_scroll.setFixedSize(350, 660)
            par.cdw_frame.setFixedSize(350, 35)
            par.cdw.setWidget(par.outf_scroll)
            par.cdw.setTitleBarWidget(par.cdw_frame)

            if int_lng == 'Russian':
                par.outf_lbl.setText('Результаты решения задачи ' + "<font color='peru'>" + par.prj_name + "</font>") 
            elif int_lng == 'English':
                par.outf_lbl.setText('Case solving results ' + "<font color='peru'>" + par.prj_name + "</font>") 
			
            f = open(f_d + '/out_run.log')
            data = f.read()     
            par.outf_edit.setText(data)	
			
            par.listWidget.clear()
            par.item = QtGui.QListWidgetItem(msg, par.listWidget)
            par.item.setTextColor(color)
            par.listWidget.addItem(par.item)
		
        if os.path.exists(f_d + '/SOLVER_BASH'):
            os.remove(f_d + '/SOLVER_BASH')
        if os.path.exists(f_d + "/out_run.log"):
            os.remove(f_d + "/out_run.log")
				
    def on_case_close_finished(return_code, par, f_d, int_lng):
        if return_code == 0:
            f_o = open(f_d + "/out_kill.log", "r")
            data = f_o.read()
            f_o.close()

            con_reg = re.compile(r"\d*")
            con_mas = con_reg.findall(data)
            proc_to_kill = con_mas[0]

            os.kill(int(proc_to_kill), signal.SIGKILL)
			
            if int_lng == 'Russian':
                msg = "Процесс решения остановлен"
            elif int_lng == 'English':
                msg = "Solving process is stopped"
            color = QtGui.QColor("red")
			
            par.treeview.setEnabled(True)
            par.task_close.setEnabled(False)
			
            par.listWidget.clear()
            par.item = QtGui.QListWidgetItem(msg, par.listWidget)
            par.item.setTextColor(color)
            par.listWidget.addItem(par.item)

        if os.path.exists(f_d + '/KILL_PROC_BASH'):
            os.remove(f_d + '/KILL_PROC_BASH')
        if os.path.exists(f_d + '/out_kill.log'):
            os.remove(f_d + '/out_kill.log')
			
    def on_case_visual_started(par, int_lng):

        if int_lng == 'Russian':
            msg = "Визуализация результатов расчетного случая " + par.prj_name + " запущена"
        elif int_lng == 'English':
            msg = "Visualisation of case " + par.prj_name + " results is started"
        color = QtGui.QColor("blue")

        par.listWidget.clear()
        par.item = QtGui.QListWidgetItem(msg, par.listWidget)
        par.item.setTextColor(color)
        par.listWidget.addItem(par.item)
			
    def on_case_visual_finished(return_code, par, f_d, int_lng):
		
        case_visual_read_file = open(f_d + "/case_visual_out.log")
        data = case_visual_read_file.read()
		
        if int_lng == 'Russian':
            par.outf_lbl.setText('Результаты визуализации результатов расчетного случая ' + par.prj_name) 
        elif int_lng == 'English':
            par.outf_lbl.setText('Vizualization results of case ' + par.prj_name) 
        par.cdw.setWidget(par.outf_scroll)
        par.cdw.setTitleBarWidget(par.cdw_frame)
        par.outf_edit.setText(data)
		
        if return_code == 0:
            if int_lng == 'Russian':
                msg = "Визуализация результатов расчетного случая " + par.prj_name + " успешно завершена"
            elif int_lng == 'English':
                msg = "Visualisation of case " + par.prj_name + " results is successfully completed"
            color = QtGui.QColor("green")

        else:
            if int_lng == 'Russian':
                msg = "При визуализации результатов расчетного случая " + par.prj_name + " возникли проблемы"
            elif int_lng == 'English':
                msg = "Visualisation of case " + par.prj_name + " results is completed with errors"
            color = QtGui.QColor("red")

        par.listWidget.clear()
        par.item = QtGui.QListWidgetItem(msg, par.listWidget)
        par.item.setTextColor(color)
        par.listWidget.addItem(par.item)	

        if os.path.exists(f_d + '/VIEW_BASH'):
            os.remove(f_d + '/VIEW_BASH') 
        if os.path.exists(f_d + '/case_visual_out.log'):
            os.remove(f_d + '/case_visual_out.log') 
		