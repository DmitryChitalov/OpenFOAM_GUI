# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class motionControl_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, motionControl_visible): 
		motionControl_obj = None
		
		#----------------Если файл motionControl.pkl существует, получаем данные из него для вывода в форму---------------#

		if motionControl_visible == True:
			motionControl_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'motionControl.pkl'
			if os.path.exists(motionControl_path_file):
		
				input = open(motionControl_path_file, 'rb')
				motionControl_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла motionControl.pkl на основе данных файла initial.pkl-------------#
		
		prs_grid = QtGui.QGridLayout()
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(prs_grid)
		
		#####-----------------------Первая часть параметров------------------------------#####
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Параметры определения свойств движения")
		elif int_lng == 'English':
			main_lbl.setText("Parameters of motion features definition")
		
		#minCellSize
		mCS_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mCS_lbl.setText("Минимальный размер ячейки (minCellSize):")
		elif int_lng == 'English':
			mCS_lbl.setText("Minimum cell size (minCellSize):")
		mCS_edit = QtGui.QDoubleSpinBox()
		mCS_edit.setRange(0, 100000000000)
		mCS_edit.setFixedSize(110, 25)
		if motionControl_obj != None:
			mCS_edit.setValue(motionControl_obj['mC_start_prs']['mCS'])
			
		#defaultPriority
		dF_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			dF_lbl.setText("Приоритет на размеры ячеек ячейки (defaultPriority):")
		elif int_lng == 'English':
			dF_lbl.setText("Priority to cell cell sizes (defaultPriority):")
		dF_edit = QtGui.QDoubleSpinBox()
		dF_edit.setRange(0, 100000000000)
		dF_edit.setFixedSize(110, 25)
		if motionControl_obj != None:
			dF_edit.setValue(motionControl_obj['mC_start_prs']['dF'])
			
		#relaxationModel
		rM_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			rM_lbl.setText("Модель смягчения (relaxationModel):")
		elif int_lng == 'English':
			rM_lbl.setText("Relaxation model (relaxationModel):")
		rM_edit = QtGui.QComboBox()
		rM_l = ["adaptiveLinear"]
		rM_edit.addItems(rM_l)
		rM_edit.setFixedSize(110, 25)
		if motionControl_obj != None:
			rM_edit_mas = rM_edit.count()  
			for t in range(rM_edit_mas):
				if rM_edit.itemText(t) == motionControl_obj['mC_start_prs']['rM']:
					rM_edit.setCurrentIndex(t)	
					
		#relaxationStart
		rS_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			rS_lbl.setText("Параметр запуска смягчения (relaxationStart):")
		elif int_lng == 'English':
			rS_lbl.setText("Start softening parameter (relaxationStart):")
		rS_edit = QtGui.QDoubleSpinBox()
		rS_edit.setRange(0, 100000000000)
		rS_edit.setFixedSize(110, 25)
		if motionControl_obj != None:
			rS_edit.setValue(motionControl_obj['mC_start_prs']['rS'])
			
		#relaxationEnd
		rE_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			rE_lbl.setText("Параметр завершения смягчения (relaxationEnd):")
		elif int_lng == 'English':
			rE_lbl.setText("Start softening parameter (relaxationEnd):")
		rE_edit = QtGui.QDoubleSpinBox()
		rE_edit.setRange(0, 100000000000)
		rE_edit.setFixedSize(110, 25)
		if motionControl_obj != None:
			rE_edit.setValue(motionControl_obj['mC_start_prs']['rE'])
		
		#objOutput
		oO_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			oO_lbl.setText("Выводить объект (objOutput):")
		elif int_lng == 'English':
			oO_lbl.setText("Output object (objOutput):")
		oO_edit = QtGui.QComboBox()
		oO_l = ["yes", "no"]
		oO_edit.addItems(oO_l)
		oO_edit.setFixedSize(110, 25)
		if motionControl_obj != None:
			oO_edit_mas = oO_edit.count()  
			for t in range(oO_edit_mas):
				if oO_edit.itemText(t) == motionControl_obj['mC_start_prs']['oO']:
					oO_edit.setCurrentIndex(t)	
					
		#meshedSurfaceOutput
		mSO_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mSO_lbl.setText("Выводить сеточную поверхность (meshedSurfaceOutput):")
		elif int_lng == 'English':
			mSO_lbl.setText("Output the mesh surface (meshedSurfaceOutput):")
		mSO_edit = QtGui.QComboBox()
		mSO_l = ["yes", "no"]
		mSO_edit.addItems(mSO_l)
		mSO_edit.setFixedSize(110, 25)
		if motionControl_obj != None:
			mSO_edit_mas = mSO_edit.count()  
			for t in range(mSO_edit_mas):
				if mSO_edit.itemText(t) == motionControl_obj['mC_start_prs']['mSO']:
					mSO_edit.setCurrentIndex(t)
					
		#nearWallAlignedDist
		nWAD_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			nWAD_lbl.setText("Количество слоев клеток, выровненных со стенкой (nearWallAlignedDist):")
		elif int_lng == 'English':
			nWAD_lbl.setText("Number of cell layers aligned with the wall (nearWallAlignedDist):")
		nWAD_edit = QtGui.QSpinBox()
		nWAD_edit.setRange(0, 100000000000)
		nWAD_edit.setFixedSize(110, 25)
		if motionControl_obj != None:
			nWAD_edit.setValue(motionControl_obj['mC_start_prs']['nWAD'])

		#https://econet.ru/articles/153327-erih-fromm-neschastnaya-sudba-lyudey-sledstvie-nesdelannogo-imi-vybora#.Wtr6YfRN8PJ.vk
		
		mC_start_prs_grid = QtGui.QGridLayout()
		
		mC_start_prs_grid.addWidget(mCS_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(mCS_edit, 0, 1, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(dF_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(dF_edit, 1, 1, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(rM_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(rM_edit, 2, 1, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(rS_lbl, 3, 0, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(rS_edit, 3, 1, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(rE_lbl, 4, 0, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(rE_edit, 4, 1, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(oO_lbl, 5, 0, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(oO_edit, 5, 1, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(mSO_lbl, 6, 0, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(mSO_edit, 6, 1, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(nWAD_lbl, 7, 0, alignment=QtCore.Qt.AlignCenter)
		mC_start_prs_grid.addWidget(nWAD_edit, 7, 1, alignment=QtCore.Qt.AlignCenter)
		
		prs_grid.addLayout(mC_start_prs_grid, 0, 0, alignment=QtCore.Qt.AlignCenter)
		
		tri_distirbTri_list = []
		tri_distirbTri_geometry_list = []
		tri_distirbTri_name_list = []
		other_geometry_list = []
		other_geometry_list_geom = []
		
		#####-----------------------Вторая часть параметров-shapeControlFunctions------------------------------#####
		
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):

			input = open(initial_path_file, 'rb')
			initial_obj = pickle.load(input)
			input.close()
				
		geometry_2_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if os.path.exists(geometry_2_path_file):

			input = open(geometry_2_path_file, 'rb')
			geometry_2_obj = pickle.load(input)
			input.close()
				
			i = 1			
			for el in geometry_2_obj:
				if el['geometry_' + str(i)] == 'Tri-surface' or el['geometry_' + str(i)] == 'Три-поверхность' \
				or el['geometry_' + str(i)] == 'Closed tri-surface' or el['geometry_' + str(i)] == 'Закрытая три-поверхность' \
				or el['geometry_' + str(i)] == 'Distributed tri-surface' \
				or el['geometry_' + str(i)] == 'Распределенная три-поверхность':
					tri_distirbTri_list.append(True)
					tri_distirbTri_geometry_list.append(el['file'])
					tri_distirbTri_name_list.append(el['name'])
					
					other_geometry_list_geom.append(el['name'])
					other_geometry_list.append(True)
				elif el['geometry_' + str(i)] == 'Base shape complex' or el['geometry_' + str(i)] == 'Набор базовых фигур':
					other_geometry_list_geom.append(el['name'])
					other_geometry_list.append(True)
				elif el['geometry_' + str(i)] == 'Base shape' or el['geometry_' + str(i)] == 'Базовая фигура':
					other_geometry_list_geom.append(el['shape'])
					other_geometry_list.append(True)
				i = i + 1
		
			#sCF
			
			sCF_surface_edit_list = []
			sCF_type_edit_list = []
			sCF_priority_edit_list = []
			sCF_mode_edit_list = []
			sCF_cellSizeFunction_edit_list = []
			sCF_distanceCellSizeCoeff_edit_list = []
			sCF_distanceCoeff_edit_list = []
			sCF_totalDistanceCoeff_edit_list = []
			sCF_surfaceOffsetCoeff_edit_list = []
			sCF_surfaceCellSizeFunction_edit_list = []
			sCF_surfaceCellSizeCoeff_edit_list = []
			
			sCF_distanceCoeff_chk_list = [] 
			sCF_totalDistanceCoeff_chk_list = []
			sCF_surfaceOffsetCoeff_chk_list = []
			
			if initial_obj['sCF'] == True and True in other_geometry_list:
			
				mC_sCF_lbl = QtGui.QLabel()	
				mC_sCF_lbl.setVisible(False)
				if int_lng == 'Russian':
					mC_sCF_lbl.setText("Список функций управления фигурами:")
				elif int_lng == 'English':
					mC_sCF_lbl.setText("List of shape control functions:")
				mC_sCF_lbl.setVisible(True)

				mC_sCF_table = QtGui.QTableWidget()
				mC_sCF_table.setRowCount(initial_obj['sCF_val'])
				mC_sCF_table.setColumnCount(11)

				mC_sCF_table.horizontalHeader().resizeSection(0, 150)
				mC_sCF_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(0, column_1)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")

				mC_sCF_table.horizontalHeader().resizeSection(1, 150)
				mC_sCF_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
				column_2 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(1, column_2)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(2, 110)
				mC_sCF_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
				column_3 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(2, column_3)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(3, 120)
				mC_sCF_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
				column_4 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(3, column_4)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(4, 210)
				mC_sCF_table.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.Fixed)
				column_5 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(4, column_5)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(5, 300)
				mC_sCF_table.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.Fixed)
				column_6 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(5, column_6)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(6, 195)
				mC_sCF_table.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.Fixed)
				column_7 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(6, column_7)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(7, 235)
				mC_sCF_table.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.Fixed)
				column_8 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(7, column_8)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(8, 300)
				mC_sCF_table.horizontalHeader().setResizeMode(8, QtGui.QHeaderView.Fixed)
				column_9 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(8, column_9)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(9, 320)
				mC_sCF_table.horizontalHeader().setResizeMode(9, QtGui.QHeaderView.Fixed)
				column_10 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(9, column_10)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				mC_sCF_table.horizontalHeader().resizeSection(10, 350)
				mC_sCF_table.horizontalHeader().setResizeMode(10, QtGui.QHeaderView.Fixed)
				column_11 = QtGui.QTableWidgetItem()
				mC_sCF_table.setHorizontalHeaderItem(10, column_11)
				mC_sCF_table.horizontalHeader().setStyleSheet("color: steelblue")

				if int_lng == 'Russian':
					column_1.setText("Поверхность")
					column_2.setText("Тип")
					column_3.setText("Приоритет")
					column_4.setText("Режим")
					column_5.setText("Функция размеров ячейки")
					column_6.setText("Коэффициент дистанции размера ячейки")
					column_7.setText("Коэффициент дистанции")
					column_8.setText("Равномерные коэффициенты")
					column_9.setText("Коэффициент смещения поверхности")
					column_10.setText("Функция определения размера ячейки")
					column_11.setText("Коэффициент определения размера ячейки")
				elif int_lng == 'English':
					column_1.setText("surface")
					column_2.setText("type")
					column_3.setText("priority")
					column_4.setText("mode")
					column_5.setText("cellSizeFunction")
					column_6.setText("distanceCellSizeCoeff")
					column_7.setText("distanceCoeff")
					column_8.setText("totalDistanceCoeff")
					column_9.setText("surfaceOffsetCoeff")
					column_10.setText("surfaceCellSizeFunction")
					column_11.setText("surfaceCellSizeCoeff")

				nof = 1
				q = 0
				height = 65
				
				while nof <= initial_obj['sCF_val']:
					mC_sCF_table.setFixedSize(990, height)
					#surface#
					sCF_surface_edit = QtGui.QComboBox()
					sCF_surface_edit.setFixedSize(110, 25)
					sCF_surface_edit.addItems(other_geometry_list_geom)
					sCF_surface_edit_hbox = QtGui.QHBoxLayout()
					sCF_surface_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_surface_edit_hbox.addWidget(sCF_surface_edit)
					sCF_surface_edit_cell_widget = QtGui.QWidget()
					sCF_surface_edit_cell_widget.setLayout(sCF_surface_edit_hbox)
					if motionControl_obj != None:
						s_mas = sCF_surface_edit.count()  
						for t in range(s_mas):
							if sCF_surface_edit.itemText(t) == motionControl_obj['mC_sCF_prs'][q]['s']:
								sCF_surface_edit.setCurrentIndex(t)	
					
					#type#
					sCF_type_edit = QtGui.QComboBox()
					sCF_type_edit.setFixedSize(140, 25)
					sCF_type_list = ['searchableSurfaceControl']
					sCF_type_edit.addItems(sCF_type_list)
					sCF_type_edit_hbox = QtGui.QHBoxLayout()
					sCF_type_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_type_edit_hbox.addWidget(sCF_type_edit)
					sCF_type_edit_cell_widget = QtGui.QWidget()
					sCF_type_edit_cell_widget.setLayout(sCF_type_edit_hbox)
					if motionControl_obj != None:
						t_mas = sCF_type_edit.count()  
						for t in range(t_mas):
							if sCF_type_edit.itemText(t) == motionControl_obj['mC_sCF_prs'][q]['t']:
								sCF_type_edit.setCurrentIndex(t)
								
					#priority#
					sCF_priority_edit = QtGui.QSpinBox()
					sCF_priority_edit.setRange(0, 100000000000)
					sCF_priority_edit.setFixedSize(100, 25)
					sCF_priority_edit_hbox = QtGui.QHBoxLayout()
					sCF_priority_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_priority_edit_hbox.addWidget(sCF_priority_edit)
					sCF_priority_edit_cell_widget = QtGui.QWidget()
					sCF_priority_edit_cell_widget.setLayout(sCF_priority_edit_hbox)
					if motionControl_obj != None:
						sCF_priority_edit.setValue(motionControl_obj['mC_sCF_prs'][q]['p'])
								
					#mode#
					sCF_mode_edit = QtGui.QComboBox()
					sCF_mode_edit.setFixedSize(110, 25)
					sCF_mode_list = ['bothSides', 'inside']
					sCF_mode_edit.addItems(sCF_mode_list)
					sCF_mode_edit_hbox = QtGui.QHBoxLayout()
					sCF_mode_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_mode_edit_hbox.addWidget(sCF_mode_edit)
					sCF_mode_edit_cell_widget = QtGui.QWidget()
					sCF_mode_edit_cell_widget.setLayout(sCF_mode_edit_hbox)
					if motionControl_obj != None:
						m_mas = sCF_mode_edit.count()  
						for t in range(m_mas):
							if sCF_mode_edit.itemText(t) == motionControl_obj['mC_sCF_prs'][q]['m']:
								sCF_mode_edit.setCurrentIndex(t)
								
					#cellSizeFunction#
					sCF_cellSizeFunction_edit = QtGui.QComboBox()
					sCF_cellSizeFunction_edit.setFixedSize(110, 25)
					sCF_cellSizeFunction_list = ['linearDistance', 'surfaceOffsetLinearDistance', 'uniform']
					sCF_cellSizeFunction_edit.addItems(sCF_cellSizeFunction_list)
					sCF_cellSizeFunction_edit_hbox = QtGui.QHBoxLayout()
					sCF_cellSizeFunction_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_cellSizeFunction_edit_hbox.addWidget(sCF_cellSizeFunction_edit)
					sCF_cellSizeFunction_edit_cell_widget = QtGui.QWidget()
					sCF_cellSizeFunction_edit_cell_widget.setLayout(sCF_cellSizeFunction_edit_hbox)
					if motionControl_obj != None:
						cSF_mas = sCF_cellSizeFunction_edit.count()  
						for t in range(cSF_mas):
							if sCF_cellSizeFunction_edit.itemText(t) == motionControl_obj['mC_sCF_prs'][q]['cSF']:
								sCF_cellSizeFunction_edit.setCurrentIndex(t)
					
					#distanceCellSizeCoeff#
					sCF_distanceCellSizeCoeff_edit = QtGui.QDoubleSpinBox()
					sCF_distanceCellSizeCoeff_edit.setRange(0, 100000000000)
					sCF_distanceCellSizeCoeff_edit.setFixedSize(100, 25)
					sCF_distanceCellSizeCoeff_edit_hbox = QtGui.QHBoxLayout()
					sCF_distanceCellSizeCoeff_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_distanceCellSizeCoeff_edit_hbox.addWidget(sCF_distanceCellSizeCoeff_edit)
					sCF_distanceCellSizeCoeff_edit_cell_widget = QtGui.QWidget()
					sCF_distanceCellSizeCoeff_edit_cell_widget.setLayout(sCF_distanceCellSizeCoeff_edit_hbox)
					if motionControl_obj != None:
						sCF_distanceCellSizeCoeff_edit.setValue(motionControl_obj['mC_sCF_prs'][q]['dCSC'])
								
					#distanceCoeff#
					sCF_distanceCoeff_chk = QtGui.QCheckBox()
					sCF_distanceCoeff_edit = QtGui.QDoubleSpinBox()
					sCF_distanceCoeff_edit.setEnabled(False)
					sCF_distanceCoeff_edit.setRange(0, 100000000000)
					sCF_distanceCoeff_edit.setFixedSize(100, 25)
					sCF_distanceCoeff_edit_hbox = QtGui.QHBoxLayout()
					sCF_distanceCoeff_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_distanceCoeff_edit_hbox.addWidget(sCF_distanceCoeff_chk, alignment=QtCore.Qt.AlignCenter)
					sCF_distanceCoeff_edit_hbox.addWidget(sCF_distanceCoeff_edit, alignment=QtCore.Qt.AlignCenter)
					sCF_distanceCoeff_edit_cell_widget = QtGui.QWidget()
					sCF_distanceCoeff_edit_cell_widget.setLayout(sCF_distanceCoeff_edit_hbox)
					if motionControl_obj != None:
						sCF_distanceCoeff_chk.setChecked(motionControl_obj['mC_sCF_prs'][q]['dC_chk'])
						if motionControl_obj['mC_sCF_prs'][q]['dC_chk'] == True:
							sCF_distanceCoeff_edit.setEnabled(True)
							sCF_distanceCoeff_edit.setValue(motionControl_obj['mC_sCF_prs'][q]['dC'])
					
								
					#totalDistanceCoeff#
					sCF_totalDistanceCoeff_chk = QtGui.QCheckBox()
					sCF_totalDistanceCoeff_edit = QtGui.QDoubleSpinBox()
					sCF_totalDistanceCoeff_edit.setEnabled(False)
					sCF_totalDistanceCoeff_edit.setRange(0, 100000000000)
					sCF_totalDistanceCoeff_edit.setFixedSize(100, 25)
					sCF_totalDistanceCoeff_edit_hbox = QtGui.QHBoxLayout()
					sCF_totalDistanceCoeff_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_totalDistanceCoeff_edit_hbox.addWidget(sCF_totalDistanceCoeff_chk, alignment=QtCore.Qt.AlignCenter)
					sCF_totalDistanceCoeff_edit_hbox.addWidget(sCF_totalDistanceCoeff_edit, alignment=QtCore.Qt.AlignCenter)
					sCF_totalDistanceCoeff_edit_cell_widget = QtGui.QWidget()
					sCF_totalDistanceCoeff_edit_cell_widget.setLayout(sCF_totalDistanceCoeff_edit_hbox)
					if motionControl_obj != None:
						sCF_totalDistanceCoeff_chk.setChecked(motionControl_obj['mC_sCF_prs'][q]['tDC_chk'])
						if motionControl_obj['mC_sCF_prs'][q]['tDC_chk'] == True:
							sCF_totalDistanceCoeff_edit.setEnabled(True)
							sCF_totalDistanceCoeff_edit.setValue(motionControl_obj['mC_sCF_prs'][q]['tDC'])
						
					#surfaceOffsetCoeff#
					sCF_surfaceOffsetCoeff_chk = QtGui.QCheckBox()
					sCF_surfaceOffsetCoeff_edit = QtGui.QDoubleSpinBox()
					sCF_surfaceOffsetCoeff_edit.setEnabled(False)
					sCF_surfaceOffsetCoeff_edit.setRange(0, 100000000000)
					sCF_surfaceOffsetCoeff_edit.setFixedSize(100, 25)
					sCF_surfaceOffsetCoeff_edit_hbox = QtGui.QHBoxLayout()
					sCF_surfaceOffsetCoeff_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_surfaceOffsetCoeff_edit_hbox.addWidget(sCF_surfaceOffsetCoeff_chk, alignment=QtCore.Qt.AlignCenter)
					sCF_surfaceOffsetCoeff_edit_hbox.addWidget(sCF_surfaceOffsetCoeff_edit, alignment=QtCore.Qt.AlignCenter)
					sCF_surfaceOffsetCoeff_edit_cell_widget = QtGui.QWidget()
					sCF_surfaceOffsetCoeff_edit_cell_widget.setLayout(sCF_surfaceOffsetCoeff_edit_hbox)
					if motionControl_obj != None:
						sCF_surfaceOffsetCoeff_chk.setChecked(motionControl_obj['mC_sCF_prs'][q]['sOC_chk'])
						if motionControl_obj['mC_sCF_prs'][q]['sOC_chk'] == True:
							sCF_surfaceOffsetCoeff_edit.setEnabled(True)
							sCF_surfaceOffsetCoeff_edit.setValue(motionControl_obj['mC_sCF_prs'][q]['sOC'])
								
					#surfaceCellSizeFunction#
					sCF_surfaceCellSizeFunction_edit = QtGui.QComboBox()
					sCF_surfaceCellSizeFunction_edit.setFixedSize(110, 25)
					sCF_surfaceCellSizeFunction_list = ['uniformValue']
					sCF_surfaceCellSizeFunction_edit.addItems(sCF_surfaceCellSizeFunction_list)
					sCF_surfaceCellSizeFunction_edit_hbox = QtGui.QHBoxLayout()
					sCF_surfaceCellSizeFunction_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_surfaceCellSizeFunction_edit_hbox.addWidget(sCF_surfaceCellSizeFunction_edit)
					sCF_surfaceCellSizeFunction_edit_cell_widget = QtGui.QWidget()
					sCF_surfaceCellSizeFunction_edit_cell_widget.setLayout(sCF_surfaceCellSizeFunction_edit_hbox)
					if motionControl_obj != None:
						sCSF_mas = sCF_surfaceCellSizeFunction_edit.count()  
						for t in range(sCSF_mas):
							if sCF_surfaceCellSizeFunction_edit.itemText(t) == motionControl_obj['mC_sCF_prs'][q]['sCSF']:
								sCF_surfaceCellSizeFunction_edit.setCurrentIndex(t)
					
					#surfaceCellSizeCoeff#
					sCF_surfaceCellSizeCoeff_edit = QtGui.QDoubleSpinBox()
					sCF_surfaceCellSizeCoeff_edit.setRange(0, 100000000000)
					sCF_surfaceCellSizeCoeff_edit.setFixedSize(100, 25)
					sCF_surfaceCellSizeCoeff_edit_hbox = QtGui.QHBoxLayout()
					sCF_surfaceCellSizeCoeff_edit_hbox.setContentsMargins(0, 0, 0, 0)
					sCF_surfaceCellSizeCoeff_edit_hbox.addWidget(sCF_surfaceCellSizeCoeff_edit, alignment=QtCore.Qt.AlignCenter)
					sCF_surfaceCellSizeCoeff_edit_cell_widget = QtGui.QWidget()
					sCF_surfaceCellSizeCoeff_edit_cell_widget.setLayout(sCF_surfaceCellSizeCoeff_edit_hbox)
					if motionControl_obj != None:
						sCF_surfaceCellSizeCoeff_edit.setValue(motionControl_obj['mC_sCF_prs'][q]['sCSC'])
								
					sCF_surface_edit_list.append(sCF_surface_edit)
					sCF_type_edit_list.append(sCF_type_edit)
					sCF_priority_edit_list.append(sCF_priority_edit)
					sCF_mode_edit_list.append(sCF_mode_edit)
					sCF_cellSizeFunction_edit_list.append(sCF_cellSizeFunction_edit)
					sCF_distanceCellSizeCoeff_edit_list.append(sCF_distanceCellSizeCoeff_edit)
					sCF_distanceCoeff_edit_list.append(sCF_distanceCoeff_edit)
					sCF_totalDistanceCoeff_edit_list.append(sCF_totalDistanceCoeff_edit)
					sCF_surfaceOffsetCoeff_edit_list.append(sCF_surfaceOffsetCoeff_edit)
					sCF_surfaceCellSizeFunction_edit_list.append(sCF_surfaceCellSizeFunction_edit)
					sCF_surfaceCellSizeCoeff_edit_list.append(sCF_surfaceCellSizeCoeff_edit)
					sCF_distanceCoeff_chk_list.append(sCF_distanceCoeff_chk) 
					sCF_totalDistanceCoeff_chk_list.append(sCF_totalDistanceCoeff_chk)
					sCF_surfaceOffsetCoeff_chk_list.append(sCF_surfaceOffsetCoeff_chk)								

					mC_sCF_table.setCellWidget(q, 0, sCF_surface_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 1, sCF_type_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 2, sCF_priority_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 3, sCF_mode_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 4, sCF_cellSizeFunction_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 5, sCF_distanceCellSizeCoeff_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 6, sCF_distanceCoeff_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 7, sCF_totalDistanceCoeff_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 8, sCF_surfaceOffsetCoeff_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 9, sCF_surfaceCellSizeFunction_edit_cell_widget)
					mC_sCF_table.setCellWidget(q, 10, sCF_surfaceCellSizeCoeff_edit_cell_widget)
					
					nof = nof + 1
					q = q + 1
					height = height + 35
	
				prs_grid.addWidget(mC_sCF_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
				prs_grid.addWidget(mC_sCF_table, 2, 0, alignment=QtCore.Qt.AlignCenter)		

		# -------------------------Кнопка сохранения --------------------------#

		motionControl_btnSave = QtGui.QPushButton()
		motionControl_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(motionControl_btnSave)
		if int_lng == 'Russian':
			motionControl_btnSave.setText("Записать")
		elif int_lng == 'English':
			motionControl_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		motionControl_grid = QtGui.QGridLayout()
		motionControl_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		motionControl_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		motionControl_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		motionControl_grid.setRowStretch(3, 6)
		motionControl_group = QtGui.QGroupBox()
		motionControl_group.setLayout(motionControl_grid)
		return motionControl_group, motionControl_btnSave, mC_start_prs_grid, sCF_surface_edit_list, sCF_type_edit_list, sCF_priority_edit_list, sCF_mode_edit_list, sCF_cellSizeFunction_edit_list, sCF_distanceCellSizeCoeff_edit_list, \
		sCF_distanceCoeff_edit_list, sCF_totalDistanceCoeff_edit_list, sCF_surfaceOffsetCoeff_edit_list, sCF_surfaceCellSizeFunction_edit_list, sCF_surfaceCellSizeCoeff_edit_list, \
		sCF_distanceCoeff_chk_list, sCF_totalDistanceCoeff_chk_list, sCF_surfaceOffsetCoeff_chk_list
