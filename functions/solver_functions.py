# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt5 import QtCore
from PyQt5 import QtSql
from PyQt5 import QtGui

from PyQt5.QtWidgets import QWidget, QFileDialog, QLineEdit, QLabel, \
    QHBoxLayout, QLineEdit, QPushButton, QGridLayout, \
    QFrame, QVBoxLayout, QFormLayout, QRadioButton, QDoubleSpinBox, \
	QSpinBox, QCheckBox, QGroupBox, QComboBox, QListWidgetItem

import pickle
import os
import shutil
import re

class str_an_functions_class():		
	
	###..............................Функция вывода результатов потока t1..........................### 
	
	def on_str_an_start(prj_path_val_th, mesh_name_txt_val_th, par, int_lng, msh_t):

		if int_lng == 'Russian':
			msg_lbl = QLabel('<span style="color:blue">' + "Выполняется стресс-анализ" + '</span>')
		elif int_lng == 'English':
			msg_lbl = QLabel('<span style="color:blue">' + "Stress-analysis making" + '</span>')

		par.listWidget.clear()
		par.item = QListWidgetItem()
		par.listWidget.addItem(par.item)
		par.listWidget.setItemWidget(par.item, msg_lbl)
	
	def on_str_an_finished(return_code, prj_path_val_th, mesh_name_txt_val_th, par, int_lng, msh_t):

		msh_read_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th + "/str_an_script.log")
		data = msh_read_file.read()

		if int_lng == 'Russian':
			par.outf_lbl.setText('Результаты проведения стресс-анализа') 
		elif int_lng == 'English':
			par.outf_lbl.setText('Stress-analys results') 
		par.cdw.setWidget(par.outf_scroll)
		par.cdw.setTitleBarWidget(par.cdw_frame)
		par.outf_edit.setText(data)

		if return_code == 0:
			if int_lng == 'Russian':
				msg_lbl = QLabel('<span style="color:green">' + "Стресс-анализ успешно выполнен" + '</span>')
			elif int_lng == 'English':
				msg_lbl = QLabel('<span style="color:green">' + "Stress-analys successful finished" + '</span>')

			par.msh_visual.setEnabled(True)

		else:
			if int_lng == 'Russian':
				msg_lbl = QLabel('<span style="color:red">' + "Стресс-анализ выполнен с ошибками" + '</span>')
			elif int_lng == 'English':
				msg_lbl = QLabel('<span style="color:red">' + "Stress-analys finished with errors" + '</span>')
					
		par.listWidget.clear()
		par.item = QListWidgetItem()
		par.listWidget.addItem(par.item)
		par.listWidget.setItemWidget(par.item, msg_lbl)
		
		if os.path.exists(par.full_dir + '/str_an_script'):
			os.remove(par.full_dir + '/str_an_script')
		if os.path.exists(par.full_dir + '/str_an_script.log'):
			os.remove(par.full_dir + '/str_an_script.log')
		
	def on_str_an_visual_run(par, int_lng, msh_t):
		
		if int_lng == 'Russian':
			msg_lbl = QLabel('<span style="color:blue">' + "Визуализация результатов стресс-анализа запущена" + '</span>')
		elif int_lng == 'English':
			msg_lbl = QLabel('<span style="color:blue">' + "Start stress-analys making" + '</span>')
					
		par.listWidget.clear()
		par.item = QListWidgetItem()
		par.listWidget.addItem(par.item)
		par.listWidget.setItemWidget(par.item, msg_lbl)
		
	def on_str_an_visual_finished(return_code, prj_path_val_th, mesh_name_txt_val_th, par, int_lng, msh_t):

		str_an_read_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th + "/str_an_script.log")
		data = str_an_read_file.read()

		if int_lng == 'Russian':
			par.outf_lbl.setText('Результаты стресс-анализа') 
		elif int_lng == 'English':
			par.outf_lbl.setText('Stress-analys results') 
		par.cdw.setWidget(par.outf_scroll)
		par.cdw.setTitleBarWidget(par.cdw_frame)
		par.outf_edit.setText(data)

		if return_code == 0:
			if int_lng == 'Russian':
				msg_lbl = QLabel('<span style="color:green">' + "Визуализация результатов стресс-анализа успешно завершена" + '</span>')
			elif int_lng == 'English':
				msg_lbl = QLabel('<span style="color:green">' + "Visualisation of stress-analys results complete" + '</span>')

		else:
			if int_lng == 'Russian':
				msg_lbl = QLabel('<span style="color:red">' + "При отображении результатов стресс-анализа возникли проблемы" + '</span>')
			elif int_lng == 'English':
				msg_lbl = QLabel('<span style="color:red">' + "Visualisation of stress-analys results complete with errors" + '</span>')
			color = QtGui.QColor("red")

		par.listWidget.clear()
		par.item = QListWidgetItem()
		par.listWidget.addItem(par.item)
		par.listWidget.setItemWidget(par.item, msg_lbl)	
		
		if os.path.exists(par.full_dir + '/str_an_script'):
			os.remove(par.full_dir + '/str_an_script')
		if os.path.exists(par.full_dir + '/str_an_script.log'):
			os.remove(par.full_dir + '/str_an_script.log')
