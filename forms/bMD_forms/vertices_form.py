# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class vertices_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, vertices_visible): 
		vertices_obj = None
		
		#----------------Если файл vertices.pkl существует, получаем данные из него для вывода в форму---------------#

		if vertices_visible == True:
			vertices_path_file = prj_path + '/' + mesh_name_txt + '/' + 'vertices.pkl'
			if os.path.exists(vertices_path_file):
		
				input = open(vertices_path_file, 'rb')
				vertices_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла vertices.pkl на основе данных файла initial.pkl-------------#
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Список координат вершин")
		elif int_lng == 'English':
			main_lbl.setText("List of coordinates of vertices")
			
		initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
		
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
					
			prs_grid = QtGui.QGridLayout()
			i = 1
			k = 0
			
			i_list = []
			vert_list_main = []
			while i <= obj['nov']:
				nov_str = QtGui.QHBoxLayout()
				n = 1
				p = 0
				vert_list = []
				while n <= 3:
										
					v_edit = QtGui.QLineEdit()
					if n == 1:
						if int_lng == 'Russian':
							v_edit.setToolTip("Укажите координату x1 вершины номер " + str(k)) 
						elif int_lng == 'English':
							v_edit.setToolTip("Specify the x1 coordinate of the vertex number " + str(k)) 
					elif n == 2:
						if int_lng == 'Russian':
							v_edit.setToolTip("Укажите координату x2 вершины номер " + str(k)) 
						elif int_lng == 'English':
							v_edit.setToolTip("Specify the x2 coordinate of the vertex number " + str(k)) 
					elif n == 3:
						if int_lng == 'Russian':
							v_edit.setToolTip("Укажите координату x3 вершины номер " + str(k)) 
						elif int_lng == 'English':
							v_edit.setToolTip("Specify the x3 coordinate of the vertex number " + str(k)) 
					v_edit.setFixedSize(35, 21)
					if vertices_obj != None:
						v_edit.setText(vertices_obj[k]['vertex_' + str(k)][p])
					validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
					v_edit.setValidator(validator)
					vert_list.append(v_edit)

					nov_str.insertWidget(n, v_edit)
				
					n = n + 1
					p = p + 1
				
				i_list.append(i)
				vert_list_main.append(vert_list)
			
				a_lbl = QtGui.QLabel("(")
				d_lbl = QtGui.QLabel(")")
			
				vert_lbl = QtGui.QLabel()
				
				if int_lng == 'Russian':
					vert_lbl.setText("// вершина номер " + str(k))
				elif int_lng == 'English':
					vert_lbl.setText("// vertex number " + str(k))
			
				prs_grid.addWidget(a_lbl, i, 0)
				prs_grid.addLayout(nov_str, i, 1)
				prs_grid.addWidget(d_lbl, i, 2)
				prs_grid.addWidget(vert_lbl, i, 3)
				
				i = i + 1
				k = k + 1
		
			prs_frame = QtGui.QFrame()
			prs_frame.setLayout(prs_grid)

        	# -------------------------Кнопка сохранения --------------------------#

			vertices_btnSave = QtGui.QPushButton()
			vertices_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(vertices_btnSave)
			if int_lng == 'Russian':
				vertices_btnSave.setText("Записать")
			elif int_lng == 'English':
				vertices_btnSave.setText("Write")

        	# -----------------------Групповой элемент формы-----------------------#

			vertices_grid = QtGui.QGridLayout()
			vertices_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			vertices_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			vertices_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			vertices_grid.setRowStretch(3, 6)
			vertices_group = QtGui.QGroupBox()
			vertices_group.setLayout(vertices_grid)

			return vertices_group, vertices_btnSave, obj, vert_list, i_list, vert_list_main

