import sys, re
import os

from PyQt4 import QtCore, QtGui

import pickle

from forms.sHMD_forms.initial_form import initial_class
from forms.sHMD_forms.geometry_1_form import geometry_1_class
from forms.sHMD_forms.geometry_2_form import geometry_2_class
from forms.sHMD_forms.castellatedMC_1_form import castellatedMC_1_class
from forms.sHMD_forms.castellatedMC_2_form import castellatedMC_2_class
from forms.sHMD_forms.layers_form import layers_class
from forms.sHMD_forms.snapC_form import snapC_class
from forms.sHMD_forms.meshQC_form import meshQC_class
from functions.snappyHexMeshDict_generation import snappyHexMeshDict_generation_class

class shmd_window_class(QtGui.QWidget):
	def __init__(self, parent, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur):
		QtGui.QWidget.__init__(self, parent)
	
		global tab
		global initial_group, initial_btnSave, geometry_visible, castellatedMC_visible, snapC_visible, layers_visible, meshQC_visible, cM_edit, s_edit, aL_edit, mT_edit, sL_edit, lS_edit, lF_edit, g_edit, f_edit, f_val, rS_edit, rS_val, rR_edit, rR_val, l_edit
		
		global geometry_1_group, geometry_1_btnSave, geometry_type_list, shape_complex_lbl_list, shape_complex_numb_list, base_shape_lbl_list, base_shape_type_list, regions_lbl_list, regions_numb_list
		global geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list
		global castellatedMC_1_group, castellatedMC_1_btnSave, prs_grid, tri_distirbTri_list, other_geometry_list, f_level_single_edit_list, f_level_multi_edit_list, f_level_multi_val_edit_list, rS_regions_edit_list, rS_regions_val_edit_list, rR_level_single_edit_list, rR_level_multi_edit_list, rR_level_multi_val_edit_list
		global castellatedMC_2_group, castellatedMC_2_btnSave, prs_lvl_grid, f_level_single_list, rR_level_single_list, el_CMC_rS_regions_list
		global layers_group, layers_btnSave, layers_prs_base_table, layers_prs_add_table
		global snapC_group, snapC_btnSave, snapC_prs_table, snapC_chcks_list, snapC_prs_list, snapC_def_list, snapC_val_list
		global meshQC_group, meshQC_btnSave, meshQC_prs_add_table, meshQC_chcks_list, meshQC_prs_list, meshQC_def_list, meshQC_val_list 
		
		global geometry_1_path, geometry_2_path, castellatedMC_1_path, castellatedMC_2_path, layers_path, snapC_path, meshQC_path
		
		global f_level_single_edit_list, f_level_multi_val_edit_list, f_level_multi_edit_list, rS_regions_edit_list, rS_regions_val_edit_list
		
		#global prj_path
		global int_lng
		#global mesh_name_txt
		#global pd_2
		
		global geometry_txt_old_mas
		global shape_complex_numb_val_old_mas
		global regions_numb_val_old_mas
		global base_shape_type_old_mas
		
		global f_level_single_edit_old_mas 
		global f_level_multi_edit_old_mas 
		global f_level_multi_val_edit_old_mas 
		global rS_regions_edit_old_mas 
		global rS_regions_val_edit_old_mas 
		global rR_level_single_edit_old_mas
		global rR_level_multi_edit_old_mas
		global rR_level_multi_val_edit_old_mas
		
		global cM_v, s_v, aL_v, mT_v, g_v, f_v, f_val_v, rS_v, rS_val_v, rR_v, rR_val_v, l_v, r_v, sL_v, lS_v, lF_v
		
		global parn
		parn = par
		
		#prj_path, mesh_name_txt, pd_2 = parent.prj_path_return()
		#int_lng = parent.int_lng_path_return()
		
		int_lng = parent.int_lng_path_return()
		global prj_path, mesh_name_txt, pd_2 
		prj_path = prj_path_cur
		mesh_name_txt = mesh_name_txt_cur
		pd_2 = pd_2_cur
		
		#------------------------------Загружаем вкладки для имеющегося файла----------------------------------#
		
		#------------------------------initial----------------------------------#
		
		tab = QtGui.QTabWidget()
		initial_group, initial_btnSave, geometry_visible, castellatedMC_visible, snapC_visible, layers_visible, meshQC_visible, cM_edit, s_edit, aL_edit, mT_edit, sL_edit, lS_edit, lF_edit, g_edit, f_edit, f_val, rS_edit, rS_val, rR_edit, rR_val, l_edit = initial_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2)
		tab.insertTab(0, initial_group, "&initial")
		g_edit.valueChanged.connect(lambda: self.g_edit_changed(g_edit))
		f_edit.stateChanged.connect(self.f_state_changed)
		rS_edit.stateChanged.connect(self.rS_state_changed)
		rR_edit.stateChanged.connect(self.rR_state_changed)
		
		cM_v = cM_edit.isChecked()
		s_v = s_edit.isChecked()
		aL_v = aL_edit.isChecked()
		mT_v = mT_edit.text()
		g_v = g_edit.value()
		f_v = f_edit.isChecked()
		f_val_v = f_val.value()
		rS_v = rS_edit.isChecked()
		rS_val_v = rS_val.value()
		rR_v = rR_edit.isChecked()
		rR_val_v = rR_val.value()
		l_v = l_edit.value()
		sL_v = sL_edit.isChecked()
		lS_v = lS_edit.isChecked()
		lF_v = lF_edit.isChecked()
		
		initial_btnSave.clicked.connect(self.on_initial_btnSave_clicked)
			
		#-------------------------------geometry_1--------------------------------#
		
		geometry_1_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_1.pkl'
		#and os.path.exists(geometry_1_path)
		if geometry_visible == True:
			geometry_1_group, geometry_1_btnSave, geometry_type_list, shape_complex_lbl_list, shape_complex_numb_list, base_shape_lbl_list, base_shape_type_list, regions_lbl_list, regions_numb_list = geometry_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
			tab.insertTab(1, geometry_1_group, "&geometry_1")
			geometry_1_btnSave.clicked.connect(self.on_geometry_1_btnSave_clicked)
			
			geometry_txt_old_mas = []
			shape_complex_numb_val_old_mas = []
			regions_numb_val_old_mas = []
			base_shape_type_old_mas = []
			
			for bvc in range(len(geometry_type_list)):
				geometry_txt_old = geometry_type_list[bvc].currentText()
				geometry_txt_old_mas.append(geometry_txt_old)
				
			for bvc in range(len(shape_complex_numb_list)):
				shape_complex_numb_val_old = shape_complex_numb_list[bvc].value()
				shape_complex_numb_val_old_mas.append(shape_complex_numb_val_old)
				
			for bvc in range(len(base_shape_type_list)):
				base_shape_type_old = base_shape_type_list[bvc].currentText()
				base_shape_type_old_mas.append(base_shape_type_old)
				
			for bvc in range(len(regions_numb_list)):
				regions_numb_val_old = regions_numb_list[bvc].value()
				regions_numb_val_old_mas.append(regions_numb_val_old)
				
		else:
			geometry_1_null_lbl = QtGui.QLabel()
			tab.insertTab(1, geometry_1_null_lbl, "&geometry_1")
			tab.setTabEnabled(1, False)
			
		#-------------------------------geometry_2------------------------------------#
	
		geometry_2_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if geometry_visible == True and os.path.exists(geometry_2_path):       
			geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list = geometry_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
			tab.insertTab(2, geometry_2_group, "&geometry_2")
			geometry_2_btnSave.clicked.connect(self.on_geometry_2_btnSave_clicked)		
		else:
			geometry_2_null_lbl = QtGui.QLabel()
			tab.insertTab(2, geometry_2_null_lbl, "&geometry_2")
			tab.setTabEnabled(2, False)
			
		#------------------------------castellatedMC_1---------------------------------#

		castellatedMC_1_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_1.pkl'
		#and os.path.exists(castellatedMC_1_path)
		if castellatedMC_visible == True:
			castellatedMC_1_group, castellatedMC_1_btnSave, prs_grid, tri_distirbTri_list, other_geometry_list, f_level_single_edit_list, f_level_multi_edit_list, f_level_multi_val_edit_list, rS_regions_edit_list, rS_regions_val_edit_list, rR_level_single_edit_list, rR_level_multi_edit_list, rR_level_multi_val_edit_list = castellatedMC_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, castellatedMC_visible)
			castellatedMC_1_btnSave.clicked.connect(self.on_castellatedMC_1_btnSave_clicked)
			tab.insertTab(3, castellatedMC_1_group, "&castellatedMC_1")
		else:
			castellatedMC_1_null_lbl = QtGui.QLabel()
			tab.insertTab(3, castellatedMC_1_null_lbl, "&castellatedMC_1")
			tab.setTabEnabled(3, False)
			
		#-------------------------------castellatedMC_2------------------------------------#
	
		castellatedMC_2_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_2.pkl'
		if castellatedMC_visible == True and os.path.exists(castellatedMC_2_path):       
			castellatedMC_2_group, castellatedMC_2_btnSave, prs_lvl_grid, f_level_single_list, rR_level_single_list, el_CMC_rS_regions_list = castellatedMC_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, castellatedMC_visible)
			tab.insertTab(4, castellatedMC_2_group, "&castellatedMC_2")
			castellatedMC_2_btnSave.clicked.connect(self.on_castellatedMC_2_btnSave_clicked)		
			
			f_level_single_edit_old_mas = []
			f_level_multi_edit_old_mas = []
			f_level_multi_val_edit_old_mas = []
			rS_regions_edit_old_mas = []
			rS_regions_val_edit_old_mas = []
			rR_level_single_edit_old_mas = []
			rR_level_multi_edit_old_mas = []
			rR_level_multi_val_edit_old_mas = []
			
			for bvc in range(len(f_level_single_edit_list)):	
				f_level_single_edit_old = f_level_single_edit_list[bvc].isChecked()
				f_level_single_edit_old_mas.append(f_level_single_edit_old)
				
			for bvc in range(len(f_level_multi_edit_list)):	
				f_level_multi_edit_old = f_level_multi_edit_list[bvc].isChecked()
				f_level_multi_edit_old_mas.append(f_level_multi_edit_old)
			
			for bvc in range(len(f_level_multi_val_edit_list)):	
				f_level_multi_val_edit_old = f_level_multi_val_edit_list[bvc].value()
				f_level_multi_val_edit_old_mas.append(f_level_multi_val_edit_old)
				
			for bvc in range(len(rS_regions_edit_list)):	
				rS_regions_edit_old = rS_regions_edit_list[bvc].isChecked()
				rS_regions_edit_old_mas.append(rS_regions_edit_old)
				
			for bvc in range(len(rS_regions_val_edit_list)):	
				rS_regions_val_edit_old = rS_regions_val_edit_list[bvc].value()
				rS_regions_val_edit_old_mas.append(rS_regions_val_edit_old)	
				
			for bvc in range(len(rR_level_single_edit_list)):	
				rR_level_single_edit_old = rR_level_single_edit_list[bvc].isChecked()
				rR_level_single_edit_old_mas.append(rR_level_single_edit_old)
				
			for bvc in range(len(rR_level_multi_edit_list)):	
				rR_level_multi_edit_old = rR_level_multi_edit_list[bvc].isChecked()
				rR_level_multi_edit_old_mas.append(rR_level_multi_edit_old)
			
			for bvc in range(len(rR_level_multi_val_edit_list)):	
				rR_level_multi_val_edit_old = rR_level_multi_val_edit_list[bvc].value()
				rR_level_multi_val_edit_old_mas.append(rR_level_multi_val_edit_old)
		else:
			castellatedMC_2_null_lbl = QtGui.QLabel()
			tab.insertTab(4, castellatedMC_2_null_lbl, "&castellatedMC_2")
			tab.setTabEnabled(4, False)
			
		#------------------------------layers---------------------------------#

		layers_path = prj_path + '/'+ mesh_name_txt + '_' + pd_2 + '/' + 'layers.pkl' 
		#and os.path.exists(layers_path)
		if layers_visible == True:
			layers_group, layers_btnSave, layers_prs_base_table, layers_prs_add_table = layers_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, layers_visible)
			layers_btnSave.clicked.connect(self.on_layers_btnSave_clicked)
			tab.insertTab(5, layers_group, "&layers")
			
		else:
			layers_null_lbl = QtGui.QLabel()
			tab.insertTab(5, layers_null_lbl, "&layers")
			tab.setTabEnabled(5, False)
			
		#------------------------------snapC---------------------------------#

		snapC_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'snapC.pkl'  
		#and os.path.exists(snapC_path)
		if snapC_visible == True:
			snapC_group, snapC_btnSave, snapC_prs_table, snapC_chcks_list, snapC_prs_list, snapC_def_list, snapC_val_list = snapC_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, snapC_visible)
			snapC_btnSave.clicked.connect(self.on_snapC_btnSave_clicked)
			tab.insertTab(6, snapC_group, "&snapC")
		else:
			snapC_null_lbl = QtGui.QLabel()
			tab.insertTab(6, snapC_null_lbl, "&snapC")
			tab.setTabEnabled(6, False)
			
		#------------------------------meshQC---------------------------------#

		meshQC_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'meshQC.pkl'  
		#and os.path.exists(meshQC_path)
		if meshQC_visible == True:
			meshQC_group, meshQC_btnSave, meshQC_prs_add_table, meshQC_chcks_list, meshQC_prs_list, meshQC_def_list, meshQC_val_list = meshQC_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, meshQC_visible)
			meshQC_btnSave.clicked.connect(self.on_meshQC_btnSave_clicked)
			tab.insertTab(7, meshQC_group, "&meshQC")
		else:
			meshQC_null_lbl = QtGui.QLabel()
			tab.insertTab(7, meshQC_null_lbl, "&meshQC")
			tab.setTabEnabled(7, False)
		
		#-------------------------Главный фрейм формы с элементами--------------------------#

		btnSave = QtGui.QPushButton("Сохранить")
		btnSave.setFixedSize(80, 25)
		btnSave.clicked.connect(self.on_btnSave_clicked)
		btnCancel = QtGui.QPushButton("Отмена")
		btnCancel.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(btnSave)
		buttons_hbox.addWidget(btnCancel)
		if int_lng == 'Russian':
			btnSave.setText("Сохранить")
			btnCancel.setText("Отмена")
		elif int_lng == 'English':	
			btnSave.setText("Save")
			btnCancel.setText("Cancel")
   
		scrollLayout = QtGui.QFormLayout()
		scrollArea = QtGui.QScrollArea()
		scrollArea.setWidgetResizable(True) 
		scrollArea.setWidget(tab)
		scrollArea.setFixedSize(760, 637)	
			
		bMD_grid = QtGui.QGridLayout()
		bMD_grid.addWidget(scrollArea, 0, 0, alignment=QtCore.Qt.AlignCenter)
		bMD_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		bMD_frame = QtGui.QFrame()
		bMD_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
		bMD_frame.setFrameShape(QtGui.QFrame.Panel)
		bMD_frame.setFrameShadow(QtGui.QFrame.Sunken)
		bMD_frame.setLayout(bMD_grid)

		fvS_vbox = QtGui.QVBoxLayout() 
		fvS_vbox.addWidget(bMD_frame)

		# ---------------------Размещение на форме всех компонентов-------------------------#

		form = QtGui.QFormLayout()
		form.addRow(fvS_vbox)
		self.setLayout(form)
		
		#---------------------Привязываем к элементам формы обработчики, если изменяем имеющийся файл сетки----------------#
		
		if geometry_visible == True and os.path.exists(geometry_1_path):	
			for bvc in range(len(geometry_type_list)):
				self.geometry_control_chng(geometry_type_list, bvc)	
				
			if os.path.exists(geometry_2_path):
				for bvc in range(len(all_tri_file_btn_list)):
					if all_tri_file_btn_list[bvc] != '':
						self.tri_file_chng(all_tri_file_btn_list, bvc)	
					
		if castellatedMC_visible == True and os.path.exists(castellatedMC_1_path):
			if f_edit.isChecked() == True:
				for bvc in range(len(f_level_single_edit_list)):
					self.f_single_level_chng(f_level_single_edit_list, f_level_multi_val_edit_list, bvc)				
				for bvc in range(len(f_level_multi_edit_list)):
					self.f_multi_level_chng(f_level_multi_edit_list, f_level_multi_val_edit_list, bvc)	
				
			elif rS_edit.isChecked() == True:
				for bvc in range(len(rS_regions_edit_list)):
					self.rS_regions_chng(rS_regions_edit_list, rS_regions_val_edit_list, bvc)
					
			if rR_edit.isChecked() == True:
				for bvc in range(len(rR_level_single_edit_list)):
					self.rR_single_level_chng(rR_level_single_edit_list, rR_level_multi_val_edit_list, bvc)				
				for bvc in range(len(rR_level_multi_edit_list)):
					self.rR_multi_level_chng(rR_level_multi_edit_list, rR_level_multi_val_edit_list, bvc)
		
		if snapC_visible == True and os.path.exists(snapC_path):
			for bvc in range(len(snapC_chcks_list)):
				self.snapC_control_chng(snapC_chcks_list, bvc)	
				
		if meshQC_visible == True and os.path.exists(meshQC_path):		
			for bvc in range(len(meshQC_chcks_list)):
				self.meshQC_control_chng(meshQC_chcks_list, bvc)	
			
	#------------------------------Связываем элементы управления с функциями----------------------------#
		
	def geometry_control_chng(self, geometry_type_list, bvc):
		geometry_type_list[bvc].activated.connect(lambda: self.geometry_on_change(bvc))
		
	def tri_file_chng(self, all_tri_file_btn_list, bvc):
		all_tri_file_btn_list[bvc].clicked.connect(lambda: self.tri_file_on_change(bvc))
		
	def	f_single_level_chng(self, f_level_single_edit_list, f_level_multi_val_edit_list, bvc):
		f_level_single_edit_list[bvc].clicked.connect(lambda: self.f_single_level_on_change(bvc))
	
	def	f_multi_level_chng(self, f_level_multi_edit_list, f_level_multi_val_edit_list, bvc):
		f_level_multi_edit_list[bvc].clicked.connect(lambda: self.f_multi_level_on_change(bvc))
	
	def	rS_regions_chng(self, rS_regions_edit_list, rS_regions_val_edit_list, bvc):
		rS_regions_edit_list[bvc].clicked.connect(lambda: self.rS_regions_on_change(bvc))
		
	def	rR_single_level_chng(self, rR_level_single_edit_list, rR_level_multi_val_edit_list, bvc):
		rR_level_single_edit_list[bvc].clicked.connect(lambda: self.rR_single_level_on_change(bvc))
	
	def	rR_multi_level_chng(self, rR_level_multi_edit_list, rR_level_multi_val_edit_list, bvc):
		rR_level_multi_edit_list[bvc].clicked.connect(lambda: self.rR_multi_level_on_change(bvc))
	
	def snapC_control_chng(self, snapC_chcks_list, bvc):
		snapC_chcks_list[bvc].clicked.connect(lambda: self.snapC_on_change(bvc))
		
	def meshQC_control_chng(self, meshQC_chcks_list, bvc):
		meshQC_chcks_list[bvc].clicked.connect(lambda: self.meshQC_on_change(bvc))
	
	#------------------------------Функции, связанные с элементами формы--------------------------------#
	def geometry_on_change(self, bvc):
		geometry_txt = geometry_type_list[bvc].currentText()
		if geometry_txt == "Набор базовых фигур" or geometry_txt == "Base shape complex":
			shape_complex_lbl_list[bvc].setVisible(True)
			shape_complex_numb_list[bvc].setVisible(True)
			base_shape_lbl_list[bvc].setVisible(False)
			base_shape_type_list[bvc].setVisible(False)
			regions_lbl_list[bvc].setVisible(False)
			regions_numb_list[bvc].setVisible(False)
		elif geometry_txt == "Базовая фигура" or geometry_txt == "Base shape":
			base_shape_lbl_list[bvc].setVisible(True)
			base_shape_type_list[bvc].setVisible(True)
			shape_complex_lbl_list[bvc].setVisible(False)
			shape_complex_numb_list[bvc].setVisible(False)
			regions_lbl_list[bvc].setVisible(False)
			regions_numb_list[bvc].setVisible(False)
		elif geometry_txt == 'Три-поверхность' or geometry_txt == 'Tri-surface' or geometry_txt == 'Распределенная три-поверхность' or geometry_txt == 'Distributed tri-surface':
			shape_complex_lbl_list[bvc].setVisible(False)
			shape_complex_numb_list[bvc].setVisible(False)
			base_shape_lbl_list[bvc].setVisible(False)
			base_shape_type_list[bvc].setVisible(False)
			regions_lbl_list[bvc].setVisible(True)
			regions_numb_list[bvc].setVisible(True)

	#---		
	
	def f_state_changed(self):
		if f_edit.isChecked() == False:
			f_val.setEnabled(False)
		elif f_edit.isChecked() == True:
			f_val.setEnabled(True)
			
	def rS_state_changed(self):
		if rS_edit.isChecked() == False:
			rS_val.setEnabled(False)
		elif rS_edit.isChecked() == True:
			rS_val.setEnabled(True)
			
	def rR_state_changed(self):
		if rR_edit.isChecked() == False:
			rR_val.setEnabled(False)
		elif rR_edit.isChecked() == True:
			rR_val.setEnabled(True)
			
	#---Для features в castellatedMC_1
	def f_single_level_on_change(self, bvc):
		flse = f_level_single_edit_list[bvc]
		if flse.isChecked() == True:
			f_level_multi_val_edit_list[bvc].setEnabled(False)
			
	def f_multi_level_on_change(self, bvc):
		flme = f_level_multi_edit_list[bvc]
		if flme.isChecked() == True:
			f_level_multi_val_edit_list[bvc].setEnabled(True)	
	
	#---Для refinementSurface
	def rS_regions_on_change(self, bvc):
		rsre = rS_regions_edit_list[bvc]
		if rsre.isChecked() == True:
			rS_regions_val_edit_list[bvc].setEnabled(True)
		elif rsre.isChecked() == False:
			rS_regions_val_edit_list[bvc].setEnabled(False)
			
	#---Для refinementRegions в castellatedMC_1
	def rR_single_level_on_change(self, bvc):
		rRlse = rR_level_single_edit_list[bvc]
		if rRlse.isChecked() == True:
			rR_level_multi_val_edit_list[bvc].setEnabled(False)
			
	def rR_multi_level_on_change(self, bvc):
		rRlme = rR_level_multi_edit_list[bvc]
		if rRlme.isChecked() == True:
			rR_level_multi_val_edit_list[bvc].setEnabled(True)	
	
	#---
	def tri_file_on_change(self, bvc):
		tri_file_elem = all_tri_file_btn_list[bvc]
		if tri_file_elem != '':
			tri_path = QtGui.QFileDialog.getOpenFileName(directory=QtCore.QDir.currentPath())
			if tri_path:
				tri_path_begin, tri_file = os.path.split(tri_path)
				tri_name, tri_rasshir = tri_file.split('.')
				if tri_rasshir == 'stl' or tri_rasshir == 'obj':
					all_tri_file_edit_list[bvc].setText(tri_file)
				else:
					if int_lng == 'Russian':
						dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Внимание!", "Файл должен иметь расширение .stl или .obj", buttons = QtGui.QMessageBox.Ok)
					elif int_lng == 'English':
						dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Attention!", "The file must have a .stl or .obj extension", buttons = QtGui.QMessageBox.Ok)
					result = dialog.exec_()
	#---			
	def g_edit_changed(self, g_edit):
		g_edit_value = g_edit.value()
		f_val.setRange(1, g_edit_value)
		
	#---
	def snapC_on_change(self, bvc):
		snapC_chck = snapC_chcks_list[bvc].isChecked()
		if snapC_chck == True:
			snapC_prs_list[bvc].setEnabled(True)
			snapC_def_list[bvc].setEnabled(True)
			snapC_val_list[bvc].setEnabled(True)
		elif snapC_chck == False:
			snapC_prs_list[bvc].setEnabled(False)
			snapC_def_list[bvc].setEnabled(False)
			snapC_val_list[bvc].setEnabled(False)
			
	#---
	def meshQC_on_change(self, bvc):
		meshQC_chck = meshQC_chcks_list[bvc].isChecked()
		if meshQC_chck == True:
			meshQC_prs_list[bvc].setEnabled(True)
			meshQC_def_list[bvc].setEnabled(True)
			meshQC_val_list[bvc].setEnabled(True)
		elif meshQC_chck == False:
			meshQC_prs_list[bvc].setEnabled(False)
			meshQC_def_list[bvc].setEnabled(False)
			meshQC_val_list[bvc].setEnabled(False)
			
	###---------------------Сохранение вкладки initial-------------------------###	
						
	def on_initial_btnSave_clicked(self):
		global f_v, f_old, f_val_v, f_val_old, rS_v, rS_old, rS_val_v, rS_val_old, rR_v, rR_old, rR_val_v, rR_val_old
		global geometry_1_group, geometry_1_btnSave, geometry_type_list, shape_complex_lbl_list, shape_complex_numb_list, base_shape_lbl_list, base_shape_type_list, regions_lbl_list, regions_numb_list
		global layers_group, layers_btnSave, layers_prs_base_table, layers_prs_add_table
		global snapC_group, snapC_btnSave, snapC_prs_table, snapC_chcks_list, snapC_prs_list, snapC_def_list, snapC_val_list
		global meshQC_group, meshQC_btnSave, meshQC_prs_add_table, meshQC_chcks_list, meshQC_prs_list, meshQC_def_list, meshQC_val_list
		
		#------------------------------Получаем текущие значения полей вкладки initial--------------------------------------#
		if cM_edit.isChecked() == True:
			cM_v = 'true'
		else:
			cM_v = 'false'
		if s_edit.isChecked() == True:
			s_v = 'true'
		else:
			s_v = 'false'
		if aL_edit.isChecked() == True:
			aL_v = 'true'
		else:
			aL_v = 'false'
		
		mT_v = mT_edit.text()
		g_v = g_edit.value()
		f_v = f_edit.isChecked()
		f_val_v = f_val.value()
		rS_v = rS_edit.isChecked()
		rS_val_v = rS_val.value()
		rR_v = rR_edit.isChecked()
		rR_val_v = rR_val.value()
		l_v = l_edit.value()
		sL_v = sL_edit.isChecked()
		lS_v = lS_edit.isChecked()
		lF_v = lF_edit.isChecked()
		
		
		#-------------------------------Сохраняем файл сетки если создаем новый----------------------------------------------#
		
		if geometry_visible == False and castellatedMC_visible == False and snapC_visible == False and layers_visible == False and meshQC_visible == False:
			
			initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
			if os.path.exists(initial_path_file) == True:
				input = open(initial_path_file, 'rb')
				obj = pickle.load(input)
				input.close()
				
				g_old = obj['g']
				
				f_val_old = None
				f_old = obj['f']
				if f_old == True:
					f_val_old = obj['f_val']
				
				rS_val_old = None
				rS_old = obj['rS']
				if rS_old == True:
					rS_val_old = obj['rS_val']
				
				rR_val_old = None
				rR_old = obj['rR']
				if rR_old == True:
					rR_val_old = obj['rR_val']
				
				l_old = obj['l']
				
			else:
				g_old = g_v
				
				f_old = f_v
				if f_old == True:
					f_val_old = f_val_v
				else:
					f_val_old = None
				
				rS_old = rS_v
				if rS_old == True:
					rS_val_old = rS_val_v
				else:
					rS_val_old = None
				
				rR_old = rR_v
				if rR_old == True:
					rR_val_old = rR_val_v
				else:
					rR_val_old = None

				l_old = l_v
					
			if f_v == True and rS_v == True and rR_v == True:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "f_val": f_val_v, "rS": rS_v, "rS_val": rS_val_v, "rR": rR_v, "rR_val": rR_val_v, "l": l_v}
			elif f_v == False and rS_v == True and rR_v == True:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "rS": rS_v, "rS_val": rS_val_v, "rR": rR_v, "rR_val": rR_val_v, "l": l_v}
			elif f_v == False and rS_v == False and rR_v == True:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "rS": rS_v, "rR": rR_v, "rR_val": rR_val_v, "l": l_v}
			elif f_v == True and rS_v == False and rR_v == False:	
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "f_val": f_val_v, "rS": rS_v, "rR": rR_v, "l": l_v}
			elif f_v == True and rS_v == True and rR_v == False:	
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "f_val": f_val_v, "rS": rS_v, "rS_val": rS_val_v, "rR": rR_v, "l": l_v}
			elif f_v == True and rS_v == False and rR_v == True:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "f_val": f_val_v, "rS": rS_v, "rR": rR_v, "rR_val": rR_val_v, "l": l_v}
			elif f_v == False and rS_v == True and rR_v == False:	
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "rS": rS_v, "rS_val": rS_val_v, "rR": rR_v, "l": l_v}
			else:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "rS": rS_v, "rR": rR_v, "l": l_v}
			
			prj_path_dir = prj_path + '/' + mesh_name_txt
			
			if os.path.exists(prj_path_dir) == False:
				os.mkdir(prj_path_dir) 
		
			output = open(initial_path_file, 'wb')

			pickle.dump(obj, output)
			output.close()
			
		#-------------------------------Сохраняем файл сетки если пересохраняем имеющийся------------------------------------#
			
		if geometry_visible == True and castellatedMC_visible == True and snapC_visible == True and layers_visible == True and meshQC_visible == True:
			initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
			
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			
			g_old = obj['g']

			f_old = obj['f']
			if f_old == True:
				f_val_old = obj['f_val']

			rS_old = obj['rS']
			if rS_old == True:	
				rS_val_old = obj['rS_val']
				
			rR_old = obj['rR']
			if rR_old == True:	
				rR_val_old = obj['rR_val']

			l_old = obj['l']
				
			if f_v == True and rS_v == True and rR_v == True:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "f_val": f_val_v, "rS": rS_v, "rS_val": rS_val_v, "rR": rR_v, "rR_val": rR_val_v, "l": l_v}
			elif f_v == False and rS_v == True and rR_v == True:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "rS": rS_v, "rS_val": rS_val_v, "rR": rR_v, "rR_val": rR_val_v, "l": l_v}
			elif f_v == False and rS_v == False and rR_v == True:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "rS": rS_v, "rR": rR_v, "rR_val": rR_val_v, "l": l_v}
			elif f_v == True and rS_v == False and rR_v == False:	
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "f_val": f_val_v, "rS": rS_v, "rR": rR_v, "l": l_v}
			elif f_v == True and rS_v == True and rR_v == False:	
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "f_val": f_val_v, "rS": rS_v, "rS_val": rS_val_v, "rR": rR_v, "l": l_v}
			elif f_v == True and rS_v == False and rR_v == True:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "f_val": f_val_v, "rS": rS_v, "rR": rR_v, "rR_val": rR_val_v, "l": l_v}
			elif f_v == False and rS_v == True and rR_v == False:	
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "rS": rS_v, "rS_val": rS_val_v, "rR": rR_v, "l": l_v}
			else:
				obj = {"cM": cM_v, "s": s_v, "al": aL_v, "mT": mT_v, "sL_flag": sL_v, "lS_flag": lS_v, "lF_flag": lF_v, "g": g_v, "f": f_v, "rS": rS_v, "rR": rR_v, "l": l_v}
		
			output = open(initial_path_file, 'wb')

			pickle.dump(obj, output)
			output.close()
			
		#----------------------------Формируем каждую из последующих вкладок если пересохраняем имеющийся файл-------------------------#
				
		if geometry_visible == True:
			if g_v != g_old:
				
				if os.path.exists(geometry_1_path) == True: 
					os.remove(geometry_1_path)
				if os.path.exists(geometry_2_path) == True:
					os.remove(geometry_2_path)
				
				tab.removeTab(1)
			
				geometry_1_group, geometry_1_btnSave, geometry_type_list, shape_complex_lbl_list, shape_complex_numb_list, base_shape_lbl_list, base_shape_type_list, regions_lbl_list, regions_numb_list = blocks_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
				geometry_1_btnSave.clicked.connect(self.on_geometry_1_btnSave_clicked)
			
				tab.insertTab(1, geometry_1_group, "&geometry_1")
				
				for bvc in range(len(geometry_type_list)):
					self.geometry_control_chng(geometry_type_list, bvc)		
			
				tab.removeTab(2)
				geometry_2_null_lbl = QtGui.QLabel()
				tab.insertTab(2, geometry_2_null_lbl, "&geometry_2")
				tab.setTabEnabled(2, False)
				tab.removeTab(3)
				castellatedMC_1_null_lbl = QtGui.QLabel()
				tab.insertTab(3, castellatedMC_1_null_lbl, "&castellatedMC_1")
				tab.setTabEnabled(3, False)
				
		if castellatedMC_visible == True:	
			if f_v == False and f_v != f_old \
			or rS_v == False and rS_v != rS_old \
			or rR_v == False and rR_v != rR_old:
				tab.removeTab(3)
				castellatedMC_1_null_lbl = QtGui.QLabel()
				tab.insertTab(3, castellatedMC_1_null_lbl, "&castellatedMC_1")
				tab.setTabEnabled(3, False)	
				
				tab.removeTab(4)
				castellatedMC_2_null_lbl = QtGui.QLabel()
				tab.insertTab(4, castellatedMC_2_null_lbl, "&castellatedMC_2")
				tab.setTabEnabled(4, False)	
				
		if layers_visible == True:
			if l_v != l_old:
				
				if os.path.exists(layers_path) == True:
					os.remove(layers_path)
				
				layers_group, layers_btnSave, layers_prs_base_table, layers_prs_add_table = layers_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, layers_visible)
				layers_btnSave.clicked.connect(self.on_layers_btnSave_clicked)
				tab.setTabEnabled(5, True)
				tab.removeTab(5)
				tab.insertTab(5, layers_group, "&layers")
				
		#----------------------------Формируем каждую из последующих вкладок если сохраняем новый файл-------------------------#
		
		if geometry_visible == False:
			if g_v != g_old or os.path.exists(geometry_1_path) == False:
				
				if os.path.exists(geometry_1_path) == True:
					os.remove(geometry_1_path)
				if os.path.exists(geometry_2_path) == True:
					os.remove(geometry_2_path)	
				
				geometry_1_group, geometry_1_btnSave, geometry_type_list, shape_complex_lbl_list, shape_complex_numb_list, base_shape_lbl_list, base_shape_type_list, regions_lbl_list, regions_numb_list = geometry_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
				geometry_1_btnSave.clicked.connect(self.on_geometry_1_btnSave_clicked)
				
				for bvc in range(len(geometry_type_list)):
					self.geometry_control_chng(geometry_type_list, bvc)	
									
				tab.setTabEnabled(1, True)
				tab.removeTab(1)
				tab.insertTab(1, geometry_1_group, "&geometry_1")

				tab.removeTab(2)
				geometry_2_null_lbl = QtGui.QLabel()
				tab.insertTab(2, geometry_2_null_lbl, "&geometry_2")
				tab.setTabEnabled(2, False)	

				tab.removeTab(3)
				castellatedMC_1_null_lbl = QtGui.QLabel()
				tab.insertTab(3, castellatedMC_1_null_lbl, "&castellatedMC_1")
				tab.setTabEnabled(3, False)		
				
				tab.removeTab(4)
				castellatedMC_2_null_lbl = QtGui.QLabel()
				tab.insertTab(4, castellatedMC_2_null_lbl, "&castellatedMC_2")
				tab.setTabEnabled(4, False)	
		
		if castellatedMC_visible == False:	
			if f_v == False and f_v != f_old \
			or rS_v == False and rS_v != rS_old \
			or rR_v == False and rR_v != rR_old:
				tab.removeTab(3)
				castellatedMC_1_null_lbl = QtGui.QLabel()
				tab.insertTab(3, castellatedMC_1_null_lbl, "&castellatedMC_1")
				tab.setTabEnabled(3, False)	
				
		if layers_visible == False:
			if l_v != l_old or os.path.exists(layers_path) == False:
				
				if os.path.exists(layers_path) == True:
					os.remove(layers_path)
				
				layers_group, layers_btnSave, layers_prs_base_table, layers_prs_add_table = layers_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, layers_visible)
				layers_btnSave.clicked.connect(self.on_layers_btnSave_clicked)
				tab.setTabEnabled(5, True)
				tab.removeTab(5)
				tab.insertTab(5, layers_group, "&layers")
				
		if snapC_visible == False:
				
			if os.path.exists(snapC_path) == False:
				
				snapC_group, snapC_btnSave, snapC_prs_table, snapC_chcks_list, snapC_prs_list, snapC_def_list, snapC_val_list = snapC_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, snapC_visible)
				snapC_btnSave.clicked.connect(self.on_snapC_btnSave_clicked)

				for bvc in range(len(snapC_chcks_list)):
					self.snapC_control_chng(snapC_chcks_list, bvc)	

				tab.setTabEnabled(6, True)
				tab.removeTab(6)
				tab.insertTab(6, snapC_group, "&snapC")
				
		if meshQC_visible == False:
				
			if os.path.exists(meshQC_path) == False:

				meshQC_group, meshQC_btnSave, meshQC_prs_add_table, meshQC_chcks_list, meshQC_prs_list, meshQC_def_list, meshQC_val_list = meshQC_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, meshQC_visible)
				meshQC_btnSave.clicked.connect(self.on_meshQC_btnSave_clicked)

				for bvc in range(len(meshQC_chcks_list)):
					self.meshQC_control_chng(meshQC_chcks_list, bvc)	

				tab.setTabEnabled(7, True)
				tab.removeTab(7)
				tab.insertTab(7, meshQC_group, "&meshQC")
		
		msg_list = []
		if mT_v == '':
			if int_lng == 'Russian':
				msg = "Укажите параметр объединения допусков в виде части граничной рамки исходной сетки"
			elif int_lng == 'English':
				msg = "Specify the tolerance combining parameter as part of the bounding box of the source mesh"
			msg_list.append(msg)
			self.on_msg_error(msg_list)
		else:
			if geometry_visible == False and castellatedMC_visible == False and snapC_visible == False and layers_visible == False and meshQC_visible == False:
				if os.path.exists(prj_path_dir) == False:
					os.mkdir(prj_path_dir) 
		
			output = open(initial_path_file, 'wb')

			pickle.dump(obj, output)
			output.close()

			if int_lng == 'Russian':
				msg = "Начальные данные успешно сохранены"
			elif int_lng == 'English':
				msg = "Initial data saved successfully"
			msg_list.append(msg)
			self.on_msg_correct(msg)
		
	###---------------------Сохранение вкладки geometry_1-------------------------###
	
	def on_geometry_1_btnSave_clicked(self):
		global geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list
		
		global geometry_txt_old_mas
		global regions_numb_val_old_mas
		global base_shape_type_old_mas
		global shape_complex_numb_val_old_mas

		obj_list = []
		i = 1
		j = 0
		for el_m in geometry_type_list:
			if el_m.currentText() == 'Набор базовых фигур' or el_m.currentText() == 'Base shape complex':
				obj = {'geometry_' + str(i): el_m.currentText(), 'shapes_number_' + str(i): shape_complex_numb_list[j].value()}
			elif el_m.currentText() == 'Три-поверхность' or el_m.currentText() == 'Tri-surface' or el_m.currentText() == 'Распределенная три-поверхность' or el_m.currentText() == 'Distributed tri-surface':
				obj = {'geometry_' + str(i): el_m.currentText(), 'regions_number_' + str(i): regions_numb_list[j].value()}
			elif el_m.currentText() == 'Базовая фигура' or el_m.currentText() == 'Base shape':
				obj = {'geometry_' + str(i): el_m.currentText(), 'shape_type_' + str(i): base_shape_type_list[j].currentText()}
			obj_list.append(obj)
				
			i = i + 1
			j = j + 1
	
		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_1.pkl', 'wb')
		pickle.dump(obj_list, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные geometry_1 успешно сохранены"
		elif int_lng == 'English':
			msg = "The geometry_1 data was successfully saved"
		self.on_msg_correct(msg)
		
		if geometry_visible == False:
			if os.path.exists(geometry_2_path) == True:
				os.remove(geometry_2_path)

			geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list = geometry_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
			geometry_2_btnSave.clicked.connect(self.on_geometry_2_btnSave_clicked)
			
			for bvc in range(len(all_tri_file_btn_list)):
				if all_tri_file_btn_list[bvc] != '':
					self.tri_file_chng(all_tri_file_btn_list, bvc)	
			
			tab.setTabEnabled(2, True)
			tab.removeTab(2)
			tab.insertTab(2, geometry_2_group, "&geometry_2")
			
		if geometry_visible == True:
			geometry_txt_new_mas = []
			regions_numb_val_new_mas = []
			base_shape_type_new_mas = []
			shape_complex_numb_val_new_mas = []
			
			for bvc in range(len(geometry_type_list)):
				geometry_txt_new = geometry_type_list[bvc].currentText()
				geometry_txt_new_mas.append(geometry_txt_new)
				
			for bvc in range(len(regions_numb_list)):
				regions_numb_val_new = regions_numb_list[bvc].value()
				regions_numb_val_new_mas.append(regions_numb_val_new)
				
			for bvc in range(len(base_shape_type_list)):
				base_shape_type_new = base_shape_type_list[bvc].currentText()
				base_shape_type_new_mas.append(base_shape_type_new)
				
			for bvc in range(len(shape_complex_numb_list)):
				shape_complex_numb_val_new = shape_complex_numb_list[bvc].value()
				shape_complex_numb_val_new_mas.append(shape_complex_numb_val_new)
			
			if geometry_txt_old_mas != geometry_txt_new_mas or shape_complex_numb_val_old_mas != shape_complex_numb_val_new_mas \
			or regions_numb_val_old_mas != regions_numb_val_new_mas or base_shape_type_old_mas != base_shape_type_new_mas \
			or os.path.exists(geometry_2_path) == False:
				if os.path.exists(geometry_2_path) == True:
					os.remove(geometry_2_path)
				geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list = geometry_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible)
				geometry_2_btnSave.clicked.connect(self.on_geometry_2_btnSave_clicked)
				
				for bvc in range(len(all_tri_file_btn_list)):
					if all_tri_file_btn_list[bvc] != '':
						self.tri_file_chng(all_tri_file_btn_list, bvc)	
				
				tab.setTabEnabled(2, True)
				tab.removeTab(2)
				tab.insertTab(2, geometry_2_group, "&geometry_2")

			geometry_txt_old_mas = geometry_txt_new_mas
			shape_complex_numb_val_old_mas = shape_complex_numb_val_new_mas
			regions_numb_val_old_mas = regions_numb_val_new_mas
			base_shape_type_old_mas = base_shape_type_new_mas
			
