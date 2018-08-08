# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------

from PyQt4 import QtCore, QtGui
import pickle
import os

class patches_1_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, patches_visible): 
		patches_1_obj = None
		
		#----------------Если файл patches_1.pkl существует, получаем данные из него для вывода в форму---------------#
		
		if patches_visible == True:
			patches_1_path_file = prj_path + '/' + mesh_name_txt + '/' + 'patches_1.pkl'
			if os.path.exists(patches_1_path_file):
		
				input = open(patches_1_path_file, 'rb')
				patches_1_obj = pickle.load(input)
				input.close()
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Список патчей")
		elif int_lng == 'English':
			main_lbl.setText("List of patches")
		
		#-------------Формируем внешний вид формы для файла patches_1.pkl на основе данных файла initial.pkl----------#

		initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
		
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			
			i = 0
			n = 1
			
			prs_vbox = QtGui.QVBoxLayout()
			pne_list = []
			pte_list = []
			cnl_list = []
			cne_list = []
			fne_list = []
			patch_def_list = []
			while n <= obj['nop']:
				patch_def = QtGui.QLabel()
				patch_def.setStyleSheet("color: darkBlue;")
				patch_def_list.append(patch_def)
				
				p_lbl = QtGui.QLabel()
				
				regexp = QtCore.QRegExp('[a-zA-Z]+')
				validator = QtGui.QRegExpValidator(regexp)
				
				patch_name_lbl = QtGui.QLabel()
				patch_name_edit = QtGui.QLineEdit()
				if patches_1_obj != None :
					patch_name_edit.setText(patches_1_obj[i]['patch_' + str(n)])
				patch_name_edit.setFixedSize(110, 21)
				patch_name_edit.setValidator(validator)
				pne_list.append(patch_name_edit)
				
				patch_type_lbl = QtGui.QLabel("Тип: ")
				patch_type_edit = QtGui.QComboBox()
				if patches_1_obj != None:
					patch_type_edit_mas = patch_type_edit.count() 
					for bvc in range(patch_type_edit_mas):
						if patch_type_edit.itemText(bvc) == patches_1_obj[i]['type_' + str(n)]:
							patch_type_edit.setCurrentIndex(bvc)
				patch_type_edit.setFixedSize(120, 21)
				patch_list = ["patch", "symmetryPlane", "empty", "wedge", "cyclic", "wall", "processor"]
				patch_type_edit.addItems(patch_list)
				pte_list.append(patch_type_edit)

				cycl_name_lbl = QtGui.QLabel()
				cycl_name_lbl.setVisible(False)
				cycl_name_edit = QtGui.QLineEdit()
				if patches_1_obj != None and patches_1_obj[i]['type_' + str(n)] == "cyclic":
					cycl_name_edit.setVisible(True)
					cycl_name_edit.setText(patches_1_obj[i]['neighb_' + str(n)])
				cycl_name_edit.setFixedSize(90, 21)
				cycl_name_edit.setVisible(False)
				cycl_name_edit.setValidator(validator)
				cnl_list.append(cycl_name_lbl)
				cne_list.append(cycl_name_edit)
				
				faces_numb_lbl = QtGui.QLabel()
				faces_numb_edit = QtGui.QSpinBox()
				if patches_1_obj != None :
					faces_numb_edit.setValue(patches_1_obj[i]['faces_' + str(n)])
				faces_numb_edit.setRange(1,100)
				faces_numb_edit.setFixedSize(50, 22)
				fne_list.append(faces_numb_edit)
				
				prs_grid = QtGui.QGridLayout()
				prs_grid.addWidget(patch_name_lbl, i, 0)
				prs_grid.addWidget(patch_name_edit, i, 1)
				prs_grid.addWidget(patch_type_lbl, i, 2)
				prs_grid.addWidget(patch_type_edit, i, 3)
				prs_grid.addWidget(cycl_name_lbl, i, 4)
				prs_grid.addWidget(cycl_name_edit, i, 5)
				prs_grid.addWidget(faces_numb_lbl, i, 6)
				prs_grid.addWidget(faces_numb_edit, i, 7)
				prs_grid.addWidget(p_lbl, i, 8)
				
				prs_vbox.addWidget(patch_def, alignment=QtCore.Qt.AlignCenter)
				prs_vbox.addLayout(prs_grid)
				
				if int_lng == 'Russian':
					patch_def.setText("Универсальный патч")
					p_lbl.setText("// " + "Патч_" + str(n))
					
					patch_name_lbl.setText("Название: ")
					patch_name_edit.setToolTip("Имя патча " + str(n) + ", формирующего границу сетки")
					patch_type_edit.setToolTip("Тип патча " + str(n) + ", формирующего границу сетки")
					
					cycl_name_lbl.setText("Сосед: ")
					cycl_name_edit.setToolTip("Имя циклического патча")
					
					faces_numb_lbl.setText("Количество граней: ")
					faces_numb_edit.setToolTip("Количество граней блока, составляющих патч")
					
				elif int_lng == 'English':
					patch_def.setText("Universal patch")
					p_lbl.setText("// " + "Patch_" + str(n))
					
					patch_name_lbl.setText("Name: ")
					patch_name_edit.setToolTip("Patch name " + str(n) + ", forming the mesh boundary")
					patch_type_edit.setToolTip("Patch type " + str(n) + ", forming the mesh boundary")
					
					cycl_name_lbl.setText("Neighbour: ")
					cycl_name_edit.setToolTip("Name of the cyclic patch")
					
					faces_numb_lbl.setText("Number of faces: ")
					faces_numb_edit.setToolTip("Number of block edges making up the patch")
					
				i = i + 1
				n = n + 1
				
			prs_frame = QtGui.QFrame()
			prs_frame.setLayout(prs_vbox)
				
			# -----------------------Кнопка сохранения------------------------#

			patches_1_btnSave = QtGui.QPushButton()
			patches_1_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(patches_1_btnSave)
			if int_lng == 'Russian':
				patches_1_btnSave.setText("Записать")
			elif int_lng == 'English':
				patches_1_btnSave.setText("Write")
				
			# ---------------------Групповой элемент формы--------------------#

			patches_1_grid = QtGui.QGridLayout()
			patches_1_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			patches_1_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			patches_1_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			patches_1_grid.setRowStretch(3, 6)
			patches_1_group = QtGui.QGroupBox()
			patches_1_group.setLayout(patches_1_grid)
		
			return patches_1_group, patches_1_btnSave, pne_list, pte_list, cnl_list, cne_list, fne_list, patch_def_list
