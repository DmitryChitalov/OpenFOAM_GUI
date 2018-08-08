import sys, re
import os

from PyQt4 import QtCore, QtGui

import pickle

from forms.fQMD_forms.initial_form import initial_class
from forms.fQMD_forms.geometry_1_form import geometry_1_class
from forms.fQMD_forms.geometry_2_form import geometry_2_class
from forms.fQMD_forms.surfaceConformation_form import surfaceConformation_class
from forms.fQMD_forms.motionControl_form import motionControl_class
from forms.fQMD_forms.shortEdgeFilter_form import shortEdgeFilter_class
from forms.fQMD_forms.extrusion_form import extrusion_class
from forms.fQMD_forms.surfaceFeatureExtractDict_form import surfaceFeatureExtractDict_class
from functions.foamyQuadMeshDict_generation import foamyQuadMeshDict_generation_class

class fqmd_window_class(QtGui.QWidget):
	def __init__(self, parent, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur):
		QtGui.QWidget.__init__(self, parent)
	
		global tab
		global initial_group, initial_btnSave, geometry_visible, surfaceConformation_visible, motionControl_visible, shortEdgeFilter_visible, extrusion_visible, surfaceFeatureExtractDict_visible, g_edit, gTCT_edit, gTCT_val, sCF_edit, sCF_val, s_edit, s_val
		
		global geometry_1_group, geometry_1_btnSave, geometry_type_list, shape_complex_lbl_list, shape_complex_numb_list, base_shape_lbl_list, base_shape_type_list, regions_lbl_list, regions_numb_list
		global geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list
		global surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, extendedFeatureEdgeMesh_list
		global motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_surface_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, \
		sCF_distanceCoeff_edit_list, sCF_totalDistanceCoeff_edit_list, sCF_surfaceOffsetCoeff_edit_list, sCF_surfaceCellSizeFunction_edit_list, sCF_surfaceCellSizeCoeff_edit_list, \
		sCF_distanceCoeff_chk_list, sCF_totalDistanceCoeff_chk_list, sCF_surfaceOffsetCoeff_chk_list
		global surfaceFeatureExtractDict_group, surfaceFeatureExtractDict_btnSave, sFED_surface_edit_list, sFED_extractionMethod_edit_list, sFED_includedAngle_edit_list, sFED_normal_list, \
		sFED_basePoint_list, sFED_nonManifoldEdges_edit_list, sFED_openEdges_edit_list, sFED_writeObj_edit_list
		global shortEdgeFilter_group, shortEdgeFilter_btnSave, sEFF_val, eATBF_val
		global extrusion_group, extrusion_btnSave, e_edit, eM_edit, pT_edit, extrusion_checks_list, extrusion_values_list, extrusion_val_pr_list, extrusion_val_def_list, axisPt_list, a_list, ang_val
		
		global geometry_1_path, geometry_2_path, surfaceConformation_path, motionControl_path, shortEdgeFilter_path, extrusion_path, surfaceFeatureExtractDict_path
				
		#global prj_path
		global int_lng
		#global mesh_name_txt
		#global pd_2
		
		global geometry_txt_old_mas
		global shape_complex_numb_val_old_mas
		global regions_numb_val_old_mas
		global base_shape_type_old_mas
		
		global g_v, gTCT_v, gTCT_val_v, sCF_v, sCF_val_v, s_v, s_val_v
		
		global parn
		parn = par
		
		#global prj_path_bm
		#prj_path_bm = prj_path
		
		#global mesh_name_txt_bm
		#mesh_name_txt_bm = mesh_name_txt
		
		#global pd_2_bm
		#pd_2_bm = pd_2
		
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
		initial_group, initial_btnSave, geometry_visible, surfaceConformation_visible, motionControl_visible, shortEdgeFilter_visible, extrusion_visible, surfaceFeatureExtractDict_visible, g_edit, gTCT_edit, gTCT_val, sCF_edit, sCF_val, s_edit, s_val = initial_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2)		
		tab.insertTab(0, initial_group, "&initial")
		g_edit.valueChanged.connect(lambda: self.g_edit_changed(g_edit))
		gTCT_edit.stateChanged.connect(self.gTCT_state_changed)
		sCF_edit.stateChanged.connect(self.sCF_state_changed)
		s_edit.stateChanged.connect(self.s_state_changed)
		
		g_v = g_edit.value()
		gTCT_v = gTCT_edit.isChecked()
		gTCT_val_v = gTCT_val.value()
		sCF_v = sCF_edit.isChecked()
		sCF_val_v = sCF_val.value()
		s_v = s_edit.isChecked()
		s_val_v = s_val.value()
		
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
			
		#------------------------------surfaceConformation---------------------------------#

		surfaceConformation_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceConformation.pkl'  
		#and os.path.exists(surfaceConformation_path)
		if surfaceConformation_visible == True:
			surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, extendedFeatureEdgeMesh_list = surfaceConformation_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceConformation_visible)
			surfaceConformation_btnSave.clicked.connect(self.on_surfaceConformation_btnSave_clicked)
			tab.insertTab(3, surfaceConformation_group, "&surfaceC")
		else:
			surfaceConformation_null_lbl = QtGui.QLabel()
			tab.insertTab(3, surfaceConformation_null_lbl, "&surfaceC")
			tab.setTabEnabled(3, False)
			
		#------------------------------motionControl---------------------------------#

		motionControl_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'motionControl.pkl'  
		#and os.path.exists(motionControl_path)
		if motionControl_visible == True:
			motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_surface_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, \
			sCF_distanceCoeff_edit_list, sCF_totalDistanceCoeff_edit_list, sCF_surfaceOffsetCoeff_edit_list, sCF_surfaceCellSizeFunction_edit_list, sCF_surfaceCellSizeCoeff_edit_list, \
			sCF_distanceCoeff_chk_list, sCF_totalDistanceCoeff_chk_list, sCF_surfaceOffsetCoeff_chk_list = motionControl_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, motionControl_visible)
			motionControl_btnSave.clicked.connect(self.on_motionControl_btnSave_clicked)
			tab.insertTab(4, motionControl_group, "&motionC")
		else:
			motionControl_null_lbl = QtGui.QLabel()
			tab.insertTab(4, motionControl_null_lbl, "&motionC")
			tab.setTabEnabled(4, False)
			
		#------------------------------surfaceFeatureExtract---------------------------------#

		surfaceFeatureExtractDict_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceFeatureExtractDict.pkl'  
		#and os.path.exists(surfaceFeatureExtractDict_path)
		if surfaceFeatureExtractDict_visible == True:
			surfaceFeatureExtractDict_group, surfaceFeatureExtractDict_btnSave, sFED_surface_edit_list, sFED_extractionMethod_edit_list, sFED_includedAngle_edit_list, sFED_normal_list, \
			sFED_basePoint_list, sFED_nonManifoldEdges_edit_list, sFED_openEdges_edit_list, sFED_writeObj_edit_list = surfaceFeatureExtractDict_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceFeatureExtractDict_visible)
			surfaceFeatureExtractDict_btnSave.clicked.connect(self.on_surfaceFeatureExtractDict_btnSave_clicked)
			tab.insertTab(5, surfaceFeatureExtractDict_group, "&surfaceFE")
		else:	
			surfaceFeatureExtractDict_null_lbl = QtGui.QLabel()
			tab.insertTab(5, surfaceFeatureExtractDict_null_lbl, "&surfaceFE")
			tab.setTabEnabled(5, False)
		
		#------------------------------shortEdgeFilter---------------------------------#
		
		shortEdgeFilter_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'shortEdgeFilter.pkl'  
		#and os.path.exists(shortEdgeFilter_path)
		if shortEdgeFilter_visible == True:
			shortEdgeFilter_group, shortEdgeFilter_btnSave, sEFF_val, eATBF_val = shortEdgeFilter_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, shortEdgeFilter_visible)
			shortEdgeFilter_btnSave.clicked.connect(self.on_shortEdgeFilter_btnSave_clicked)
			tab.insertTab(6, shortEdgeFilter_group, "&shortEdgeFilter")
		else:
			shortEdgeFilter_null_lbl = QtGui.QLabel()
			tab.insertTab(6, shortEdgeFilter_null_lbl, "&shortEdgeFilter")
			tab.setTabEnabled(6, False)
			
		#------------------------------extrusion---------------------------------#
		
		extrusion_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'extrusion.pkl'  
		#and os.path.exists(extrusion_path)
		if extrusion_visible == True:
			extrusion_group, extrusion_btnSave, e_edit, eM_edit, pT_edit, extrusion_checks_list, extrusion_values_list, extrusion_val_pr_list, extrusion_val_def_list, axisPt_list, a_list, ang_val = extrusion_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, extrusion_visible)
			extrusion_btnSave.clicked.connect(self.on_extrusion_btnSave_clicked)
			tab.insertTab(7, extrusion_group, "&extrusion")
		else:
			extrusion_null_lbl = QtGui.QLabel()
			tab.insertTab(7, extrusion_null_lbl, "&extrusion")
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
			
		fQMD_grid = QtGui.QGridLayout()
		fQMD_grid.addWidget(scrollArea, 0, 0, alignment=QtCore.Qt.AlignCenter)
		fQMD_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		fQMD_frame = QtGui.QFrame()
		fQMD_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
		fQMD_frame.setFrameShape(QtGui.QFrame.Panel)
		fQMD_frame.setFrameShadow(QtGui.QFrame.Sunken)
		fQMD_frame.setLayout(fQMD_grid)

		fQMD_vbox = QtGui.QVBoxLayout() 
		fQMD_vbox.addWidget(fQMD_frame)

		# ---------------------Размещение на форме всех компонентов-------------------------#

		form = QtGui.QFormLayout()
		form.addRow(fQMD_vbox)
		self.setLayout(form)
		
		#---------------------Привязываем к элементам формы обработчики, если изменяем имеющийся файл сетки----------------#
		
		if geometry_visible == True and os.path.exists(geometry_1_path):	
			for bvc in range(len(geometry_type_list)):
				self.geometry_control_chng(geometry_type_list, bvc)	
				
			if os.path.exists(geometry_2_path):
				for bvc in range(len(all_tri_file_btn_list)):
					if all_tri_file_btn_list[bvc] != '':
						self.tri_file_chng(all_tri_file_btn_list, bvc)	
						
		if motionControl_visible == True and os.path.exists(motionControl_path):
			for bvc in range(len(sCF_distanceCoeff_chk_list)):
				self.distanceCoeff_control_chng(sCF_distanceCoeff_chk_list, bvc)	
			
			for bvc in range(len(sCF_totalDistanceCoeff_chk_list)):
				self.totalDistanceCoeff_control_chng(sCF_totalDistanceCoeff_chk_list, bvc)	
				
			for bvc in range(len(sCF_surfaceOffsetCoeff_chk_list)):
				self.surfaceOffsetCoeff_control_chng(sCF_surfaceOffsetCoeff_chk_list, bvc)	
				
		if extrusion_visible == True and os.path.exists(extrusion_path):
			for bvc in range(len(extrusion_checks_list)):
				self.extrusion_control_chng(extrusion_checks_list, bvc)				
						
	#------------------------------Связываем элементы управления с функциями----------------------------#
		
	def geometry_control_chng(self, geometry_type_list, bvc):
		geometry_type_list[bvc].activated.connect(lambda: self.geometry_on_change(bvc))
		
	def tri_file_chng(self, all_tri_file_btn_list, bvc):
		all_tri_file_btn_list[bvc].clicked.connect(lambda: self.tri_file_on_change(bvc))
		
	def distanceCoeff_control_chng(self, sCF_distanceCoeff_chk_list, bvc):
		sCF_distanceCoeff_chk_list[bvc].clicked.connect(lambda: self.distanceCoeff_on_change(bvc))
		
	def totalDistanceCoeff_control_chng(self, sCF_totalDistanceCoeff_chk_list, bvc):
		sCF_totalDistanceCoeff_chk_list[bvc].clicked.connect(lambda: self.totalDistanceCoeff_on_change(bvc))
		
	def surfaceOffsetCoeff_control_chng(self, sCF_surfaceOffsetCoeff_chk_list, bvc):
		sCF_surfaceOffsetCoeff_chk_list[bvc].clicked.connect(lambda: self.surfaceOffsetCoeff_on_change(bvc))
		
	def extrusion_control_chng(self, extrusion_checks_list, bvc):
		extrusion_checks_list[bvc].clicked.connect(lambda: self.extrusion_on_change(bvc))
		
	#------------------------------Функции, связанные с элементами формы--------------------------------#
	
	def g_edit_changed(self, g_edit):
		g_edit_value = g_edit.value()
		s_val.setRange(1, g_edit_value)
		
	def gTCT_state_changed(self):
		if gTCT_edit.isChecked() == False:
			gTCT_val.setEnabled(False)
		elif gTCT_edit.isChecked() == True:
			gTCT_val.setEnabled(True)
			
	def sCF_state_changed(self):
		if sCF_edit.isChecked() == False:
			sCF_val.setEnabled(False)
		elif sCF_edit.isChecked() == True:
			sCF_val.setEnabled(True)
			
	def s_state_changed(self):
		if s_edit.isChecked() == False:
			s_val.setEnabled(False)
		elif s_edit.isChecked() == True:
			s_val.setEnabled(True)
			
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
					
	def distanceCoeff_on_change(self, bvc):
		sCF_distanceCoeff_chk = sCF_distanceCoeff_chk_list[bvc].isChecked()
		if sCF_distanceCoeff_chk == True:
			sCF_distanceCoeff_edit_list[bvc].setEnabled(True)
		elif sCF_distanceCoeff_chk == False:
			sCF_distanceCoeff_edit_list[bvc].setEnabled(False)
			
	def totalDistanceCoeff_on_change(self, bvc):
		sCF_totalDistanceCoeff_chk = sCF_totalDistanceCoeff_chk_list[bvc].isChecked()
		if sCF_totalDistanceCoeff_chk == True:
			sCF_totalDistanceCoeff_edit_list[bvc].setEnabled(True)
		elif sCF_totalDistanceCoeff_chk == False:
			sCF_totalDistanceCoeff_edit_list[bvc].setEnabled(False)
			
	def surfaceOffsetCoeff_on_change(self, bvc):
		sCF_surfaceOffsetCoeff_chk = sCF_surfaceOffsetCoeff_chk_list[bvc].isChecked()
		if sCF_surfaceOffsetCoeff_chk == True:
			sCF_surfaceOffsetCoeff_edit_list[bvc].setEnabled(True)
		elif sCF_surfaceOffsetCoeff_chk == False:
			sCF_surfaceOffsetCoeff_edit_list[bvc].setEnabled(False)
				
	def extrusion_on_change(self, bvc):
		extrusion_chck = extrusion_checks_list[bvc].isChecked()
		if extrusion_chck == True:
			if type(extrusion_values_list[bvc]) == list:
				extrusion_values_list[bvc][0].setEnabled(True)
				extrusion_values_list[bvc][1].setEnabled(True)
				extrusion_values_list[bvc][2].setEnabled(True)
				extrusion_values_list[bvc][3].setEnabled(True)
				extrusion_values_list[bvc][4].setEnabled(True)
				extrusion_values_list[bvc][5].setEnabled(True)
			else:
				extrusion_values_list[bvc].setEnabled(True)
			extrusion_val_pr_list[bvc].setEnabled(True)
			extrusion_val_def_list[bvc].setEnabled(True)
		elif extrusion_chck == False:
			if type(extrusion_values_list[bvc]) == list:
				extrusion_values_list[bvc][0].setEnabled(False)
				extrusion_values_list[bvc][1].setEnabled(False)
				extrusion_values_list[bvc][2].setEnabled(False)
				extrusion_values_list[bvc][3].setEnabled(False)
				extrusion_values_list[bvc][4].setEnabled(False)
				extrusion_values_list[bvc][5].setEnabled(False)
			else:
				extrusion_values_list[bvc].setEnabled(False)
			extrusion_val_pr_list[bvc].setEnabled(False)
			extrusion_val_def_list[bvc].setEnabled(False)
						
	###---------------------Сохранение вкладки initial-------------------------###	
						
	def on_initial_btnSave_clicked(self):
		global g_v, gTCT_v, gTCT_val_v, sCF_v, sCF_val_v, s_v, s_val_v, g_old, gTCT_old, gTCT_val_old, sCF_old, sCF_val_old, s_old, s_val_old
		global geometry_1_group, geometry_1_btnSave, geometry_type_list, shape_complex_lbl_list, shape_complex_numb_list, base_shape_lbl_list, base_shape_type_list, regions_lbl_list, regions_numb_list
		global shortEdgeFilter_group, shortEdgeFilter_btnSave, sEFF_val, eATBF_val
		global extrusion_group, extrusion_btnSave, e_edit, eM_edit, pT_edit, extrusion_checks_list, extrusion_values_list, extrusion_val_pr_list, extrusion_val_def_list, axisPt_list, a_list, ang_val
		
		#------------------------------Получаем текущие значения полей вкладки initial--------------------------------------#
		
		g_v = g_edit.value()
		gTCT_v = gTCT_edit.isChecked()
		gTCT_val_v = gTCT_val.value()
		sCF_v = sCF_edit.isChecked()
		sCF_val_v = sCF_val.value()
		s_v = s_edit.isChecked()
		s_val_v = s_val.value()		
		
		#-------------------------------Сохраняем файл сетки если создаем новый----------------------------------------------#
		
		if geometry_visible == False and surfaceConformation_visible == False and motionControl_visible == False and shortEdgeFilter_visible == False and extrusion_visible == False and surfaceFeatureExtractDict_visible == False:
			
			initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
			if os.path.exists(initial_path_file) == True:
				input = open(initial_path_file, 'rb')
				initial_obj = pickle.load(input)
				input.close()
				
				g_old = initial_obj['g']
				
				gTCT_val_old = None
				gTCT_old = initial_obj['gTCT']
				if gTCT_old == True:
					gTCT_val_old = initial_obj['gTCT_val']
					
				sCF_val_old = None
				sCF_old = initial_obj['sCF']
				if sCF_old == True:
					sCF_val_old = initial_obj['sCF_val']
					
				s_val_old = None
				s_old = initial_obj['sCF']
				if s_old == True:
					s_val_old = initial_obj['s_val']	
				
			else:
				g_old = g_v
				
				gTCT_old = gTCT_v
				if gTCT_old == True:
					gTCT_val_old = gTCT_val_v
				else:
					gTCT_val_old = None
					
				sCF_old = sCF_v
				if sCF_old == True:
					sCF_val_old = sCF_val_v
				else:
					sCF_val_old = None
					
				s_old = s_v
				if s_old == True:
					s_val_old = s_val_v
				else:
					s_val_old = None
				
			if gTCT_v == True and sCF_v == True and s_v == True:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "gTCT_val": gTCT_val_v, "sCF": sCF_v, "sCF_val": sCF_val_v, "s": s_v, "s_val": s_val_v}	
			elif gTCT_v == False and sCF_v == True and s_v == True:	
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "sCF": sCF_v, "sCF_val": sCF_val_v, "s": s_v, "s_val": s_val_v}	
			elif gTCT_v == False and sCF_v == False and s_v == True:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "sCF": sCF_v, "s": s_v, "s_val": s_val_v}	
			elif gTCT_v == True and sCF_v == False and s_v == False:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "gTCT_val": gTCT_val_v, "sCF": sCF_v, "s_val": s_val_v}
			elif gTCT_v == True and sCF_v == True and s_v == False:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "gTCT_val": gTCT_val_v, "sCF": sCF_v, "sCF_val": sCF_val_v, "s_val": s_val_v}	
			elif gTCT_v == True and sCF_v == False and s_v == True:	
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "gTCT_val": gTCT_val_v, "sCF": sCF_v, "s": s_v, "s_val": s_val_v}	
			elif gTCT_v == False and sCF_v == True and s_v == False:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "sCF": sCF_v, "sCF_val": sCF_val_v, "s_val": s_val_v}	
			else:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "sCF": sCF_v, "s": s_v}	
			
			prj_path_dir = prj_path + '/' + mesh_name_txt
			
			if os.path.exists(prj_path_dir) == False:
				os.mkdir(prj_path_dir) 
		
			output = open(initial_path_file, 'wb')

			pickle.dump(initial_obj, output)
			output.close()
			
		#-------------------------------Сохраняем файл сетки если пересохраняем имеющийся------------------------------------#
			
		if geometry_visible == True and surfaceConformation_visible == True and motionControl_visible == True and shortEdgeFilter_visible == True and extrusion_visible == True and surfaceFeatureExtractDict_visible == True:
			initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
			
			input = open(initial_path_file, 'rb')
			initial_obj = pickle.load(input)
			input.close()
			
			g_old = initial_obj['g']

			gTCT_old = initial_obj['gTCT']
			if gTCT_old == True:
				gTCT_val_old = initial_obj['gTCT_val']

			sCF_old = initial_obj['sCF']
			if sCF_old == True:
				sCF_val_old = initial_obj['sCF_val']
				
			s_old = initial_obj['s']
			if s_old == True:
				s_val_old = initial_obj['s_val']
				
			if gTCT_v == True and sCF_v == True and s_v == True:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "gTCT_val": gTCT_val_v, "sCF": sCF_v, "sCF_val": sCF_val_v, "s": s_v, "s_val": s_val_v}	
			elif gTCT_v == False and sCF_v == True and s_v == True:	
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "sCF": sCF_v, "sCF_val": sCF_val_v, "s": s_v, "s_val": s_val_v}	
			elif gTCT_v == False and sCF_v == False and s_v == True:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "sCF": sCF_v, "s": s_v, "s_val": s_val_v}	
			elif gTCT_v == True and sCF_v == False and s_v == False:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "gTCT_val": gTCT_val_v, "sCF": sCF_v, "s_val": s_val_v}
			elif gTCT_v == True and sCF_v == True and s_v == False:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "gTCT_val": gTCT_val_v, "sCF": sCF_v, "sCF_val": sCF_val_v, "s_val": s_val_v}	
			elif gTCT_v == True and sCF_v == False and s_v == True:	
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "gTCT_val": gTCT_val_v, "sCF": sCF_v, "s": s_v, "s_val": s_val_v}	
			elif gTCT_v == False and sCF_v == True and s_v == False:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "sCF": sCF_v, "sCF_val": sCF_val_v, "s_val": s_val_v}	
			else:
				initial_obj = {"g": g_v, "gTCT": gTCT_v, "sCF": sCF_v, "s": s_v}	
		
			output = open(initial_path_file, 'wb')

			pickle.dump(initial_obj, output)
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
				
		if shortEdgeFilter_visible == False:
			if os.path.exists(shortEdgeFilter_path) == False:
				
				shortEdgeFilter_group, shortEdgeFilter_btnSave, sEFF_val, eATBF_val = shortEdgeFilter_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, shortEdgeFilter_visible)
				shortEdgeFilter_btnSave.clicked.connect(self.on_shortEdgeFilter_btnSave_clicked)	

				tab.setTabEnabled(6, True)
				tab.removeTab(6)
				tab.insertTab(6, shortEdgeFilter_group, "&shortEdgeFilter")
				
		if extrusion_visible == False:
			if os.path.exists(extrusion_path) == False:
				
				extrusion_group, extrusion_btnSave, e_edit, eM_edit, pT_edit, extrusion_checks_list, extrusion_values_list, extrusion_val_pr_list, extrusion_val_def_list, axisPt_list, a_list, ang_val = extrusion_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, extrusion_visible)
				extrusion_btnSave.clicked.connect(self.on_extrusion_btnSave_clicked)	
				
				for bvc in range(len(extrusion_checks_list)):
					self.extrusion_control_chng(extrusion_checks_list, bvc)	

				tab.setTabEnabled(7, True)
				tab.removeTab(7)
				tab.insertTab(7, extrusion_group, "&extrusion")
				
		if geometry_visible == False and surfaceConformation_visible == False and motionControl_visible == False and shortEdgeFilter_visible == False and extrusion_visible == False and surfaceFeatureExtractDict_visible == False:
			if os.path.exists(prj_path_dir) == False:
				os.mkdir(prj_path_dir) 
		
		msg_list = []
		output = open(initial_path_file, 'wb')

		pickle.dump(initial_obj, output)
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
			elif el_m.currentText() == 'Три-поверхность' or el_m.currentText() == 'Tri-surface' \
			or el_m.currentText() == 'Распределенная три-поверхность' or el_m.currentText() == 'Distributed tri-surface' \
			or el_m.currentText() == 'Закрытая три-поверхность' or el_m.currentText() == 'Closed tri-surface':
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
		global surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, extendedFeatureEdgeMesh_list
		global motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_surface_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, \
		sCF_distanceCoeff_edit_list, sCF_totalDistanceCoeff_edit_list, sCF_surfaceOffsetCoeff_edit_list, sCF_surfaceCellSizeFunction_edit_list, sCF_surfaceCellSizeCoeff_edit_list, \
		sCF_distanceCoeff_chk_list, sCF_totalDistanceCoeff_chk_list, sCF_surfaceOffsetCoeff_chk_list
		global surfaceFeatureExtractDict_group, surfaceFeatureExtractDict_btnSave, sFED_surface_edit_list, sFED_extractionMethod_edit_list, sFED_includedAngle_edit_list, sFED_normal_list, \
		sFED_basePoint_list, sFED_nonManifoldEdges_edit_list, sFED_openEdges_edit_list, sFED_writeObj_edit_list
		
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
				
			###############################################closed_tri_table#########################################################
			if all_geometry_list_lbls[t] == 'closed_tri_table':

				closed_tri_table_stroka = []
				
				#file
				file_val = el_m.cellWidget(0, 0).layout().itemAt(0).widget().text()
					
				if file_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Файл' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'file' of geometry " + str(n)
					msg_list.append(msg)
				else:
					closed_tri_table_stroka.append(file_val)
				#type
				type_val = el_m.cellWidget(0, 1).layout().itemAt(0).widget().currentText()
				closed_tri_table_stroka.append(type_val)
				#name
				name_val = el_m.cellWidget(0, 2).layout().itemAt(0).widget().text()
				if name_val == '':
					if int_lng == 'Russian':
						msg = "Укажите значение поля 'Название' геометрии " + str(n)
					elif int_lng == 'English':
						msg = "Specify the value of field 'name' of geometry " + str(n)
					msg_list.append(msg)
				else:
					closed_tri_table_stroka.append(name_val)
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

				if len(closed_tri_table_stroka) == 3 and len(one_region_list) == cC-3:
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
			
			if surfaceConformation_visible == False or surfaceConformation_visible == True:
				if gTCT_v == True and gTCT_v != gTCT_old or gTCT_v == True and os.path.exists(surfaceConformation_path) == False or gTCT_v == True and gTCT_v == gTCT_old and gTCT_val_v != gTCT_val_old \
				or gTCT_v == False:
				
					if os.path.exists(surfaceConformation_path) == True:
						os.remove(surfaceConformation_path)
						
					surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, extendedFeatureEdgeMesh_list = surfaceConformation_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceConformation_visible)
					surfaceConformation_btnSave.clicked.connect(self.on_surfaceConformation_btnSave_clicked)
					
					tab.setTabEnabled(3, True)
					tab.removeTab(3)
					tab.insertTab(3, surfaceConformation_group, "&surfaceC")
			
			if motionControl_visible == False or motionControl_visible == True:
				if sCF_v == True and sCF_v != sCF_old or sCF_v == True and os.path.exists(motionControl_path) == False or sCF_v == True and sCF_v == sCF_old and sCF_val_v != sCF_val_old \
				or sCF_v == False:
				
					if os.path.exists(motionControl_path) == True:
						os.remove(motionControl_path)
						
					motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_surface_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, \
					sCF_distanceCoeff_edit_list, sCF_totalDistanceCoeff_edit_list, sCF_surfaceOffsetCoeff_edit_list, sCF_surfaceCellSizeFunction_edit_list, sCF_surfaceCellSizeCoeff_edit_list, \
					sCF_distanceCoeff_chk_list, sCF_totalDistanceCoeff_chk_list, sCF_surfaceOffsetCoeff_chk_list = motionControl_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, motionControl_visible)
					motionControl_btnSave.clicked.connect(self.on_motionControl_btnSave_clicked)
					
					for bvc in range(len(sCF_distanceCoeff_chk_list)):
						self.distanceCoeff_control_chng(sCF_distanceCoeff_chk_list, bvc)	
			
					for bvc in range(len(sCF_totalDistanceCoeff_chk_list)):
						self.totalDistanceCoeff_control_chng(sCF_totalDistanceCoeff_chk_list, bvc)	
				
					for bvc in range(len(sCF_surfaceOffsetCoeff_chk_list)):
						self.surfaceOffsetCoeff_control_chng(sCF_surfaceOffsetCoeff_chk_list, bvc)	
					
					tab.setTabEnabled(4, True)
					tab.removeTab(4)
					tab.insertTab(4, motionControl_group, "&motionC")
					
			if surfaceFeatureExtractDict_visible == False or surfaceFeatureExtractDict_visible == True:
				if s_v == True and s_v != s_old or s_v == True and os.path.exists(motionControl_path) == False or s_v == True and s_v == s_old and s_val_v != s_val_old \
				or s_v == False:
				
					if os.path.exists(surfaceFeatureExtractDict_path) == True:
						os.remove(surfaceFeatureExtractDict_path)
						
					surfaceFeatureExtractDict_group, surfaceFeatureExtractDict_btnSave, sFED_surface_edit_list, sFED_extractionMethod_edit_list, sFED_includedAngle_edit_list, sFED_normal_list, \
					sFED_basePoint_list, sFED_nonManifoldEdges_edit_list, sFED_openEdges_edit_list, sFED_writeObj_edit_list = surfaceFeatureExtractDict_class.out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceFeatureExtractDict_visible)
					surfaceFeatureExtractDict_btnSave.clicked.connect(self.on_surfaceFeatureExtractDict_btnSave_clicked)	
						
					tab.setTabEnabled(5, True)
					tab.removeTab(5)
					tab.insertTab(5, surfaceFeatureExtractDict_group, "&surfaceFE")
					
	###---------------------Сохранение вкладки surfaceConformation-------------------------###		
		
	def on_surfaceConformation_btnSave_clicked(self):
		sC_obj = {}
		
		lIM_edit_x = sC_start_prs_grid.itemAtPosition(0,1).widget()
		lIM_edit_y = sC_start_prs_grid.itemAtPosition(0,2).widget()
		lIM_edit_z = sC_start_prs_grid.itemAtPosition(0,3).widget()
		
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
			
		pPDC_edit = sC_start_prs_grid.itemAtPosition(1,1).widget()
		mELC_edit = sC_start_prs_grid.itemAtPosition(2,1).widget()
		mNLC_edit = sC_start_prs_grid.itemAtPosition(3,1).widget()
		mNPDC_edit = sC_start_prs_grid.itemAtPosition(4,1).widget()
		mQA_edit = sC_start_prs_grid.itemAtPosition(5,1).widget()
		iSNPP_edit = sC_start_prs_grid.itemAtPosition(6,1).widget()
		mP_edit = sC_start_prs_grid.itemAtPosition(7,1).widget()
		iSNePP_edit = sC_start_prs_grid.itemAtPosition(8,1).widget()
		mBCI_edit = sC_start_prs_grid.itemAtPosition(9,1).widget()
		rIG_edit = sC_start_prs_grid.itemAtPosition(10,1).widget()
		rP_edit = sC_start_prs_grid.itemAtPosition(11,1).widget()
		
		if pPDC_edit.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра 'pointPairDistanceCoeff'"
			elif int_lng == 'English':
				msg = "Specify the value of parameter 'pointPairDistanceCoeff'"
			msg_list.append(msg)
			
		if mELC_edit.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра 'minEdgeLenCoeff'"
			elif int_lng == 'English':
				msg = "Specify the value of parameter 'minEdgeLenCoeff'"
			msg_list.append(msg)
			
		if mNPDC_edit.text() == '':
			if int_lng == 'Russian':
				msg = "Укажите значение параметра 'minNearPointDistCoeff'"
			elif int_lng == 'English':
				msg = "Specify the value of parameter 'minNearPointDistCoeff'"
			msg_list.append(msg)

		obj_sC_start_prs_obj = {'lIM': lIM_list, 'pPDC': pPDC_edit.text(), 'mELC': mELC_edit.text(), 'mNLC': mNLC_edit.value(), 'mNPDC': mNPDC_edit.text(), 'mQA': mQA_edit.value(), \
		'iSNPP': iSNPP_edit.currentText(), 'mP': mP_edit.currentText(), 'iSNePP': iSNePP_edit.currentText(), 'mBCI': mBCI_edit.value(), 'rIG': rIG_edit.currentText(), 'rP': rP_edit.value()} 
		sC_obj['sC_start_prs'] = obj_sC_start_prs_obj
		
		k = 1
		i = 0
		conf_obj_list = []
		for el_g in range(len(geometry_list)):
			conf_obj = {'g': geometry_list[i].currentText(), 'fM': featureMethod_list[i].currentText(), 'eFEM': extendedFeatureEdgeMesh_list[i].currentText()}
			conf_obj_list.append(conf_obj)
			
			k = k + 1
			i = i + 1
		
		sC_obj['sC_conf_prs'] = conf_obj_list
			
		if len(lIM_list) == 3 and pPDC_edit.text() != '' and mELC_edit.text() != '' and mNPDC_edit.text() != '':
			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceConformation.pkl', 'wb')
			pickle.dump(sC_obj, output)
			output.close()
						
			if int_lng == 'Russian':
				msg = "Данные 'surfaceConformation' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'surfaceConformation' data was successfully saved"

			self.on_msg_correct(msg)	
	
	###---------------------Сохранение вкладки motionControl-------------------------###		
	
	def on_motionControl_btnSave_clicked(self):
		mC_obj = {}
		
		mCS_edit = mC_start_prs_grid.itemAtPosition(0,1).widget()
		dF_edit = mC_start_prs_grid.itemAtPosition(1,1).widget()
		rM_edit = mC_start_prs_grid.itemAtPosition(2,1).widget()
		rS_edit = mC_start_prs_grid.itemAtPosition(3,1).widget()
		rE_edit = mC_start_prs_grid.itemAtPosition(4,1).widget()
		oO_edit = mC_start_prs_grid.itemAtPosition(5,1).widget()
		mSO_edit = mC_start_prs_grid.itemAtPosition(6,1).widget()
		nWAD_edit = mC_start_prs_grid.itemAtPosition(7,1).widget()
		
		obj_mC_start_prs_obj = {'mCS': mCS_edit.value(), 'dF': dF_edit.value(), 'rM': rM_edit.currentText(), 'rS': rS_edit.value(), 'rE': rE_edit.value(), 'oO': oO_edit.currentText(), 'mSO': mSO_edit.currentText(), 'nWAD': nWAD_edit.value()}
		
		mC_obj['mC_start_prs'] = obj_mC_start_prs_obj
		
		k = 1
		i = 0
		sCF_obj_list = []
		for el_s in range(len(sCF_surface_edit_list)):
			sCF_obj = {}
			sCF_obj['s'] = sCF_surface_edit_list[i].currentText()
			sCF_obj['t'] = sCF_type_edit_list[i].currentText()
			sCF_obj['p'] = sCF_priority_edit_list[i].value()
			sCF_obj['m'] = sCF_mode_edit_list[i].currentText()
			sCF_obj['cSF'] = sCF_cellSizeFunction_edit_list[i].currentText()
			sCF_obj['dCSC'] = sCF_distanceCellSizeCoeff_edit_list[i].value()
			
			if sCF_distanceCoeff_chk_list[i].isChecked() == True:
				sCF_obj['dC_chk'] = sCF_distanceCoeff_chk_list[i].isChecked()
				sCF_obj['dC'] = sCF_distanceCoeff_edit_list[i].value()
			else:
				sCF_obj['dC_chk'] = sCF_distanceCoeff_chk_list[i].isChecked()
				
			if sCF_totalDistanceCoeff_chk_list[i].isChecked() == True:
				sCF_obj['tDC_chk'] = sCF_totalDistanceCoeff_chk_list[i].isChecked()
				sCF_obj['tDC'] = sCF_totalDistanceCoeff_edit_list[i].value()
			else:
				sCF_obj['tDC_chk'] = sCF_totalDistanceCoeff_chk_list[i].isChecked()
				
			if sCF_surfaceOffsetCoeff_chk_list[i].isChecked() == True:
				sCF_obj['sOC_chk'] = sCF_surfaceOffsetCoeff_chk_list[i].isChecked()
				sCF_obj['sOC'] = sCF_surfaceOffsetCoeff_edit_list[i].value()
			else:
				sCF_obj['sOC_chk'] = sCF_surfaceOffsetCoeff_chk_list[i].isChecked()
			sCF_obj['sCSF'] = sCF_surfaceCellSizeFunction_edit_list[i].currentText()
			sCF_obj['sCSC'] = sCF_surfaceCellSizeCoeff_edit_list[i].value()
			
			sCF_obj_list.append(sCF_obj)
			
			k = k + 1
			i = i + 1
			
		mC_obj['mC_sCF_prs'] = sCF_obj_list
		
		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'motionControl.pkl', 'wb')
		pickle.dump(mC_obj, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные 'motionControl' успешно сохранены"
		elif int_lng == 'English':
			msg = "The 'motionControl' data was successfully saved"

		self.on_msg_correct(msg)
		
	###---------------------Сохранение вкладки surfaceFeatureExtractDict-------------------------###	
	
	def on_surfaceFeatureExtractDict_btnSave_clicked(self):
			
		k = 1
		i = 0
		normal_list_all = []
		basePoint_list_all = []
		
		msg_list = []
		
		sFED_obj_list = []
		
		for el_sFED in range(len(sFED_surface_edit_list)):
			sFED_obj = {}
			
			sFED_obj['s'] = sFED_surface_edit_list[i].currentText()
			sFED_obj['eM'] = sFED_extractionMethod_edit_list[i].currentText()
			sFED_obj['iA'] = sFED_includedAngle_edit_list[i].value()
			
			for el_n in sFED_normal_list:
				normal_list = []
				if el_n[0].text() == '':
					if int_lng == 'Russian':
						msg = "Укажите координату 'x' нормали ребер"
					elif int_lng == 'English':
						msg = "Specify the 'x' coordinate of edges normal"
					msg_list.append(msg)
				else:
					normal_list.append(el_n[0].text())
					
				if el_n[1].text() == '':
					if int_lng == 'Russian':
						msg = "Укажите координату 'y' нормали ребер"
					elif int_lng == 'English':
						msg = "Specify the 'y' coordinate of edges normal"
					msg_list.append(msg)
				else:
					normal_list.append(el_n[1].text())
					
				if el_n[2].text() == '':
					if int_lng == 'Russian':
						msg = "Укажите координату 'z' нормали ребер"
					elif int_lng == 'English':
						msg = "Specify the 'z' coordinate of edges normal"
					msg_list.append(msg)
				else:
					normal_list.append(el_n[2].text())
					
				if len(normal_list) == 3:
					sFED_obj['n'] = normal_list	
				
			for el_bP in sFED_basePoint_list:
				basePoint_list = []
				if el_bP[0].text() == '':
					if int_lng == 'Russian':
						msg = "Укажите координату 'x' базовой точки"
					elif int_lng == 'English':
						msg = "Specify the 'x' coordinate of base point"
					msg_list.append(msg)
				else:
					basePoint_list.append(el_bP[0].text())
					
				if el_bP[1].text() == '':
					if int_lng == 'Russian':
						msg = "Укажите координату 'y' базовой точки"
					elif int_lng == 'English':
						msg = "Specify the 'y' coordinate of base point"
					msg_list.append(msg)
				else:
					basePoint_list.append(el_bP[1].text())
					
				if el_bP[2].text() == '':
					if int_lng == 'Russian':
						msg = "Укажите координату 'z' базовой точки"
					elif int_lng == 'English':
						msg = "Specify the 'z' coordinate of base point"
					msg_list.append(msg)
				else:
					basePoint_list.append(el_bP[2].text())
					
				if len(basePoint_list) == 3:
					sFED_obj['bP'] = basePoint_list
				
			sFED_obj['nME'] = sFED_nonManifoldEdges_edit_list[i].currentText()
			sFED_obj['oE'] = sFED_openEdges_edit_list[i].currentText()
			sFED_obj['wO'] = sFED_writeObj_edit_list[i].currentText()
			
			if len(sFED_obj) == 8:
				sFED_obj_list.append(sFED_obj)
				
			self.on_msg_error(msg_list)
			
			k = k + 1
			i = i + 1
		
		if len(sFED_obj_list) == len(sFED_surface_edit_list):
			output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceFeatureExtractDict.pkl', 'wb')
			pickle.dump(sFED_obj_list, output)
			output.close()
			
			if int_lng == 'Russian':
				msg = "Данные 'surfaceFeatureExtractDict' успешно сохранены"
			elif int_lng == 'English':
				msg = "The 'surfaceFeatureExtractDict' data was successfully saved"

			self.on_msg_correct(msg)	

	###---------------------Сохранение вкладки shortEdgeFilter-------------------------###	
	
	def on_shortEdgeFilter_btnSave_clicked(self):
		sEF_obj = {'sEFF': sEFF_val.value(), 'eATBF': eATBF_val.value()}
		
		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'shortEdgeFilter.pkl', 'wb')
		pickle.dump(sEF_obj, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные 'shortEdgeFilter' успешно сохранены"
		elif int_lng == 'English':
			msg = "The 'shortEdgeFilter' data was successfully saved"

		self.on_msg_correct(msg)	
		
	###---------------------Сохранение вкладки extrusion-------------------------###
	
	def on_extrusion_btnSave_clicked(self):
		
		extr_obj = {}
		
		extr_obj['e'] = e_edit.currentText()
		extr_obj['eM'] = eM_edit.currentText()
		extr_obj['pT'] = pT_edit.currentText()
		
		axisPt_v_list = []
		for el_axisPt in axisPt_list:
			axisPt_v_list.append(el_axisPt.value())
		
		extr_obj['axisPt'] = axisPt_v_list
		
		a_v_list = []
		for el_a in a_list:
			a_v_list.append(el_a.value())
			
		extr_obj['a'] = a_v_list
		extr_obj['ang'] = ang_val.value()
		
		if extrusion_checks_list[0].isChecked() == True:
			extr_obj['nL_chck'] = extrusion_checks_list[0].isChecked()
			extr_obj['nL_val'] = extrusion_values_list[0].value()
		else:
			extr_obj['nL_chck'] = extrusion_checks_list[0].isChecked()
			
		if extrusion_checks_list[1].isChecked() == True:
			extr_obj['eR_chck'] = extrusion_checks_list[1].isChecked()
			extr_obj['eR_val'] = extrusion_values_list[1].value()
		else:
			extr_obj['eR_chck'] = extrusion_checks_list[1].isChecked()
			
		if extrusion_checks_list[2].isChecked() == True:
			extr_obj['d_chck'] = extrusion_checks_list[2].isChecked()
			d_val_list = []
			d_val_list.append(extrusion_values_list[2][3].value())
			d_val_list.append(extrusion_values_list[2][4].value())
			d_val_list.append(extrusion_values_list[2][5].value())
			
			extr_obj['d_val'] = d_val_list
		else:
			extr_obj['d_chck'] = extrusion_checks_list[2].isChecked()
			
		if extrusion_checks_list[3].isChecked() == True:
			extr_obj['t_chck'] = extrusion_checks_list[3].isChecked()
			extr_obj['t_val'] = extrusion_values_list[3].value()
		else:
			extr_obj['t_chck'] = extrusion_checks_list[3].isChecked()

		output = open(prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'extrusion.pkl', 'wb')
		pickle.dump(extr_obj, output)
		output.close()
		
		if int_lng == 'Russian':
			msg = "Данные 'extrusion' успешно сохранены"
		elif int_lng == 'English':
			msg = "The 'extrusion' data was successfully saved"

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

	###---------------------Запуск сохранения файла foamyQuadMeshDict-------------------------###			
			
	def on_btnSave_clicked(self):
		foamyQuadMeshDict_generation_class.foamyQuadMeshDict_func(int_lng, parn, tab, gTCT_edit, sCF_edit, s_edit, prj_path, mesh_name_txt, pd_2, self)
	             