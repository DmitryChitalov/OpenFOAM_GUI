# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class edges_1_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, edges_visible): 
		edges_1_obj = None
		
		#----------------Если файл edges_1.pkl существует, получаем данные из него для вывода в форму---------------#

		if edges_visible == True:	
			edges_1_path_file = prj_path + '/' + mesh_name_txt + '/' + 'edges_1.pkl'
			if os.path.exists(edges_1_path_file):
		
				input = open(edges_1_path_file, 'rb')
				edges_1_obj = pickle.load(input)
				input.close()

				edges_1_keys = []
				for el_m in edges_1_obj:
					for key in el_m.keys():
						edges_1_keys.append(key)
		
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Список записей для изогнутых ребер")
		elif int_lng == 'English':
			main_lbl.setText("List of entries for curved edges")
			
		#-------------Формируем внешний вид формы для файла edges_1.pkl на основе данных файла initial.pkl----------#

		initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
		
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()

			if obj['spe'] == True:
				prs_grid = QtGui.QGridLayout()
				i = 1
				k = 0
				edge_1_list = []
				dots_quant_list = []
				dots_quant_lbl_list = []
				while i <= obj['nospe']:
					edge_type_lbl = QtGui.QLabel()
					edge_type_name = QtGui.QComboBox()
					edge_type_name.setFixedSize(150, 25)
					if int_lng == 'Russian':
						edge_type_list = ["Дуга окружности", "Сплайновая кривая", "Набор линий", "B-сплайновая кривая"]
					elif int_lng == 'English':
						edge_type_list = ["Arc of a circle", "Spline curve", "Set of lines", "B-spline curve"]
					edge_type_name.addItems(edge_type_list)
					if edges_1_obj != None:
						for bvc in range(edge_type_name.count()):
							if edge_type_name.itemText(bvc) == edges_1_keys[k]:
								edge_type_name.setCurrentIndex(bvc)
					
					dots_quant_lbl = QtGui.QLabel()
					dots_quant_lbl.setVisible(False)
					dots_quant = QtGui.QSpinBox()
					dots_quant.setRange(2, 1000)
					dots_quant.setFixedSize(50, 25)
					dots_quant.setVisible(False)
					if edges_1_obj != None and edges_1_obj[k][edges_1_keys[k]] != None:
						dots_quant.setValue(edges_1_obj[k][edges_1_keys[k]])
						dots_quant_lbl.setVisible(True)
						dots_quant.setVisible(True)
						
					edge_1_list.append(edge_type_name)
					dots_quant_list.append(dots_quant)
					dots_quant_lbl_list.append(dots_quant_lbl)

					prs_grid.addWidget(edge_type_name, i, 0)
					prs_grid.addWidget(edge_type_lbl, i, 1)
					prs_grid.addWidget(dots_quant, i, 2)
					prs_grid.addWidget(dots_quant_lbl, i, 3)

					if int_lng == 'Russian':
						edge_type_lbl.setText("Тип кривой для ребра " + str(i))
						edge_type_name.setToolTip("Тип изогнутого ребра")
						dots_quant_lbl.setText("Количество точек интерполяции")
						dots_quant.setToolTip("Количество точек должно быть не менее двух")
					elif int_lng == 'English':
						edge_type_lbl.setText("Type of curve for the edge " + str(i))
						edge_type_name.setToolTip("Type of curved edge")
						dots_quant_lbl.setText("Number of interpolation points")
						dots_quant.setToolTip("The number of points must be at least two")
					i = i + 1
					k = k + 1

				prs_frame = QtGui.QFrame()
				prs_frame.setLayout(prs_grid)

				# -----------------------Кнопка сохранения------------------------#

				edges_1_btnSave = QtGui.QPushButton()
				if int_lng == 'Russian':
					edges_1_btnSave.setText("Записать")
				elif int_lng == 'English':	
					edges_1_btnSave.setText("Write")
				edges_1_btnSave.setFixedSize(80, 25)
				buttons_hbox = QtGui.QHBoxLayout()
				buttons_hbox.addWidget(edges_1_btnSave)

				# ---------------------Групповой элемент формы--------------------#

				edges_1_grid = QtGui.QGridLayout()
				edges_1_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
				edges_1_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
				edges_1_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
				edges_1_grid.setRowStretch(3, 6)
				edges_1_group = QtGui.QGroupBox()
				edges_1_group.setLayout(edges_1_grid)

				return edges_1_group, edges_1_btnSave, obj, edge_1_list, dots_quant_list, dots_quant_lbl_list