###---------------------Сохранение вкладки geometry_2-------------------------###		
		
	def on_geometry_2_btnSave_clicked(self):
		global castellatedMC_1_group, castellatedMC_1_btnSave, prs_grid, tri_distirbTri_list, other_geometry_list, f_level_single_edit_list, f_level_multi_edit_list, f_level_multi_val_edit_list, rS_regions_edit_list, rS_regions_val_edit_list, rR_level_single_edit_list, rR_level_multi_edit_list, rR_level_multi_val_edit_list
		obj_list = []

		n = 1
		t = 0
		
		msg_list = []
		for el_m in all_geometry_list:	
			##################################complex_list#####################################
			
			if all_geometry_list_lbls[t] == 'complex_list':
				
				complex_table_list_strok_itog = []
				
				b = 0
				for el_cl in all_complex_list_lbls[t]:
					if el_cl == 'complex_name_edit':
						complex_name_val = el_m[b].text()
						if complex_name_val == '':
							if int_lng == 'Russian':
								msg = "Укажите название набора фигур " + str(n)
							elif int_lng == 'English':
								msg = "Specify the name of the set of shapes " + str(n)
							msg_list.append(msg)
						else:
							complex_table_list_strok_itog.append(complex_name_val)
					elif el_cl == 'complex_type_edit':
						complex_type_val = el_m[b].currentText()
						complex_table_list_strok_itog.append(complex_type_val)
					elif el_cl == 'complex_msr_edit':
						complex_msr_val = el_m[b].currentText()
						complex_table_list_strok_itog.append(complex_msr_val)
					elif el_cl == 'complex_shape_table':
						complex_table = el_m[b]
						ctn = complex_table.rowCount()
						
						k = 1
						p = 1
						y = 0
						
						complex_table_list_strok = []
						
						while p <= ctn:
							complex_table_stroka = []
							#shape
							shape_val = el_m[b].cellWidget(y, 0).text()
							if shape_val == '':
								if int_lng == 'Russian':
									msg = "Укажите значение поля 'Название' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the value of the field 'shape' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								complex_table_stroka.append(shape_val)
							#surface
							surface_val = el_m[b].cellWidget(y, 1).currentText()
							complex_table_stroka.append(surface_val)
							#scale							
							scale_val = []
							scale_hbox = el_m[b].cellWidget(y, 2).layout()
							scale_x = scale_hbox.itemAt(1).widget().text()
							if scale_x == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'x' поля 'Масштабирование' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'x' parameter of the field 'scale' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								scale_val.append(scale_x)
							scale_y = scale_hbox.itemAt(3).widget().text()
							if scale_y == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'y' поля 'Масштабирование' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'y' parameter of the field 'scale' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								scale_val.append(scale_y)
							scale_z = scale_hbox.itemAt(5).widget().text()
							if scale_z == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'z' поля 'Масштабирование' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'z' parameter of the field 'scale' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								scale_val.append(scale_z)
							if len(scale_val) == 3:
								complex_table_stroka.append(scale_val)
							#type														
							type_val = el_m[b].cellWidget(y, 3).currentText()
							complex_table_stroka.append(type_val)
							#origin							
							origin_val = []
							origin_hbox = el_m[b].cellWidget(y, 4).layout()
							origin_x = origin_hbox.itemAt(1).widget().text()							
							if origin_x == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'x' поля 'Происхождение' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'x' parameter of the field 'origin' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								origin_val.append(origin_x)
							origin_y = origin_hbox.itemAt(3).widget().text()
							if origin_y == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'y' поля 'Происхождение' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'y' parameter of the field 'origin' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								origin_val.append(origin_y)
							origin_z = origin_hbox.itemAt(5).widget().text()
							if origin_z == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'z' поля 'Происхождение' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'z' parameter of the field 'origin' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								origin_val.append(origin_z)
							if len(origin_val) == 3:
								complex_table_stroka.append(origin_val)																		
							#e1
							e1_val = []
							e1_hbox = el_m[b].cellWidget(y, 5).layout()
							e1_x = e1_hbox.itemAt(1).widget().text()	
							if e1_x == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'x' поля 'Параметр e1' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'x' parameter of the field 'e1' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								e1_val.append(e1_x)
							e1_y = e1_hbox.itemAt(3).widget().text()
							if e1_y == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'y' поля 'Параметр e1' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'y' parameter of the field 'e1' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								e1_val.append(e1_y)
							e1_z = e1_hbox.itemAt(5).widget().text()
							if e1_z == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'z' поля 'Параметр e1' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'z' parameter of the field 'e1' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								e1_val.append(e1_z)
							if len(e1_val) == 3:
								complex_table_stroka.append(e1_val)
							#e3							
							e3_val = []
							e3_hbox = el_m[b].cellWidget(y, 6).layout()
							e3_x = e3_hbox.itemAt(1).widget().text()															
							if e3_x == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'x' поля 'Параметр e3' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'x' parameter of the field 'e3' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								e3_val.append(e3_x)
							e3_y = e3_hbox.itemAt(3).widget().text()
							if e3_y == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'y' поля 'Параметр e3' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'y' parameter of the field 'e3' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								e3_val.append(e3_y)
							e3_z = e3_hbox.itemAt(5).widget().text()
							if e3_z == '':
								if int_lng == 'Russian':
									msg = "Укажите параметр 'z' поля 'Параметр e3' фигуры " + str(k) + " геометрии " + str(n)
								elif int_lng == 'English':
									msg = "Specify the 'z' parameter of the field 'e3' of shape " + str(k) + " of geometry " + str(n)
								msg_list.append(msg)
							else:
								e3_val.append(e3_z)
							if len(e3_val) == 3:
								complex_table_stroka.append(e3_val)
							
							if len(complex_table_stroka) == 7:
								complex_table_list_strok.append(complex_table_stroka)
								
							k = k + 1
							p = p + 1
							y = y + 1
							
						if len(complex_table_list_strok) == ctn:
							complex_table_list_strok_itog.append(complex_table_list_strok)
					b = b + 1	
						
						
				if len(complex_table_list_strok_itog) == 4:		
					obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'name': complex_name_val, 'type': complex_type_val, 'mergeSubRegions': complex_msr_val, 'parameters': complex_table_list_strok}
					obj_list.append(obj)
				
			###############################################tri_table#########################################################
			if all_geometry_list_lbls[t] == 'tri_table':

				tri_table_stroka = []
				
				#file
				file_val = el_m.cellWidget(0, 0).layout().itemAt(0).widget().text()
					
				if file_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Файл' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'file' of geometry " + str(n)
					msg_list.append(msg)
				else:
					tri_table_stroka.append(file_val)
				#type
				type_val = el_m.cellWidget(0, 1).layout().itemAt(0).widget().currentText()
				tri_table_stroka.append(type_val)
				#name
				name_val = el_m.cellWidget(0, 2).layout().itemAt(0).widget().text()
				if name_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Название' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'name' of geometry " + str(n)
					msg_list.append(msg)
				else:
					tri_table_stroka.append(name_val)
				#regions
				cC = el_m.columnCount()
				a = 3
				f = 4
				z = 1
				one_region_list = []
				while f <= cC:
					region_list = []
					STL_region_name = el_m.cellWidget(0, a).layout().itemAtPosition(0,1).widget().text()
					user_region_name = el_m.cellWidget(0, a).layout().itemAtPosition(1,1).widget().text()

					if STL_region_name == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля STL-имя " + "подобласти " + str(z) + " геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Define the value of field STL-name " + "of the region " + str(z) + " of geometry " + str(n)
						msg_list.append(msg)
					else:
						region_list.append(STL_region_name)
					if user_region_name == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля Usr-имя " + "подобласти " + str(z) + " геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Define the value of field Usr-name " + "of the region " + str(z) + " of geometry " + str(n)
						msg_list.append(msg)
					else:
						region_list.append(user_region_name)
					if len(region_list) == 2:
						one_region_obj = {'region_' + str(z): region_list}
						one_region_list.append(one_region_obj)
					a = a + 1
					z = z + 1
					f = f + 1

				if len(tri_table_stroka) == 3 and len(one_region_list) == cC-3:
					obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'file': file_val, 'type': type_val, 'name': name_val, 'regions': one_region_list}
					obj_list.append(obj)
			
			###############################################distrib_tri_table##################################################
			if all_geometry_list_lbls[t] == 'distrib_tri_table':
				
				distrib_tri_table_stroka = []
				
				#file
				file_val = el_m.cellWidget(0, 0).layout().itemAt(0).widget().text()
				if file_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Файл' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'file' of geometry " + str(n)
					msg_list.append(msg)
				else:
					distrib_tri_table_stroka.append(file_val)
				#type
				type_val = el_m.cellWidget(0, 1).layout().itemAt(0).widget().currentText()
				distrib_tri_table_stroka.append(type_val)
				#distributionType
				distributionType_val = el_m.cellWidget(0, 2).layout().itemAt(0).widget().currentText()
				distrib_tri_table_stroka.append(distributionType_val)
				#name
				name_val = el_m.cellWidget(0, 3).layout().itemAt(0).widget().text()
				if name_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Название' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'name' of geometry " + str(n)
					msg_list.append(msg)
				else:
					distrib_tri_table_stroka.append(name_val)
					
				#regions
				cC = el_m.columnCount()
				a = 4
				f = 5
				z = 1
				one_region_list = []
				while f <= cC:
					region_list = []
					STL_region_name = el_m.cellWidget(0, a).layout().itemAtPosition(0,1).widget().text()
					user_region_name = el_m.cellWidget(0, a).layout().itemAtPosition(1,1).widget().text()

					if STL_region_name == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля STL-имя " + "подобласти " + str(z) + " геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Define the value of field STL-name " + "of the region " + str(z) + " of geometry " + str(n)
						msg_list.append(msg)
					else:
						region_list.append(STL_region_name)
					if user_region_name == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля Usr-имя " + "подобласти " + str(z) + " геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Define the value of field Usr-name " + "of the region " + str(z) + " of geometry " + str(n)
						msg_list.append(msg)
					else:
						region_list.append(user_region_name)
					if len(region_list) == 2:
						one_region_obj = {'region_' + str(z): region_list}
						one_region_list.append(one_region_obj)
					a = a + 1
					z = z + 1
					f = f + 1
					
				if len(distrib_tri_table_stroka) == 4 and len(one_region_list) == cC-4:
					obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'file': file_val, 'type': type_val, 'distributionType': distributionType_val, 'name': name_val, 'regions': one_region_list}
					obj_list.append(obj)
			
			###############################################box_table##################################################
			if all_geometry_list_lbls[t] == 'box_table':
				
				btn = el_m.rowCount()

				p = 1
				y = 0
				box_table_stroka = []
				while p <= btn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						box_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					box_table_stroka.append(type_val)
					#min
					min_val = []
					min_hbox = el_m.cellWidget(y, 2).layout()
					min_x = min_hbox.itemAt(1).widget().text()
					if min_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Мин' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'min' of geometry " + str(n)
						msg_list.append(msg)
					else:
						min_val.append(min_x)
					min_y = min_hbox.itemAt(3).widget().text()
					if min_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Мин' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'min' of geometry " + str(n)
						msg_list.append(msg)
					else:
						min_val.append(min_y)
					min_z = min_hbox.itemAt(5).widget().text()
					if min_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Мин' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'min' of geometry " + str(n)
						msg_list.append(msg)
					else:
						min_val.append(min_z)
					if len(min_val) == 3:
						box_table_stroka.append(min_val)
					
					#max
					max_val = []
					max_hbox = el_m.cellWidget(y, 3).layout()
					max_x = max_hbox.itemAt(1).widget().text()
					if max_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Макс' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'max' of geometry " + str(n)
						msg_list.append(msg)
					else:
						max_val.append(max_x)
					max_y = max_hbox.itemAt(3).widget().text()
					if max_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Макс' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'max' of geometry " + str(n)
						msg_list.append(msg)
					else:
						max_val.append(max_y)
					max_z = max_hbox.itemAt(5).widget().text()
					if max_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Макс' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'max' of geometry " + str(n)
						msg_list.append(msg)
					else:
						max_val.append(max_z)
					if len(max_val) == 3:
						box_table_stroka.append(max_val)
					
					p = p + 1
					y = y + 1
					
					if len(box_table_stroka) == 4:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'min': min_val, 'max': max_val}
						obj_list.append(obj)
			
			###############################################sphere_table##################################################
			if all_geometry_list_lbls[t] == 'sphere_table':
				
				stn = el_m.rowCount()

				p = 1
				y = 0
				sphere_table_stroka = []
				while p <= stn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						sphere_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					sphere_table_stroka.append(type_val)
					#centre					
					centre_val = []					
					centre_hbox = el_m.cellWidget(y, 2).layout()
					centre_x = centre_hbox.itemAt(1).widget().text()				
					if centre_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Центр' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'centre' of geometry " + str(n)
						msg_list.append(msg)
					else:
						centre_val.append(centre_x)
					centre_y = centre_hbox.itemAt(3).widget().text()	
					if centre_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Центр' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'centre' of geometry " + str(n)
						msg_list.append(msg)
					else:
						centre_val.append(centre_y)
					centre_z = centre_hbox.itemAt(5).widget().text()	
					if centre_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Центр' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'centre' of geometry " + str(n)
						msg_list.append(msg)
					else:
						centre_val.append(centre_z)
					if len(centre_val) == 3:
						sphere_table_stroka.append(centre_val)
					
					#radius
					radius_val = el_m.cellWidget(y, 3).text()
					if radius_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Радиус' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of the field 'radius' of geometry " + str(n)
						msg_list.append(msg)
					else:
						sphere_table_stroka.append(radius_val)
										
					p = p + 1
					y = y + 1
					
					if len(sphere_table_stroka) == 4:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'centre': centre_val, 'radius': radius_val}
						obj_list.append(obj)
			
			###############################################cylinder_table##################################################
			if all_geometry_list_lbls[t] == 'cylinder_table':
				
				ctn = el_m.rowCount()

				p = 1
				y = 0
				cylinder_table_stroka = []
				while p <= ctn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						cylinder_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					cylinder_table_stroka.append(type_val)
					#point1					
					point1_val = []					
					point1_hbox = el_m.cellWidget(y, 2).layout()
					point1_x = point1_hbox.itemAt(1).widget().text()					
					if point1_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Точка_1' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'point1' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point1_val.append(point1_x)
					point1_y = point1_hbox.itemAt(3).widget().text()	
					if point1_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Точка_1' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'point1' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point1_val.append(point1_y)
					point1_z = point1_hbox.itemAt(5).widget().text()	
					if point1_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Точка_1' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'point1' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point1_val.append(point1_z)
					if len(point1_val) == 3:
						cylinder_table_stroka.append(point1_val)
					#point2
					point2_val = []					
					point2_hbox = el_m.cellWidget(y, 3).layout()
					point2_x = point2_hbox.itemAt(1).widget().text()	
					if point2_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Точка_2' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'point2' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point2_val.append(point2_x)
					point2_y = point2_hbox.itemAt(3).widget().text()
					if point2_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Точка_2' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'point2' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point2_val.append(point2_y)
					point2_z = point2_hbox.itemAt(5).widget().text()
					if point2_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Точка_2' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'point2' of geometry " + str(n)
						msg_list.append(msg)
					else:
						point2_val.append(point2_z)
					
					if len(point2_val) == 3:
						cylinder_table_stroka.append(point2_val)
					
					#radius
					radius_val = el_m.cellWidget(y, 4).value()
					cylinder_table_stroka.append(radius_val)
					if radius_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Радиус' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of the field 'Radius' of geometry " + str(n)
						msg_list.append(msg)
					else:
						cylinder_table_stroka.append(radius_val)
																				
					p = p + 1
					y = y + 1
					
					if len(cylinder_table_stroka) == 5:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'point1': point1_val, 'point2': point1_val, 'radius': radius_val}
						obj_list.append(obj)

			###############################################plane_table##################################################		
			if all_geometry_list_lbls[t] == 'plane_table':
				
				ptn = el_m.rowCount()

				p = 1
				y = 0
				plane_table_stroka = []
				while p <= ptn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						plane_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					plane_table_stroka.append(type_val)
					#planeType
					planeType_val = el_m.cellWidget(y, 2).currentText()
					plane_table_stroka.append(planeType_val)
					#basePoint
					basePoint_val = []					
					basePoint_hbox = el_m.cellWidget(y, 3).layout()
					basePoint_x = basePoint_hbox.itemAt(1).widget().text()	
					if basePoint_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Базовая точка' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'basePoint' of geometry " + str(n)
						msg_list.append(msg)
					else:
						basePoint_val.append(basePoint_x)
					basePoint_y = basePoint_hbox.itemAt(3).widget().text()	
					if basePoint_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Базовая точка' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'basePoint' of geometry " + str(n)
						msg_list.append(msg)
					else:
						basePoint_val.append(basePoint_y)
					basePoint_z = basePoint_hbox.itemAt(5).widget().text()	
					if basePoint_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Базовая точка' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'basePoint' of geometry " + str(n)
						msg_list.append(msg)
					else:
						basePoint_val.append(basePoint_z)
						
					if len(basePoint_val) == 3:
						plane_table_stroka.append(basePoint_val)
					
					#normalVector					
					normalVector_val = []					
					normalVector_hbox = el_m.cellWidget(y, 4).layout()
					normalVector_x = basePoint_hbox.itemAt(1).widget().text()	
					if normalVector_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Вектор нормали' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'normalVector' of geometry " + str(n)
						msg_list.append(msg)
					else:
						normalVector_val.append(normalVector_x)
					normalVector_y = basePoint_hbox.itemAt(3).widget().text()	
					if normalVector_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Вектор нормали' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'normalVector' of geometry " + str(n)
						msg_list.append(msg)
					else:
						normalVector_val.append(normalVector_y)
					normalVector_z = basePoint_hbox.itemAt(5).widget().text()	
					if normalVector_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Вектор нормали' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'normalVector' of geometry " + str(n)
						msg_list.append(msg)
					else:
						normalVector_val.append(normalVector_z)
						
					if len(basePoint_val) == 3:
						plane_table_stroka.append(normalVector_val)
														
					p = p + 1
					y = y + 1
					
					if len(plane_table_stroka) == 5:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'planeType': planeType_val, 'basePoint': basePoint_val, 'normalVector': normalVector_val}
						obj_list.append(obj)
			
			###############################################plate_table##################################################		
			if all_geometry_list_lbls[t] == 'plate_table':
				
				ptn = el_m.rowCount()

				p = 1
				y = 0
				plate_table_stroka = []
				while p <= ptn:
					#shape
					shape_val = el_m.cellWidget(y, 0).text()
					if shape_val == '':
						if int_lng == 'Russian':
							msg = "Укажите значение поля 'Название' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the value of field 'shape' of geometry " + str(n)
						msg_list.append(msg)
					else:
						plate_table_stroka.append(shape_val)
					#type
					type_val = el_m.cellWidget(y, 1).currentText()
					plate_table_stroka.append(type_val)
					#origin					
					origin_val = []					
					origin_hbox = el_m.cellWidget(y, 2).layout()
					origin_x = origin_hbox.itemAt(1).widget().text()						
					if origin_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Происхождение' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'origin' of geometry " + str(n)
						msg_list.append(msg)
					else:
						origin_val.append(origin_x)
					origin_y = origin_hbox.itemAt(3).widget().text()
					if origin_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Происхождение' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'origin' of geometry " + str(n)
						msg_list.append(msg)
					else:
						origin_val.append(origin_x)
					origin_z = origin_hbox.itemAt(5).widget().text()
					if origin_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Происхождение' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'origin' of geometry " + str(n)
						msg_list.append(msg)
					else:
						origin_val.append(origin_z)
					
					if len(origin_val) == 3:
						plate_table_stroka.append(origin_val)
					#span
					span_val = []					
					span_hbox = el_m.cellWidget(y, 3).layout()
					span_x = span_hbox.itemAt(1).widget().text()		
					if span_x == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'x' поля 'Пролет' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'x' parameter of the field 'span' of geometry " + str(n)
						msg_list.append(msg)
					else:
						span_val.append(span_x)
					
					span_y = span_hbox.itemAt(3).widget().text()
					if span_y == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'y' поля 'Пролет' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'y' parameter of the field 'span' of geometry " + str(n)
						msg_list.append(msg)
					else:
						span_val.append(span_y)
					span_z = span_hbox.itemAt(5).widget().text()
					if span_z == '':
						if int_lng == 'Russian':
							msg = "Укажите параметр 'z' поля 'Пролет' геометрии " + str(n)
						elif int_lng == 'English':
							msg = "Specify the 'z' parameter of the field 'span' of geometry " + str(n)
						msg_list.append(msg)
					else:
						span_val.append(span_z)
					
					if len(span_val) == 3:
						plate_table_stroka.append(span_val)					
					
					p = p + 1
					y = y + 1
					
					if len(plate_table_stroka) == 4:
						obj = {'geometry_' + str(n): geometry_type_list[t].currentText(), 'shape': shape_val, 'type': type_val, 'origin': origin_val, 'span': span_val}
						obj_list.append(obj)
				
			n = n + 1	
			t = t + 1
				
		self.on_msg_error(msg_list)	
		
		#####---------------------Итоговое сохранение geometry_2-------------------------#####
		
		if len(all_geometry_list) == len(obj_list):
			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl', 'wb')
			pickle.dump(obj_list, output)
			output.close()	
				
			if int_lng == 'Russian':
				msg = "Данные 'geometry_2' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'geometry_2' data was successfully saved"

			self.on_msg_correct(msg)	

			if castellatedMC_visible == False or castellatedMC_visible == True:
				if f_v == True and f_v != f_old or f_v == True and os.path.exists(castellatedMC_1_path) == False or f_v == True and f_v == f_old and f_val_v != f_val_old \
				or rS_v == True and rS_v != rS_old or rS_v == True and os.path.exists(castellatedMC_1_path) == False or rS_v == True and rS_v == rS_old and rS_val_v != rS_val_old \
				or rR_v == True and rR_v != rR_old or rR_v == True and os.path.exists(castellatedMC_1_path) == False or rR_v == True and rR_v == rR_old and rR_val_v != rR_val_old \
				or f_v == False and rS_v == False and rR_v == False:
				
					if os.path.exists(castellatedMC_1_path) == True:
						os.remove(castellatedMC_1_path)

					castellatedMC_1_group, castellatedMC_1_btnSave, prs_grid, tri_distirbTri_list, other_geometry_list, f_level_single_edit_list, f_level_multi_edit_list, f_level_multi_val_edit_list, rS_regions_edit_list, rS_regions_val_edit_list, rR_level_single_edit_list, rR_level_multi_edit_list, rR_level_multi_val_edit_list = castellatedMC_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, castellatedMC_visible)
					castellatedMC_1_btnSave.clicked.connect(self.on_castellatedMC_1_btnSave_clicked)
					
					if f_v == True and True in tri_distirbTri_list:	
						cMC_f_lbl = prs_grid.itemAtPosition(1,0).widget()
						cMC_f_lbl.setVisible(True)
						cMC_features_table = prs_grid.itemAtPosition(2,0).widget()
						cMC_features_table.setVisible(True)
							
						for bvc in range(len(f_level_single_edit_list)):
							self.f_single_level_chng(f_level_single_edit_list, f_level_multi_val_edit_list, bvc)	
							
						for bvc in range(len(f_level_multi_edit_list)):
							self.f_multi_level_chng(f_level_multi_edit_list, f_level_multi_val_edit_list, bvc)	
					
						cMC_sFED_lbl = prs_grid.itemAtPosition(3,0).widget()
						cMC_sFED_lbl.setVisible(True)
						cMC_sFED_table = prs_grid.itemAtPosition(4,0).widget()
						cMC_sFED_table.setVisible(True)
					if rS_v == True and True in tri_distirbTri_list:
						cMC_rS_lbl = prs_grid.itemAtPosition(5,0).widget()
						cMC_rS_lbl.setVisible(True)
	
						cMC_refinementSurfaces_table = prs_grid.itemAtPosition(6,0).widget()
						cMC_refinementSurfaces_table.setVisible(True)
							
						for bvc in range(len(rS_regions_edit_list)):
							self.rS_regions_chng(rS_regions_edit_list, rS_regions_val_edit_list, bvc)
					if rR_v == True and True in other_geometry_list:
						cMC_rR_lbl = prs_grid.itemAtPosition(7,0).widget()
						cMC_rR_lbl.setVisible(True)
						
						cMC_refinementRegions_table = prs_grid.itemAtPosition(8,0).widget()
						cMC_refinementRegions_table.setVisible(True)
						
						for bvc in range(len(rR_level_single_edit_list)):
							self.rR_single_level_chng(rR_level_single_edit_list, rR_level_multi_val_edit_list, bvc)	
							
						for bvc in range(len(rR_level_multi_edit_list)):
							self.rR_multi_level_chng(rR_level_multi_edit_list, rR_level_multi_val_edit_list, bvc)	
									
					tab.setTabEnabled(3, True)
					tab.removeTab(3)
					tab.insertTab(3, castellatedMC_1_group, "&castellatedMC_1")
				
	###---------------------Сохранение вкладки castellatedMC_1-------------------------###		
		
	def on_castellatedMC_1_btnSave_clicked(self):
		global castellatedMC_2_group, castellatedMC_2_btnSave, prs_lvl_grid, f_level_single_list, rR_level_single_list, el_CMC_rS_regions_list
		global f_level_single_edit_old_mas, f_level_multi_edit_old_mas, f_level_multi_val_edit_old_mas, rS_regions_edit_old_mas, rS_regions_val_edit_old_mas, rR_level_single_edit_old_mas, rR_level_multi_edit_old_mas, rR_level_multi_val_edit_old_mas 
		
		cMC_obj = {}
		
		cMC_start_prs_grid = prs_grid.itemAtPosition(0,0).layout()
		
		mGC_edit = cMC_start_prs_grid.itemAtPosition(0,1).widget()
		mLC_edit = cMC_start_prs_grid.itemAtPosition(1,1).widget()
		mRC_edit = cMC_start_prs_grid.itemAtPosition(2,1).widget()
		nCBL_edit = cMC_start_prs_grid.itemAtPosition(3,1).widget()
		rFA_edit = cMC_start_prs_grid.itemAtPosition(4,1).widget()
		aFSZF_edit = cMC_start_prs_grid.itemAtPosition(5,1).widget()
		
		lIM_edit_x = cMC_start_prs_grid.itemAtPosition(6,1).widget()
		lIM_edit_y = cMC_start_prs_grid.itemAtPosition(6,2).widget()
		lIM_edit_z = cMC_start_prs_grid.itemAtPosition(6,3).widget()
		
		msg_list = []
		lIM_list = []
		if lIM_edit_x.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите параметр 'x' вектора locationInMesh"
			elif int_lng == 'English':
				msg = "Specify the 'x' parameter of vector locationInMesh"
			msg_list.append(msg)
		else:
			lIM_list.append(lIM_edit_x.text())
		if lIM_edit_y.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите параметр 'y' вектора locationInMesh"
			elif int_lng == 'English':
				msg = "Specify the 'y' parameter of vector locationInMesh"
			msg_list.append(msg)
		else:
			lIM_list.append(lIM_edit_y.text())
		if lIM_edit_z.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите параметр 'z' вектора locationInMesh"
			elif int_lng == 'English':
				msg = "Specify the 'z' parameter of vector locationInMesh"
			msg_list.append(msg)
		else:
			lIM_list.append(lIM_edit_z.text())
		
		self.on_msg_error(msg_list)	
		if len(lIM_list) == 3:
			obj_cMC_start_prs_obj = {'mGC': mGC_edit.value(), 'mLC': mLC_edit.value(), 'mRC': mRC_edit.value(), 'nCBL': nCBL_edit.value(), 'rFA': rFA_edit.value(), 'aFSZF': aFSZF_edit.currentText(), 'lIM': lIM_list}
			cMC_obj['cMC_start_prs'] = obj_cMC_start_prs_obj

		if f_v == True and True in tri_distirbTri_list:	
			cMC_features_table = prs_grid.itemAtPosition(2,0).widget()
			cMC_sFED_table = prs_grid.itemAtPosition(4,0).widget()
		if rS_v == True and True in tri_distirbTri_list:
			cMC_refinementSurfaces_table = prs_grid.itemAtPosition(6,0).widget()
		if rR_v == True and True in other_geometry_list:
			cMC_refinementRegions_table = prs_grid.itemAtPosition(8,0).widget()
		
		if f_v == True and True in tri_distirbTri_list:	
			###Записываем features!!!###
			f = 0
			f_geometry_edit_list = []
			cMC_features_obj_list = []
			for el_feature in range(cMC_features_table.rowCount()):
				f_geometry_edit = cMC_features_table.cellWidget(f, 0).layout().itemAt(0).widget()
				f_geometry_edit_list.append(f_geometry_edit)

				if f_level_single_edit_list[f].isChecked() == True:
					cMC_features_obj = {'f_geometry': f_geometry_edit_list[f].currentText(), 'f_level_single': f_level_single_edit_list[f].isChecked(), 'f_level_multi': f_level_multi_edit_list[f].isChecked()}
				elif f_level_multi_edit_list[f].isChecked() == True:
					cMC_features_obj = {'f_geometry': f_geometry_edit_list[f].currentText(), 'f_level_single': f_level_single_edit_list[f].isChecked(), 'f_level_multi': f_level_multi_edit_list[f].isChecked(), 'f_level_multi_val': f_level_multi_val_edit_list[f].value()}
				cMC_features_obj_list.append(cMC_features_obj)

				f = f + 1
			cMC_obj['features'] = cMC_features_obj_list
			
			###Записываем sFED!!!###
			sFED = 0
			sFED_geometry_edit_list = []
			sFED_extractionMethod_edit_list = []
			sFED_includedAngle_edit_list = []
			sFED_writeObj_edit_list = []
			cMC_sFED_obj_list = []
			for el_sFED in range(cMC_sFED_table.rowCount()):
				sFED_geometry_edit = cMC_sFED_table.cellWidget(sFED, 0).layout().itemAt(0).widget()
				sFED_geometry_edit_list.append(sFED_geometry_edit)
				sFED_extractionMethod_edit = cMC_sFED_table.cellWidget(sFED, 1).layout().itemAt(0).widget()
				sFED_extractionMethod_edit_list.append(sFED_extractionMethod_edit)
				sFED_includedAngle_edit = cMC_sFED_table.cellWidget(sFED, 2).layout().itemAt(0).widget()
				sFED_includedAngle_edit_list.append(sFED_includedAngle_edit)
				sFED_writeObj_edit = cMC_sFED_table.cellWidget(sFED, 3).layout().itemAt(0).widget()
				sFED_writeObj_edit_list.append(sFED_writeObj_edit)

				cMC_sFED_obj = {'sFED_geometry': sFED_geometry_edit_list[sFED].currentText(), 'sFED_extractionMethod': sFED_extractionMethod_edit_list[sFED].currentText(), 'sFED_includedAngle': sFED_includedAngle_edit_list[sFED].value(), 'sFED_writeObj': sFED_writeObj_edit_list[sFED].currentText()}
				cMC_sFED_obj_list.append(cMC_sFED_obj)

				sFED = sFED + 1
			cMC_obj['sFED']	= cMC_sFED_obj_list

		else:
			cMC_obj['features'] = False
			cMC_obj['sFED']	= False
		
		if rS_v == True and True in tri_distirbTri_list:
			###Записываем refinementSurfaces###
			rS = 0
			rS_surface_edit_list = []
			rS_level_min_list = []
			rS_level_max_list = []
			
			cMC_rS_obj_list = []
			for el_rS in range(cMC_refinementSurfaces_table.rowCount()):
				rS_surface_edit = cMC_refinementSurfaces_table.cellWidget(rS, 0).layout().itemAt(0).widget()
				rS_surface_edit_list.append(rS_surface_edit)
				rS_level_min = cMC_refinementSurfaces_table.cellWidget(rS, 1).layout().itemAt(1).widget()
				rS_level_min_list.append(rS_level_min)
				rS_level_max = cMC_refinementSurfaces_table.cellWidget(rS, 1).layout().itemAt(3).widget()
				rS_level_max_list.append(rS_level_max)
				
				if rS_regions_edit_list[rS].isChecked() == True:
					cMC_rS_obj = {'rS_surface': rS_surface_edit_list[rS].currentText(), 'rS_level_min': rS_level_min_list[rS].value(), 'rS_level_max': rS_level_max_list[rS].value(), 'rS_regions': rS_regions_edit_list[rS].isChecked(), 'rS_regions_val': rS_regions_val_edit_list[rS].value()}
				elif rS_regions_edit_list[rS].isChecked() == False:
					cMC_rS_obj = {'rS_surface': rS_surface_edit_list[rS].currentText(), 'rS_level_min': rS_level_min_list[rS].value(), 'rS_level_max': rS_level_max_list[rS].value(), 'rS_regions': rS_regions_edit_list[rS].isChecked()}
				cMC_rS_obj_list.append(cMC_rS_obj)

				rS = rS + 1
			cMC_obj['refinementSurfaces'] = cMC_rS_obj_list

		else:
			cMC_obj['refinementSurfaces'] = False
		
		if rR_v == True and True in other_geometry_list:
			###Записываем refinementRegions###
			rR = 0
			cMC_rR_obj_list = []
			for el_rR in range(cMC_refinementRegions_table.rowCount()):
				rR_surface_edit = cMC_refinementRegions_table.cellWidget(rR, 0).layout().itemAt(0).widget()
				rR_mode_edit = cMC_refinementRegions_table.cellWidget(rR, 1).layout().itemAt(0).widget()
				if rR_level_single_edit_list[rR].isChecked() == True:
					cMC_rR_obj = {'rR_surface': rR_surface_edit.currentText(), 'rR_mode': rR_mode_edit.currentText(), 'rR_level_single': True, 'rR_level_multi': False}
				elif rR_level_single_edit_list[rR].isChecked() == False:
					cMC_rR_obj = {'rR_surface': rR_surface_edit.currentText(), 'rR_mode': rR_mode_edit.currentText(), 'rR_level_single': False, 'rR_level_multi': True, 'rR_level_multi_val': rR_level_multi_val_edit_list[rR].value()}

				cMC_rR_obj_list.append(cMC_rR_obj)

				rR = rR + 1
			cMC_obj['refinementRegions'] = cMC_rR_obj_list

		else:
			cMC_obj['refinementRegions'] = False
		
		if len(cMC_obj) == 5:
			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_1.pkl', 'wb')
			pickle.dump(cMC_obj, output)
			output.close()
						
			if int_lng == 'Russian':
				msg = "Данные castellatedMC_1' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'castellatedMC_1' data was successfully saved"

			self.on_msg_correct(msg)	
		
			if castellatedMC_visible == False:
				if os.path.exists(castellatedMC_2_path) == True:
					os.remove(castellatedMC_2_path)

				rS_regions_edit_new_mas = []	
				f_level_single_edit_new_mas = []
				f_level_multi_edit_new_mas = []
				rR_level_single_edit_new_mas = []
				rR_level_multi_edit_new_mas = []
				for bvc in range(len(f_level_single_edit_list)):	
					f_level_single_edit_new = f_level_single_edit_list[bvc].isChecked()
					f_level_single_edit_new_mas.append(f_level_single_edit_new)

				for bvc in range(len(f_level_multi_edit_list)):	
					f_level_multi_edit_new = f_level_multi_edit_list[bvc].isChecked()
					f_level_multi_edit_new_mas.append(f_level_multi_edit_new)
				for bvc in range(len(rS_regions_edit_list)):	
					rS_regions_edit_new = rS_regions_edit_list[bvc].isChecked()
					rS_regions_edit_new_mas.append(rS_regions_edit_new)

				for bvc in range(len(rR_level_single_edit_list)):	
					rR_level_single_edit_new = rR_level_single_edit_list[bvc].isChecked()
					rR_level_single_edit_new_mas.append(rR_level_single_edit_new)

				for bvc in range(len(rR_level_multi_edit_list)):	
					rR_level_multi_edit_new = rR_level_multi_edit_list[bvc].isChecked()
					rR_level_multi_edit_new_mas.append(rR_level_multi_edit_new)

				if True in rS_regions_edit_new_mas or True in f_level_single_edit_new_mas or True in f_level_multi_edit_new_mas or True in rR_level_single_edit_new_mas or True in rR_level_multi_edit_new_mas:

					castellatedMC_2_group, castellatedMC_2_btnSave, prs_lvl_grid, f_level_single_list, rR_level_single_list, el_CMC_rS_regions_list = castellatedMC_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, castellatedMC_visible)

					castellatedMC_2_btnSave.clicked.connect(self.on_castellatedMC_2_btnSave_clicked)

					tab.setTabEnabled(4, True)
					tab.removeTab(4)
					tab.insertTab(4, castellatedMC_2_group, "&castellatedMC_2")

			if castellatedMC_visible == True:
				f_level_single_edit_new_mas = []
				f_level_multi_edit_new_mas = []
				f_level_multi_val_edit_new_mas = []
				rS_regions_edit_new_mas = []
				rS_regions_val_edit_new_mas = []

				for bvc in range(len(f_level_single_edit_list)):	
					f_level_single_edit_new = f_level_single_edit_list[bvc].isChecked()
					f_level_single_edit_new_mas.append(f_level_single_edit_new)

				for bvc in range(len(f_level_multi_edit_list)):	
					f_level_multi_edit_new = f_level_multi_edit_list[bvc].isChecked()
					f_level_multi_edit_new_mas.append(f_level_multi_edit_new)

				for bvc in range(len(f_level_multi_val_edit_list)):	
					f_level_multi_val_edit_new = f_level_multi_val_edit_list[bvc].value()
					f_level_multi_val_edit_new_mas.append(f_level_multi_val_edit_new)

				for bvc in range(len(rS_regions_edit_list)):	
					rS_regions_edit_new = rS_regions_edit_list[bvc].isChecked()
					rS_regions_edit_new_mas.append(rS_regions_edit_new)

				for bvc in range(len(rS_regions_val_edit_list)):	
					rS_regions_val_edit_new = rS_regions_val_edit_list[bvc].value()
					rS_regions_val_edit_new_mas.append(rS_regions_val_edit_new)

				for bvc in range(len(rR_level_single_edit_list)):	
					rR_level_single_edit_new = rR_level_single_edit_list[bvc].isChecked()
					rR_level_single_edit_new_mas.append(rR_level_single_edit_new)

				for bvc in range(len(rR_level_multi_edit_list)):	
					rR_level_multi_edit_new = rR_level_multi_edit_list[bvc].isChecked()
					rR_level_multi_edit_new_mas.append(rR_level_multi_edit_new)

				for bvc in range(len(rR_level_multi_val_edit_list)):	
					rR_level_multi_val_edit_new = rR_level_multi_val_edit_list[bvc].value()
					rR_level_multi_val_edit_new_mas.append(rR_level_multi_val_edit_new)

				if f_level_single_edit_old_mas != f_level_single_edit_new_mas or f_level_multi_edit_old_mas != f_level_multi_edit_new_mas \
				or f_level_multi_val_edit_old_mas != f_level_multi_val_edit_new_mas or rS_regions_edit_old_mas != rS_regions_edit_new_mas and not False in rS_regions_edit_new_mas \
				or rS_regions_val_edit_old_mas != rS_regions_val_edit_new_mas or rR_level_single_edit_old_mas != rR_level_single_edit_new_mas \
				or rR_level_single_edit_old_mas != rR_level_single_edit_new_mas or rR_level_multi_edit_old_mas != rR_level_multi_edit_new_mas or os.path.exists(castellatedMC_2_path) == False:

					if os.path.exists(castellatedMC_2_path) == True:
						os.remove(castellatedMC_2_path)

					castellatedMC_2_group, castellatedMC_2_btnSave, prs_lvl_grid, f_level_single_list, rR_level_single_list, el_CMC_rS_regions_list = castellatedMC_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, castellatedMC_visible)
					castellatedMC_2_btnSave.clicked.connect(self.on_castellatedMC_2_btnSave_clicked)

					tab.setTabEnabled(4, True)
					tab.removeTab(4)
					tab.insertTab(4, castellatedMC_2_group, "&castellatedMC_2")

				f_level_single_edit_old_mas = f_level_single_edit_new_mas
				f_level_multi_edit_old_mas = f_level_multi_edit_new_mas
				f_level_multi_val_edit_old_mas = f_level_multi_val_edit_new_mas
				rS_regions_edit_old_mas = rS_regions_edit_new_mas
				rS_regions_val_edit_old_mas = rS_regions_val_edit_new_mas
				rR_level_single_edit_old_mas = rR_level_single_edit_new_mas
				rR_level_multi_edit_old_mas = rR_level_multi_edit_new_mas
				rR_level_multi_val_edit_old_mas = rR_level_multi_val_edit_new_mas

	###---------------------Сохранение вкладки castellatedMC_2-------------------------###		
		
	def on_castellatedMC_2_btnSave_clicked(self):
		msg_list = []
		cMC_obj_lvl = {}
		
		####################################Сохраняем уровни для features###########################################
		if f_v == True and True in tri_distirbTri_list:
			cMC_f_lvl_table = prs_lvl_grid.itemAtPosition(1,0).widget()
		
			f = 0
			u = 1
			CM_features_lvl_list = []
			for el_f in range(cMC_f_lvl_table.rowCount()):
				CM_features_lvl_obj = {}
				f_geometry_edit = cMC_f_lvl_table.cellWidget(f, 0).layout().itemAt(0).widget()
				CM_features_lvl_obj['geometry'] = f_geometry_edit.currentText()
				if f_level_single_list[f] == True:
					lvl_single_obj = {}
					f_level_single = cMC_f_lvl_table.cellWidget(f, 1).layout().itemAt(0).widget()
					
					lvl_single_obj['lvl_single'] = f_level_single.value()
					CM_features_lvl_obj['lvl_prs'] = lvl_single_obj
					CM_features_lvl_list.append(CM_features_lvl_obj)
				elif f_level_single_list[f] == False:
					flmv_min_max_hbox = cMC_f_lvl_table.cellWidget(f, 1).layout()
					fmg = cMC_f_lvl_table.columnCount() - 1
		
					k = 0
					j = 1
					lvl_multi_obj_list = []
					for el in range(fmg):
						flmv_min_max = []
						lvl_multi_obj = {}
						flmv_min = flmv_min_max_hbox.itemAt(1).widget()
						flmv_max = flmv_min_max_hbox.itemAt(3).widget()
						flmv_min_max.append(flmv_min.value())
						flmv_min_max.append(flmv_max.value())
						lvl_multi_obj['lvl_multi_' + str(j)] = flmv_min_max
						lvl_multi_obj_list.append(lvl_multi_obj)
						k = k + 1
						j = j + 1

					CM_features_lvl_obj['lvl_prs'] = False
					CM_features_lvl_obj['multi_prs'] = lvl_multi_obj_list
					CM_features_lvl_list.append(CM_features_lvl_obj)
				f = f + 1
				u = u + 1
			
			cMC_obj_lvl['CM_features_lvl'] = CM_features_lvl_list
		
		rS_region_txt_itog_list = []
		###############################Сохраняем уровни для refinementSurfaces######################################
		if rS_v == True and True in el_CMC_rS_regions_list:
			cMC_rS_lvl_table = prs_lvl_grid.itemAtPosition(3,0).widget()
			
			rS = 0
			n = 1
			
			CM_refinementSurface_lvl_list = []
			for el_rS in range(cMC_rS_lvl_table.rowCount()):
				CM_refinementSurfaces_lvl_obj = {}
				rS_geometry_edit = cMC_rS_lvl_table.cellWidget(rS, 0).layout().itemAt(0).widget()	
				CM_refinementSurfaces_lvl_obj['rS_surface'] = rS_geometry_edit.currentText()
				
				rslmv_min_max = cMC_rS_lvl_table.cellWidget(rS, 1).layout()
				rsrv = cMC_rS_lvl_table.columnCount() - 1
				
				k = 0
				j = 1
				rS_region_txt_list = []
				for el in range(rsrv):
					rS_region_edit = rslmv_min_max.itemAt(0).widget()
					if rS_region_edit.text() == '':
						if int_lng == 'Russian':
							msg = "Укажите название подобласти " + str(j) + " для поверхности " + str(n)
						elif int_lng == 'English':
							msg = "Specify the name of surface " + str(j) + " for surface " + str(n)
						msg_list.append(msg)
					else:
						rS_region_txt_list.append(rS_region_edit.text())
					k = k + 1
					j = j + 1
					
				if len(rS_region_txt_list) == rsrv:
					rS_region_txt_itog_list.append(rS_region_txt_list)
					
				CM_refinementSurfaces_lvl_obj['rS_regions'] = rS_region_txt_list

				rslmv_min_max_itog_list = []
				for el in range(rsrv):
					rslmv_min_max_list = []
					rslmv_min = rslmv_min_max.itemAt(2).widget()
					rslmv_max = rslmv_min_max.itemAt(4).widget()
					rslmv_min_max_list.append(rslmv_min.value())
					rslmv_min_max_list.append(rslmv_max.value())
					rslmv_min_max_itog_list.append(rslmv_min_max_list)
					
				CM_refinementSurfaces_lvl_obj['rS_levels'] = rslmv_min_max_itog_list
				CM_refinementSurface_lvl_list.append(CM_refinementSurfaces_lvl_obj)	
				rS = rS + 1
				n = n + 1
				
			cMC_obj_lvl['CM_refinementSurface_lvl'] = CM_refinementSurface_lvl_list
		
		####################################Сохраняем уровни для refinementRegions###########################################
		if rR_v == True:
			cMC_rR_lvl_table = prs_lvl_grid.itemAtPosition(5,0).widget()
		
			rR = 0
			u = 1
			CM_refinementRegions_lvl_list = []
			for el_rR in range(cMC_rR_lvl_table.rowCount()):
				CM_refinementRegions_lvl_obj = {}
				rR_geometry_edit = cMC_rR_lvl_table.cellWidget(rR, 0).layout().itemAt(0).widget()

				CM_refinementRegions_lvl_obj['rR_surface'] = rR_geometry_edit.currentText()
				if rR_level_single_list[rR] == True:
					lvl_single_obj = {}
					rR_level_single_min = cMC_rR_lvl_table.cellWidget(rR, 1).layout().itemAt(1).widget()
					rR_level_single_max = cMC_rR_lvl_table.cellWidget(rR, 1).layout().itemAt(3).widget()

					lvl_single_obj['lvl_single_min'] = rR_level_single_min.value()
					lvl_single_obj['lvl_single_max'] = rR_level_single_max.value()
					
					CM_refinementRegions_lvl_obj['lvl_prs'] = lvl_single_obj
					CM_refinementRegions_lvl_list.append(CM_refinementRegions_lvl_obj)
				elif rR_level_single_list[rR] == False:
					rRlmv_min_max_hbox = cMC_rR_lvl_table.cellWidget(rR, 1).layout()
					rRmg = cMC_rR_lvl_table.columnCount() - 1
		
					k = 0
					j = 1
					lvl_multi_obj_list = []
					for el in range(rRmg):
						rRlmv_min_max = []
						lvl_multi_obj = {}
						rRlmv_min = rRlmv_min_max_hbox.itemAt(1).widget()
						rRlmv_max = rRlmv_min_max_hbox.itemAt(3).widget()
						rRlmv_min_max.append(rRlmv_min.value())
						rRlmv_min_max.append(rRlmv_max.value())
						lvl_multi_obj['lvl_multi_' + str(j)] = rRlmv_min_max
						lvl_multi_obj_list.append(lvl_multi_obj)
						k = k + 1
						j = j + 1

					CM_refinementRegions_lvl_obj['lvl_prs'] = False
					CM_refinementRegions_lvl_obj['multi_prs'] = lvl_multi_obj_list
					CM_refinementRegions_lvl_list.append(CM_refinementRegions_lvl_obj)
				rR = rR + 1
				u = u + 1
			
			cMC_obj_lvl['CM_refinementRegions_lvl'] = CM_refinementRegions_lvl_list
			
		self.on_msg_error(msg_list)	
		
		if f_v == True and True in tri_distirbTri_list:
			
			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_2.pkl', 'wb')
			pickle.dump(cMC_obj_lvl, output)
			output.close()

			if int_lng == 'Russian':
				msg = "Данные castellatedMC_2' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'castellatedMC_2' data was successfully saved"

			self.on_msg_correct(msg)
			
		elif rS_v == True and True in el_CMC_rS_regions_list:
			if len(rS_region_txt_itog_list) == cMC_rS_lvl_table.rowCount():
				output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_2.pkl', 'wb')
				pickle.dump(cMC_obj_lvl, output)
				output.close()

				if int_lng == 'Russian':
					msg = "Данные castellatedMC_2' успешно сохранены"
				elif int_lng == 'English':
					msg = "The 'castellatedMC_2' data was successfully saved"

				self.on_msg_correct(msg)
		elif rS_v == True and False in el_CMC_rS_regions_list:

			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_2.pkl', 'wb')
			pickle.dump(cMC_obj_lvl, output)
			output.close()

			if int_lng == 'Russian':
				msg = "Данные castellatedMC_2' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'castellatedMC_2' data was successfully saved"	
				
			self.on_msg_correct(msg)
			
		elif rR_v == True:

			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_2.pkl', 'wb')
			pickle.dump(cMC_obj_lvl, output)
			output.close()

			if int_lng == 'Russian':
				msg = "Данные castellatedMC_2' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'castellatedMC_2' data was successfully saved"	
				
			self.on_msg_correct(msg)
			
	###---------------------Сохранение вкладки layers-------------------------###		
		
	def on_layers_btnSave_clicked(self):
		msg_list = []
		layers_base_obj_list = []
		layers_main_obj = {}
		l = 0
		k = 1
		layers_list = []
		for el_base in range(layers_prs_base_table.rowCount()):
			layer_edit = layers_prs_base_table.cellWidget(l, 0).layout().itemAt(0).widget()	
			layer_val = layers_prs_base_table.cellWidget(l, 1).layout().itemAt(0).widget()	
			
			layers_base_obj = {}
			layers_base_obj['layer_' + str(k)] = layer_edit.text()
			layers_base_obj['layer_val_' + str(k)] = layer_val.value()
			
			layers_base_obj_list.append(layers_base_obj)
			
			if layer_edit.text() == '':
				if int_lng == 'Russian':
					msg = "Укажите название слоя " + str(k)
				elif int_lng == 'English':
					msg = "Specify the name of layer " + str(k)
				msg_list.append(msg)
			else:
				layers_list.append(layer_edit.text())
			
			l = l + 1
			k = k + 1
		
		layers_add_obj = {}

		fLT_val = layers_prs_add_table.cellWidget(0, 2).layout().itemAt(0).widget()
		layers_add_obj['finalLayerThickness'] = fLT_val.value()

		eR_val = layers_prs_add_table.cellWidget(1, 2).layout().itemAt(0).widget()
		layers_add_obj['expansionRatio'] = eR_val.value()

		mT_val = layers_prs_add_table.cellWidget(2, 2).layout().itemAt(0).widget()
		layers_add_obj['minThickness'] = mT_val.value()

		rS_val = layers_prs_add_table.cellWidget(3, 2).layout().itemAt(0).widget()
		layers_add_obj['relativeSizes'] = rS_val.currentText()

		fA_val = layers_prs_add_table.cellWidget(4, 2).layout().itemAt(0).widget()
		layers_add_obj['featureAngle'] = fA_val.value()

		nSSN_val = layers_prs_add_table.cellWidget(5, 2).layout().itemAt(0).widget()
		layers_add_obj['nSmoothSurfaceNormals'] = nSSN_val.value()

		nSN_val = layers_prs_add_table.cellWidget(6, 2).layout().itemAt(0).widget()
		layers_add_obj['nSmoothNormals'] = nSN_val.value()

		nST_val = layers_prs_add_table.cellWidget(7, 2).layout().itemAt(0).widget()
		layers_add_obj['nSmoothThickness'] = nST_val.value()

		mMAA_val = layers_prs_add_table.cellWidget(8, 2).layout().itemAt(0).widget()
		layers_add_obj['minMedianAxisAngle'] = mMAA_val.value()

		mTTMR_val = layers_prs_add_table.cellWidget(9, 2).layout().itemAt(0).widget()
		layers_add_obj['maxThicknessToMedialRatio'] = mTTMR_val.value()

		mFTR_val = layers_prs_add_table.cellWidget(10, 2).layout().itemAt(0).widget()
		layers_add_obj['maxFaceThicknessRatio'] = mFTR_val.value()

		nLI_val = layers_prs_add_table.cellWidget(11, 2).layout().itemAt(0).widget()
		layers_add_obj['nLayerIter'] = nLI_val.value()

		nRI_val = layers_prs_add_table.cellWidget(12, 2).layout().itemAt(0).widget()
		layers_add_obj['nRelaxedIter'] = nRI_val.value()

		nRIter_val = layers_prs_add_table.cellWidget(13, 2).layout().itemAt(0).widget()
		layers_add_obj['nRelaxIter'] = nRIter_val.value()

		nG_val = layers_prs_add_table.cellWidget(14, 2).layout().itemAt(0).widget()
		layers_add_obj['nGrow'] = nG_val.value()

		nBCNE_val = layers_prs_add_table.cellWidget(15, 2).layout().itemAt(0).widget()
		layers_add_obj['nBufferCellsNoExtrude'] = nBCNE_val.value()
			
		layers_main_obj['layers_base'] = layers_base_obj_list
		layers_main_obj['layers_add'] = layers_add_obj
		
		self.on_msg_error(msg_list)	
		
		if len(layers_list) == layers_prs_base_table.rowCount():
			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'layers.pkl', 'wb')
			pickle.dump(layers_main_obj, output)
			output.close()

			if int_lng == 'Russian':
				msg = "Данные 'layers' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'layers' data was successfully saved"	
				
			self.on_msg_correct(msg)
	
	###---------------------Сохранение вкладки snapC-------------------------###	
	
	def on_snapC_btnSave_clicked(self):
		snapC_obj = {}

		nSP_val = snapC_prs_table.cellWidget(0, 3).layout().itemAt(0).widget()
		snapC_obj['nSmoothPatch'] = nSP_val.value()

		t_val = snapC_prs_table.cellWidget(1, 3).layout().itemAt(0).widget()
		snapC_obj['tolerance'] = t_val.value()

		nSI_val = snapC_prs_table.cellWidget(2, 3).layout().itemAt(0).widget()
		snapC_obj['nSolveIter'] = nSI_val.value()

		nRI_val = snapC_prs_table.cellWidget(3, 3).layout().itemAt(0).widget()
		snapC_obj['nRelaxIter'] = nRI_val.value()

		nFSI_chck = snapC_prs_table.cellWidget(4, 0).layout().itemAt(0).widget()
		if nFSI_chck.isChecked() == True:
			nFSI_val = snapC_prs_table.cellWidget(4, 3).layout().itemAt(0).widget()
			snapC_obj['nFeatureSnapIter'] = nFSI_val.value()

		iFS_chck = snapC_prs_table.cellWidget(5, 0).layout().itemAt(0).widget()
		if iFS_chck.isChecked() == True:
			iFS_val = snapC_prs_table.cellWidget(5, 3).layout().itemAt(0).widget()
			snapC_obj['implicitFeatureSnap'] = iFS_val.currentText()

		eFS_chck = snapC_prs_table.cellWidget(6, 0).layout().itemAt(0).widget()
		if eFS_chck.isChecked() == True:
			eFS_val = snapC_prs_table.cellWidget(6, 3).layout().itemAt(0).widget()
			snapC_obj['explicitFeatureSnap'] = eFS_val.currentText()

		mRFS_chck = snapC_prs_table.cellWidget(7, 0).layout().itemAt(0).widget()
		if mRFS_chck.isChecked() == True:
			mRFS_val = snapC_prs_table.cellWidget(7, 3).layout().itemAt(0).widget()
			snapC_obj['multiRegionFeatureSnap'] = mRFS_val.currentText()

		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'snapC.pkl', 'wb')
		pickle.dump(snapC_obj, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные 'snapC' успешно сохранены"
		elif int_lng == 'English':
			msg = "The 'snapC' data was successfully saved"	

		self.on_msg_correct(msg)
	
	###---------------------Сохранение вкладки meshQC-------------------------###	

	def on_meshQC_btnSave_clicked(self):
		msg_list = []
		meshQC_add_obj = {}
		meshQC_main_obj = {}
		
		mQC_prs_list = []
		mQC_chcks_list = []
		#
		rMNO_chck = meshQC_prs_add_table.cellWidget(0, 0).layout().itemAt(0).widget()
		if rMNO_chck.isChecked() == True:
			rMNO_val = meshQC_prs_add_table.cellWidget(0, 3).layout().itemAt(0).widget()
			meshQC_add_obj['relaxed_maxNonOrtho'] = rMNO_val.value()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		nSS_val = meshQC_prs_add_table.cellWidget(1, 3).layout().itemAt(0).widget()
		meshQC_add_obj['nSmoothScale'] = nSS_val.value()
		mQC_prs_list.append(True)
		mQC_chcks_list.append(True)
		#
		eR_val = meshQC_prs_add_table.cellWidget(2, 3).layout().itemAt(0).widget()
		meshQC_add_obj['errorReduction'] = eR_val.value()
		mQC_prs_list.append(True)
		mQC_chcks_list.append(True)
		#
		mNO_chck = meshQC_prs_add_table.cellWidget(3, 0).layout().itemAt(0).widget()
		if mNO_chck.isChecked() == True:
			mNO_val = meshQC_prs_add_table.cellWidget(3, 3).layout().itemAt(0).widget()
			meshQC_add_obj['maxNonOrtho'] = mNO_val.value()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mBS_chck = meshQC_prs_add_table.cellWidget(4, 0).layout().itemAt(0).widget()
		if mBS_chck.isChecked() == True:
			mBS_val = meshQC_prs_add_table.cellWidget(4, 3).layout().itemAt(0).widget()
			meshQC_add_obj['maxBoundarySkewness'] = mBS_val.value()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mIS_chck = meshQC_prs_add_table.cellWidget(5, 0).layout().itemAt(0).widget()
		if mIS_chck.isChecked() == True:
			mIS_val = meshQC_prs_add_table.cellWidget(5, 3).layout().itemAt(0).widget()
			meshQC_add_obj['maxInternalSkewness'] = mIS_val.value()
			meshQC_prs_list.append(True)
			meshQC_chcks_list.append(True)
		#
		mC_chck = meshQC_prs_add_table.cellWidget(6, 0).layout().itemAt(0).widget()
		if mC_chck.isChecked() == True:
			mC_val = meshQC_prs_add_table.cellWidget(6, 3).layout().itemAt(0).widget()
			meshQC_add_obj['maxConcave'] = mC_val.value()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mV_chck = meshQC_prs_add_table.cellWidget(7, 0).layout().itemAt(0).widget()
		if mV_chck.isChecked() == True:
			mV_val = meshQC_prs_add_table.cellWidget(7, 3).layout().itemAt(0).widget()
			meshQC_add_obj['minVol'] = mV_val.text()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mA_chck = meshQC_prs_add_table.cellWidget(8, 0).layout().itemAt(0).widget()
		if mA_chck.isChecked() == True:
			mA_val = meshQC_prs_add_table.cellWidget(8, 3).layout().itemAt(0).widget()
			meshQC_add_obj['minArea'] = mA_val.text()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mTQ_chck = meshQC_prs_add_table.cellWidget(9, 0).layout().itemAt(0).widget()
		if mTQ_chck.isChecked() == True:
			mTQ_val = meshQC_prs_add_table.cellWidget(9, 3).layout().itemAt(0).widget()
			meshQC_add_obj['minTetQuality'] = mTQ_val.text()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mT_chck = meshQC_prs_add_table.cellWidget(10, 0).layout().itemAt(0).widget()
		if mT_chck.isChecked() == True:
			mT_val = meshQC_prs_add_table.cellWidget(10, 3).layout().itemAt(0).widget()
			meshQC_add_obj['minTwist'] = mT_val.value()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mD_chck = meshQC_prs_add_table.cellWidget(11, 0).layout().itemAt(0).widget()
		if mD_chck.isChecked() == True:
			mQC_chcks_list.append(True)
			mD_val = meshQC_prs_add_table.cellWidget(11, 3).layout().itemAt(0).widget()
			if mD_val.text() == '':
				if int_lng == 'Russian':
					msg = "Укажите минимальную нормированную детерминанту ячейки"
				elif int_lng == 'English':
					msg = "Specify the minimum normalised cell determinant"
				msg_list.append(msg)
			else:
				meshQC_add_obj['minDeterminant'] = mD_val.text()
				mQC_prs_list.append(True)
				
		#
		mFW_chck = meshQC_prs_add_table.cellWidget(12, 0).layout().itemAt(0).widget()
		if mFW_chck.isChecked() == True:
			mFW_val = meshQC_prs_add_table.cellWidget(12, 3).layout().itemAt(0).widget()
			meshQC_add_obj['minFaceWeight'] = mFW_val.value()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mVR_chck = meshQC_prs_add_table.cellWidget(13, 0).layout().itemAt(0).widget()
		if mVR_chck.isChecked() == True:
			mVR_val = meshQC_prs_add_table.cellWidget(13, 3).layout().itemAt(0).widget()
			meshQC_add_obj['minVolRatio'] = mVR_val.value()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		#
		mTT_chck = meshQC_prs_add_table.cellWidget(14, 0).layout().itemAt(0).widget()
		if mTT_chck.isChecked() == True:
			mTT_val = meshQC_prs_add_table.cellWidget(14, 3).layout().itemAt(0).widget()
			mQC_chcks_list.append(True)
			if mTT_val.text() == '':
				if int_lng == 'Russian':
					msg = "Укажите минимальное треугольное скручивание"
				elif int_lng == 'English':
					msg = "Specify the minimum triangle twist"
				msg_list.append(msg)
			else:
				meshQC_add_obj['minTriangleTwist'] = mTT_val.text()
				mQC_prs_list.append(True)
				
		#
		mVCR_chck = meshQC_prs_add_table.cellWidget(15, 0).layout().itemAt(0).widget()
		if mVCR_chck.isChecked() == True:
			mVCR_val = meshQC_prs_add_table.cellWidget(15, 3).layout().itemAt(0).widget()
			meshQC_add_obj['minVolCollapseRatio'] = mVCR_val.value()
			mQC_prs_list.append(True)
			mQC_chcks_list.append(True)
		
		meshQC_main_obj['meshQC_add'] = meshQC_add_obj

		self.on_msg_error(msg_list)		
			
		if len(mQC_prs_list) == len(mQC_chcks_list):

			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'meshQC.pkl', 'wb')
			pickle.dump(meshQC_main_obj, output)
			output.close()

			if int_lng == 'Russian':
				msg = "Данные 'meshQC' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'meshQC' data was successfully saved"	

			self.on_msg_correct(msg)

	###--------------------Функции вывода служебных сообщений-------------------------------#
			
	def on_msg_correct(self, msg):
		parn.listWidget.clear()
		parn.item = QtGui.QListWidgetItem(msg, parn.listWidget)
		color = QtGui.QColor("green")
		parn.item.setTextColor(color)
		parn.listWidget.addItem(parn.item)		
	def on_msg_error(self, msg_list):
		parn.listWidget.clear()
		for msg in msg_list:
			parn.item = QtGui.QListWidgetItem(msg, parn.listWidget)
			color = QtGui.QColor("red")
			parn.item.setTextColor(color)
			parn.listWidget.addItem(parn.item)

	###---------------------Запуск сохранения файла blocksMeshDict-------------------------###			
			
	def on_btnSave_clicked(self):
		snappyHexMeshDict_generation_class.snappyHexMeshDict_func(int_lng, parn, tab, f_edit, rS_edit, rR_edit, prj_path, mesh_name_txt, pd_2, self)
	             
