# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм--------------------------#

from PyQt5 import QtCore
from PyQt5 import QtSql
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QWidget, QFileDialog, QLineEdit, QLabel, \
    QHBoxLayout, QLineEdit, QPushButton, QGridLayout, \
    QFrame, QVBoxLayout, QFormLayout, QRadioButton, QDoubleSpinBox, \
	QSpinBox, QCheckBox, QGroupBox, QComboBox, QListWidgetItem

import os
import subprocess
import time

class str_an_thread(QtCore.QThread):
	str_an_sig = pyqtSignal(int, 'QString', 'QString', 'PyQt_PyObject', 'QString', 'QString')
	str_an_sig_start = pyqtSignal('QString', 'QString', 'PyQt_PyObject', 'QString', 'QString')
	def __init__(self, prj_path_val, mesh_name_txt_val, pp_dir, parent, interface_lng_val, msh_type):
		QtCore.QThread.__init__(self, parent)
		
		global prj_path_val_th
		global mesh_name_txt_val_th_a
		global mesh_name_txt_val_th_new
		global pp_dir_th
		global par
		global int_lng
		global msh_t
		

		prj_path_val_th = prj_path_val
		#mesh_name_txt_val_th = mesh_name_txt_val + '_foamyHexMesh'
		mesh_name_txt_val_th_new = mesh_name_txt_val
		pp_dir_th = pp_dir
		par = parent
		int_lng = interface_lng_val
		msh_t = msh_type
		
	def run(self):
		MeshDict_file = prj_path_val_th + '/' + msh_t + "Dict"
		if os.path.exists(MeshDict_file) == True:
			if msh_t == 'blockMesh':
				mesh_name_txt_val_th_a = mesh_name_txt_val_th_new + '_blockMesh'
		
				str_an_bash_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th_a + '/' + 'str_an_script', 'w')
				str_an_bash_file.write('#!/bin/sh' + '\n' + '. /opt/openfoam6/etc/bashrc' + '\n' + 'solidDisplacementFoam' + '\n' + 'exit')
				str_an_bash_file.close()
				
			elif msh_t == 'snappyHexMesh':
				mesh_name_txt_val_th_a = mesh_name_txt_val_th_new + '_snappyHexMesh'
		
				str_an_bash_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th_a + '/' + 'str_an_script', 'w')
				str_an_bash_file.write('#!/bin/sh' + '\n' + '. /opt/openfoam6/etc/bashrc' + '\n' + 'solidDisplacementFoam' + '\n' + 'exit')
				str_an_bash_file.close()
				
			str_an_out_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th_a + '/' + 'str_an_script.log', "w")
			str_an_run_subprocess = subprocess.Popen(["bash " + prj_path_val_th + '/' + mesh_name_txt_val_th_a + "/" + "str_an_script"], cwd = pp_dir_th, shell=True, stdout=str_an_out_file, stderr=str_an_out_file)
			str_an_out_file.close()
			
			self.str_an_sig_start.emit(prj_path_val_th, mesh_name_txt_val_th_a, par, int_lng, msh_t)	

			while str_an_run_subprocess.poll() is None:
				time.sleep(0.5)
			
			return_code = str_an_run_subprocess.returncode
			self.str_an_sig.emit(return_code, prj_path_val_th, mesh_name_txt_val_th_a, par, int_lng, msh_t)	

		else:
			if int_lng == 'Russian':
				msg_lbl = QLabel('<span style="color:blue">' + "Сначала выполните сохранение расчетной сетки - файл " + msh_t + '</span>')
			elif int_lng == 'English':
				msg_lbl = QLabel('<span style="color:blue">' + "First of all save the mesh - " + msh_t + "file"+ '</span>')
					
			par.listWidget.clear()
			par.item = QListWidgetItem()
			par.listWidget.addItem(par.item)
			par.listWidget.setItemWidget(par.item, msg_lbl)
			
			
class on_str_an_visualisation_thread(QtCore.QThread):
	str_an_vis_start_sig = pyqtSignal('PyQt_PyObject', 'QString', 'QString')
	str_an_vis_finish_sig = pyqtSignal(int, 'QString', 'QString', 'PyQt_PyObject', 'QString', 'QString')
	def __init__(self, prj_path_val, mesh_name_txt_val, pp_dir, parent, interface_lng_val, msh_type):
		QtCore.QThread.__init__(self, parent)
		
		global prj_path_val_th
		global mesh_name_txt_val_th
		global pp_dir_th
		global par
		global int_lng
		global msh_t

		prj_path_val_th = prj_path_val
		#mesh_name_txt_val_th = mesh_name_txt_val
		mesh_name_txt_val_th_new = mesh_name_txt_val
		pp_dir_th = pp_dir
		par = parent
		int_lng = interface_lng_val
		msh_t = msh_type
		
	def run(self):
		self.str_an_vis_start_sig.emit(par, int_lng, msh_t)
		if msh_t == 'blockMesh':
			mesh_name_txt_val_th_a = mesh_name_txt_val_th_new + '_blockMesh'
			MeshDict_file = pp_dir_th + '/' + 'system' + '/' + 'blockMeshDict'
			
		elif msh_t == 'snappyHexMesh':
			mesh_name_txt_val_th_a = mesh_name_txt_val_th_new + '_snappyHexMesh'
			MeshDict_file = pp_dir_th + '/' + 'system' + '/' + 'snappyHexMeshDict'

		#blockMeshDict_file = pp_dir_th + '/' + 'constant' + '/' + 'extendedFeatureEdgeMesh'
		#if os.path.exists(blockMeshDict_file) == True:
		str_an_vis_bash_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th_a + '/' + 'str_an_script', 'w')
		str_an_vis_bash_file.write('#!/bin/sh' + '\n' + '. /opt/openfoam6/etc/bashrc' + '\n' + 'paraFoam' + '\n' + 'exit')
		str_an_vis_bash_file.close()

		str_an_vis_out_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th_a + '/' + 'str_an_script.log', "w")
		str_an_vis_run_subprocess = subprocess.Popen(["bash " + prj_path_val_th + '/' + mesh_name_txt_val_th_a + "/" + "str_an_script"], cwd = pp_dir_th, shell=True, stdout=str_an_vis_out_file, stderr=str_an_vis_out_file)
		str_an_vis_out_file.close()

		#self.emit(QtCore.SIGNAL("started(PyQt_PyObject, QString, QString)"), par, int_lng, msh_t)

		while str_an_vis_run_subprocess.poll() is None:
			time.sleep(0.3)

		return_code = str_an_vis_run_subprocess.returncode

		self.str_an_vis_finish_sig.emit(return_code, prj_path_val_th, mesh_name_txt_val_th_a, par, int_lng, msh_t)

