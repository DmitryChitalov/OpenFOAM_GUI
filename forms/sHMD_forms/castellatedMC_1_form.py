# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class castellatedMC_1_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, castellatedMC_visible): 
		castellatedMC_1_obj = None
		
		#----------------Если файл castellatedMC_1.pkl существует, получаем данные из него для вывода в форму---------------#

		if castellatedMC_visible == True:
			castellatedMC_1_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_1.pkl'
			if os.path.exists(castellatedMC_1_path_file):
		
				input = open(castellatedMC_1_path_file, 'rb')
				castellatedMC_1_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла castellatedMC_1.pkl на основе данных файла initial.pkl-------------#
		
		prs_grid = QtGui.QGridLayout()
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(prs_grid)
		
		#####-----------------------Первая часть параметров------------------------------#####
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Параметры для зубчатой сетки")
		elif int_lng == 'English':
			main_lbl.setText("Parameters for toothed mesh")
			
		#maxGlobalCells#
		mGC_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mGC_lbl.setText("Общий предел ячеек во время измельчения (maxGlobalCells):")
		elif int_lng == 'English':
			mGC_lbl.setText("The total limit of the cells during grinding (maxGlobalCells):")
		mGC_edit = QtGui.QSpinBox()
		mGC_edit.setRange(0, 100000000000)
		mGC_edit.setFixedSize(100, 25)
		if castellatedMC_1_obj != None:
			mGC_edit.setValue(castellatedMC_1_obj['cMC_start_prs']['mGC'])

		#maxLocalCells#
		mLC_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mLC_lbl.setText("Макс. число ячеек на процессор во время измельчения (maxLocalCells):")
		elif int_lng == 'English':
			mLC_lbl.setText("Maximum number of cells per processor during grinding (maxLocalCells):")
		mLC_edit = QtGui.QSpinBox()
		mLC_edit.setRange(0, 100000000000)
		mLC_edit.setFixedSize(100, 25)
		if castellatedMC_1_obj != None:
			mLC_edit.setValue(castellatedMC_1_obj['cMC_start_prs']['mLC'])

		#minRefinementCells#
		mRC_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mRC_lbl.setText("Минимальное число усточняющих ячеек (minRefinementCells):")
		elif int_lng == 'English':
			mRC_lbl.setText("Minimum number of settling cells (minRefinementCells):")
		mRC_edit = QtGui.QSpinBox()
		mRC_edit.setRange(0, 100000000000)
		mRC_edit.setFixedSize(100, 25)
		if castellatedMC_1_obj != None:
			mRC_edit.setValue(castellatedMC_1_obj['cMC_start_prs']['mRC'])

		#nCellsBetweenLevels#
		nCBL_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			nCBL_lbl.setText("Число буферных слоев между уровнями измельчения (nCellsBetweenLevels):")
		elif int_lng == 'English':
			nCBL_lbl.setText("Number of buffer layers between levels of grinding (nCellsBetweenLevels):")
		nCBL_edit = QtGui.QSpinBox()
		nCBL_edit.setRange(0, 100000000000)
		nCBL_edit.setFixedSize(100, 25)
		if castellatedMC_1_obj != None:
			nCBL_edit.setValue(castellatedMC_1_obj['cMC_start_prs']['nCBL'])

		#resolveFeatureAngle#
		rFA_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			rFA_lbl.setText("Максимальный уровень измельчения ячеек (resolveFeatureAngle):")
		elif int_lng == 'English':
			rFA_lbl.setText("The maximum level of grinding of cells (resolveFeatureAngle):")
		rFA_edit = QtGui.QSpinBox()
		rFA_edit.setRange(0, 100000000000)
		rFA_edit.setFixedSize(100, 25)
		if castellatedMC_1_obj != None:
			rFA_edit.setValue(castellatedMC_1_obj['cMC_start_prs']['rFA'])

		#allowFreeStandingZoneFaces#
		aFSZF_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			aFSZF_lbl.setText("Максимальный уровень измельчения ячеек (allowFreeStandingZoneFaces):")
		elif int_lng == 'English':
			aFSZF_lbl.setText("The maximum level of grinding of cells (allowFreeStandingZoneFaces):")
		aFSZF_edit = QtGui.QComboBox()
		aFSZF_l = ["true", "false"]
		aFSZF_edit.addItems(aFSZF_l)
		aFSZF_edit.setFixedSize(100, 25)
		if castellatedMC_1_obj != None:
			aFSZF_edit_mas = aFSZF_edit.count()  
			for t in range(aFSZF_edit_mas):
				if aFSZF_edit.itemText(t) == castellatedMC_1_obj['cMC_start_prs']['aFSZF']:
					aFSZF_edit.setCurrentIndex(t)
					
		#locationInMesh#
		lIM_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			lIM_lbl.setText("Вектор местоположения внутри области - сетки (locationInMesh):")
		elif int_lng == 'English':
			lIM_lbl.setText("Location vector inside the region to be meshed (locationInMesh):")
			
		lIM_edit_x = QtGui.QLineEdit()
		lIM_edit_x.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_x))
		lIM_edit_x.setFixedSize(80, 25)
		lIM_edit_y = QtGui.QLineEdit()
		lIM_edit_y.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_y))
		lIM_edit_y.setFixedSize(80, 25)
		lIM_edit_z = QtGui.QLineEdit()
		lIM_edit_z.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_z))
		lIM_edit_z.setFixedSize(80, 25)
		if castellatedMC_1_obj != None:
			lIM_edit_x.setText(castellatedMC_1_obj['cMC_start_prs']['lIM'][0])
			lIM_edit_y.setText(castellatedMC_1_obj['cMC_start_prs']['lIM'][1])
			lIM_edit_z.setText(castellatedMC_1_obj['cMC_start_prs']['lIM'][2])
		
		cMC_start_prs_grid = QtGui.QGridLayout()
		cMC_start_prs_grid.addWidget(mGC_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(mGC_edit, 0, 1, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(mLC_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(mLC_edit, 1, 1, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(mRC_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(mRC_edit, 2, 1, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(nCBL_lbl, 3, 0, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(nCBL_edit, 3, 1, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(rFA_lbl, 4, 0, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(rFA_edit, 4, 1, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(aFSZF_lbl, 5, 0, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(aFSZF_edit, 5, 1, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(lIM_lbl, 6, 0, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(lIM_edit_x, 6, 1, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(lIM_edit_y, 6, 2, alignment=QtCore.Qt.AlignCenter)
		cMC_start_prs_grid.addWidget(lIM_edit_z, 6, 3, alignment=QtCore.Qt.AlignCenter)
		
		prs_grid.addLayout(cMC_start_prs_grid, 0, 0, alignment=QtCore.Qt.AlignCenter)
		
		tri_distirbTri_list = []
		tri_distirbTri_geometry_list = []
		other_geometry_list = []
		other_geometry_list_geom = []
		
		#####-----------------------Вторая часть параметров-features------------------------------#####
		
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):

			input = open(initial_path_file, 'rb')
			obj_initial = pickle.load(input)
			input.close()
				
		geometry_2_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if os.path.exists(geometry_2_path_file):

			input = open(geometry_2_path_file, 'rb')
			obj_2_geometry = pickle.load(input)
			input.close()
				
			i = 1			
			for el in obj_2_geometry:
				if el['geometry_' + str(i)] == 'Tri-surface' or el['geometry_' + str(i)] == 'Три-поверхность' or el['geometry_' + str(i)] == 'Distributed tri-surface' or el['geometry_' + str(i)] == 'Распределенная три-поверхность':
					tri_distirbTri_list.append(True)
					tri_distirbTri_geometry_list.append(el['file'])
					other_geometry_list.append(False)
					#other_geometry_list_geom.append(el['file'])
				elif el['geometry_' + str(i)] == 'Base shape complex' or el['geometry_' + str(i)] == 'Набор базовых фигур':
					other_geometry_list_geom.append(el['name'])
					other_geometry_list.append(True)
				elif el['geometry_' + str(i)] == 'Base shape' or el['geometry_' + str(i)] == 'Базовая фигура':
					other_geometry_list_geom.append(el['shape'])
					other_geometry_list.append(True)
				i = i + 1
			
			f_level_single_edit_list = []
			f_level_multi_edit_list = []
			f_level_multi_val_edit_list = []

			if obj_initial['f'] == True and True in tri_distirbTri_list:
			
				cMC_f_lbl = QtGui.QLabel()	
				cMC_f_lbl.setVisible(False)
				if int_lng == 'Russian':
					cMC_f_lbl.setText("Список элементов для измельчения:")
				elif int_lng == 'English':
					cMC_f_lbl.setText("List of elements for grinding:")
				if castellatedMC_1_obj != None:
					if castellatedMC_1_obj['features']:
						cMC_f_lbl.setVisible(True)

				cMC_features_table = QtGui.QTableWidget()
				cMC_features_table.setVisible(False)
				cMC_features_table.setRowCount(obj_initial['f_val'])
				cMC_features_table.setColumnCount(2)
				cMC_features_table.verticalHeader().hide()
				if castellatedMC_1_obj != None:
					if castellatedMC_1_obj['features']:
						cMC_features_table.setVisible(True)

				cMC_features_table.horizontalHeader().resizeSection(0, 150)
				cMC_features_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				cMC_features_table.setHorizontalHeaderItem(0, column_1)
				cMC_features_table.horizontalHeader().setStyleSheet("color: steelblue")

				cMC_features_table.horizontalHeader().resizeSection(1, 390)
				cMC_features_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
				column_2 = QtGui.QTableWidgetItem()
				cMC_features_table.setHorizontalHeaderItem(1, column_2)
				cMC_features_table.horizontalHeader().setStyleSheet("color: steelblue")

				if int_lng == 'Russian':
					column_1.setText("Три-поверхность")
					column_2.setText("Параметры уровней")	
				elif int_lng == 'English':
					column_1.setText("Tri-surface")
					column_2.setText("Level parameters")

				nof = 1
				q = 0
				height = 60
				
				while nof <= obj_initial['f_val']:
					cMC_features_table.setFixedSize(545, height)

					#geometry#
					f_geometry_edit = QtGui.QComboBox()
					f_geometry_edit.setFixedSize(110, 25)
					f_geometry_edit.addItems(tri_distirbTri_geometry_list)
					f_geometry_hbox = QtGui.QHBoxLayout()
					f_geometry_hbox.setContentsMargins(0, 0, 0, 0)
					f_geometry_hbox.addWidget(f_geometry_edit)
					f_geometry_cell_widget = QtGui.QWidget()
					f_geometry_cell_widget.setLayout(f_geometry_hbox)
					if castellatedMC_1_obj != None:
						f_geometry_edit_mas = f_geometry_edit.count()  
						for t in range(f_geometry_edit_mas):
							if f_geometry_edit.itemText(t) == castellatedMC_1_obj['features'][q]['f_geometry']:
								f_geometry_edit.setCurrentIndex(t)

					#level_prs#
					f_level_single_lbl = QtGui.QLabel()
					f_level_multi_lbl = QtGui.QLabel()
					f_level_multi_val_lbl = QtGui.QLabel()
					f_level_multi_val_lbl.setEnabled(False)
					if int_lng == 'Russian':
						f_level_single_lbl.setText("Уровень:")
						f_level_multi_lbl.setText("Дистанция уровней:")	
						f_level_multi_val_lbl.setText("Количество:")
					elif int_lng == 'English':
						f_level_single_lbl.setText("Level:")
						f_level_multi_lbl.setText("Level distance:")
						f_level_multi_val_lbl.setText("Number:")
					f_level_single_edit = QtGui.QRadioButton()
					
					if castellatedMC_1_obj != None:
						f_level_single_edit.setChecked(castellatedMC_1_obj['features'][q]['f_level_single'])
					else:
						f_level_single_edit.setChecked(True)
					
					f_level_single_edit_list.append(f_level_single_edit)
					f_level_multi_edit = QtGui.QRadioButton()
					f_level_multi_edit_list.append(f_level_multi_edit)
					if castellatedMC_1_obj != None:
						f_level_multi_edit.setChecked(castellatedMC_1_obj['features'][q]['f_level_multi'])

					f_level_multi_val_edit = QtGui.QSpinBox()
					f_level_multi_val_edit.setFixedSize(50, 25)
					f_level_multi_val_edit.setRange(1, 1000)
					f_level_multi_val_edit.setEnabled(False)
					f_level_multi_val_edit_list.append(f_level_multi_val_edit)
					if castellatedMC_1_obj != None:
						if castellatedMC_1_obj['features'][q]['f_level_multi'] == True:
							f_level_multi_val_edit.setEnabled(True)
							f_level_multi_val_lbl.setEnabled(True)
							f_level_multi_val_edit.setValue(castellatedMC_1_obj['features'][q]['f_level_multi_val'])

					f_level_hbox = QtGui.QHBoxLayout()
					f_level_hbox.setContentsMargins(0, 0, 0, 0)
					f_level_hbox.addWidget(f_level_single_lbl)
					f_level_hbox.addWidget(f_level_single_edit)
					f_level_hbox.addWidget(f_level_multi_lbl)
					f_level_hbox.addWidget(f_level_multi_edit)
					f_level_hbox.addWidget(f_level_multi_val_lbl)
					f_level_hbox.addWidget(f_level_multi_val_edit)
					f_level_cell_widget = QtGui.QWidget()
					f_level_cell_widget.setLayout(f_level_hbox)

					cMC_features_table.setCellWidget(q, 0, f_geometry_cell_widget)
					cMC_features_table.setCellWidget(q, 1, f_level_cell_widget)

					nof = nof + 1
					q = q + 1
					height = height + 30
	
				prs_grid.addWidget(cMC_f_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
				prs_grid.addWidget(cMC_features_table, 2, 0, alignment=QtCore.Qt.AlignCenter)
				
		#####-----------------------Третья часть параметров-surfaceFeatureExtractDict------------------------------#####				

				cMC_sFED_lbl = QtGui.QLabel()
				cMC_sFED_lbl.setVisible(False)
				if int_lng == 'Russian':
					cMC_sFED_lbl.setText("Параметры извлечения поверхностей:")
				elif int_lng == 'English':
					cMC_sFED_lbl.setText("Parameters of surface extracting:")
				if castellatedMC_1_obj != None:
					cMC_sFED_lbl.setVisible(True)

				cMC_sFED_table = QtGui.QTableWidget()
				cMC_sFED_table.setVisible(False)
				cMC_sFED_table.setRowCount(obj_initial['f_val'])
				cMC_sFED_table.setColumnCount(4)
				cMC_sFED_table.verticalHeader().hide()
				if castellatedMC_1_obj != None:
					cMC_sFED_table.setVisible(True)

				cMC_sFED_table.horizontalHeader().resizeSection(0, 150)
				cMC_sFED_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				cMC_sFED_table.setHorizontalHeaderItem(0, column_1)
				cMC_sFED_table.horizontalHeader().setStyleSheet("color: steelblue")

				cMC_sFED_table.horizontalHeader().resizeSection(1, 150)
				cMC_sFED_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
				column_2 = QtGui.QTableWidgetItem()
				cMC_sFED_table.setHorizontalHeaderItem(1, column_2)
				cMC_sFED_table.horizontalHeader().setStyleSheet("color: steelblue")

				cMC_sFED_table.horizontalHeader().resizeSection(2, 120)
				cMC_sFED_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
				column_3 = QtGui.QTableWidgetItem()
				cMC_sFED_table.setHorizontalHeaderItem(2, column_3)
				cMC_sFED_table.horizontalHeader().setStyleSheet("color: steelblue")

				cMC_sFED_table.horizontalHeader().resizeSection(3, 120)
				cMC_sFED_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
				column_4 = QtGui.QTableWidgetItem()
				cMC_sFED_table.setHorizontalHeaderItem(3, column_4)
				cMC_sFED_table.horizontalHeader().setStyleSheet("color: steelblue")
					
				if int_lng == 'Russian':
					column_1.setText("Поверхность")
					column_2.setText("Метод извлечения")	
					column_3.setText("Величина угла")
					column_4.setText("Опция записи")	
				elif int_lng == 'English':
					column_1.setText("surface")
					column_2.setText("extractionMethod")
					column_3.setText("includedAngle")
					column_4.setText("writeObj")
				
				nof = 1
				q = 0
				height = 60
				while nof <= obj_initial['f_val']:
					cMC_sFED_table.setFixedSize(545, height)
					#geometry#
					sFED_geometry_edit = QtGui.QComboBox()
					sFED_geometry_edit.setFixedSize(120, 25)
					sFED_geometry_edit.addItems(tri_distirbTri_geometry_list)
					sFED_geometry_hbox = QtGui.QHBoxLayout()
					sFED_geometry_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_geometry_hbox.addWidget(sFED_geometry_edit)
					sFED_geometry_cell_widget = QtGui.QWidget()
					sFED_geometry_cell_widget.setLayout(sFED_geometry_hbox)
					if castellatedMC_1_obj != None:
						sFED_geometry_edit_mas = sFED_geometry_edit.count()  
						for t in range(sFED_geometry_edit_mas):
							if sFED_geometry_edit.itemText(t) == castellatedMC_1_obj['sFED'][q]['sFED_geometry']:
								sFED_geometry_edit.setCurrentIndex(t)

					#extractionMethod#
					sFED_extractionMethod_edit = QtGui.QComboBox()
					sFED_extractionMethod_edit.setFixedSize(140, 25)
					sFED_extractionMethod_list = ['extractFromFile', 'extractFromSurface']
					sFED_extractionMethod_edit.addItems(sFED_extractionMethod_list)
					sFED_extractionMethod_hbox = QtGui.QHBoxLayout()
					sFED_extractionMethod_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_extractionMethod_hbox.addWidget(sFED_extractionMethod_edit)
					sFED_extractionMethod_cell_widget = QtGui.QWidget()
					sFED_extractionMethod_cell_widget.setLayout(sFED_extractionMethod_hbox)
					if castellatedMC_1_obj != None:
						sFED_extractionMethod_edit_mas = sFED_extractionMethod_edit.count()  
						for t in range(sFED_extractionMethod_edit_mas):
							if sFED_extractionMethod_edit.itemText(t) == castellatedMC_1_obj['sFED'][q]['sFED_extractionMethod']:
								sFED_extractionMethod_edit.setCurrentIndex(t)

					#includedAngle#
					sFED_includedAngle_edit = QtGui.QSpinBox()
					sFED_includedAngle_edit.setFixedSize(50, 25)
					sFED_includedAngle_edit.setRange(1, 1000)
					sFED_includedAngle_hbox = QtGui.QHBoxLayout()
					sFED_includedAngle_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_includedAngle_hbox.addWidget(sFED_includedAngle_edit)
					sFED_includedAngle_cell_widget = QtGui.QWidget()
					sFED_includedAngle_cell_widget.setLayout(sFED_includedAngle_hbox)
					if castellatedMC_1_obj != None:
						sFED_includedAngle_edit.setValue(castellatedMC_1_obj['sFED'][q]['sFED_includedAngle'])

					#writeObj#
					sFED_writeObj_edit = QtGui.QComboBox()
					sFED_writeObj_edit.setFixedSize(50, 25)
					sFED_writeObj_list = ['yes', 'no']
					sFED_writeObj_edit.addItems(sFED_writeObj_list)
					sFED_writeObj_hbox = QtGui.QHBoxLayout()
					sFED_writeObj_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_writeObj_hbox.addWidget(sFED_writeObj_edit)
					sFED_writeObj_cell_widget = QtGui.QWidget()
					sFED_writeObj_cell_widget.setLayout(sFED_writeObj_hbox)
					if castellatedMC_1_obj != None:
						sFED_writeObj_edit_mas = sFED_writeObj_edit.count()  
						for t in range(sFED_writeObj_edit_mas):
							if sFED_writeObj_edit.itemText(t) == castellatedMC_1_obj['sFED'][q]['sFED_writeObj']:
								sFED_writeObj_edit.setCurrentIndex(t)

					cMC_sFED_table.setCellWidget(q, 0, sFED_geometry_cell_widget)
					cMC_sFED_table.setCellWidget(q, 1, sFED_extractionMethod_cell_widget)
					cMC_sFED_table.setCellWidget(q, 2, sFED_includedAngle_cell_widget)
					cMC_sFED_table.setCellWidget(q, 3, sFED_writeObj_cell_widget)
					
					nof = nof + 1
					q = q + 1
					height = height + 30
				
				prs_grid.addWidget(cMC_sFED_lbl, 3, 0, alignment=QtCore.Qt.AlignCenter)
				prs_grid.addWidget(cMC_sFED_table, 4, 0, alignment=QtCore.Qt.AlignCenter)
			
			#####-----------------------Четвертая часть параметров-refinementSurfaces------------------------------#####
			rS_regions_edit_list = []
			rS_regions_val_edit_list = []
			if obj_initial['rS'] == True and True in tri_distirbTri_list:				
					
				cMC_rS_lbl = QtGui.QLabel()	
				cMC_rS_lbl.setVisible(False)
				if int_lng == 'Russian':
					cMC_rS_lbl.setText("Cловарь поверхностей для измельчения:")
				elif int_lng == 'English':
					cMC_rS_lbl.setText("Set of surfaces for grinding:")
				if castellatedMC_1_obj != None:
					cMC_rS_lbl.setVisible(True)

				cMC_refinementSurfaces_table = QtGui.QTableWidget()
				cMC_refinementSurfaces_table.setVisible(False)
				cMC_refinementSurfaces_table.setRowCount(obj_initial['rS_val'])
				cMC_refinementSurfaces_table.setColumnCount(3)
				cMC_refinementSurfaces_table.verticalHeader().hide()
				if castellatedMC_1_obj != None:
					cMC_refinementSurfaces_table.setVisible(True)

				cMC_refinementSurfaces_table.horizontalHeader().resizeSection(0, 125)
				cMC_refinementSurfaces_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				cMC_refinementSurfaces_table.setHorizontalHeaderItem(0, column_1)
				cMC_refinementSurfaces_table.horizontalHeader().setStyleSheet("color: steelblue")

				cMC_refinementSurfaces_table.horizontalHeader().resizeSection(1, 195)
				cMC_refinementSurfaces_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
				column_2 = QtGui.QTableWidgetItem()
				cMC_refinementSurfaces_table.setHorizontalHeaderItem(1, column_2)
				cMC_refinementSurfaces_table.horizontalHeader().setStyleSheet("color: steelblue")

				cMC_refinementSurfaces_table.horizontalHeader().resizeSection(2, 244)
				cMC_refinementSurfaces_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
				column_3 = QtGui.QTableWidgetItem()
				cMC_refinementSurfaces_table.setHorizontalHeaderItem(2, column_3)
				cMC_refinementSurfaces_table.horizontalHeader().setStyleSheet("color: steelblue")

				if int_lng == 'Russian':
					column_1.setText("Поверхность")
					column_2.setText("Уровень для поверхности")	
					column_3.setText("Параметры подобластей")	
				elif int_lng == 'English':
					column_1.setText("surface")
					column_2.setText("level for surface")
					column_3.setText("Regions parameters")	
					
				norS = 1
				q = 0
				height = 60
				
				while norS <= obj_initial['rS_val']:
					cMC_refinementSurfaces_table.setFixedSize(570, height)
					
					#surface#
					rS_surface_edit = QtGui.QComboBox()
					rS_surface_edit.setFixedSize(110, 25)
					rS_surface_edit.addItems(tri_distirbTri_geometry_list)
					rS_surface_hbox = QtGui.QHBoxLayout()
					rS_surface_hbox.setContentsMargins(0, 0, 0, 0)
					rS_surface_hbox.addWidget(rS_surface_edit)
					rS_surface_cell_widget = QtGui.QWidget()
					rS_surface_cell_widget.setLayout(rS_surface_hbox)
					if castellatedMC_1_obj != None:
						rS_surface_edit_mas = rS_surface_edit.count()  
						for t in range(rS_surface_edit_mas):
							if rS_surface_edit.itemText(t) == castellatedMC_1_obj['refinementSurfaces'][q]['rS_surface']:
								rS_surface_edit.setCurrentIndex(t)

					#level#
					rS_level_min_lbl = QtGui.QLabel()	
					rS_level_max_lbl = QtGui.QLabel()	
					if int_lng == 'Russian':
						rS_level_min_lbl.setText("Мин:")
						rS_level_max_lbl.setText("Макс:")	
					elif int_lng == 'English':
						rS_level_min_lbl.setText("Min:")
						rS_level_max_lbl.setText("Max:")

					rS_level_min_edit = QtGui.QSpinBox()
					rS_level_min_edit.setFixedSize(50, 25)
					rS_level_min_edit.setRange(1, 1000)
					if castellatedMC_1_obj != None:
						rS_level_min_edit.setValue(castellatedMC_1_obj['refinementSurfaces'][q]['rS_level_min'])
					
					rS_level_max_edit = QtGui.QSpinBox()
					rS_level_max_edit.setFixedSize(50, 25)
					rS_level_max_edit.setRange(1, 1000)
					if castellatedMC_1_obj != None:
						rS_level_max_edit.setValue(castellatedMC_1_obj['refinementSurfaces'][q]['rS_level_max'])

					rS_level_hbox = QtGui.QHBoxLayout()
					rS_level_hbox.setContentsMargins(0, 0, 0, 0)
					rS_level_hbox.addWidget(rS_level_min_lbl)
					rS_level_hbox.addWidget(rS_level_min_edit)
					rS_level_hbox.addWidget(rS_level_max_lbl)
					rS_level_hbox.addWidget(rS_level_max_edit)
					rS_level_cell_widget = QtGui.QWidget()
					rS_level_cell_widget.setLayout(rS_level_hbox)

					#regions_prs#
					rS_regions_lbl = QtGui.QLabel()	
					rS_regions_val_lbl = QtGui.QLabel()	
					rS_regions_val_lbl.setEnabled(False)	

					if int_lng == 'Russian':
						rS_regions_lbl.setText("Подобласти:")
						rS_regions_val_lbl.setText("Количество:")	
					elif int_lng == 'English':
						rS_regions_lbl.setText("Regions:")
						rS_regions_val_lbl.setText("Number:")

					rS_regions_edit = QtGui.QCheckBox()	
					rS_regions_edit_list.append(rS_regions_edit)
					if castellatedMC_1_obj != None:
						rS_regions_edit.setChecked(castellatedMC_1_obj['refinementSurfaces'][q]['rS_regions'])
						
					rS_regions_val_edit = QtGui.QSpinBox()
					rS_regions_val_edit.setFixedSize(50, 25)
					rS_regions_val_edit.setRange(1, 1000)
					rS_regions_val_edit.setEnabled(False)
					rS_regions_val_edit_list.append(rS_regions_val_edit)
					if castellatedMC_1_obj != None:
						if castellatedMC_1_obj['refinementSurfaces'][q]['rS_regions'] == True:
							rS_regions_val_lbl.setEnabled(True)	
							rS_regions_val_edit.setEnabled(True)
							rS_regions_val_edit.setValue(castellatedMC_1_obj['refinementSurfaces'][q]['rS_regions_val'])
				
					rS_regions_hbox = QtGui.QHBoxLayout()
					rS_regions_hbox.setContentsMargins(0, 0, 0, 0)
					rS_regions_hbox.addWidget(rS_regions_lbl)
					rS_regions_hbox.addWidget(rS_regions_edit)
					rS_regions_hbox.addWidget(rS_regions_val_lbl)
					rS_regions_hbox.addWidget(rS_regions_val_edit)
					rS_regions_cell_widget = QtGui.QWidget()
					rS_regions_cell_widget.setLayout(rS_regions_hbox)

					cMC_refinementSurfaces_table.setCellWidget(q, 0, rS_surface_cell_widget)
					cMC_refinementSurfaces_table.setCellWidget(q, 1, rS_level_cell_widget)
					cMC_refinementSurfaces_table.setCellWidget(q, 2, rS_regions_cell_widget)

					norS = norS + 1
					q = q + 1
					height = height + 30
					
				prs_grid.addWidget(cMC_rS_lbl, 5, 0, alignment=QtCore.Qt.AlignCenter)
				prs_grid.addWidget(cMC_refinementSurfaces_table, 6, 0, alignment=QtCore.Qt.AlignCenter)
						
			#####-----------------------Четвертая часть параметров-refinementRegions------------------------------#####	
			
			rR_level_single_edit_list = []
			rR_level_multi_edit_list = []
			rR_level_multi_val_edit_list = []			
			if obj_initial['rR'] == True and True in other_geometry_list:	
				
				cMC_rR_lbl = QtGui.QLabel()	
				cMC_rR_lbl.setVisible(False)
				if int_lng == 'Russian':
					cMC_rR_lbl.setText("Cловарь областей для измельчения:")
				elif int_lng == 'English':
					cMC_rR_lbl.setText("Set of areas for grinding:")
				if castellatedMC_1_obj != None:
					cMC_rR_lbl.setVisible(True)
					
				cMC_refinementRegions_table = QtGui.QTableWidget()
				cMC_refinementRegions_table.setVisible(False)
				cMC_refinementRegions_table.setRowCount(obj_initial['rR_val'])
				cMC_refinementRegions_table.setColumnCount(3)
				cMC_refinementRegions_table.verticalHeader().hide()
				if castellatedMC_1_obj != None:
					cMC_refinementRegions_table.setVisible(True)

				cMC_refinementRegions_table.horizontalHeader().resizeSection(0, 140)
				cMC_refinementRegions_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				cMC_refinementRegions_table.setHorizontalHeaderItem(0, column_1)
				cMC_refinementRegions_table.horizontalHeader().setStyleSheet("color: steelblue")

				cMC_refinementRegions_table.horizontalHeader().resizeSection(1, 140)
				cMC_refinementRegions_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
				column_2 = QtGui.QTableWidgetItem()
				cMC_refinementRegions_table.setHorizontalHeaderItem(1, column_2)
				cMC_refinementRegions_table.horizontalHeader().setStyleSheet("color: steelblue")

				cMC_refinementRegions_table.horizontalHeader().resizeSection(2, 390)
				cMC_refinementRegions_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
				column_3 = QtGui.QTableWidgetItem()
				cMC_refinementRegions_table.setHorizontalHeaderItem(2, column_3)
				cMC_refinementRegions_table.horizontalHeader().setStyleSheet("color: steelblue")

				if int_lng == 'Russian':
					column_1.setText("Поверхность")
					column_2.setText("Режим")	
					column_3.setText("Параметры уровней")	
				elif int_lng == 'English':
					column_1.setText("Surface")
					column_2.setText("Mode")
					column_3.setText("Level parameters")	
					
				norR = 1
				q = 0
				height = 60
				while norR <= obj_initial['rR_val']:
					cMC_refinementRegions_table.setFixedSize(675, height)
					#surface#
					rR_surface_edit = QtGui.QComboBox()
					rR_surface_edit.setFixedSize(120, 25)
					rR_surface_edit.addItems(other_geometry_list_geom)
					rR_surface_hbox = QtGui.QHBoxLayout()
					rR_surface_hbox.setContentsMargins(0, 0, 0, 0)
					rR_surface_hbox.addWidget(rR_surface_edit)
					rR_surface_cell_widget = QtGui.QWidget()
					rR_surface_cell_widget.setLayout(rR_surface_hbox)
					if castellatedMC_1_obj != None:
						rR_surface_edit_mas = rR_surface_edit.count()  
						for t in range(rR_surface_edit_mas):
							if rR_surface_edit.itemText(t) == castellatedMC_1_obj['refinementRegions'][q]['rR_surface']:
								rR_surface_edit.setCurrentIndex(t)

					#mode#
					rR_mode_edit = QtGui.QComboBox()
					rR_mode_edit.setFixedSize(110, 25)
					mode_list = ['inside', 'outside', 'distance']
					rR_mode_edit.addItems(mode_list)
					rR_mode_hbox = QtGui.QHBoxLayout()
					rR_mode_hbox.setContentsMargins(0, 0, 0, 0)
					rR_mode_hbox.addWidget(rR_mode_edit)
					rR_mode_cell_widget = QtGui.QWidget()
					rR_mode_cell_widget.setLayout(rR_mode_hbox)
					if castellatedMC_1_obj != None:
						rR_mode_edit_mas = rR_mode_edit.count()  
						for t in range(rR_mode_edit_mas):
							if rR_mode_edit.itemText(t) == castellatedMC_1_obj['refinementRegions'][q]['rR_mode']:
								rR_mode_edit.setCurrentIndex(t)

					#levels#	
					rR_level_single_lbl = QtGui.QLabel()
					rR_level_multi_lbl = QtGui.QLabel()
					rR_level_multi_val_lbl = QtGui.QLabel()
					
					rR_level_multi_val_lbl.setEnabled(False)
					if int_lng == 'Russian':
						rR_level_single_lbl.setText("Уровень:")
						rR_level_multi_lbl.setText("Дистанция уровней:")	
						rR_level_multi_val_lbl.setText("Количество:")
					elif int_lng == 'English':
						rR_level_single_lbl.setText("Level:")
						rR_level_multi_lbl.setText("Level distance:")
						rR_level_multi_val_lbl.setText("Number:")
					rR_level_single_edit = QtGui.QRadioButton()
					if castellatedMC_1_obj != None:
						rR_level_single_edit.setChecked(castellatedMC_1_obj['refinementRegions'][q]['rR_level_single'])
												
					else:
						rR_level_single_edit.setChecked(True)	
												
					rR_level_multi_edit = QtGui.QRadioButton()
					
					if castellatedMC_1_obj != None:
						rR_level_multi_edit.setChecked(castellatedMC_1_obj['refinementRegions'][q]['rR_level_multi'])

					rR_level_multi_val_edit = QtGui.QSpinBox()
					rR_level_multi_val_edit.setFixedSize(50, 25)
					rR_level_multi_val_edit.setRange(1, 1000)
					rR_level_multi_val_edit.setEnabled(False)
					if castellatedMC_1_obj != None:
						if rR_level_multi_edit.isChecked() == True:
							rR_level_multi_val_lbl.setEnabled(True)
							rR_level_multi_val_edit.setEnabled(True)
							rR_level_multi_val_edit.setValue(castellatedMC_1_obj['refinementRegions'][q]['rR_level_multi_val'])
					
					rR_level_single_edit_list.append(rR_level_single_edit)
					rR_level_multi_edit_list.append(rR_level_multi_edit)
					rR_level_multi_val_edit_list.append(rR_level_multi_val_edit)
					
					rR_level_hbox = QtGui.QHBoxLayout()
					rR_level_hbox.setContentsMargins(0, 0, 0, 0)
					rR_level_hbox.addWidget(rR_level_single_lbl)
					rR_level_hbox.addWidget(rR_level_single_edit)
					rR_level_hbox.addWidget(rR_level_multi_lbl)
					rR_level_hbox.addWidget(rR_level_multi_edit)
					rR_level_hbox.addWidget(rR_level_multi_val_lbl)
					rR_level_hbox.addWidget(rR_level_multi_val_edit)

					rR_level_cell_widget = QtGui.QWidget()
					rR_level_cell_widget.setLayout(rR_level_hbox)

					cMC_refinementRegions_table.setCellWidget(q, 0, rR_surface_cell_widget)
					cMC_refinementRegions_table.setCellWidget(q, 1, rR_mode_cell_widget)
					cMC_refinementRegions_table.setCellWidget(q, 2, rR_level_cell_widget)

					norR = norR + 1
					q = q + 1
					height = height + 30
				
				prs_grid.addWidget(cMC_rR_lbl, 7, 0, alignment=QtCore.Qt.AlignCenter)
				prs_grid.addWidget(cMC_refinementRegions_table, 8, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

		castellatedMC_1_btnSave = QtGui.QPushButton()
		castellatedMC_1_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(castellatedMC_1_btnSave)
		if int_lng == 'Russian':
			castellatedMC_1_btnSave.setText("Записать")
		elif int_lng == 'English':
			castellatedMC_1_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		castellatedMC_1_grid = QtGui.QGridLayout()
		castellatedMC_1_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		castellatedMC_1_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		castellatedMC_1_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		castellatedMC_1_grid.setRowStretch(3, 6)
		castellatedMC_1_group = QtGui.QGroupBox()
		castellatedMC_1_group.setLayout(castellatedMC_1_grid)
		return castellatedMC_1_group, castellatedMC_1_btnSave, prs_grid, tri_distirbTri_list, other_geometry_list, f_level_single_edit_list, f_level_multi_edit_list, f_level_multi_val_edit_list, rS_regions_edit_list, rS_regions_val_edit_list, rR_level_single_edit_list, rR_level_multi_edit_list, rR_level_multi_val_edit_list

