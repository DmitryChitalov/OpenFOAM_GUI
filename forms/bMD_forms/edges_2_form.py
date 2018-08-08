# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class edges_2_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, edges_visible): 
		edges_2_obj = None
		
		#----------------Если файл edges_2.pkl существует, получаем данные из него для вывода в форму---------------#
		
		if edges_visible == True:
		
			edges_2_path_file = prj_path + '/' + mesh_name_txt + '/' + 'edges_2.pkl'
			if os.path.exists(edges_2_path_file):
		
				input = open(edges_2_path_file, 'rb')
				edges_2_obj = pickle.load(input)
				input.close()
				
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Координаты точек для изогнутых ребер")
		elif int_lng == 'English':
			main_lbl.setText("Coordinates of points for curved edges")
		
		#---------------Формируем внешний вид формы для файла edges_2.pkl на основе данных файла edges_1.pkl-------------#
		
		edges_1_path_file = prj_path + '/' + mesh_name_txt + '/' + 'edges_1.pkl'
		if os.path.exists(edges_1_path_file):
		
			input = open(edges_1_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			
			prs_grid = QtGui.QGridLayout()
			i = 0
			r = 1
			nod_main_list = []
			nod_lbl_list = []
			nod_metk_list = []
			for el_m in obj:
				for key in el_m.keys():
					vkr_lbl = QtGui.QLabel()
					tkr_lbl = QtGui.QLabel()
					edg_lbl = QtGui.QLabel()
					if int_lng == 'Russian':
						vkr_lbl.setText("Метки вершин:")
						tkr_lbl.setText("Координаты точек:")
						edg_lbl.setText("// ребро " + str(r) + ", тип - " + key)
					elif int_lng == 'English':
						vkr_lbl.setText("Vertices labels:")
						tkr_lbl.setText("Coordinates of points:")
						edg_lbl.setText("// edge " + str(r) + ", type - " + key)
					
					prs_grid.addWidget(vkr_lbl, i, 0)
						
					k = 1
					p = 0
					vkr_hbox = QtGui.QHBoxLayout()
					vkr_list = []
					while k <= 2:
						
						vkr_edit = QtGui.QLineEdit()
						if int_lng == 'Russian':
							vkr_edit.setToolTip("Метка вершины " + str(k) + " ребра")
						elif int_lng == 'English':
							vkr_edit.setToolTip("Label of the vertex " + str(k) + " edge")
						if edges_2_obj != None:
							vkr_edit.setText(edges_2_obj[i]['metk_' + str(r)][p])
						vkr_edit.setFixedSize(30, 21)
						validator = QtGui.QRegExpValidator(QtCore.QRegExp("\\d*\\.\\d+"))
						vkr_edit.setValidator(validator)
						vkr_hbox.addWidget(vkr_edit)
						vkr_list.append(vkr_edit)
						k = k + 1	
						p = p + 1
					nod_metk_list.append(vkr_list)					   
					prs_grid.addLayout(vkr_hbox, i, 1)
					prs_grid.addWidget(tkr_lbl, i, 2)
					prs_grid.addWidget(edg_lbl, i, 4)
				   
					if key == 'Дуга окружности' or key == 'Arc of a circle':
										   											   													   
						g = 1
						p = 0
						tkr_hbox = QtGui.QHBoxLayout()
						tkr_list = []
						while g <= 3:
						
							tkr_edit = QtGui.QLineEdit()
							if g == 1:
								if int_lng == 'Russian':
									tkr_edit.setToolTip("Координата 'x' точки ребра " + str(r))
								elif int_lng == 'English':
									tkr_edit.setToolTip("The 'x' coordinate of the point of the edge " + str(r))
							elif g == 2:
								if int_lng == 'Russian':
									tkr_edit.setToolTip("Координата 'y' точки ребра " + str(r))
								elif int_lng == 'English':
									tkr_edit.setToolTip("The 'y' coordinate of the point of the edge" + str(r))
							elif g == 3:
								if int_lng == 'Russian':
									tkr_edit.setToolTip("Координата 'z' точки ребра " + str(r))
								elif int_lng == 'English':
									tkr_edit.setToolTip("The 'z' coordinate of the point of the edge " + str(r))
							if edges_2_obj != None:
								tkr_edit.setText(edges_2_obj[i]['values_' + str(r)][p])
							tkr_edit.setFixedSize(30, 21)
							tkr_edit.setValidator(validator)
							tkr_hbox.addWidget(tkr_edit)
							tkr_list.append(tkr_edit)
							g = g + 1
							p = p + 1
						
						prs_grid.addLayout(tkr_hbox, i, 3)
						nod_main_list.append(tkr_list)
					
					elif key == 'Сплайновая кривая' or key == 'Набор линий' or key == 'B-сплайновая кривая' or key == 'Spline curve' or key == 'Set of lines' or key == 'B-spline curve':
						
						nod = el_m[key]
						g = 1
						l = 0
						p = 0
						sk_grid = QtGui.QGridLayout() 
						nod_list = []
						while g <= nod:
							h = 1
							p = 0
							dk_hbox = QtGui.QHBoxLayout()
							dl_list = []
							while h <= 3:
								dk_edit = QtGui.QLineEdit()
								if h == 1:
									if int_lng == 'Russian':
										dk_edit.setToolTip("Координата 'x' точки " + str(g) + " ребра " + str(r))
									elif int_lng == 'English':
										dk_edit.setToolTip("The 'x' coordinate of the point " + str(g) + " edge " + str(r))
								elif h == 2:
									if int_lng == 'Russian':
										dk_edit.setToolTip("Координата 'y' точки " + str(g) + " ребра " + str(r))
									elif int_lng == 'English':
										dk_edit.setToolTip("The 'y' coordinate of the point " + str(g) + " edge " + str(r))
								elif h == 3:
									if int_lng == 'Russian':
										dk_edit.setToolTip("Координата 'z' точки " + str(g) + " ребра " + str(r))
									elif int_lng == 'English':
										dk_edit.setToolTip("The 'z' coordinate of the point " + str(g) + " ребра " + str(r))
								if edges_2_obj != None:
									dk_edit.setText(edges_2_obj[i]['values_' + str(r)][l][p])

								dk_edit.setFixedSize(30, 21)
								dk_edit.setValidator(validator)
								dk_hbox.addWidget(dk_edit)
								dl_list.append(dk_edit)
								h = h + 1
								p = p + 1
							nod_list.append(dl_list)
							sk_grid.addLayout(dk_hbox, l, 0)
							g = g + 1
							l = l + 1
							p = p + 1
						prs_grid.addLayout(sk_grid, i, 3)	
						
						nod_main_list.append(nod_list)
					nod_lbl_list.append(key)
										   
					i = i + 1
					r = r + 1
				
			prs_frame = QtGui.QFrame()
			prs_frame.setLayout(prs_grid)
				
			# --------------------Кнопка сохранения--------------------------#

			edges_2_btnSave = QtGui.QPushButton()
			edges_2_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(edges_2_btnSave)
			if int_lng == 'Russian':
				edges_2_btnSave.setText("Записать")
			elif int_lng == 'English':
				edges_2_btnSave.setText("Write")
			
			# -------------------Групповой элемент формы---------------------#

			edges_2_grid = QtGui.QGridLayout()
			edges_2_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			edges_2_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			edges_2_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			edges_2_grid.setRowStretch(3, 6)
			edges_2_group = QtGui.QGroupBox()
			edges_2_group.setLayout(edges_2_grid)
				
			return edges_2_group, edges_2_btnSave, nod_lbl_list, nod_main_list, nod_metk_list


