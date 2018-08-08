# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class surfaceFeatureExtractDict_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, surfaceFeatureExtractDict_visible): 
		surfaceFeatureExtractDict_obj = None
		
		#----------------Если файл surfaceFeatureExtractDict.pkl существует, получаем данные из него для вывода в форму---------------#

		if surfaceFeatureExtractDict_visible == True:
			surfaceFeatureExtractDict_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceFeatureExtractDict.pkl'
			if os.path.exists(surfaceFeatureExtractDict_path_file):
		
				input = open(surfaceFeatureExtractDict_path_file, 'rb')
				surfaceFeatureExtractDict_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла surfaceFeatureExtractDict.pkl на основе данных файла initial.pkl-------------#
		
		prs_grid = QtGui.QGridLayout()
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(prs_grid)
		
		tri_distirbTri_list = []
		tri_distirbTri_geometry_list = []
		other_geometry_list = []
		other_geometry_list_geom = []
		
		#####-----------------------------------------------------#####
		
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):

			input = open(initial_path_file, 'rb')
			initial_obj = pickle.load(input)
			input.close()
				
		geometry_2_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if os.path.exists(geometry_2_path_file):

			input = open(geometry_2_path_file, 'rb')
			geometry_obj_2 = pickle.load(input)
			input.close()
				
			i = 1			
			for el in geometry_obj_2:
				if el['geometry_' + str(i)] == 'Tri-surface' or el['geometry_' + str(i)] == 'Три-поверхность' \
				or el['geometry_' + str(i)] == 'Distributed tri-surface' or el['geometry_' + str(i)] == 'Распределенная три-поверхность' \
				or el['geometry_' + str(i)] == 'Closed tri-surface' or el['geometry_' + str(i)] == 'Закрытая три-поверхность':
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
					
		#####-----------------------Третья часть параметров-surfaceFeatureExtractDict------------------------------#####				

				main_lbl = QtGui.QLabel()
				if int_lng == 'Russian':
					main_lbl.setText("Параметры извлечения поверхностей краевой сетки из файлов три-поверхностей:")
				elif int_lng == 'English':
					main_lbl.setText("Parameters of surface extracting:")
				if surfaceFeatureExtractDict_obj != None:
					main_lbl.setVisible(True)

				sFED_table = QtGui.QTableWidget()
				sFED_table.setRowCount(initial_obj['s_val'])
				sFED_table.setColumnCount(8)
				sFED_table.verticalHeader().hide()

				sFED_table.horizontalHeader().resizeSection(0, 150)
				sFED_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				sFED_table.setHorizontalHeaderItem(0, column_1)
				sFED_table.horizontalHeader().setStyleSheet("color: steelblue")

				sFED_table.horizontalHeader().resizeSection(1, 150)
				sFED_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
				column_2 = QtGui.QTableWidgetItem()
				sFED_table.setHorizontalHeaderItem(1, column_2)
				sFED_table.horizontalHeader().setStyleSheet("color: steelblue")

				sFED_table.horizontalHeader().resizeSection(2, 120)
				sFED_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
				column_3 = QtGui.QTableWidgetItem()
				sFED_table.setHorizontalHeaderItem(2, column_3)
				sFED_table.horizontalHeader().setStyleSheet("color: steelblue")

				sFED_table.horizontalHeader().resizeSection(3, 215)
				sFED_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
				column_4 = QtGui.QTableWidgetItem()
				sFED_table.setHorizontalHeaderItem(3, column_4)
				sFED_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				sFED_table.horizontalHeader().resizeSection(4, 215)
				sFED_table.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.Fixed)
				column_5 = QtGui.QTableWidgetItem()
				sFED_table.setHorizontalHeaderItem(4, column_5)
				sFED_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				sFED_table.horizontalHeader().resizeSection(5, 270)
				sFED_table.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.Fixed)
				column_6 = QtGui.QTableWidgetItem()
				sFED_table.setHorizontalHeaderItem(5, column_6)
				sFED_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				sFED_table.horizontalHeader().resizeSection(6, 210)
				sFED_table.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.Fixed)
				column_7 = QtGui.QTableWidgetItem()
				sFED_table.setHorizontalHeaderItem(6, column_7)
				sFED_table.horizontalHeader().setStyleSheet("color: steelblue")
				
				sFED_table.horizontalHeader().resizeSection(7, 120)
				sFED_table.horizontalHeader().setResizeMode(7, QtGui.QHeaderView.Fixed)
				column_8 = QtGui.QTableWidgetItem()
				sFED_table.setHorizontalHeaderItem(7, column_8)
				sFED_table.horizontalHeader().setStyleSheet("color: steelblue")
					
				if int_lng == 'Russian':
					column_1.setText("Поверхность")
					column_2.setText("Метод извлечения")	
					column_3.setText("Величина угла")
					column_4.setText("Нормаль ребер")
					column_5.setText("Базовая точка ребер")
					column_6.setText("Установить ребра без многообразия")
					column_7.setText("Установить открытые ребра")
					column_8.setText("Опция записи")	
				elif int_lng == 'English':
					column_1.setText("surface")
					column_2.setText("extractionMethod")
					column_3.setText("includedAngle")
					column_4.setText("normal")
					column_5.setText("basePoint")
					column_6.setText("nonManifoldEdges")
					column_7.setText("openEdges")
					column_8.setText("writeObj")
					
				sFED_surface_edit_list = []
				sFED_extractionMethod_edit_list = []
				sFED_includedAngle_edit_list = []
				sFED_normal_list = []
				sFED_basePoint_list = []
				sFED_nonManifoldEdges_edit_list = []
				sFED_openEdges_edit_list = []
				sFED_writeObj_edit_list = []
				
				nos = 1
				q = 0
				height = 70
				while nos <= initial_obj['s_val']:
					sFED_table.setFixedSize(1115, height)
					#surface#
					sFED_surface_edit = QtGui.QComboBox()
					sFED_surface_edit.setFixedSize(120, 25)
					sFED_surface_edit.addItems(tri_distirbTri_geometry_list)
					sFED_surface_hbox = QtGui.QHBoxLayout()
					sFED_surface_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_surface_hbox.addWidget(sFED_surface_edit)
					sFED_surface_cell_widget = QtGui.QWidget()
					sFED_surface_cell_widget.setLayout(sFED_surface_hbox)
					if surfaceFeatureExtractDict_obj != None:
						sFED_surface_edit_mas = sFED_surface_edit.count()  
						for t in range(sFED_surface_edit_mas):
							if sFED_surface_edit.itemText(t) == surfaceFeatureExtractDict_obj[q]['s']:
								sFED_surface_edit.setCurrentIndex(t)

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
					if surfaceFeatureExtractDict_obj != None:
						sFED_extractionMethod_edit_mas = sFED_extractionMethod_edit.count()  
						for t in range(sFED_extractionMethod_edit_mas):
							if sFED_extractionMethod_edit.itemText(t) == surfaceFeatureExtractDict_obj[q]['eM']:
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
					if surfaceFeatureExtractDict_obj != None:
						sFED_includedAngle_edit.setValue(surfaceFeatureExtractDict_obj[q]['iA'])
					
					#plane normal#
					normal_edit_list = []
					basePoint_edit_list = []
					
					normal_edit_x_lbl = QtGui.QLabel('x:')
					normal_edit_x = QtGui.QLineEdit()
					normal_edit_x.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, normal_edit_x))
					normal_edit_x.setFixedSize(50, 25)
					normal_edit_y_lbl = QtGui.QLabel('y:')
					normal_edit_y = QtGui.QLineEdit()
					normal_edit_y.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, normal_edit_y))
					normal_edit_y.setFixedSize(50, 25)
					normal_edit_z_lbl = QtGui.QLabel('z:')
					normal_edit_z = QtGui.QLineEdit()
					normal_edit_z.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, normal_edit_z))
					normal_edit_z.setFixedSize(50, 25)	
					sFED_normal_hbox = QtGui.QHBoxLayout()
					sFED_normal_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_normal_hbox.addWidget(normal_edit_x_lbl)
					sFED_normal_hbox.addWidget(normal_edit_x)
					sFED_normal_hbox.addWidget(normal_edit_y_lbl)
					sFED_normal_hbox.addWidget(normal_edit_y)
					sFED_normal_hbox.addWidget(normal_edit_z_lbl)
					sFED_normal_hbox.addWidget(normal_edit_z)
					sFED_normal_cell_widget = QtGui.QWidget()
					sFED_normal_cell_widget.setLayout(sFED_normal_hbox)
					normal_edit_list.append(normal_edit_x)
					normal_edit_list.append(normal_edit_y)
					normal_edit_list.append(normal_edit_z)
					if int_lng == 'Russian':
						normal_edit_x.setToolTip("Введите число") 
						normal_edit_y.setToolTip("Введите число") 
						normal_edit_z.setToolTip("Введите число") 
					elif int_lng == 'English':
						normal_edit_x.setToolTip("Enter the number") 
						normal_edit_y.setToolTip("Enter the number") 
						normal_edit_z.setToolTip("Enter the number")
					if surfaceFeatureExtractDict_obj != None:
						normal_edit_x.setText(surfaceFeatureExtractDict_obj[q]['n'][0])
						normal_edit_y.setText(surfaceFeatureExtractDict_obj[q]['n'][1])
						normal_edit_z.setText(surfaceFeatureExtractDict_obj[q]['n'][2])
					
					#plane basePoint#
					basePoint_edit_x_lbl = QtGui.QLabel('x:')
					basePoint_edit_x = QtGui.QLineEdit()
					basePoint_edit_x.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, basePoint_edit_x))
					basePoint_edit_x.setFixedSize(50, 25)
					basePoint_edit_y_lbl = QtGui.QLabel('y:')
					basePoint_edit_y = QtGui.QLineEdit()
					basePoint_edit_y.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, basePoint_edit_y))
					basePoint_edit_y.setFixedSize(50, 25)
					basePoint_edit_z_lbl = QtGui.QLabel('z:')
					basePoint_edit_z = QtGui.QLineEdit()
					basePoint_edit_z.setValidator(QtGui.QDoubleValidator(-9999999.9999999, 9999999.9999999, 7, basePoint_edit_z))
					basePoint_edit_z.setFixedSize(50, 25)
					sFED_basePoint_hbox = QtGui.QHBoxLayout()
					sFED_basePoint_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_basePoint_hbox.addWidget(basePoint_edit_x_lbl)
					sFED_basePoint_hbox.addWidget(basePoint_edit_x)
					sFED_basePoint_hbox.addWidget(basePoint_edit_y_lbl)
					sFED_basePoint_hbox.addWidget(basePoint_edit_y)
					sFED_basePoint_hbox.addWidget(basePoint_edit_z_lbl)
					sFED_basePoint_hbox.addWidget(basePoint_edit_z)
					sFED_basePoint_cell_widget = QtGui.QWidget()
					sFED_basePoint_cell_widget.setLayout(sFED_basePoint_hbox)
					basePoint_edit_list.append(basePoint_edit_x)
					basePoint_edit_list.append(basePoint_edit_y)
					basePoint_edit_list.append(basePoint_edit_z)
					
					if int_lng == 'Russian':
						basePoint_edit_x.setToolTip("Введите число") 
						basePoint_edit_y.setToolTip("Введите число") 
						basePoint_edit_z.setToolTip("Введите число") 
					elif int_lng == 'English':
						basePoint_edit_x.setToolTip("Enter the number") 
						basePoint_edit_y.setToolTip("Enter the number") 
						basePoint_edit_z.setToolTip("Enter the number")
						
					if surfaceFeatureExtractDict_obj != None:
						basePoint_edit_x.setText(surfaceFeatureExtractDict_obj[q]['bP'][0])
						basePoint_edit_y.setText(surfaceFeatureExtractDict_obj[q]['bP'][1])
						basePoint_edit_z.setText(surfaceFeatureExtractDict_obj[q]['bP'][2])
					
					#nonManifoldEdges#
					sFED_nonManifoldEdges_edit = QtGui.QComboBox()
					sFED_nonManifoldEdges_edit.setFixedSize(50, 25)
					sFED_nonManifoldEdges_list = ['yes', 'no']
					sFED_nonManifoldEdges_edit.addItems(sFED_nonManifoldEdges_list)
					sFED_nonManifoldEdges_hbox = QtGui.QHBoxLayout()
					sFED_nonManifoldEdges_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_nonManifoldEdges_hbox.addWidget(sFED_nonManifoldEdges_edit)
					sFED_nonManifoldEdges_cell_widget = QtGui.QWidget()
					sFED_nonManifoldEdges_cell_widget.setLayout(sFED_nonManifoldEdges_hbox)
					if surfaceFeatureExtractDict_obj != None:
						sFED_nonManifoldEdges_edit_mas = sFED_nonManifoldEdges_edit.count()  
						for t in range(sFED_nonManifoldEdges_edit_mas):
							if sFED_nonManifoldEdges_edit.itemText(t) == surfaceFeatureExtractDict_obj[q]['nME']:
								sFED_nonManifoldEdges_edit.setCurrentIndex(t)
					
					#openEdges#
					sFED_openEdges_edit = QtGui.QComboBox()
					sFED_openEdges_edit.setFixedSize(50, 25)
					sFED_openEdges_list = ['yes', 'no']
					sFED_openEdges_edit.addItems(sFED_openEdges_list)
					sFED_openEdges_hbox = QtGui.QHBoxLayout()
					sFED_openEdges_hbox.setContentsMargins(0, 0, 0, 0)
					sFED_openEdges_hbox.addWidget(sFED_openEdges_edit)
					sFED_openEdges_cell_widget = QtGui.QWidget()
					sFED_openEdges_cell_widget.setLayout(sFED_openEdges_hbox)
					if surfaceFeatureExtractDict_obj != None:
						sFED_openEdges_edit_mas = sFED_openEdges_edit.count()  
						for t in range(sFED_openEdges_edit_mas):
							if sFED_openEdges_edit.itemText(t) == surfaceFeatureExtractDict_obj[q]['oE']:
								sFED_openEdges_edit.setCurrentIndex(t)

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
					if surfaceFeatureExtractDict_obj != None:
						sFED_writeObj_edit_mas = sFED_writeObj_edit.count()  
						for t in range(sFED_writeObj_edit_mas):
							if sFED_writeObj_edit.itemText(t) == surfaceFeatureExtractDict_obj[q]['wO']:
								sFED_writeObj_edit.setCurrentIndex(t)
								
					sFED_surface_edit_list.append(sFED_surface_edit)
					sFED_extractionMethod_edit_list.append(sFED_extractionMethod_edit)
					sFED_includedAngle_edit_list.append(sFED_includedAngle_edit)
					sFED_normal_list.append(normal_edit_list)
					sFED_basePoint_list.append(basePoint_edit_list)
					sFED_nonManifoldEdges_edit_list.append(sFED_nonManifoldEdges_edit)
					sFED_openEdges_edit_list.append(sFED_openEdges_edit)
					sFED_writeObj_edit_list.append(sFED_writeObj_edit)			
								
					sFED_table.setCellWidget(q, 0, sFED_surface_cell_widget)
					sFED_table.setCellWidget(q, 1, sFED_extractionMethod_cell_widget)
					sFED_table.setCellWidget(q, 2, sFED_includedAngle_cell_widget)
					sFED_table.setCellWidget(q, 3, sFED_normal_cell_widget)
					sFED_table.setCellWidget(q, 4, sFED_basePoint_cell_widget)
					sFED_table.setCellWidget(q, 5, sFED_nonManifoldEdges_cell_widget)
					sFED_table.setCellWidget(q, 6, sFED_openEdges_cell_widget)
					sFED_table.setCellWidget(q, 7, sFED_writeObj_cell_widget)
					
					nos = nos + 1
					q = q + 1
					height = height + 30
				
				prs_grid.addWidget(sFED_table, 0, 0, alignment=QtCore.Qt.AlignCenter)
			
		# -------------------------Кнопка сохранения --------------------------#

		surfaceFeatureExtractDict_btnSave = QtGui.QPushButton()
		surfaceFeatureExtractDict_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(surfaceFeatureExtractDict_btnSave)
		if int_lng == 'Russian':
			surfaceFeatureExtractDict_btnSave.setText("Записать")
		elif int_lng == 'English':
			surfaceFeatureExtractDict_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		surfaceFeatureExtractDict_grid = QtGui.QGridLayout()
		surfaceFeatureExtractDict_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceFeatureExtractDict_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceFeatureExtractDict_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		surfaceFeatureExtractDict_grid.setRowStretch(3, 6)
		surfaceFeatureExtractDict_group = QtGui.QGroupBox()
		surfaceFeatureExtractDict_group.setLayout(surfaceFeatureExtractDict_grid)
		return surfaceFeatureExtractDict_group, surfaceFeatureExtractDict_btnSave, sFED_surface_edit_list, sFED_extractionMethod_edit_list, sFED_includedAngle_edit_list, sFED_normal_list, \
		sFED_basePoint_list, sFED_nonManifoldEdges_edit_list, sFED_openEdges_edit_list, sFED_writeObj_edit_list
		
		
		
				
				
				