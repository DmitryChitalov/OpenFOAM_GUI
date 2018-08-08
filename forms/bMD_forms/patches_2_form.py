# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------

from PyQt4 import QtCore, QtGui
import pickle
import os

class patches_2_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, patches_visible): 
		patches_2_obj = None
		
		#----------------Если файл patches_2.pkl существует, получаем данные из него для вывода в форму---------------#
		
		if patches_visible == True:
			patches_2_path_file = prj_path + '/' + mesh_name_txt + '/' + 'patches_2.pkl'
			if os.path.exists(patches_2_path_file):
		
				input = open(patches_2_path_file, 'rb')
				patches_2_obj = pickle.load(input)
				input.close()
					
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Список граней для патчей")
		elif int_lng == 'English':
			main_lbl.setText("List of faces for patches")
		
		#-------------Формируем внешний вид формы для файла patches_2.pkl на основе данных файла patches_1.pkl----------#
		
		patches_1_path_file = prj_path + '/' + mesh_name_txt + '/' + 'patches_1.pkl'
		if os.path.exists(patches_1_path_file):
		
			input = open(patches_1_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			
			k = 1
			i = 0
			
			p_list = []
			fe_main_list = []

			f_vbox = QtGui.QVBoxLayout()
			for el_m in obj:

				p_name = el_m['patch_' + str(k)]
				p_list.append(p_name)
				t_name = el_m['type_' + str(k)]
				f_name = el_m['faces_' + str(k)]		
					
				if el_m['type_' + str(k)] == 'cyclic':
					n_name = el_m['neighb_' + str(k)]
					patch_lbl = QtGui.QLabel("Патч: " + p_name + ", " + "Тип: " + t_name + ", " + "Сосед: " + n_name)
				else:		
					patch_lbl = QtGui.QLabel("Патч: " + p_name + ", " + "Тип: " + t_name)
						
				g = 1
				b = 0
				
				f_grid = QtGui.QGridLayout()
				f_frame = QtGui.QFrame()
				prs_grid = QtGui.QGridLayout()

				fe_pred_main = []
				while g <= f_name:					
					t = 1

					validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+"))

					f_hbox = QtGui.QHBoxLayout()
					
					fe_list = []
					p = 0
					while t <= 4:
						
						face_edit = QtGui.QLineEdit()
						if t == 1:
							if int_lng == 'Russian':
								face_edit.setToolTip("Метка 1 грани блока, входящей в патч")
							elif int_lng == 'English':
								face_edit.setToolTip("Label 1 of the edge of the block included in the patch")
						elif t == 2:
							if int_lng == 'Russian':
								face_edit.setToolTip("Метка 2 грани блока, входящей в патч")
							elif int_lng == 'English':
								face_edit.setToolTip("Label 2 of the edge of the block included in the patch")
						elif t == 3:
							if int_lng == 'Russian':
								face_edit.setToolTip("Метка 3 грани блока, входящей в патч")
							elif int_lng == 'English':
								face_edit.setToolTip("Label 3 of the edge of the block included in the patch")
						elif t == 4:
							if int_lng == 'Russian':
								face_edit.setToolTip("Метка 4 грани блока, входящей в патч")
							elif int_lng == 'English':
								face_edit.setToolTip("Label 4 of the edge of the block included in the patch")
						if patches_2_obj != None:
							face_edit.setText(patches_2_obj[i][p_name][b][p])
						face_edit.setFixedSize(30, 21)
						face_edit.setValidator(validator)
						f_hbox.addWidget(face_edit)
						fe_list.append(face_edit)
						t = t + 1
						p = p + 1
						
					if f_name == 1 and g == 1:				
						f_grid.addLayout(f_hbox, b, 0)
						fe_main_list.append(fe_list)
					else:
						f_grid.addLayout(f_hbox, b, 0)
						fe_pred_main.append(fe_list)
				
					g = g + 1
					b = b + 1
				if fe_pred_main != []:	
					fe_main_list.append(fe_pred_main)
						
				prs_grid.addLayout(f_grid, 0, 0)
				prs_grid.addWidget(patch_lbl, 0, 1)
				f_frame.setLayout(prs_grid)
				f_vbox.addWidget(f_frame)
					
				k = k + 1
				i = i + 1
			
			prs_frame = QtGui.QFrame()
			prs_frame.setLayout(f_vbox)
				
			# -----------------------Кнопка сохранения------------------------#

			patches_2_btnSave = QtGui.QPushButton()
			patches_2_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(patches_2_btnSave)
			if int_lng == 'Russian':
				patches_2_btnSave.setText("Записать")
			elif int_lng == 'English':
				patches_2_btnSave.setText("Write")
			
			# ---------------------Групповой элемент формы--------------------#

			patches_2_grid = QtGui.QGridLayout()
			patches_2_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			patches_2_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			patches_2_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			patches_2_grid.setRowStretch(3, 6)
			patches_2_group = QtGui.QGroupBox()
			patches_2_group.setLayout(patches_2_grid)
				
			return patches_2_group, patches_2_btnSave, p_list, fe_main_list
		
			
