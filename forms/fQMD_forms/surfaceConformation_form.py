# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class surfaceConformation_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceConformation_visible): 
		surfaceConformation_obj = None
		
		#----------------Если файл surfaceConformation.pkl существует, получаем данные из него для вывода в форму---------------#

		if surfaceConformation_visible == True:
			surfaceConformation_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceConformation.pkl'
			if os.path.exists(surfaceConformation_path_file):
		
				input = open(surfaceConformation_path_file, 'rb')
				surfaceConformation_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла surfaceConformation.pkl на основе данных файла initial.pkl-------------#
		
		prs_grid = QtGui.QGridLayout()
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(prs_grid)
		
		#####-----------------------Первая часть параметров------------------------------#####
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Параметры управления конформацией поверхностей")
		elif int_lng == 'English':
			main_lbl.setText("Parameters of surface conformation")
			
		#locationInMesh#
		lIM_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			lIM_lbl.setText("Вектор координат плоскости (locationInMesh):")
		elif int_lng == 'English':
			lIM_lbl.setText("The coordinate vector of the plane (locationInMesh):")
			
		lIM_edit_x = QtGui.QLineEdit()
		lIM_edit_x.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_x))
		lIM_edit_x.setFixedSize(80, 25)
		lIM_edit_y = QtGui.QLineEdit()
		lIM_edit_y.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_y))
		lIM_edit_y.setFixedSize(80, 25)
		lIM_edit_z = QtGui.QLineEdit()
		lIM_edit_z.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, lIM_edit_z))
		lIM_edit_z.setFixedSize(80, 25)
		if surfaceConformation_obj != None:
			lIM_edit_x.setText(surfaceConformation_obj['sC_start_prs']['lIM'][0])
			lIM_edit_y.setText(surfaceConformation_obj['sC_start_prs']['lIM'][1])
			lIM_edit_z.setText(surfaceConformation_obj['sC_start_prs']['lIM'][2])
			
		#pointPairDistanceCoeff
		pPDC_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			pPDC_lbl.setText("Расстояние генерирования соседних точек-дуплетов (pointPairDistanceCoeff):")
		elif int_lng == 'English':
			pPDC_lbl.setText("Distance of generation of neighboring doublets (pointPairDistanceCoeff):")
			
		pPDC_edit = QtGui.QLineEdit()
		pPDC_edit.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, pPDC_edit))
		pPDC_edit.setFixedSize(80, 25)	
		if surfaceConformation_obj != None:
			pPDC_edit.setText(surfaceConformation_obj['sC_start_prs']['pPDC'])
		
		#minEdgeLenCoeff
		mELC_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mELC_lbl.setText("Коэффициент минимальной длины ряда (minEdgeLenCoeff):")
		elif int_lng == 'English':
			mELC_lbl.setText("The coefficient of the minimum length of the series (minEdgeLenCoeff):")
		
		mELC_edit = QtGui.QLineEdit()
		mELC_edit.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, mELC_edit))
		mELC_edit.setFixedSize(80, 25)	
		if surfaceConformation_obj != None:
			mELC_edit.setText(surfaceConformation_obj['sC_start_prs']['mELC'])
			
		#maxNotchLenCoeff
		mNLC_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mNLC_lbl.setText("Максимальное количество выступающих ячеек (maxNotchLenCoeff):")
		elif int_lng == 'English':
			mNLC_lbl.setText("Maximum number of projecting cells (maxNotchLenCoeff):")
		mNLC_edit = QtGui.QDoubleSpinBox()
		mNLC_edit.setRange(0, 100000000000)
		mNLC_edit.setFixedSize(100, 25)
		if surfaceConformation_obj != None:
			mNLC_edit.setValue(surfaceConformation_obj['sC_start_prs']['mNLC'])
			
		#minNearPointDistCoeff
		mNPDC_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mNPDC_lbl.setText("Коэффициент минимального расстояния между точками (minNearPointDistCoeff):")
		elif int_lng == 'English':
			mNPDC_lbl.setText("The minimum distance between points (minNearPointDistCoeff):")
		
		mNPDC_edit = QtGui.QLineEdit()
		mNPDC_edit.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, mNPDC_edit))
		mNPDC_edit.setFixedSize(80, 25)	
		if surfaceConformation_obj != None:
			mNPDC_edit.setText(surfaceConformation_obj['sC_start_prs']['mNPDC'])
			
		#maxQuadAngle
		mQA_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mQA_lbl.setText("Максимальный квадратный угол (maxQuadAngle):")
		elif int_lng == 'English':
			mQA_lbl.setText("Maximum square angle (maxQuadAngle):")
		mQA_edit = QtGui.QSpinBox()
		mQA_edit.setRange(0, 100000000000)
		mQA_edit.setFixedSize(100, 25)
		if surfaceConformation_obj != None:
			mQA_edit.setValue(surfaceConformation_obj['sC_start_prs']['mQA'])
			
		#insertSurfaceNearestPointPairs
		iSNPP_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			iSNPP_lbl.setText("Вставить поверхность в окрестности точки или точек-пар (insertSurfaceNearestPointPairs):")
		elif int_lng == 'English':
			iSNPP_lbl.setText("The maximum level of grinding of cells (insertSurfaceNearestPointPairs):")
		iSNPP_edit = QtGui.QComboBox()
		iSNPP_l = ["yes", "no"]
		iSNPP_edit.addItems(iSNPP_l)
		iSNPP_edit.setFixedSize(100, 25)
		if surfaceConformation_obj != None:
			iSNPP_edit_mas = iSNPP_edit.count()  
			for t in range(iSNPP_edit_mas):
				if iSNPP_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['iSNPP']:
					iSNPP_edit.setCurrentIndex(t)	
					
		#mirrorPoints
		mP_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mP_lbl.setText("Зеркально приближать граничные точки, а не вставлять точки-пары (mirrorPoints):")
		elif int_lng == 'English':
			mP_lbl.setText("Mirror approximate the boundary points, rather than insert point-pairs (mirrorPoints):")
		mP_edit = QtGui.QComboBox()
		mP_l = ["yes", "no"]
		mP_edit.addItems(mP_l)
		mP_edit.setFixedSize(100, 25)
		if surfaceConformation_obj != None:
			mP_edit_mas = mP_edit.count()  
			for t in range(mP_edit_mas):
				if mP_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['mP']:
					mP_edit.setCurrentIndex(t)	
					
		#insertSurfaceNearPointPairs
		iSNePP_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			iSNePP_lbl.setText("Вставить точки-пары или двухэлементные вершины очень близко к поверхности (insertSurfaceNearPointPairs):")
		elif int_lng == 'English':
			iSNePP_lbl.setText("Insert point-pairs or two-element vertices very close to the surface (insertSurfaceNearPointPairs):")
		iSNePP_edit = QtGui.QComboBox()
		iSNePP_l = ["yes", "no"]
		iSNePP_edit.addItems(iSNePP_l)
		iSNePP_edit.setFixedSize(100, 25)
		if surfaceConformation_obj != None:
			iSNePP_edit_mas = iSNePP_edit.count()  
			for t in range(iSNePP_edit_mas):
				if iSNePP_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['iSNePP']:
					iSNePP_edit.setCurrentIndex(t)	
					
		#maxBoundaryConformingIter
		mBCI_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			mBCI_lbl.setText("Максимальное количество итераций, используемых в boundaryConforming (maxBoundaryConformingIter):")
		elif int_lng == 'English':
			mBCI_lbl.setText("The maximum number of iterations used in boundaryConforming (maxBoundaryConformingIter):")
		mBCI_edit = QtGui.QSpinBox()
		mBCI_edit.setRange(0, 100000000000)
		mBCI_edit.setFixedSize(100, 25)
		if surfaceConformation_obj != None:
			mBCI_edit.setValue(surfaceConformation_obj['sC_start_prs']['mBCI'])
			
		#randomiseInitialGrid
		rIG_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			rIG_lbl.setText("Рандомизировать начальную сетку, созданную insertGrid (randomiseInitialGrid):")
		elif int_lng == 'English':
			rIG_lbl.setText("Randomize the initial grid created by insertGrid (randomiseInitialGrid):")
		rIG_edit = QtGui.QComboBox()
		rIG_l = ["yes", "no"]
		rIG_edit.addItems(rIG_l)
		rIG_edit.setFixedSize(100, 25)
		if surfaceConformation_obj != None:
			rIG_edit_mas = rIG_edit.count()  
			for t in range(rIG_edit_mas):
				if rIG_edit.itemText(t) == surfaceConformation_obj['sC_start_prs']['rIG']:
					rIG_edit.setCurrentIndex(t)	
					
		#randomPerturbation
		rP_lbl = QtGui.QLabel()	
		if int_lng == 'Russian':
			rP_lbl.setText("Произвольное искажение (randomPerturbation):")
		elif int_lng == 'English':
			rP_lbl.setText("Arbitrary distortion (randomPerturbation):")
		rP_edit = QtGui.QDoubleSpinBox()
		rP_edit.setRange(0, 100000000000)
		rP_edit.setFixedSize(100, 25)
		if surfaceConformation_obj != None:
			rP_edit.setValue(surfaceConformation_obj['sC_start_prs']['rP'])
				
		sC_start_prs_grid = QtGui.QGridLayout()
		sC_start_prs_grid.addWidget(lIM_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(lIM_edit_x, 0, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(lIM_edit_y, 0, 2, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(lIM_edit_z, 0, 3, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(pPDC_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(pPDC_edit, 1, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mELC_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mELC_edit, 2, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mNLC_lbl, 3, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mNLC_edit, 3, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mNPDC_lbl, 4, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mNPDC_edit, 4, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mQA_lbl, 5, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mQA_edit, 5, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(iSNPP_lbl, 6, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(iSNPP_edit, 6, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mP_lbl, 7, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mP_edit, 7, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(iSNePP_lbl, 8, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(iSNePP_edit, 8, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mBCI_lbl, 9, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(mBCI_edit, 9, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(rIG_lbl, 10, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(rIG_edit, 10, 1, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(rP_lbl, 11, 0, alignment=QtCore.Qt.AlignCenter)
		sC_start_prs_grid.addWidget(rP_edit, 11, 1, alignment=QtCore.Qt.AlignCenter)
		
		prs_grid.addLayout(sC_start_prs_grid, 0, 0, alignment=QtCore.Qt.AlignCenter)
		
		tri_distirbTri_list = []
		tri_distirbTri_geometry_list = []
		tri_distirbTri_name_list = []
		other_geometry_list = []
		other_geometry_list_geom = []
		
		#####-----------------------Вторая часть параметров-geometryToConformTo------------------------------#####
		
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
					other_geometry_list.append(False)
				elif el['geometry_' + str(i)] == 'Base shape complex' or el['geometry_' + str(i)] == 'Набор базовых фигур':
					other_geometry_list_geom.append(el['name'])
					other_geometry_list.append(True)
				elif el['geometry_' + str(i)] == 'Base shape' or el['geometry_' + str(i)] == 'Базовая фигура':
					other_geometry_list_geom.append(el['shape'])
					other_geometry_list.append(True)
				i = i + 1
			
			geometry_list = []
			featureMethod_list = []
			extendedFeatureEdgeMesh_list = []
			if initial_obj['gTCT'] == True and True in tri_distirbTri_list:
			
				sC_gTCT_lbl = QtGui.QLabel()	
				sC_gTCT_lbl.setVisible(False)
				if int_lng == 'Russian':
					sC_gTCT_lbl.setText("Список конформаций поверхностей:")
				elif int_lng == 'English':
					sC_gTCT_lbl.setText("List of surfaces conformations:")
				sC_gTCT_lbl.setVisible(True)

				sC_gTCT_table = QtGui.QTableWidget()
				sC_gTCT_table.setRowCount(initial_obj['gTCT_val'])
				sC_gTCT_table.setColumnCount(3)

				sC_gTCT_table.horizontalHeader().resizeSection(0, 150)
				sC_gTCT_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				sC_gTCT_table.setHorizontalHeaderItem(0, column_1)
				sC_gTCT_table.horizontalHeader().setStyleSheet("color: steelblue")

				sC_gTCT_table.horizontalHeader().resizeSection(1, 200)
				sC_gTCT_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
				column_2 = QtGui.QTableWidgetItem()
				sC_gTCT_table.setHorizontalHeaderItem(1, column_2)
				sC_gTCT_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				sC_gTCT_table.horizontalHeader().resizeSection(2, 290)
				sC_gTCT_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
				column_3 = QtGui.QTableWidgetItem()
				sC_gTCT_table.setHorizontalHeaderItem(2, column_3)
				sC_gTCT_table.horizontalHeader().setStyleSheet("color: steelblue")

				if int_lng == 'Russian':
					column_1.setText("Три-поверхность")
					column_2.setText("Метод определения")
					column_3.setText("Расширенная функциональная решетка")
				elif int_lng == 'English':
					column_1.setText("Tri-surface")
					column_2.setText("Method of determination")
					column_3.setText("Extended function mesh")

				nof = 1
				q = 0
				height = 60
				
				while nof <= initial_obj['gTCT_val']:
					sC_gTCT_table.setFixedSize(660, height)

					#geometry#
					gTCT_geometry_edit = QtGui.QComboBox()
					gTCT_geometry_edit.setFixedSize(110, 25)
					gTCT_geometry_edit.addItems(tri_distirbTri_name_list)
					gTCT_geometry_hbox = QtGui.QHBoxLayout()
					gTCT_geometry_hbox.setContentsMargins(0, 0, 0, 0)
					gTCT_geometry_hbox.addWidget(gTCT_geometry_edit)
					gTCT_geometry_cell_widget = QtGui.QWidget()
					gTCT_geometry_cell_widget.setLayout(gTCT_geometry_hbox)
					if surfaceConformation_obj != None:
						g_geometry_edit_mas = gTCT_geometry_edit.count()  
						for t in range(g_geometry_edit_mas):
							if gTCT_geometry_edit.itemText(t) == surfaceConformation_obj['sC_conf_prs'][q]['g']:
								gTCT_geometry_edit.setCurrentIndex(t)
								
					#featureMethod#
					gTCT_featureMethod_edit = QtGui.QComboBox()
					gTCT_featureMethod_edit.setFixedSize(180, 25)
					gTCT_featureMethod_list = ['extendedFeatureEdgeMesh']
					gTCT_featureMethod_edit.addItems(gTCT_featureMethod_list)
					gTCT_featureMethod_hbox = QtGui.QHBoxLayout()
					gTCT_featureMethod_hbox.setContentsMargins(0, 0, 0, 0)
					gTCT_featureMethod_hbox.addWidget(gTCT_featureMethod_edit)
					gTCT_featureMethod_cell_widget = QtGui.QWidget()
					gTCT_featureMethod_cell_widget.setLayout(gTCT_featureMethod_hbox)
					if surfaceConformation_obj != None:
						fM_geometry_edit_mas = gTCT_featureMethod_edit.count()  
						for t in range(fM_geometry_edit_mas):
							if gTCT_featureMethod_edit.itemText(t) == surfaceConformation_obj['sC_conf_prs'][q]['fM']:
								gTCT_featureMethod_edit.setCurrentIndex(t)
					
					#extendedFeatureEdgeMesh#
					gTCT_extendedFEM_edit = QtGui.QComboBox()
					gTCT_extendedFEM_edit.setFixedSize(140, 25)
					gTCT_extendedFEM_edit.addItems(tri_distirbTri_geometry_list)
					gTCT_extendedFEM_hbox = QtGui.QHBoxLayout()
					gTCT_extendedFEM_hbox.setContentsMargins(0, 0, 0, 0)
					gTCT_extendedFEM_hbox.addWidget(gTCT_extendedFEM_edit)
					gTCT_extendedFEM_cell_widget = QtGui.QWidget()
					gTCT_extendedFEM_cell_widget.setLayout(gTCT_extendedFEM_hbox)
					if surfaceConformation_obj != None:
						eFEM_geometry_edit_mas = gTCT_extendedFEM_edit.count()  
						for t in range(eFEM_geometry_edit_mas):
							if gTCT_extendedFEM_edit.itemText(t) == surfaceConformation_obj['sC_conf_prs'][q]['eFEM']:
								gTCT_extendedFEM_edit.setCurrentIndex(t)
									
					geometry_list.append(gTCT_geometry_edit)
					featureMethod_list.append(gTCT_featureMethod_edit)
					extendedFeatureEdgeMesh_list.append(gTCT_extendedFEM_edit)

					sC_gTCT_table.setCellWidget(q, 0, gTCT_geometry_cell_widget)
					sC_gTCT_table.setCellWidget(q, 1, gTCT_featureMethod_cell_widget)
					sC_gTCT_table.setCellWidget(q, 2, gTCT_extendedFEM_cell_widget)
					
					nof = nof + 1
					q = q + 1
					height = height + 30
	
				prs_grid.addWidget(sC_gTCT_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
				prs_grid.addWidget(sC_gTCT_table, 2, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

		surfaceConformation_btnSave = QtGui.QPushButton()
		surfaceConformation_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(surfaceConformation_btnSave)
		if int_lng == 'Russian':
			surfaceConformation_btnSave.setText("Записать")
		elif int_lng == 'English':
			surfaceConformation_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		surfaceConformation_grid = QtGui.QGridLayout()
		surfaceConformation_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceConformation_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceConformation_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceConformation_grid.setRowStretch(3, 6)
		surfaceConformation_group = QtGui.QGroupBox()
		surfaceConformation_group.setLayout(surfaceConformation_grid)
		return surfaceConformation_group, surfaceConformation_btnSave, sC_start_prs_grid, geometry_list, featureMethod_list, extendedFeatureEdgeMesh_list

