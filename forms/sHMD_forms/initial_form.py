# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class initial_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2): 
		obj = None
		
		#----------------Если файл initial.pkl существует, получаем данные из него для вывода в форму---------------#

		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			geometry_visible = True
			castellatedMC_visible = True
			snapC_visible = True
			layers_visible = True
			meshQC_visible = True
				
		else:
			geometry_visible = False
			castellatedMC_visible = False
			snapC_visible = False
			layers_visible = False
			meshQC_visible = False
		
		#-----------------------Формируем внешний вид формы для файла initial.pkl----------------------#	
		
		main_lbl = QtGui.QLabel()
		
		#######################################Список названий параметров###############################	
		
		cM_key = QtGui.QLabel("castellatedMesh")
		s_key = QtGui.QLabel("snap") 
		aL_key = QtGui.QLabel("addLayers") 
		mT_key = QtGui.QLabel("mergeTolerance") 
		g_key = QtGui.QLabel("geometry")
		f_key = QtGui.QLabel("features")
		rS_key = QtGui.QLabel("refinementSurfaces")
		rR_key = QtGui.QLabel("refinementRegions")
		l_key = QtGui.QLabel("layers")
		
		###flags###
		sL_flag = QtGui.QLabel("scalarLevels")
		lS_flag = QtGui.QLabel("layerSets")
		lF_flag = QtGui.QLabel("layerFields")
		
		#######################################Список описаний параметров###############################	

		cM_lbl = QtGui.QLabel()
		s_lbl = QtGui.QLabel() 
		aL_lbl = QtGui.QLabel() 
		mT_lbl = QtGui.QLabel() 
		g_lbl = QtGui.QLabel()
		f_lbl = QtGui.QLabel()
		rS_lbl = QtGui.QLabel()
		rR_lbl = QtGui.QLabel()
		l_lbl = QtGui.QLabel()
		
		###flags###
		sL_lbl = QtGui.QLabel()
		lS_lbl = QtGui.QLabel()
		lF_lbl = QtGui.QLabel()
		
		#####################Список элементов управления для значений параметров########################	

		cM_edit = QtGui.QCheckBox()
		cM_hbox = QtGui.QHBoxLayout()
		cM_hbox.setContentsMargins(0, 0, 0, 0)
		cM_hbox.addWidget(cM_edit)
		cM_hbox.setAlignment(QtCore.Qt.AlignCenter)
		cM_cell_widget = QtGui.QWidget()
		cM_cell_widget.setLayout(cM_hbox)
		if obj != None:
			if obj['cM'] == 'true':
				cM_edit.setChecked(True)
			elif obj['cM'] == 'false':
				cM_edit.setChecked(False)
				
		s_edit = QtGui.QCheckBox()
		s_hbox = QtGui.QHBoxLayout()
		s_hbox.setContentsMargins(0, 0, 0, 0)
		s_hbox.addWidget(s_edit)
		s_hbox.setAlignment(QtCore.Qt.AlignCenter)
		s_cell_widget = QtGui.QWidget()
		s_cell_widget.setLayout(s_hbox)
		if obj != None:
			if obj['s'] == 'true':
				s_edit.setChecked(True)
			elif obj['s'] == 'false':
				s_edit.setChecked(False)
		
		aL_edit = QtGui.QCheckBox()
		aL_hbox = QtGui.QHBoxLayout()
		aL_hbox.setContentsMargins(0, 0, 0, 0)
		aL_hbox.addWidget(aL_edit)
		aL_hbox.setAlignment(QtCore.Qt.AlignCenter)
		aL_cell_widget = QtGui.QWidget()
		aL_cell_widget.setLayout(aL_hbox)
		if obj != None:
			if obj['al'] == 'true':
				aL_edit.setChecked(True)
			elif obj['al'] == 'false':
				aL_edit.setChecked(False)
		
		mT_edit = QtGui.QLineEdit()
		mT_edit.setText("1E-06")
		mT_edit.setInputMask("9E-99;_")
		mT_hbox = QtGui.QHBoxLayout()
		mT_hbox.setContentsMargins(0, 2, 0, 0)
		mT_hbox.addWidget(mT_edit)
		mT_hbox.setAlignment(QtCore.Qt.AlignCenter)
		mT_cell_widget = QtGui.QWidget()
		mT_cell_widget.setLayout(mT_hbox)
		if obj != None:
			if obj['mT'] == True:
				mT_edit.setText(obj['mT'])
				
		g_edit = QtGui.QSpinBox()
		g_edit.setRange(1, 1000)
		g_hbox = QtGui.QHBoxLayout()
		g_hbox.setContentsMargins(0, 2, 0, 0)
		g_hbox.addWidget(g_edit)
		g_hbox.setAlignment(QtCore.Qt.AlignCenter)
		g_cell_widget = QtGui.QWidget()
		g_cell_widget.setLayout(g_hbox)
		if obj != None:
			g_edit.setValue(obj['g'])
				
		f_edit = QtGui.QCheckBox()
		f_hbox = QtGui.QHBoxLayout()
		f_hbox.setContentsMargins(0, 0, 0, 0)
		f_hbox.addWidget(f_edit)
		f_hbox.setAlignment(QtCore.Qt.AlignCenter)
		f_cell_widget = QtGui.QWidget()
		f_cell_widget.setLayout(f_hbox)
		f_val = QtGui.QSpinBox()
		f_val.setRange(1, 1000)
		f_val_hbox = QtGui.QHBoxLayout()
		f_val_hbox.setContentsMargins(0, 0, 0, 0)
		f_val_hbox.addWidget(f_val)
		f_val_hbox.setAlignment(QtCore.Qt.AlignCenter)
		f_val_cell_widget = QtGui.QWidget()
		f_val_cell_widget.setLayout(f_val_hbox)
		f_val.setEnabled(False)
		if obj != None:
			if obj['f'] == True:
				f_edit.setChecked(True)
				f_val.setEnabled(True)
				f_val.setValue(obj['f_val'])
		
		rS_edit = QtGui.QCheckBox()
		rS_hbox = QtGui.QHBoxLayout()
		rS_hbox.setContentsMargins(0, 0, 0, 0)
		rS_hbox.addWidget(rS_edit)
		rS_hbox.setAlignment(QtCore.Qt.AlignCenter)
		rS_cell_widget = QtGui.QWidget()
		rS_cell_widget.setLayout(rS_hbox)
		rS_val = QtGui.QSpinBox()
		rS_val.setRange(1, 1000)
		rS_val_hbox = QtGui.QHBoxLayout()
		rS_val_hbox.setContentsMargins(0, 0, 0, 0)
		rS_val_hbox.addWidget(rS_val)
		rS_val_hbox.setAlignment(QtCore.Qt.AlignCenter)
		rS_val_cell_widget = QtGui.QWidget()
		rS_val_cell_widget.setLayout(rS_val_hbox)
		rS_val.setEnabled(False)
		if obj != None:
			if obj['rS'] == True:
				rS_edit.setChecked(True)
				rS_val.setEnabled(True)
				rS_val.setValue(obj['rS_val'])	
		
		rR_edit = QtGui.QCheckBox()
		rR_hbox = QtGui.QHBoxLayout()
		rR_hbox.setContentsMargins(0, 0, 0, 0)
		rR_hbox.addWidget(rR_edit)
		rR_hbox.setAlignment(QtCore.Qt.AlignCenter)
		rR_cell_widget = QtGui.QWidget()
		rR_cell_widget.setLayout(rR_hbox)
		rR_val = QtGui.QSpinBox()
		rR_val.setRange(1, 1000)
		rR_val_hbox = QtGui.QHBoxLayout()
		rR_val_hbox.setContentsMargins(0, 0, 0, 0)
		rR_val_hbox.addWidget(rR_val)
		rR_val_hbox.setAlignment(QtCore.Qt.AlignCenter)
		rR_val_cell_widget = QtGui.QWidget()
		rR_val_cell_widget.setLayout(rR_val_hbox)
		rR_val.setEnabled(False)
		if obj != None:
			if obj['rR'] == True:
				rR_edit.setChecked(True)
				rR_val.setEnabled(True)
				rR_val.setValue(obj['rR_val'])		
			
		l_edit = QtGui.QSpinBox()
		l_edit.setRange(1, 1000)
		l_hbox = QtGui.QHBoxLayout()
		l_hbox.setContentsMargins(0, 2, 0, 0)
		l_hbox.addWidget(l_edit)
		l_hbox.setAlignment(QtCore.Qt.AlignCenter)
		l_cell_widget = QtGui.QWidget()
		l_cell_widget.setLayout(l_hbox)
		if obj != None:
			l_edit.setValue(obj['l'])
			
		sL_edit = QtGui.QCheckBox()
		sL_hbox = QtGui.QHBoxLayout()
		sL_hbox.setContentsMargins(0, 0, 0, 0)
		sL_hbox.addWidget(sL_edit)
		sL_hbox.setAlignment(QtCore.Qt.AlignCenter)
		sL_cell_widget = QtGui.QWidget()
		sL_cell_widget.setLayout(sL_hbox)
		if obj != None:
			if obj['sL_flag'] == True:
				sL_edit.setChecked(True)
			elif obj['sL_flag'] == False:
				sL_edit.setChecked(False)
				
		lS_edit = QtGui.QCheckBox()
		lS_hbox = QtGui.QHBoxLayout()
		lS_hbox.setContentsMargins(0, 0, 0, 0)
		lS_hbox.addWidget(lS_edit)
		lS_hbox.setAlignment(QtCore.Qt.AlignCenter)
		lS_cell_widget = QtGui.QWidget()
		lS_cell_widget.setLayout(lS_hbox)
		if obj != None:
			if obj['lS_flag'] == True:
				lS_edit.setChecked(True)
			elif obj['lS_flag'] == False:
				lS_edit.setChecked(False)
				
		lF_edit = QtGui.QCheckBox()
		lF_hbox = QtGui.QHBoxLayout()
		lF_hbox.setContentsMargins(0, 0, 0, 0)
		lF_hbox.addWidget(lF_edit)
		lF_hbox.setAlignment(QtCore.Qt.AlignCenter)
		lF_cell_widget = QtGui.QWidget()
		lF_cell_widget.setLayout(lF_hbox)
		if obj != None:
			if obj['lF_flag'] == True:
				lF_edit.setChecked(True)
			elif obj['lF_flag'] == False:
				lF_edit.setChecked(False)
		
		mT_edit.setFixedSize(90, 22)
		g_edit.setFixedSize(100, 22) 
		f_val.setFixedSize(100, 22)
		rS_val.setFixedSize(100, 22)
		rR_val.setFixedSize(100, 22)
		l_edit.setFixedSize(100, 22)
		
		############################################Таблица параметров##################################
		
		initial_table = QtGui.QTableWidget()
		initial_table.setFixedSize(700, 390)
		initial_table.setRowCount(12)
		initial_table.setColumnCount(4)
		
		initial_table.horizontalHeader().resizeSection(0, 120)
		initial_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
		column_1 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(0, column_1)
		initial_table.horizontalHeader().setStyleSheet("color: steelblue")

		initial_table.horizontalHeader().resizeSection(1, 330)
		initial_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
		column_2 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(1, column_2)
		
		initial_table.horizontalHeader().resizeSection(2, 100)
		initial_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
		column_3 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(2, column_3)
		
		initial_table.horizontalHeader().resizeSection(3, 120)
		initial_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
		column_4 = QtGui.QTableWidgetItem()
		initial_table.setHorizontalHeaderItem(3, column_4)		
		
		initial_table.setCellWidget(0,0, cM_key)
		initial_table.setCellWidget(0,1, cM_lbl)
		initial_table.setCellWidget(0,2, cM_cell_widget)
		
		initial_table.setCellWidget(1,0, s_key)
		initial_table.setCellWidget(1,1, s_lbl)
		initial_table.setCellWidget(1,2, s_cell_widget)
		
		initial_table.setCellWidget(2,0, aL_key)
		initial_table.setCellWidget(2,1, aL_lbl)
		initial_table.setCellWidget(2,2, aL_cell_widget)
		
		initial_table.setCellWidget(3,0, mT_key)
		initial_table.setCellWidget(3,1, mT_lbl)
		initial_table.setCellWidget(3,2, mT_cell_widget)
		
		initial_table.setCellWidget(4,0, g_key)
		initial_table.setCellWidget(4,1, g_lbl)
		initial_table.setCellWidget(4,2, g_cell_widget)
		
		initial_table.setCellWidget(5,0, f_key)
		initial_table.setCellWidget(5,1, f_lbl)
		initial_table.setCellWidget(5,2, f_cell_widget)
		initial_table.setCellWidget(5,3, f_val_cell_widget)
		
		initial_table.setCellWidget(6,0, rS_key)
		initial_table.setCellWidget(6,1, rS_lbl)
		initial_table.setCellWidget(6,2, rS_cell_widget)
		initial_table.setCellWidget(6,3, rS_val_cell_widget)

		initial_table.setCellWidget(7,0, rR_key)
		initial_table.setCellWidget(7,1, rR_lbl)
		initial_table.setCellWidget(7,2, rR_cell_widget)
		initial_table.setCellWidget(7,3, rR_val_cell_widget)
		
		initial_table.setCellWidget(8,0, l_key)
		initial_table.setCellWidget(8,1, l_lbl)
		initial_table.setCellWidget(8,2, l_cell_widget)
		
		initial_table.setCellWidget(9,0, sL_flag)
		initial_table.setCellWidget(9,1, sL_lbl)
		initial_table.setCellWidget(9,2, sL_cell_widget)
		
		initial_table.setCellWidget(10,0, lS_flag)
		initial_table.setCellWidget(10,1, lS_lbl)
		initial_table.setCellWidget(10,2, lS_cell_widget)
		
		initial_table.setCellWidget(11,0, lF_flag)
		initial_table.setCellWidget(11,1, lF_lbl)
		initial_table.setCellWidget(11,2, lF_cell_widget)
		
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
			
			cM_lbl.setText("Сформировать зубчатую сетку")
			s_lbl.setText("Осуществить привязку к поверхности") 
			aL_lbl.setText("Добавить поверхностные слои") 
			
			mT_lbl.setText("Параметр объединения допусков") 
			mT_edit.setToolTip("Введите значение по маске")
			
			g_lbl.setText("Количество используемых геометрий")
			f_lbl.setText("Количество элементов для измельчения")
			rS_lbl.setText("Количество поверхностей для измельчения")
			rR_lbl.setText("Количество областей для измельчения")
			l_lbl.setText("Количество слоев")
			
			sL_lbl.setText("Записать volScalarField с cellLevel для постобработки")
			lS_lbl.setText("Записать cellSets, faceSets граней в слое")
			lF_lbl.setText("Записать volScalarField для покрытия слоя")
			
			initial_btnSave.setText("Записать")
			
		elif int_lng == 'English':
			
			main_lbl.setText("Initial data")
			
			column_1.setText("Parameter")
			column_2.setText("Description")
			column_3.setText("Value")
			column_4.setText("Additionally")
			
			cM_lbl.setText("Form a toothed mesh")
			s_lbl.setText("Link to the surface") 
			aL_lbl.setText("Add surface layers") 
			
			mT_lbl.setText("Tolerance merging parameter") 
			mT_edit.setToolTip("Enter a value by mask")
			
			g_lbl.setText("Number of used geometries")
			f_lbl.setText("Number of elements for grinding")
			rS_lbl.setText("Number of surfaces for grinding")
			rR_lbl.setText("Number of areas for grinding")
			l_lbl.setText("Number of layers")
			
			sL_lbl.setText("Write volScalarField with cellLevel for postprocessing")
			lS_lbl.setText("Write cellSets, faceSets of faces in layer")
			lF_lbl.setText("Write volScalarField for layer coverage")
			
			initial_btnSave.setText("Write")
			
        # -------------------------Групповой элемент формы---------------------------#

		initial_grid = QtGui.QGridLayout()
		initial_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.addWidget(initial_table, 1, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.setRowStretch(3, 6)

		initial_group = QtGui.QGroupBox()
		initial_group.setLayout(initial_grid)
			
		return initial_group, initial_btnSave, geometry_visible, castellatedMC_visible, snapC_visible, layers_visible, meshQC_visible, cM_edit, s_edit, aL_edit, mT_edit, sL_edit, lS_edit, lF_edit, g_edit, f_edit, f_val, rS_edit, rS_val, rR_edit, rR_val, l_edit

	
	
