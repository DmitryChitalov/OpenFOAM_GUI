# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class geometry_1_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, geometry_visible): 
		geometry_1_obj = None
		
		#----------------Если файл geometry_1.pkl существует, получаем данные из него для вывода в форму---------------#

		if geometry_visible == True:
			geometry_1_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_1.pkl'
			if os.path.exists(geometry_1_path_file):
		
				input = open(geometry_1_path_file, 'rb')
				geometry_1_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла geometry_1.pkl на основе данных файла initial.pkl-------------#
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Список используемых геометрий")
		elif int_lng == 'English':
			main_lbl.setText("List of used geometries")
			
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'

		if os.path.exists(initial_path_file):
	
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			
			prs_grid = QtGui.QGridLayout()
			geometry_type_list = []
			shape_complex_lbl_list = []
			shape_complex_numb_list = []
			base_shape_lbl_list = []
			base_shape_type_list = []
			regions_lbl_list = []
			regions_numb_list = []
			
			i = 1
			k = 0
			while i <= obj['g']:
				
				#Надпись 'Тип геометрии'#
				geometry_type_lbl = QtGui.QLabel()
				if int_lng == 'Russian':
					geometry_type_lbl.setText("Тип геометрии:")
				elif int_lng == 'English':
					geometry_type_lbl.setText("Type of geometry:")
					
				#Тип геометрии#
				geometry_type = QtGui.QComboBox()
				geometry_type.setFixedSize(220, 25)		
				if int_lng == 'Russian':
					geometry_type_l = ["Три-поверхность", "Распределенная три-поверхность", "Базовая фигура", "Набор базовых фигур"]
				elif int_lng == 'English':
					geometry_type_l = ["Tri-surface", "Distributed tri-surface", "Base shape", "Base shape complex"]
				geometry_type.addItems(geometry_type_l)
				
				if geometry_1_obj != None:
					geometry_type_mas = geometry_type.count()  
					for t in range(geometry_type_mas):
						if geometry_type.itemText(t) == geometry_1_obj[k]['geometry_' + str(i)]:
							geometry_type.setCurrentIndex(t)
				
				#Надпись 'Количество подобластей'#
				regions_lbl = QtGui.QLabel()
				if int_lng == 'Russian':
					regions_lbl.setText("Количество подобластей:")
				elif int_lng == 'English':
					regions_lbl.setText("Number of regions:")
				
				#Количество подобластей#
				regions_numb = QtGui.QSpinBox()
				regions_numb.setFixedSize(50, 25)
				if geometry_1_obj != None:
					if geometry_1_obj[k]['geometry_' + str(i)] == "Три-поверхность" or geometry_1_obj[k]['geometry_' + str(i)] == "Tri-surface" or geometry_1_obj[k]['geometry_' + str(i)] == "Распределенная три-поверхность" or geometry_1_obj[k]['geometry_' + str(i)] == "Distributed tri-surface":
						regions_numb.setValue(geometry_1_obj[k]['regions_number_' + str(i)])
						regions_lbl.setVisible(True)
						regions_lbl.setVisible(True)
				regions_numb.setRange(0, 1000)
				
				#Надпись 'Количество фигур'#
				shape_complex_lbl = QtGui.QLabel()
				if int_lng == 'Russian':
					shape_complex_lbl.setText("Количество фигур:")
				elif int_lng == 'English':
					shape_complex_lbl.setText("Number of shapes:")
				shape_complex_lbl.setVisible(False)
				
				#Количество фигур
				shape_complex_numb = QtGui.QSpinBox()
				shape_complex_numb.setRange(2, 1000)
				shape_complex_numb.setFixedSize(50, 25)
				shape_complex_numb.setVisible(False)
				if geometry_1_obj != None:
					if geometry_1_obj[k]['geometry_' + str(i)] == "Набор базовых фигур" or geometry_1_obj[k]['geometry_' + str(i)] == "Base shape complex":
						shape_complex_numb.setValue(geometry_1_obj[k]['shapes_number_' + str(i)])
						shape_complex_lbl.setVisible(True)
						shape_complex_numb.setVisible(True)
				
				#Надпись 'Тип фигуры'#
				base_shape_lbl = QtGui.QLabel()
				if int_lng == 'Russian':
					base_shape_lbl.setText("Тип фигуры:")
				elif int_lng == 'English':
					base_shape_lbl.setText("Shape type:")
				base_shape_lbl.setVisible(False)
					
				#Тип фигуры#
				base_shape_type = QtGui.QComboBox()
				base_shape_type.setFixedSize(120, 25)
				base_shape_type.setVisible(False)
				if int_lng == 'Russian':
					base_shape_list = ["шестигранник", "цилиндр", "сфера", "плоскость", "пластина"]
				elif int_lng == 'English':
					base_shape_list = ["box", "cylinder", "sphere", "plane", "plate"]
				base_shape_type.addItems(base_shape_list)
				
				if geometry_1_obj != None:
					if geometry_1_obj[k]['geometry_' + str(i)] == "Базовая фигура" or geometry_1_obj[k]['geometry_' + str(i)] == "Base shape":
						base_shape_mas = base_shape_type.count()   
						for t in range(base_shape_mas):
							if base_shape_type.itemText(t) == geometry_1_obj[k]['shape_type_' + str(i)]:
								base_shape_type.setCurrentIndex(t)
								base_shape_type.setVisible(True)
								base_shape_lbl.setVisible(True)
				
				#Геометрия#
				geom_lbl = QtGui.QLabel()
				if int_lng == 'Russian':
					geom_lbl.setText("// геометрия " + str(i))
				elif int_lng == 'English':
					geom_lbl.setText("// geometry " + str(i))
				
				prs_grid.addWidget(geometry_type_lbl, k, 0)
				prs_grid.addWidget(geometry_type, k, 1)
				prs_grid.addWidget(regions_lbl, k, 2)
				prs_grid.addWidget(regions_numb, k, 3)
				prs_grid.addWidget(geom_lbl, k, 4)
				
				prs_grid.addWidget(shape_complex_lbl, k, 2)
				prs_grid.addWidget(shape_complex_numb, k, 3)
				prs_grid.addWidget(base_shape_lbl, k, 2)
				prs_grid.addWidget(base_shape_type, k, 3)
				
				geometry_type_list.append(geometry_type)
				shape_complex_lbl_list.append(shape_complex_lbl)
				shape_complex_numb_list.append(shape_complex_numb)
				base_shape_lbl_list.append(base_shape_lbl)
				base_shape_type_list.append(base_shape_type)
				regions_lbl_list.append(regions_lbl)
				regions_numb_list.append(regions_numb)
				
				i = i + 1
				k = k + 1
			
			prs_frame = QtGui.QFrame()
			prs_frame.setLayout(prs_grid)

			# -------------------------Кнопка сохранения --------------------------#

			geometry_1_btnSave = QtGui.QPushButton()
			geometry_1_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(geometry_1_btnSave)
			if int_lng == 'Russian':
				geometry_1_btnSave.setText("Записать")
			elif int_lng == 'English':
				geometry_1_btnSave.setText("Write")

			# -----------------------Групповой элемент формы-----------------------#

			geometry_1_grid = QtGui.QGridLayout()
			geometry_1_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			geometry_1_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			geometry_1_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			geometry_1_grid.setRowStretch(3, 6)
			geometry_1_group = QtGui.QGroupBox()
			geometry_1_group.setLayout(geometry_1_grid)

			return geometry_1_group, geometry_1_btnSave, geometry_type_list, shape_complex_lbl_list, shape_complex_numb_list, base_shape_lbl_list, base_shape_type_list, regions_lbl_list, regions_numb_list

	

