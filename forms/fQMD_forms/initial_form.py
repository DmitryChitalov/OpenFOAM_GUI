# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class initial_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2): 
		initial_obj = None
		
		#----------------Если файл initial.pkl существует, получаем данные из него для вывода в форму---------------#

		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
			input = open(initial_path_file, 'rb')
			initial_obj = pickle.load(input)
			input.close()
			
			geometry_visible = True
			surfaceConformation_visible = True
			motionControl_visible = True	
			shortEdgeFilter_visible = True
			extrusion_visible = True
			surfaceFeatureExtractDict_visible = True
		else:
			geometry_visible = False
			surfaceConformation_visible = False
			motionControl_visible = False
			shortEdgeFilter_visible = False
			extrusion_visible = False
			surfaceFeatureExtractDict_visible = False
		
		#-----------------------Формируем внешний вид формы для файла initial.pkl----------------------#	
		
		main_lbl = QtGui.QLabel()
		
		#######################################Список названий параметров###############################	
		
		g_key = QtGui.QLabel("geometry")
		gTCT_key = QtGui.QLabel("geometryToConformTo")
		sCF_key = QtGui.QLabel("shapeControlFunctions")
		s_key = QtGui.QLabel("surfaces for extract")
		
		#######################################Список описаний параметров###############################	

		g_lbl = QtGui.QLabel()
		gTCT_lbl = QtGui.QLabel()
		sCF_lbl = QtGui.QLabel()
		s_lbl = QtGui.QLabel()
		
		#####################Список элементов управления для значений параметров########################	
				
		g_edit = QtGui.QSpinBox()
		g_edit.setRange(1, 1000)
		g_hbox = QtGui.QHBoxLayout()
		g_hbox.setContentsMargins(0, 2, 0, 0)
		g_hbox.addWidget(g_edit)
		g_hbox.setAlignment(QtCore.Qt.AlignCenter)
		g_cell_widget = QtGui.QWidget()
		g_cell_widget.setLayout(g_hbox)
		if initial_obj != None:
			g_edit.setValue(initial_obj['g'])
		
		gTCT_edit = QtGui.QCheckBox()
		gTCT_hbox = QtGui.QHBoxLayout()
		gTCT_hbox.setContentsMargins(0, 0, 0, 0)
		gTCT_hbox.addWidget(gTCT_edit)
		gTCT_hbox.setAlignment(QtCore.Qt.AlignCenter)
		gTCT_cell_widget = QtGui.QWidget()
		gTCT_cell_widget.setLayout(gTCT_hbox)
		gTCT_val = QtGui.QSpinBox()
		gTCT_val.setRange(1, 1000)
		gTCT_val_hbox = QtGui.QHBoxLayout()
		gTCT_val_hbox.setContentsMargins(0, 0, 0, 0)
		gTCT_val_hbox.addWidget(gTCT_val)
		gTCT_val_hbox.setAlignment(QtCore.Qt.AlignCenter)
		gTCT_val_cell_widget = QtGui.QWidget()
		gTCT_val_cell_widget.setLayout(gTCT_val_hbox)
		gTCT_val.setEnabled(False)
		if initial_obj != None:
			if initial_obj['gTCT'] == True:
				gTCT_edit.setChecked(True)
				gTCT_val.setEnabled(True)
				gTCT_val.setValue(initial_obj['gTCT_val'])	
		
		sCF_edit = QtGui.QCheckBox()
		sCF_hbox = QtGui.QHBoxLayout()
		sCF_hbox.setContentsMargins(0, 0, 0, 0)
		sCF_hbox.addWidget(sCF_edit)
		sCF_hbox.setAlignment(QtCore.Qt.AlignCenter)
		sCF_cell_widget = QtGui.QWidget()
		sCF_cell_widget.setLayout(sCF_hbox)
		sCF_val = QtGui.QSpinBox()
		sCF_val.setRange(1, 1000)
		sCF_val_hbox = QtGui.QHBoxLayout()
		sCF_val_hbox.setContentsMargins(0, 0, 0, 0)
		sCF_val_hbox.addWidget(sCF_val)
		sCF_val_hbox.setAlignment(QtCore.Qt.AlignCenter)
		sCF_val_cell_widget = QtGui.QWidget()
		sCF_val_cell_widget.setLayout(sCF_val_hbox)
		sCF_val.setEnabled(False)
		if initial_obj != None:
			if initial_obj['sCF'] == True:
				sCF_edit.setChecked(True)
				sCF_val.setEnabled(True)
				sCF_val.setValue(initial_obj['sCF_val'])	
				
		s_edit = QtGui.QCheckBox()
		s_hbox = QtGui.QHBoxLayout()
		s_hbox.setContentsMargins(0, 0, 0, 0)
		s_hbox.addWidget(s_edit)
		s_hbox.setAlignment(QtCore.Qt.AlignCenter)
		s_cell_widget = QtGui.QWidget()
		s_cell_widget.setLayout(s_hbox)
		s_val = QtGui.QSpinBox()
		s_val.setRange(1, 1000)
		s_val_hbox = QtGui.QHBoxLayout()
		s_val_hbox.setContentsMargins(0, 0, 0, 0)
		s_val_hbox.addWidget(s_val)
		s_val_hbox.setAlignment(QtCore.Qt.AlignCenter)
		s_val_cell_widget = QtGui.QWidget()
		s_val_cell_widget.setLayout(s_val_hbox)
		s_val.setEnabled(False)
		if initial_obj != None:
			if initial_obj['s'] == True:
				s_edit.setChecked(True)
				s_val.setEnabled(True)
			s_val.setValue(initial_obj['s_val'])	
		
		g_edit.setFixedSize(70, 22) 
		gTCT_val.setFixedSize(100, 22) 
		sCF_val.setFixedSize(100, 22) 
		s_val.setFixedSize(100, 22) 
		
		############################################Таблица параметров##################################
		
		initial_table = QtGui.QTableWidget()
		initial_table.setFixedSize(730, 150)
		initial_table.setRowCount(4)
		initial_table.setColumnCount(4)
		
		initial_table.horizontalHeader().resizeSection(0, 155)
		initial_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
		column_1 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(0, column_1)
		initial_table.horizontalHeader().setStyleSheet("color: steelblue")

		initial_table.horizontalHeader().resizeSection(1, 360)
		initial_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
		column_2 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(1, column_2)
		
		initial_table.horizontalHeader().resizeSection(2, 75)
		initial_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
		column_3 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(2, column_3)
		
		initial_table.horizontalHeader().resizeSection(3, 120)
		initial_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
		column_4 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(3, column_4)		
		
		initial_table.setCellWidget(0,0, g_key)
		initial_table.setCellWidget(0,1, g_lbl)
		initial_table.setCellWidget(0,2, g_cell_widget)
		
		initial_table.setCellWidget(1,0, gTCT_key)
		initial_table.setCellWidget(1,1, gTCT_lbl)
		initial_table.setCellWidget(1,2, gTCT_cell_widget)
		initial_table.setCellWidget(1,3, gTCT_val_cell_widget)
		
		initial_table.setCellWidget(2,0, sCF_key)
		initial_table.setCellWidget(2,1, sCF_lbl)
		initial_table.setCellWidget(2,2, sCF_cell_widget)
		initial_table.setCellWidget(2,3, sCF_val_cell_widget)
		
		initial_table.setCellWidget(3,0, s_key)
		initial_table.setCellWidget(3,1, s_lbl)
		initial_table.setCellWidget(3,2, s_cell_widget)
		initial_table.setCellWidget(3,3, s_val_cell_widget)
		
        # -----------------------------Кнопка сохранения--------------------------#

		initial_btnSave = QtGui.QPushButton()
		initial_btnSave.setFixedSize(80, 25)

		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(initial_btnSave)
		
		# ----------------------Определяем параметры интерфейса окна--------------#
		
		if int_lng == 'Russian':
			
			main_lbl.setText("Начальные данные")
			
			column_1.setText("Параметр")
			column_2.setText("Описание")
			column_3.setText("Значение")
			column_4.setText("Дополнительно")
			
			g_lbl.setText("Количество используемых геометрий")
			gTCT_lbl.setText("Количество конформаций поверхностей")
			sCF_lbl.setText("Количество функций управления фигурами")
			s_lbl.setText("Количество поверхностей при извлечении краевой сетки")
			
			initial_btnSave.setText("Записать")
			
		elif int_lng == 'English':
			
			main_lbl.setText("Initial data")
			
			column_1.setText("Parameter")
			column_2.setText("Description")
			column_3.setText("Value")
			column_4.setText("Additionally")
			
			g_lbl.setText("Number of used geometries")
			gTCT_lbl.setText("Number of surfaces conformations")
			sCF_lbl.setText("Number of shape control functions")
			s_lbl.setText("Number of surfaces when removing the edge mesh")
			
			initial_btnSave.setText("Write")
			
        # -------------------------Групповой элемент формы---------------------------#

		initial_grid = QtGui.QGridLayout()
		initial_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.addWidget(initial_table, 1, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.setRowStretch(3, 6)

		initial_group = QtGui.QGroupBox()
		initial_group.setLayout(initial_grid)
		#print(initial_group)
		return initial_group, initial_btnSave, geometry_visible, surfaceConformation_visible, motionControl_visible, shortEdgeFilter_visible, extrusion_visible, surfaceFeatureExtractDict_visible, g_edit, gTCT_edit, gTCT_val, sCF_edit, sCF_val, s_edit, s_val
	

	
	
