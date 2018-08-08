# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class geometry_2_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible): 
		geometry_2_obj = None
		
		#----------------Если файл geometry_2.pkl существует, получаем данные из него для вывода в форму---------------#
		
		if geometry_visible == True:
			geometry_2_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
			if os.path.exists(geometry_2_path_file):
		
				input = open(geometry_2_path_file, 'rb')
				geometry_2_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла geometry_2.pkl на основе данных файла initial.pkl-------------#
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Параметры геометрий")
		elif int_lng == 'English':
			main_lbl.setText("Geometries parameters")
			
		geometry_1_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_1.pkl'
		if os.path.exists(geometry_1_path_file):
		
			input = open(geometry_1_path_file, 'rb')
			obj_list = pickle.load(input)
			input.close()
			
			main_grid = QtGui.QGridLayout()
			main_frame = QtGui.QFrame()
			main_frame.setLayout(main_grid)
			
			all_geometry_list = []
			
			all_geometry_list_lbls = []
			all_complex_list_lbls = []
			
			all_tri_file_btn_list = []
			all_tri_file_edit_list = []
			
			i = 1
			j = 0
			y = 0
			for el in obj_list:
				if el['geometry_' + str(i)] == 'Набор базовых фигур' or el['geometry_' + str(i)] == 'Base shape complex':
					sn = el['shapes_number_' + str(i)]
					prs_grid = QtGui.QGridLayout()
					
					complex_list = []
					complex_list_lbls = []
					
					#------------------------Таблица, если комплекс фигур------------------------------------#
						
					complex_name_lbl = QtGui.QLabel()	
					if int_lng == 'Russian':
						complex_name_lbl.setText("Название набора:")
					elif int_lng == 'English':
						complex_name_lbl.setText("Complex name:")
					complex_name_edit = QtGui.QLineEdit()
					complex_name_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
					complex_name_edit.setValidator(complex_name_validator)
					complex_name_edit.setFixedSize(190, 25)
					if geometry_2_obj != None:
						complex_name_edit.setText(geometry_2_obj[y]['name'])
					
					complex_type_lbl = QtGui.QLabel()	
					if int_lng == 'Russian':
						complex_type_lbl.setText("Тип:")
					elif int_lng == 'English':
						complex_type_lbl.setText("Type:")
					complex_type_edit = QtGui.QComboBox()
					complex_type_edit.setFixedSize(190, 30)
					complex_type_edit_list = ["searchableSurfaceCollection"]
					complex_type_edit.addItems(complex_type_edit_list)
					if geometry_2_obj != None:
						complex_type_edit_mas = complex_type_edit.count()  
						for t in range(complex_type_edit_mas):
							if complex_type_edit.itemText(t) == geometry_2_obj[y]['type']:
								complex_type_edit.setCurrentIndex(t)
					
					complex_msr_lbl = QtGui.QLabel()
					if int_lng == 'Russian':
						complex_msr_lbl.setText("Объединить подобласти:")
					elif int_lng == 'English':
						complex_msr_lbl.setText("Merge the subregions:")
					complex_msr_edit = QtGui.QComboBox()	
					complex_msr_edit.setFixedSize(60, 30)
					complex_msr_edit_list = ["true", "false"]
					complex_msr_edit.addItems(complex_msr_edit_list)
					if geometry_2_obj != None:
						complex_msr_edit_mas = complex_msr_edit.count()  
						for t in range(complex_msr_edit_mas):
							if complex_msr_edit.itemText(t) == geometry_2_obj[y]['mergeSubRegions']:
								complex_msr_edit.setCurrentIndex(t)
					
					complex_prs = QtGui.QGridLayout()
					complex_prs.addWidget(complex_name_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
					complex_prs.addWidget(complex_name_edit, 0, 1, alignment=QtCore.Qt.AlignCenter)
					complex_prs.addWidget(complex_type_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
					complex_prs.addWidget(complex_type_edit, 1, 1, alignment=QtCore.Qt.AlignCenter)
					complex_prs.addWidget(complex_msr_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
					complex_prs.addWidget(complex_msr_edit, 2, 1, alignment=QtCore.Qt.AlignCenter)
					
					#
					
					complex_shape_table = QtGui.QTableWidget()
					complex_shape_table.setFixedSize(695, 70)
					complex_shape_table.setRowCount(sn)
					complex_shape_table.setColumnCount(7)
					complex_shape_table.verticalHeader().hide()

					complex_shape_table.horizontalHeader().resizeSection(0, 100)
					complex_shape_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
					column_1 = QtGui.QTableWidgetItem()
					complex_shape_table.setHorizontalHeaderItem(0, column_1)
					complex_shape_table.horizontalHeader().setStyleSheet("color: steelblue")

					complex_shape_table.horizontalHeader().resizeSection(1, 90)
					complex_shape_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
					column_2 = QtGui.QTableWidgetItem()
					complex_shape_table.setHorizontalHeaderItem(1, column_2)
					complex_shape_table.horizontalHeader().setStyleSheet("color: steelblue")

					complex_shape_table.horizontalHeader().resizeSection(2, 140)
					complex_shape_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
					column_3 = QtGui.QTableWidgetItem()
					complex_shape_table.setHorizontalHeaderItem(2, column_3)
					complex_shape_table.horizontalHeader().setStyleSheet("color: steelblue")

					complex_shape_table.horizontalHeader().resizeSection(3, 80)
					complex_shape_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
					column_4 = QtGui.QTableWidgetItem()
					complex_shape_table.setHorizontalHeaderItem(3, column_4)
					complex_shape_table.horizontalHeader().setStyleSheet("color: steelblue")

					complex_shape_table.horizontalHeader().resizeSection(4, 145)
					complex_shape_table.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.Fixed)
					column_5 = QtGui.QTableWidgetItem()
					complex_shape_table.setHorizontalHeaderItem(4, column_5)
					complex_shape_table.horizontalHeader().setStyleSheet("color: steelblue")

					complex_shape_table.horizontalHeader().resizeSection(5, 145)
					complex_shape_table.horizontalHeader().setResizeMode(5, QtGui.QHeaderView.Fixed)
					column_6 = QtGui.QTableWidgetItem()
					complex_shape_table.setHorizontalHeaderItem(5, column_6)
					complex_shape_table.horizontalHeader().setStyleSheet("color: steelblue")

					complex_shape_table.horizontalHeader().resizeSection(6, 145)
					complex_shape_table.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.Fixed)
					column_7 = QtGui.QTableWidgetItem()
					complex_shape_table.setHorizontalHeaderItem(6, column_7)
					complex_shape_table.horizontalHeader().setStyleSheet("color: steelblue")

					if int_lng == 'Russian':
						column_1.setText("Название")
						column_2.setText("Вид")
						column_3.setText("Масштабирование")
						column_4.setText("Тип СК")
						column_5.setText("Происхождение")
						column_6.setText("Параметр e1")
						column_7.setText("Параметр e3")
					elif int_lng == 'English':
						column_1.setText("shape")
						column_2.setText("surface")
						column_3.setText("scale")
						column_4.setText("type")
						column_5.setText("origin")
						column_6.setText("e1")
						column_7.setText("e3")
						
					k = 1
					q = 0
					
					height = 70
					while k <= sn:
						complex_shape_table.setFixedSize(695, height)
						#shape#
						c_shape = QtGui.QLineEdit()
						c_shape_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
						c_shape.setValidator(c_shape_validator)
						c_shape.setContentsMargins(3, 3, 3, 0)
						c_shape.setFixedSize(100, 27)
						if geometry_2_obj != None:
							c_shape.setText(geometry_2_obj[y]['parameters'][q][0])
						
						#surface#
						c_surface = QtGui.QComboBox()
						c_surface.setFixedSize(90, 25)
						if int_lng == 'Russian':
							c_surface_list = ["шестигранник", "цилиндр", "сфера", "плоскость", "пластина"]
						elif int_lng == 'English':
							c_surface_list = ["box", "cylinder", "sphere", "plane", "plate"]
						c_surface.addItems(c_surface_list)
						if geometry_2_obj != None:
							c_surface_mas = c_surface.count()  
							for t in range(c_surface_mas):
								if c_surface.itemText(t) == geometry_2_obj[y]['parameters'][q][1]:
									c_surface.setCurrentIndex(t)
						
						#scale#
						scale_x_lbl = QtGui.QLabel('x:')
						scale_y_lbl = QtGui.QLabel('y:')
						scale_z_lbl = QtGui.QLabel('z:')

						scale_x = QtGui.QLineEdit()
						scale_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						scale_x.setValidator(scale_validator)
						scale_x.setFixedSize(27, 25)
						scale_y = QtGui.QLineEdit()
						scale_y.setValidator(scale_validator)
						scale_y.setFixedSize(27, 25)
						scale_z = QtGui.QLineEdit()
						scale_z.setValidator(scale_validator)
						scale_z.setFixedSize(27, 25)
						if geometry_2_obj != None:
							scale_x.setText(geometry_2_obj[y]['parameters'][q][2][0])
							scale_y.setText(geometry_2_obj[y]['parameters'][q][2][1])
							scale_z.setText(geometry_2_obj[y]['parameters'][q][2][2])

						scale_hbox = QtGui.QHBoxLayout()
						scale_hbox.setContentsMargins(0, 0, 0, 0)
						scale_hbox.addWidget(scale_x_lbl)
						scale_hbox.addWidget(scale_x)
						scale_hbox.addWidget(scale_y_lbl)
						scale_hbox.addWidget(scale_y)
						scale_hbox.addWidget(scale_z_lbl)
						scale_hbox.addWidget(scale_z)
						
						complex_shape_scale_cell_widget = QtGui.QWidget()
						complex_shape_scale_cell_widget.setLayout(scale_hbox)
						
						#type#
						c_type = QtGui.QComboBox()
						c_type.setFixedSize(80, 25)
						c_type_list = ["cartesian"]
						c_type.addItems(c_type_list)
						if geometry_2_obj != None:
							c_type_mas = c_surface.count()  
							for t in range(c_type_mas):
								if c_type.itemText(t) == geometry_2_obj[y]['parameters'][q][3]:
									c_type.setCurrentIndex(t)
						
						#origin#
						origin_x_lbl = QtGui.QLabel('x:')
						origin_y_lbl = QtGui.QLabel('y:')
						origin_z_lbl = QtGui.QLabel('z:')

						origin_x = QtGui.QLineEdit()
						origin_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						origin_x.setValidator(origin_validator)
						origin_x.setFixedSize(27, 25)
						origin_y = QtGui.QLineEdit()
						origin_y.setValidator(origin_validator)
						origin_y.setFixedSize(27, 25)
						origin_z = QtGui.QLineEdit()
						origin_z.setValidator(origin_validator)
						origin_z.setFixedSize(27, 25)
						if geometry_2_obj != None:
							origin_x.setText(geometry_2_obj[y]['parameters'][q][4][0])
							origin_y.setText(geometry_2_obj[y]['parameters'][q][4][1])
							origin_z.setText(geometry_2_obj[y]['parameters'][q][4][2])

						origin_hbox = QtGui.QHBoxLayout()
						origin_hbox.setContentsMargins(0, 0, 0, 0)
						origin_hbox.addWidget(origin_x_lbl)
						origin_hbox.addWidget(origin_x)
						origin_hbox.addWidget(origin_y_lbl)
						origin_hbox.addWidget(origin_y)
						origin_hbox.addWidget(origin_z_lbl)
						origin_hbox.addWidget(origin_z)
						
						complex_shape_origin_cell_widget = QtGui.QWidget()
						complex_shape_origin_cell_widget.setLayout(origin_hbox)
						
						#e1#
						e1_x_lbl = QtGui.QLabel('x:')
						e1_y_lbl = QtGui.QLabel('y:')
						e1_z_lbl = QtGui.QLabel('z:')

						e1_x = QtGui.QLineEdit()
						e1_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						e1_x.setValidator(e1_validator)
						e1_x.setFixedSize(27, 25)
						e1_y = QtGui.QLineEdit()
						e1_y.setValidator(e1_validator)
						e1_y.setFixedSize(27, 25)
						e1_z = QtGui.QLineEdit()
						e1_z.setValidator(e1_validator)
						e1_z.setFixedSize(27, 25)
						if geometry_2_obj != None:
							e1_x.setText(geometry_2_obj[y]['parameters'][q][5][0])
							e1_y.setText(geometry_2_obj[y]['parameters'][q][5][1])
							e1_z.setText(geometry_2_obj[y]['parameters'][q][5][2])

						e1_hbox = QtGui.QHBoxLayout()
						e1_hbox.setContentsMargins(0, 0, 0, 0)
						e1_hbox.addWidget(e1_x_lbl)
						e1_hbox.addWidget(e1_x)
						e1_hbox.addWidget(e1_y_lbl)
						e1_hbox.addWidget(e1_y)
						e1_hbox.addWidget(e1_z_lbl)
						e1_hbox.addWidget(e1_z)
						
						complex_shape_e1_cell_widget = QtGui.QWidget()
						complex_shape_e1_cell_widget.setLayout(e1_hbox)
						
						#e3#
						e3_x_lbl = QtGui.QLabel('x:')
						e3_y_lbl = QtGui.QLabel('y:')
						e3_z_lbl = QtGui.QLabel('z:')

						e3_x = QtGui.QLineEdit()
						e3_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						e3_x.setValidator(e3_validator)
						e3_x.setFixedSize(27, 25)
						e3_y = QtGui.QLineEdit()
						e3_y.setValidator(e3_validator)
						e3_y.setFixedSize(27, 25)
						e3_z = QtGui.QLineEdit()
						e3_z.setValidator(e3_validator)
						e3_z.setFixedSize(27, 25)
						if geometry_2_obj != None:
							e3_x.setText(geometry_2_obj[y]['parameters'][q][6][0])
							e3_y.setText(geometry_2_obj[y]['parameters'][q][6][1])
							e3_z.setText(geometry_2_obj[y]['parameters'][q][6][2])

						e3_hbox = QtGui.QHBoxLayout()
						e3_hbox.setContentsMargins(0, 0, 0, 0)
						e3_hbox.addWidget(e3_x_lbl)
						e3_hbox.addWidget(e3_x)
						e3_hbox.addWidget(e3_y_lbl)
						e3_hbox.addWidget(e3_y)
						e3_hbox.addWidget(e3_z_lbl)
						e3_hbox.addWidget(e3_z)
						
						complex_shape_e3_cell_widget = QtGui.QWidget()
						complex_shape_e3_cell_widget.setLayout(e3_hbox)
						
						complex_shape_table.setCellWidget(q, 0, c_shape)
						complex_shape_table.setCellWidget(q, 1, c_surface)
						complex_shape_table.setCellWidget(q, 2, complex_shape_scale_cell_widget)
						complex_shape_table.setCellWidget(q, 3, c_type)
						complex_shape_table.setCellWidget(q, 4, complex_shape_origin_cell_widget)
						complex_shape_table.setCellWidget(q, 5, complex_shape_e1_cell_widget)
						complex_shape_table.setCellWidget(q, 6, complex_shape_e3_cell_widget)
						
						k = k + 1
						q = q + 1
						height = height + 30
					
					complex_list.append(complex_name_edit)
					complex_list.append(complex_type_edit)
					complex_list.append(complex_msr_edit)
					complex_list.append(complex_shape_table)
					
					complex_list_lbls.append('complex_name_edit')
					complex_list_lbls.append('complex_type_edit')
					complex_list_lbls.append('complex_msr_edit')
					complex_list_lbls.append('complex_shape_table')
					
					all_geometry_list.append(complex_list)
					all_geometry_list_lbls.append('complex_list')
					all_complex_list_lbls.append(complex_list_lbls)
					all_tri_file_btn_list.append('')
					all_tri_file_edit_list.append('')
					
					prs_grid.addLayout(complex_prs, 0, 0, alignment=QtCore.Qt.AlignCenter)
					prs_grid.addWidget(complex_shape_table, 1, 0, alignment=QtCore.Qt.AlignCenter)
					
					prs_frame = QtGui.QFrame()
					prs_frame.setLayout(prs_grid)
					
					geometry_numb = QtGui.QLabel()
					if int_lng == 'Russian':
						geometry_numb.setText("Геометрия_" + str(i) + " - набор фигур")
					elif int_lng == 'English':
						geometry_numb.setText("Geometry_" + str(i) + " - shapes complex")
					
					main_grid.addWidget(geometry_numb, j, 0, alignment=QtCore.Qt.AlignCenter)
					main_grid.addWidget(prs_frame, j+1, 0, alignment=QtCore.Qt.AlignCenter)
					
				#-------------------------Таблица параметров для три-поверхности---------------------------#

				if el['geometry_' + str(i)] == 'Три-поверхность' or el['geometry_' + str(i)] == 'Tri-surface':
					rn = el['regions_number_' + str(i)]
					
					tri_table = QtGui.QTableWidget()
					tri_table.setFixedSize(385, 62)
					tri_table.setRowCount(1)
					tri_table.setColumnCount(3+rn)
					tri_table.verticalHeader().hide()
					
					tri_table.horizontalHeader().resizeSection(0, 140)
					tri_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
					column_1 = QtGui.QTableWidgetItem()
					tri_table.setHorizontalHeaderItem(0, column_1)
					tri_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					tri_table.horizontalHeader().resizeSection(1, 120)
					tri_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
					column_2 = QtGui.QTableWidgetItem()
					tri_table.setHorizontalHeaderItem(1, column_2)
					tri_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					tri_table.horizontalHeader().resizeSection(2, 120)
					tri_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
					column_3 = QtGui.QTableWidgetItem()
					tri_table.setHorizontalHeaderItem(2, column_3)
					tri_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					if int_lng == 'Russian':
						column_1.setText("Файл")
						column_2.setText("Тип")
						column_3.setText("Название")
					elif int_lng == 'English':
						column_1.setText("file")
						column_2.setText("type")
						column_3.setText("name")

					tri_file_edit = QtGui.QLineEdit()
					tri_file_edit.setEnabled(False)
					tri_file_edit.setFixedSize(105, 25)
					tri_file_btn = QtGui.QPushButton("...")
					tri_file_btn.setFixedSize(25, 25)
					tri_file_hbox = QtGui.QHBoxLayout()
					tri_file_hbox.setContentsMargins(0, 0, 0, 0)
					tri_file_hbox.addWidget(tri_file_edit)
					tri_file_hbox.addWidget(tri_file_btn)
					tri_file_cell_widget = QtGui.QWidget()
					tri_file_cell_widget.setLayout(tri_file_hbox)
					if geometry_2_obj != None:
						tri_file_edit.setText(geometry_2_obj[y]['file'])

					tri_type_edit = QtGui.QComboBox()
					tri_type_edit.setFixedSize(105, 25)
					tri_type_edit_list = ["triSurfaceMesh"]
					tri_type_edit.addItems(tri_type_edit_list)
					tri_type_hbox = QtGui.QHBoxLayout()
					tri_type_hbox.setContentsMargins(0, 0, 0, 0)
					tri_type_hbox.addWidget(tri_type_edit)
					tri_type_cell_widget = QtGui.QWidget()
					tri_type_cell_widget.setLayout(tri_type_hbox)
					if geometry_2_obj != None:
						tri_type_mas = tri_type_edit.count()  
						for t in range(tri_type_mas):
							if tri_type_edit.itemText(t) == geometry_2_obj[y]['type']:
								tri_type_edit.setCurrentIndex(t)

					tri_name_edit = QtGui.QLineEdit()
					tri_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
					tri_name_edit.setValidator(tri_validator)
					tri_name_edit.setFixedSize(117, 27)
					tri_name_hbox = QtGui.QHBoxLayout()
					tri_name_hbox.setContentsMargins(0, 0, 0, 0)
					tri_name_hbox.addWidget(tri_name_edit)
					tri_name_cell_widget = QtGui.QWidget()
					tri_name_cell_widget.setLayout(tri_name_hbox)
					if geometry_2_obj != None:
						tri_name_edit.setText(geometry_2_obj[y]['name'])

					tri_table.setCellWidget(0,0, tri_file_cell_widget)
					tri_table.setCellWidget(0,1, tri_type_cell_widget)
					tri_table.setCellWidget(0,2, tri_name_cell_widget)
					
					all_geometry_list.append(tri_table)
					all_geometry_list_lbls.append('tri_table')
					all_complex_list_lbls.append('')
					all_tri_file_btn_list.append(tri_file_btn)
					all_tri_file_edit_list.append(tri_file_edit)

					geometry_numb = QtGui.QLabel()
					if int_lng == 'Russian':
						geometry_numb.setText("Геометрия_" + str(i) + " - Три-поверхность")
					elif int_lng == 'English':
						geometry_numb.setText("Geometry_" + str(i) + " - Tri-surface")
					
					z = 1
					a = 3
					p = 0
					width = 575
				
					while z <= rn:
						tri_table.setFixedSize(width, 110)
						
						tri_table.horizontalHeader().resizeSection(a, 190)
						tri_table.horizontalHeader().setResizeMode(a, QtGui.QHeaderView.Fixed)
						column_dinamic = QtGui.QTableWidgetItem()
						tri_table.setHorizontalHeaderItem(a, column_dinamic)
						tri_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						tri_table.setRowHeight(0, 100)
						
						if int_lng == 'Russian':
							column_dinamic.setText("Подобласть_" + str(z))
						elif int_lng == 'English':
							column_dinamic.setText("Region " + str(z))
							
						STL_name_lbl = QtGui.QLabel()
						user_name_lbl = QtGui.QLabel()
						if int_lng == 'Russian':
							STL_name_lbl.setText("STL-имя:")
							user_name_lbl.setText("Usr-имя:")
						elif int_lng == 'English':
							STL_name_lbl.setText("STL-name:")
							user_name_lbl.setText("Usr-name:")
						
						STL_name_edit = QtGui.QLineEdit()
						STL_name_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
						STL_name_edit.setValidator(STL_name_validator)
						if geometry_2_obj != None:
							STL_name_edit.setText(geometry_2_obj[y]['regions'][p]['region_' + str(z)][0])
						user_name_edit = QtGui.QLineEdit()
						user_name_edit.setValidator(STL_name_validator)
						STL_name_edit.setFixedSize(120, 30)
						user_name_edit.setFixedSize(120, 30)
						if geometry_2_obj != None:
							user_name_edit.setText(geometry_2_obj[y]['regions'][p]['region_' + str(z)][1])
						
						regions_grid = QtGui.QGridLayout()
						regions_grid.addWidget(STL_name_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
						regions_grid.addWidget(STL_name_edit, 0, 1, alignment=QtCore.Qt.AlignCenter)
						regions_grid.addWidget(user_name_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
						regions_grid.addWidget(user_name_edit, 1, 1, alignment=QtCore.Qt.AlignCenter)
						regions_grid.setRowStretch(3, 6)
						
						regions_cell_widget = QtGui.QWidget()
						regions_cell_widget.setLayout(regions_grid)
						tri_table.setCellWidget(0, a, regions_cell_widget)

						z = z + 1
						a = a + 1
						p = p + 1
						width = width + 190
						
					main_grid.addWidget(geometry_numb, j, 0, alignment=QtCore.Qt.AlignCenter)
					main_grid.addWidget(tri_table, j+1, 0, alignment=QtCore.Qt.AlignCenter)
					
				#-------------------------Таблица параметров для распределенной три-поверхности---------------------------#

				if el['geometry_' + str(i)] == 'Распределенная три-поверхность' or el['geometry_' + str(i)] == 'Distributed tri-surface':
					rn = el['regions_number_' + str(i)]
					print(el['geometry_' + str(i)])
					distrib_tri_table = QtGui.QTableWidget()
					distrib_tri_table.setFixedSize(615, 62)
					distrib_tri_table.setRowCount(1)
					distrib_tri_table.setColumnCount(4+rn)
					distrib_tri_table.verticalHeader().hide()
					
					distrib_tri_table.horizontalHeader().resizeSection(0, 160)
					distrib_tri_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
					column_1 = QtGui.QTableWidgetItem()
					distrib_tri_table.setHorizontalHeaderItem(0, column_1)
					distrib_tri_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					distrib_tri_table.horizontalHeader().resizeSection(1, 180)
					distrib_tri_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
					column_2 = QtGui.QTableWidgetItem()
					distrib_tri_table.setHorizontalHeaderItem(1, column_2)
					distrib_tri_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					distrib_tri_table.horizontalHeader().resizeSection(2, 150)
					distrib_tri_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
					column_3 = QtGui.QTableWidgetItem()
					distrib_tri_table.setHorizontalHeaderItem(2, column_3)
					distrib_tri_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					distrib_tri_table.horizontalHeader().resizeSection(3, 120)
					distrib_tri_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
					column_4 = QtGui.QTableWidgetItem()
					distrib_tri_table.setHorizontalHeaderItem(3, column_4)
					distrib_tri_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					if int_lng == 'Russian':
						column_1.setText("Файл")
						column_2.setText("Тип")
						column_3.setText("Тип распределения")
						column_4.setText("Название")
					elif int_lng == 'English':
						column_1.setText("file")
						column_2.setText("type")
						column_3.setText("distributionType")
						column_4.setText("name")

					distrib_tri_file_edit = QtGui.QLineEdit()
					distrib_tri_file_edit.setEnabled(False)
					distrib_tri_file_edit.setFixedSize(125, 25)
					distrib_tri_file_btn = QtGui.QPushButton("...")
					distrib_tri_file_btn.setFixedSize(25, 25)
					distrib_tri_file_hbox = QtGui.QHBoxLayout()
					distrib_tri_file_hbox.setContentsMargins(0, 0, 0, 0)
					distrib_tri_file_hbox.addWidget(distrib_tri_file_edit)
					distrib_tri_file_hbox.addWidget(distrib_tri_file_btn)
					distrib_tri_file_cell_widget = QtGui.QWidget()
					distrib_tri_file_cell_widget.setLayout(distrib_tri_file_hbox)
					if geometry_2_obj != None:
						distrib_tri_file_edit.setText(geometry_2_obj[y]['file'])
						
					distrib_tri_type_edit = QtGui.QComboBox()
					distrib_tri_type_edit_list = ["distributedTriSurfaceMesh"]
					distrib_tri_type_edit.addItems(distrib_tri_type_edit_list)
					distrib_tri_type_hbox = QtGui.QHBoxLayout()
					distrib_tri_type_hbox.setContentsMargins(0, 0, 0, 0)
					distrib_tri_type_hbox.addWidget(distrib_tri_type_edit)
					distrib_tri_type_cell_widget = QtGui.QWidget()
					distrib_tri_type_cell_widget.setLayout(distrib_tri_type_hbox)
					if geometry_2_obj != None:
						distrib_tri_type_mas = distrib_tri_type_edit.count()  
						for t in range(distrib_tri_type_mas):
							if distrib_tri_type_edit.itemText(t) == geometry_2_obj[y]['type']:
								distrib_tri_type_edit.setCurrentIndex(t)

					distribution_tri_type_edit = QtGui.QComboBox()
					distribution_tri_type_edit_list = ["follow", "independent", "frozen"]
					distribution_tri_type_edit.addItems(distribution_tri_type_edit_list)
					distribution_tri_type_hbox = QtGui.QHBoxLayout()
					distribution_tri_type_hbox.setContentsMargins(0, 0, 0, 0)
					distribution_tri_type_hbox.addWidget(distribution_tri_type_edit)
					distribution_tri_type_cell_widget = QtGui.QWidget()
					distribution_tri_type_cell_widget.setLayout(distribution_tri_type_hbox)
					if geometry_2_obj != None:
						distribution_tri_type_mas = distribution_tri_type_edit.count()  
						for t in range(distribution_tri_type_mas):
							if distribution_tri_type_edit.itemText(t) == geometry_2_obj[y]['distributionType']:
								distribution_tri_type_edit.setCurrentIndex(t)

					distrib_tri_name_edit = QtGui.QLineEdit()
					distrib_tri_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
					distrib_tri_name_edit.setValidator(distrib_tri_validator)
					distrib_tri_name_edit.setContentsMargins(3, 3, 3, 0)
					distrib_tri_name_edit.setFixedSize(120, 27)
					distrib_tri_name_hbox = QtGui.QHBoxLayout()
					distrib_tri_name_hbox.setContentsMargins(0, 0, 0, 0)
					distrib_tri_name_hbox.addWidget(distrib_tri_name_edit)
					distrib_tri_name_cell_widget = QtGui.QWidget()
					distrib_tri_name_cell_widget.setLayout(distrib_tri_name_hbox)
					if geometry_2_obj != None:
						distrib_tri_name_edit.setText(geometry_2_obj[y]['name'])

					distrib_tri_table.setCellWidget(0,0, distrib_tri_file_cell_widget)
					distrib_tri_table.setCellWidget(0,1, distrib_tri_type_cell_widget)
					distrib_tri_table.setCellWidget(0,2, distribution_tri_type_cell_widget)
					distrib_tri_table.setCellWidget(0,3, distrib_tri_name_cell_widget)
					
					all_geometry_list.append(distrib_tri_table)
					all_geometry_list_lbls.append('distrib_tri_table')
					all_complex_list_lbls.append('')
					all_tri_file_btn_list.append(distrib_tri_file_btn)
					all_tri_file_edit_list.append(distrib_tri_file_edit)
					
					geometry_numb = QtGui.QLabel()
					if int_lng == 'Russian':
						geometry_numb.setText("Геометрия_" + str(i) + " - Три-поверхность")
					elif int_lng == 'English':
						geometry_numb.setText("Geometry_" + str(i) + " - Tri-surface")
					
					z = 1
					a = 4
					p = 0
					width = 805
				
					while z <= rn:
						distrib_tri_table.setFixedSize(width, 110)
						
						distrib_tri_table.horizontalHeader().resizeSection(a, 190)
						distrib_tri_table.horizontalHeader().setResizeMode(a, QtGui.QHeaderView.Fixed)
						column_dinamic = QtGui.QTableWidgetItem()
						distrib_tri_table.setHorizontalHeaderItem(a, column_dinamic)
						distrib_tri_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						distrib_tri_table.setRowHeight(0, 100)
						
						if int_lng == 'Russian':
							column_dinamic.setText("Подобласть_" + str(z))
						elif int_lng == 'English':
							column_dinamic.setText("Region " + str(z))
							
						STL_name_lbl = QtGui.QLabel()
						user_name_lbl = QtGui.QLabel()
						if int_lng == 'Russian':
							STL_name_lbl.setText("STL-имя:")
							user_name_lbl.setText("Usr-имя:")
						elif int_lng == 'English':
							STL_name_lbl.setText("STL-name:")
							user_name_lbl.setText("Usr-name:")
						
						STL_name_edit = QtGui.QLineEdit()
						STL_name_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
						STL_name_edit.setValidator(STL_name_validator)
						if geometry_2_obj != None:
							STL_name_edit.setText(geometry_2_obj[y]['regions'][p]['region_' + str(z)][0])
						
						user_name_edit = QtGui.QLineEdit()
						user_name_edit.setValidator(STL_name_validator)
						STL_name_edit.setFixedSize(120, 30)
						user_name_edit.setFixedSize(120, 30)
						if geometry_2_obj != None:
							user_name_edit.setText(geometry_2_obj[y]['regions'][p]['region_' + str(z)][1])
						
						regions_grid = QtGui.QGridLayout()
						regions_grid.addWidget(STL_name_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
						regions_grid.addWidget(STL_name_edit, 0, 1, alignment=QtCore.Qt.AlignCenter)
						regions_grid.addWidget(user_name_lbl, 1, 0, alignment=QtCore.Qt.AlignCenter)
						regions_grid.addWidget(user_name_edit, 1, 1, alignment=QtCore.Qt.AlignCenter)
						regions_grid.setRowStretch(3, 6)
						
						regions_cell_widget = QtGui.QWidget()
						regions_cell_widget.setLayout(regions_grid)
						distrib_tri_table.setCellWidget(0, a, regions_cell_widget)

						z = z + 1
						a = a + 1
						p = p + 1
						width = width + 190

					geometry_numb = QtGui.QLabel()
					if int_lng == 'Russian':
						geometry_numb.setText("Геометрия_" + str(i) + " - Распределенная три-поверхность")
					elif int_lng == 'English':
						geometry_numb.setText("Geometry_" + str(i) + " - Distributed tri-surface")
	
					main_grid.addWidget(geometry_numb, j, 0, alignment=QtCore.Qt.AlignCenter)
					main_grid.addWidget(distrib_tri_table, j+1, 0, alignment=QtCore.Qt.AlignCenter)
								
				if el['geometry_' + str(i)] == 'Базовая фигура' or el['geometry_' + str(i)] == 'Base shape':
					
					#--------------------------Таблица параметров для фигуры box------------------------------#

					if el['shape_type_' + str(i)] == 'шестигранник' or el['shape_type_' + str(i)] == 'box':
						
						box_table = QtGui.QTableWidget()
						box_table.setFixedSize(625, 60)
						box_table.setRowCount(1)
						box_table.setColumnCount(4)
						box_table.verticalHeader().hide()

						box_table.horizontalHeader().resizeSection(0, 120)
						box_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
						column_1 = QtGui.QTableWidgetItem()
						box_table.setHorizontalHeaderItem(0, column_1)
						box_table.horizontalHeader().setStyleSheet("color: steelblue")

						box_table.horizontalHeader().resizeSection(1, 160)
						box_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
						column_2 = QtGui.QTableWidgetItem()
						box_table.setHorizontalHeaderItem(1, column_2)
						box_table.horizontalHeader().setStyleSheet("color: steelblue")

						box_table.horizontalHeader().resizeSection(2, 170)
						box_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
						column_3 = QtGui.QTableWidgetItem()
						box_table.setHorizontalHeaderItem(2, column_3)
						box_table.horizontalHeader().setStyleSheet("color: steelblue")

						box_table.horizontalHeader().resizeSection(3, 170)
						box_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
						column_4 = QtGui.QTableWidgetItem()
						box_table.setHorizontalHeaderItem(3, column_4)
						box_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						if int_lng == 'Russian':
							column_1.setText("Название")
							column_2.setText("Тип")
							column_3.setText("Мин")
							column_4.setText("Макс")
						elif int_lng == 'English':
							column_1.setText("shape")
							column_2.setText("type")
							column_3.setText("min")
							column_4.setText("max")

						#Shape#
						box_edit = QtGui.QLineEdit()
						box_edit.setContentsMargins(3, 3, 3, 0)
						box_edit.setFixedSize(120, 27)
						box_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
						box_edit.setValidator(box_validator)
						if geometry_2_obj != None:
							box_edit.setText(geometry_2_obj[y]['shape'])

						#type#
						box_type_edit = QtGui.QComboBox()
						box_type_edit_list = ["searchableBox"]
						box_type_edit.addItems(box_type_edit_list)
						if geometry_2_obj != None:
							box_type_edit_mas = box_type_edit.count()  
							for t in range(box_type_edit_mas):
								if box_type_edit.itemText(t) == geometry_2_obj[y]['type']:
									box_type_edit.setCurrentIndex(t)

						#min#
						min_x_lbl = QtGui.QLabel('x:')
						min_y_lbl = QtGui.QLabel('y:')
						min_z_lbl = QtGui.QLabel('z:')

						min_x = QtGui.QLineEdit()
						box_min_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						min_x.setValidator(box_min_validator)
						min_x.setFixedSize(35, 25)
						min_y = QtGui.QLineEdit()
						min_y.setValidator(box_min_validator)
						min_y.setFixedSize(35, 25)
						min_z = QtGui.QLineEdit()
						min_z.setValidator(box_min_validator)
						min_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							min_x.setText(geometry_2_obj[y]['min'][0])
							min_y.setText(geometry_2_obj[y]['min'][1])
							min_z.setText(geometry_2_obj[y]['min'][2])

						min_hbox = QtGui.QHBoxLayout()
						min_hbox.setContentsMargins(0, 0, 0, 0)
						min_hbox.addWidget(min_x_lbl)
						min_hbox.addWidget(min_x)
						min_hbox.addWidget(min_y_lbl)
						min_hbox.addWidget(min_y)
						min_hbox.addWidget(min_z_lbl)
						min_hbox.addWidget(min_z)
						
						box_min_cell_widget = QtGui.QWidget()
						box_min_cell_widget.setLayout(min_hbox)

						#max#
						max_x_lbl = QtGui.QLabel('x:')
						max_y_lbl = QtGui.QLabel('y:')
						max_z_lbl = QtGui.QLabel('z:')

						max_x = QtGui.QLineEdit()
						box_max_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						max_x.setValidator(box_max_validator)
						max_x.setFixedSize(35, 25)
						max_y = QtGui.QLineEdit()
						max_y.setValidator(box_max_validator)
						max_y.setFixedSize(35, 25)
						max_z = QtGui.QLineEdit()
						max_z.setValidator(box_max_validator)
						max_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							max_x.setText(geometry_2_obj[y]['max'][0])
							max_y.setText(geometry_2_obj[y]['max'][1])
							max_z.setText(geometry_2_obj[y]['max'][2])

						max_hbox = QtGui.QHBoxLayout()
						max_hbox.setContentsMargins(0, 0, 0, 0)
						max_hbox.addWidget(max_x_lbl)
						max_hbox.addWidget(max_x)
						max_hbox.addWidget(max_y_lbl)
						max_hbox.addWidget(max_y)
						max_hbox.addWidget(max_z_lbl)
						max_hbox.addWidget(max_z)
						
						box_max_cell_widget = QtGui.QWidget()
						box_max_cell_widget.setLayout(max_hbox)

						#add_to_table
						box_table.setCellWidget(0,0, box_edit)
						box_table.setCellWidget(0,1, box_type_edit)
						box_table.setCellWidget(0,2, box_min_cell_widget)
						box_table.setCellWidget(0,3, box_max_cell_widget)
						
						all_geometry_list.append(box_table)
						all_geometry_list_lbls.append('box_table')
						all_complex_list_lbls.append('')
						all_tri_file_btn_list.append('')
						all_tri_file_edit_list.append('')
						
						geometry_numb = QtGui.QLabel()
						if int_lng == 'Russian':
							geometry_numb.setText("Геометрия_" + str(i) + " - шестигранник")
						elif int_lng == 'English':
							geometry_numb.setText("Geometry_" + str(i) + " - box")

						main_grid.addWidget(geometry_numb, j, 0, alignment=QtCore.Qt.AlignCenter)
						main_grid.addWidget(box_table, j+1, 0, alignment=QtCore.Qt.AlignCenter)
						
					#--------------------------Таблица параметров для фигуры sphere------------------------------#
						
					if el['shape_type_' + str(i)] == 'сфера' or el['shape_type_' + str(i)] == 'sphere':
					
						sphere_table = QtGui.QTableWidget()
						sphere_table.setFixedSize(540, 60)
						sphere_table.setRowCount(1)
						sphere_table.setColumnCount(4)
						sphere_table.verticalHeader().hide()

						sphere_table.horizontalHeader().resizeSection(0, 120)
						sphere_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
						column_1 = QtGui.QTableWidgetItem()
						sphere_table.setHorizontalHeaderItem(0, column_1)
						sphere_table.horizontalHeader().setStyleSheet("color: steelblue")

						sphere_table.horizontalHeader().resizeSection(1, 160)
						sphere_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
						column_2 = QtGui.QTableWidgetItem()
						sphere_table.setHorizontalHeaderItem(1, column_2)
						sphere_table.horizontalHeader().setStyleSheet("color: steelblue")

						sphere_table.horizontalHeader().resizeSection(2, 170)
						sphere_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
						column_3 = QtGui.QTableWidgetItem()
						sphere_table.setHorizontalHeaderItem(2, column_3)
						sphere_table.horizontalHeader().setStyleSheet("color: steelblue")

						sphere_table.horizontalHeader().resizeSection(3, 85)
						sphere_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
						column_4 = QtGui.QTableWidgetItem()
						sphere_table.setHorizontalHeaderItem(3, column_4)
						sphere_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						if int_lng == 'Russian':
							column_1.setText("Название")
							column_2.setText("Тип")
							column_3.setText("Центр")
							column_4.setText("Радиус")
						elif int_lng == 'English':
							column_1.setText("shape")
							column_2.setText("type")
							column_3.setText("centre")
							column_4.setText("radius")

						#Shape#
						sphere_edit = QtGui.QLineEdit()
						sphere_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
						sphere_edit.setValidator(sphere_validator)
						sphere_edit.setFixedSize(25, 25)
						sphere_edit.setContentsMargins(3, 3, 3, 0)
						sphere_edit.setFixedSize(120, 27)
						if geometry_2_obj != None:
							sphere_edit.setText(geometry_2_obj[y]['shape'])
						

						#type#
						sphere_type_edit = QtGui.QComboBox()
						sphere_type_edit_list = ["searchableSphere"]
						sphere_type_edit.addItems(sphere_type_edit_list)
						if geometry_2_obj != None:
							sphere_type_edit_mas = sphere_type_edit.count()  
							for t in range(sphere_type_edit_mas):
								if sphere_type_edit.itemText(t) == geometry_2_obj[y]['type']:
									sphere_type_edit.setCurrentIndex(t)

						#centre#
						centre_x_lbl = QtGui.QLabel('x:')
						centre_y_lbl = QtGui.QLabel('y:')
						centre_z_lbl = QtGui.QLabel('z:')

						centre_x = QtGui.QLineEdit()
						sphere_centre_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						centre_x.setValidator(sphere_centre_validator)
						centre_x.setFixedSize(35, 25)
						centre_y = QtGui.QLineEdit()
						centre_y.setValidator(sphere_centre_validator)
						centre_y.setFixedSize(35, 25)
						centre_z = QtGui.QLineEdit()
						centre_z.setValidator(sphere_centre_validator)
						centre_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							centre_x.setText(geometry_2_obj[y]['centre'][0])
							centre_y.setText(geometry_2_obj[y]['centre'][1])
							centre_z.setText(geometry_2_obj[y]['centre'][2])

						centre_hbox = QtGui.QHBoxLayout()
						centre_hbox.setContentsMargins(0, 0, 0, 0)
						centre_hbox.addWidget(centre_x_lbl)
						centre_hbox.addWidget(centre_x)
						centre_hbox.addWidget(centre_y_lbl)
						centre_hbox.addWidget(centre_y)
						centre_hbox.addWidget(centre_z_lbl)
						centre_hbox.addWidget(centre_z)
						
						sphere_centre_cell_widget = QtGui.QWidget()
						sphere_centre_cell_widget.setLayout(centre_hbox)

						#radius#
						sphere_radius_edit = QtGui.QLineEdit()
						sphere_radius_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						sphere_radius_edit.setValidator(sphere_radius_validator)
						sphere_radius_edit.setContentsMargins(0, 0, 0, 0)
						sphere_radius_edit.setFixedSize(80, 27)
						if geometry_2_obj != None:
							sphere_radius_edit.setText(geometry_2_obj[y]['radius'])

						#add_to_table
						sphere_table.setCellWidget(0,0, sphere_edit)
						sphere_table.setCellWidget(0,1, sphere_type_edit)
						sphere_table.setCellWidget(0,2, sphere_centre_cell_widget)
						sphere_table.setCellWidget(0,3, sphere_radius_edit)
						
						all_geometry_list.append(sphere_table)
						all_geometry_list_lbls.append('sphere_table')
						all_complex_list_lbls.append('')
						all_tri_file_btn_list.append('')
						all_tri_file_edit_list.append('')
						
						geometry_numb = QtGui.QLabel()
						if int_lng == 'Russian':
							geometry_numb.setText("Геометрия_" + str(i) + " - сфера")
						elif int_lng == 'English':
							geometry_numb.setText("Geometry_" + str(i) + " - sphere")

						main_grid.addWidget(geometry_numb, j, 0, alignment=QtCore.Qt.AlignCenter)
						main_grid.addWidget(sphere_table, j+1, 0, alignment=QtCore.Qt.AlignCenter)
						
					#--------------------------Таблица параметров для фигуры cylinder------------------------------#
						
					if el['shape_type_' + str(i)] == 'цилиндр' or el['shape_type_' + str(i)] == 'cylinder':
						
						cylinder_table = QtGui.QTableWidget()
						cylinder_table.setFixedSize(710, 60)
						cylinder_table.setRowCount(1)
						cylinder_table.setColumnCount(5)
						cylinder_table.verticalHeader().hide()

						cylinder_table.horizontalHeader().resizeSection(0, 120)
						cylinder_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
						column_1 = QtGui.QTableWidgetItem()
						cylinder_table.setHorizontalHeaderItem(0, column_1)
						cylinder_table.horizontalHeader().setStyleSheet("color: steelblue")

						cylinder_table.horizontalHeader().resizeSection(1, 160)
						cylinder_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
						column_2 = QtGui.QTableWidgetItem()
						cylinder_table.setHorizontalHeaderItem(1, column_2)
						cylinder_table.horizontalHeader().setStyleSheet("color: steelblue")

						cylinder_table.horizontalHeader().resizeSection(2, 170)
						cylinder_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
						column_3 = QtGui.QTableWidgetItem()
						cylinder_table.setHorizontalHeaderItem(2, column_3)
						cylinder_table.horizontalHeader().setStyleSheet("color: steelblue")

						cylinder_table.horizontalHeader().resizeSection(3, 170)
						cylinder_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
						column_4 = QtGui.QTableWidgetItem()
						cylinder_table.setHorizontalHeaderItem(3, column_4)
						cylinder_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						cylinder_table.horizontalHeader().resizeSection(4, 85)
						cylinder_table.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.Fixed)
						column_5 = QtGui.QTableWidgetItem()
						cylinder_table.setHorizontalHeaderItem(4, column_5)
						cylinder_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						if int_lng == 'Russian':
							column_1.setText("Название")
							column_2.setText("Тип")
							column_3.setText("Точка_1")
							column_4.setText("Точка_2")
							column_5.setText("Радиус")
						elif int_lng == 'English':
							column_1.setText("shape")
							column_2.setText("type")
							column_3.setText("point1")
							column_4.setText("point2")
							column_5.setText("radius")

						#Shape#
						cylinder_edit = QtGui.QLineEdit()
						cylinder_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
						cylinder_edit.setValidator(cylinder_validator)
						cylinder_edit.setContentsMargins(3, 3, 3, 0)
						cylinder_edit.setFixedSize(120, 27)
						if geometry_2_obj != None:
							cylinder_edit.setText(geometry_2_obj[y]['shape'])

						#type#
						cylinder_type_edit = QtGui.QComboBox()
						cylinder_type_edit_list = ["searchableCylinder"]
						cylinder_type_edit.addItems(cylinder_type_edit_list)
						if geometry_2_obj != None:
							cylinder_type_edit_mas = cylinder_type_edit.count()  
							for t in range(cylinder_type_edit_mas):
								if cylinder_type_edit.itemText(t) == geometry_2_obj[y]['type']:
									cylinder_type_edit.setCurrentIndex(t)

						#point1#
						point1_x_lbl = QtGui.QLabel('x:')
						point1_y_lbl = QtGui.QLabel('y:')
						point1_z_lbl = QtGui.QLabel('z:')

						point1_x = QtGui.QLineEdit()
						cylinder_point1_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						point1_x.setValidator(cylinder_point1_validator)
						point1_x.setFixedSize(35, 25)
						point1_y = QtGui.QLineEdit()
						point1_y.setValidator(cylinder_point1_validator)
						point1_y.setFixedSize(35, 25)
						point1_z = QtGui.QLineEdit()
						point1_z.setValidator(cylinder_point1_validator)
						point1_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							point1_x.setText(geometry_2_obj[y]['point1'][0])
							point1_y.setText(geometry_2_obj[y]['point1'][1])
							point1_z.setText(geometry_2_obj[y]['point1'][2])

						point1_hbox = QtGui.QHBoxLayout()
						point1_hbox.setContentsMargins(0, 0, 0, 0)
						point1_hbox.addWidget(point1_x_lbl)
						point1_hbox.addWidget(point1_x)
						point1_hbox.addWidget(point1_y_lbl)
						point1_hbox.addWidget(point1_y)
						point1_hbox.addWidget(point1_z_lbl)
						point1_hbox.addWidget(point1_z)
						
						cylinder_point1_cell_widget = QtGui.QWidget()
						cylinder_point1_cell_widget.setLayout(point1_hbox)

						#point2#
						point2_x_lbl = QtGui.QLabel('x:')
						point2_y_lbl = QtGui.QLabel('y:')
						point2_z_lbl = QtGui.QLabel('z:')

						point2_x = QtGui.QLineEdit()
						cylinder_point2_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						point2_x.setValidator(cylinder_point2_validator)
						point2_x.setFixedSize(35, 25)
						point2_y = QtGui.QLineEdit()
						point2_y.setValidator(cylinder_point2_validator)
						point2_y.setFixedSize(35, 25)
						point2_z = QtGui.QLineEdit()
						point2_z.setValidator(cylinder_point2_validator)
						point2_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							point2_x.setText(geometry_2_obj[y]['point2'][0])
							point2_y.setText(geometry_2_obj[y]['point2'][1])
							point2_z.setText(geometry_2_obj[y]['point2'][2])

						point2_hbox = QtGui.QHBoxLayout()
						point2_hbox.setContentsMargins(0, 0, 0, 0)
						point2_hbox.addWidget(point2_x_lbl)
						point2_hbox.addWidget(point2_x)
						point2_hbox.addWidget(point2_y_lbl)
						point2_hbox.addWidget(point2_y)
						point2_hbox.addWidget(point2_z_lbl)
						point2_hbox.addWidget(point2_z)
						
						cylinder_point2_cell_widget = QtGui.QWidget()
						cylinder_point2_cell_widget.setLayout(point2_hbox)
						#radius#
						cylinder_radius_edit = QtGui.QLineEdit()
						cylinder_radius_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						cylinder_radius_edit.setValidator(cylinder_radius_validator)
						cylinder_radius_edit.setContentsMargins(0, 0, 0, 0)
						cylinder_radius_edit.setFixedSize(80, 27)
						if geometry_2_obj != None:
							cylinder_radius_edit.setText(geometry_2_obj[y]['radius'])

						#add_to_table
						cylinder_table.setCellWidget(0,0, cylinder_edit)
						cylinder_table.setCellWidget(0,1, cylinder_type_edit)
						cylinder_table.setCellWidget(0,2, cylinder_point1_cell_widget)
						cylinder_table.setCellWidget(0,3, cylinder_point2_cell_widget)
						cylinder_table.setCellWidget(0,4, cylinder_radius_edit)
						
						all_geometry_list.append(cylinder_table)
						all_geometry_list_lbls.append('cylinder_table')
						all_complex_list_lbls.append('')
						all_tri_file_btn_list.append('')
						all_tri_file_edit_list.append('')
						
						geometry_numb = QtGui.QLabel()
						if int_lng == 'Russian':
							geometry_numb.setText("Геометрия_" + str(i) + " - цилиндр")
						elif int_lng == 'English':
							geometry_numb.setText("Geometry_" + str(i) + " - cylinder")

						main_grid.addWidget(geometry_numb, j, 0, alignment=QtCore.Qt.AlignCenter)
						main_grid.addWidget(cylinder_table, j+1, 0, alignment=QtCore.Qt.AlignCenter)

					#--------------------------Таблица параметров для фигуры plane------------------------------#
					
					if el['shape_type_' + str(i)] == 'плоскость' or el['shape_type_' + str(i)] == 'plane':
												
						plane_table = QtGui.QTableWidget()
						plane_table.setFixedSize(715, 60)
						plane_table.setRowCount(1)
						plane_table.setColumnCount(5)
						plane_table.verticalHeader().hide()

						plane_table.horizontalHeader().resizeSection(0, 120)
						plane_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
						column_1 = QtGui.QTableWidgetItem()
						plane_table.setHorizontalHeaderItem(0, column_1)
						plane_table.horizontalHeader().setStyleSheet("color: steelblue")

						plane_table.horizontalHeader().resizeSection(1, 120)
						plane_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
						column_2 = QtGui.QTableWidgetItem()
						plane_table.setHorizontalHeaderItem(1, column_2)
						plane_table.horizontalHeader().setStyleSheet("color: steelblue")

						plane_table.horizontalHeader().resizeSection(2, 135)
						plane_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
						column_3 = QtGui.QTableWidgetItem()
						plane_table.setHorizontalHeaderItem(2, column_3)
						plane_table.horizontalHeader().setStyleSheet("color: steelblue")

						plane_table.horizontalHeader().resizeSection(3, 170)
						plane_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
						column_4 = QtGui.QTableWidgetItem()
						plane_table.setHorizontalHeaderItem(3, column_4)
						plane_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						plane_table.horizontalHeader().resizeSection(4, 165)
						plane_table.horizontalHeader().setResizeMode(4, QtGui.QHeaderView.Fixed)
						column_5 = QtGui.QTableWidgetItem()
						plane_table.setHorizontalHeaderItem(4, column_5)
						plane_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						if int_lng == 'Russian':
							column_1.setText("Название")
							column_2.setText("Тип")
							column_3.setText("Тип фигуры plane")
							column_4.setText("Базовая точка")
							column_5.setText("Вектор нормали")
						elif int_lng == 'English':
							column_1.setText("shape")
							column_2.setText("type")
							column_3.setText("planeType")
							column_4.setText("basePoint")
							column_5.setText("normalVector")

						#Shape#
						plane_edit = QtGui.QLineEdit()
						plane_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
						plane_edit.setValidator(plane_validator)
						plane_edit.setContentsMargins(3, 3, 3, 0)
						plane_edit.setFixedSize(120, 27)
						if geometry_2_obj != None:
							plane_edit.setText(geometry_2_obj[y]['shape'])

						#type#
						plane_type_edit = QtGui.QComboBox()
						plane_type_edit_list = ["searchablePlane"]
						plane_type_edit.addItems(plane_type_edit_list)
						if geometry_2_obj != None:
							plane_type_edit_mas = plane_type_edit.count()  
							for t in range(plane_type_edit_mas):
								if plane_type_edit.itemText(t) == geometry_2_obj[y]['type']:
									plane_type_edit.setCurrentIndex(t)

						#planeType#
						planeType_edit = QtGui.QComboBox()
						planeType_edit_list = ["pointAndNormal"]
						planeType_edit.addItems(planeType_edit_list)
						if geometry_2_obj != None:
							planeType_edit_mas = planeType_edit.count()  
							for t in range(planeType_edit_mas):
								if planeType_edit.itemText(t) == geometry_2_obj[y]['planeType']:
									planeType_edit.setCurrentIndex(t)

						#basePoint#
						basePoint_x_lbl = QtGui.QLabel('x:')
						basePoint_y_lbl = QtGui.QLabel('y:')
						basePoint_z_lbl = QtGui.QLabel('z:')

						basePoint_x = QtGui.QLineEdit()
						plane_basePoint_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						basePoint_x.setValidator(plane_basePoint_validator)
						basePoint_x.setFixedSize(35, 25)
						basePoint_y = QtGui.QLineEdit()
						basePoint_y.setValidator(plane_basePoint_validator)
						basePoint_y.setFixedSize(35, 25)
						basePoint_z = QtGui.QLineEdit()
						basePoint_z.setValidator(plane_basePoint_validator)
						basePoint_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							basePoint_x.setText(geometry_2_obj[y]['basePoint'][0])
							basePoint_y.setText(geometry_2_obj[y]['basePoint'][1])
							basePoint_z.setText(geometry_2_obj[y]['basePoint'][2])

						basePoint_hbox = QtGui.QHBoxLayout()
						basePoint_hbox.setContentsMargins(0, 0, 0, 0)
						basePoint_hbox.addWidget(basePoint_x_lbl)
						basePoint_hbox.addWidget(basePoint_x)
						basePoint_hbox.addWidget(basePoint_y_lbl)
						basePoint_hbox.addWidget(basePoint_y)
						basePoint_hbox.addWidget(basePoint_z_lbl)
						basePoint_hbox.addWidget(basePoint_z)
						
						plane_basePoint_cell_widget = QtGui.QWidget()
						plane_basePoint_cell_widget.setLayout(basePoint_hbox)

						#normalVector#
						normalVector_x_lbl = QtGui.QLabel('x:')
						normalVector_y_lbl = QtGui.QLabel('y:')
						normalVector_z_lbl = QtGui.QLabel('z:')

						normalVector_x = QtGui.QLineEdit()
						plane_normalVector_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						normalVector_x.setValidator(plane_normalVector_validator)
						normalVector_x.setFixedSize(35, 25)
						normalVector_y = QtGui.QLineEdit()
						normalVector_y.setValidator(plane_normalVector_validator)
						normalVector_y.setFixedSize(35, 25)
						normalVector_z = QtGui.QLineEdit()
						normalVector_z.setValidator(plane_normalVector_validator)
						normalVector_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							normalVector_x.setText(geometry_2_obj[y]['normalVector'][0])
							normalVector_y.setText(geometry_2_obj[y]['normalVector'][1])
							normalVector_z.setText(geometry_2_obj[y]['normalVector'][2])

						normalVector_hbox = QtGui.QHBoxLayout()
						normalVector_hbox.setContentsMargins(0, 0, 0, 0)
						normalVector_hbox.addWidget(normalVector_x_lbl)
						normalVector_hbox.addWidget(normalVector_x)
						normalVector_hbox.addWidget(normalVector_y_lbl)
						normalVector_hbox.addWidget(normalVector_y)
						normalVector_hbox.addWidget(normalVector_z_lbl)
						normalVector_hbox.addWidget(normalVector_z)
						
						plane_normalVector_cell_widget = QtGui.QWidget()
						plane_normalVector_cell_widget.setLayout(normalVector_hbox)

						#add_to_table
						plane_table.setCellWidget(0,0, plane_edit)
						plane_table.setCellWidget(0,1, plane_type_edit)
						plane_table.setCellWidget(0,2, planeType_edit)
						plane_table.setCellWidget(0,3, plane_basePoint_cell_widget)
						plane_table.setCellWidget(0,4, plane_normalVector_cell_widget)
						
						all_geometry_list.append(plane_table)
						all_geometry_list_lbls.append('plane_table')
						all_complex_list_lbls.append('')
						all_tri_file_btn_list.append('')
						all_tri_file_edit_list.append('')
						
						geometry_numb = QtGui.QLabel()
						if int_lng == 'Russian':
							geometry_numb.setText("Геометрия_" + str(i) + " - плоскость")
						elif int_lng == 'English':
							geometry_numb.setText("Geometry_" + str(i) + " - plane")

						main_grid.addWidget(geometry_numb, j, 0, alignment=QtCore.Qt.AlignCenter)
						main_grid.addWidget(plane_table, j+1, 0, alignment=QtCore.Qt.AlignCenter)

					#--------------------------Таблица параметров для фигуры plate------------------------------#
					
					if el['shape_type_' + str(i)] == 'пластина' or el['shape_type_' + str(i)] == 'plate':
						
						plate_table = QtGui.QTableWidget()
						plate_table.setFixedSize(585, 60)
						plate_table.setRowCount(1)
						plate_table.setColumnCount(4)
						plate_table.verticalHeader().hide()

						plate_table.horizontalHeader().resizeSection(0, 120)
						plate_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
						column_1 = QtGui.QTableWidgetItem()
						plate_table.setHorizontalHeaderItem(0, column_1)
						plate_table.horizontalHeader().setStyleSheet("color: steelblue")

						plate_table.horizontalHeader().resizeSection(1, 120)
						plate_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
						column_2 = QtGui.QTableWidgetItem()
						plate_table.setHorizontalHeaderItem(1, column_2)
						plate_table.horizontalHeader().setStyleSheet("color: steelblue")

						plate_table.horizontalHeader().resizeSection(2, 170)
						plate_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
						column_3 = QtGui.QTableWidgetItem()
						plate_table.setHorizontalHeaderItem(2, column_3)
						plate_table.horizontalHeader().setStyleSheet("color: steelblue")

						plate_table.horizontalHeader().resizeSection(3, 170)
						plate_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
						column_4 = QtGui.QTableWidgetItem()
						plate_table.setHorizontalHeaderItem(3, column_4)
						plate_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						if int_lng == 'Russian':
							column_1.setText("Название")
							column_2.setText("Тип")
							column_3.setText("Происхождение")
							column_4.setText("Пролет")
						elif int_lng == 'English':
							column_1.setText("shape")
							column_2.setText("type")
							column_3.setText("origin")
							column_4.setText("span")
							
						#Shape#
						plate_edit = QtGui.QLineEdit()
						plate_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+'))
						plate_edit.setValidator(plate_validator)
						plate_edit.setContentsMargins(3, 3, 3, 0)
						plate_edit.setFixedSize(120, 27)
						if geometry_2_obj != None:
							plate_edit.setText(geometry_2_obj[y]['shape'])

						#type#
						plate_type_edit = QtGui.QComboBox()
						plate_type_edit_list = ["searchablePlate"]
						plate_type_edit.addItems(plate_type_edit_list)
						if geometry_2_obj != None:
							plate_type_edit_mas = plate_type_edit.count()  
							for t in range(plate_type_edit_mas):
								if plate_type_edit.itemText(t) == geometry_2_obj[y]['type']:
									plate_type_edit.setCurrentIndex(t)

						#origin#
						origin_x_lbl = QtGui.QLabel('x:')
						origin_y_lbl = QtGui.QLabel('y:')
						origin_z_lbl = QtGui.QLabel('z:')

						origin_x = QtGui.QLineEdit()
						plate_origin_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						origin_x.setValidator(plate_origin_validator)
						origin_x.setFixedSize(35, 25)
						origin_y = QtGui.QLineEdit()
						origin_y.setValidator(plate_origin_validator)
						origin_y.setFixedSize(35, 25)
						origin_z = QtGui.QLineEdit()
						origin_z.setValidator(plate_origin_validator)
						origin_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							origin_x.setText(geometry_2_obj[y]['origin'][0])
							origin_y.setText(geometry_2_obj[y]['origin'][1])
							origin_z.setText(geometry_2_obj[y]['origin'][2])

						origin_hbox = QtGui.QHBoxLayout()
						origin_hbox.setContentsMargins(0, 0, 0, 0)
						origin_hbox.addWidget(origin_x_lbl)
						origin_hbox.addWidget(origin_x)
						origin_hbox.addWidget(origin_y_lbl)
						origin_hbox.addWidget(origin_y)
						origin_hbox.addWidget(origin_z_lbl)
						origin_hbox.addWidget(origin_z)
						
						plate_normalVector_cell_widget = QtGui.QWidget()
						plate_normalVector_cell_widget.setLayout(origin_hbox)

						#span#
						span_x_lbl = QtGui.QLabel('x:')
						span_y_lbl = QtGui.QLabel('y:')
						span_z_lbl = QtGui.QLabel('z:')

						span_x = QtGui.QLineEdit()
						plate_span_validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
						span_x.setValidator(plate_span_validator)
						span_x.setFixedSize(35, 25)
						span_y = QtGui.QLineEdit()
						span_y.setValidator(plate_span_validator)
						span_y.setFixedSize(35, 25)
						span_z = QtGui.QLineEdit()
						span_z.setValidator(plate_span_validator)
						span_z.setFixedSize(35, 25)
						if geometry_2_obj != None:
							span_x.setText(geometry_2_obj[y]['span'][0])
							span_y.setText(geometry_2_obj[y]['span'][1])
							span_z.setText(geometry_2_obj[y]['span'][2])

						span_hbox = QtGui.QHBoxLayout()
						span_hbox.setContentsMargins(0, 0, 0, 0)
						span_hbox.addWidget(span_x_lbl)
						span_hbox.addWidget(span_x)
						span_hbox.addWidget(span_y_lbl)
						span_hbox.addWidget(span_y)
						span_hbox.addWidget(span_z_lbl)
						span_hbox.addWidget(span_z)
						
						plate_span_cell_widget = QtGui.QWidget()
						plate_span_cell_widget.setLayout(span_hbox)
						#add_to_table
						plate_table.setCellWidget(0,0, plate_edit)
						plate_table.setCellWidget(0,1, plate_type_edit)
						plate_table.setCellWidget(0,2, plate_normalVector_cell_widget)
						plate_table.setCellWidget(0,3, plate_span_cell_widget)
						
						all_geometry_list.append(plate_table)
						all_geometry_list_lbls.append('plate_table')
						all_complex_list_lbls.append('')
						all_tri_file_btn_list.append('')
						all_tri_file_edit_list.append('')
						
						geometry_numb = QtGui.QLabel()
						if int_lng == 'Russian':
							geometry_numb.setText("Геометрия_" + str(i) + " - пластина")
						elif int_lng == 'English':
							geometry_numb.setText("Geometry_" + str(i) + " - plate")

						main_grid.addWidget(geometry_numb, j, 0, alignment=QtCore.Qt.AlignCenter)
						main_grid.addWidget(plate_table, j+1, 0, alignment=QtCore.Qt.AlignCenter)
				i = i + 1
				j = j + 2
				y = y + 1

        	# -------------------------Кнопка сохранения --------------------------#

			geometry_2_btnSave = QtGui.QPushButton()
			geometry_2_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(geometry_2_btnSave)
			if int_lng == 'Russian':
				geometry_2_btnSave.setText("Записать")
			elif int_lng == 'English':
				geometry_2_btnSave.setText("Write")

        	# -----------------------Групповой элемент формы-----------------------#

			geometry_2_grid = QtGui.QGridLayout()
			geometry_2_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			geometry_2_grid.addWidget(main_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			geometry_2_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			geometry_2_grid.setRowStretch(3, 6)
			geometry_2_group = QtGui.QGroupBox()
			geometry_2_group.setLayout(geometry_2_grid)

			return geometry_2_group, geometry_2_btnSave, all_geometry_list, all_geometry_list_lbls, all_complex_list_lbls, all_tri_file_btn_list, all_tri_file_edit_list

