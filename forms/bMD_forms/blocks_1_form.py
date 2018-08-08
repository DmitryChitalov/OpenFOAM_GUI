# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class blocks_1_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, blocks_visible): 
		blocks_1_obj = None
		
		#----------------Если файл blocks_1.pkl существует, получаем данные из него для вывода в форму---------------#
		
		if blocks_visible == True:		
			blocks_1_path_file = prj_path + '/' + mesh_name_txt + '/' + 'blocks_1.pkl'
			if os.path.exists(blocks_1_path_file):
		
				input = open(blocks_1_path_file, 'rb')
				blocks_1_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла blocks_1.pkl на основе данных файла initial.pkl-------------#

		main_lbl = QtGui.QLabel()
		
		if int_lng == 'Russian':
			main_lbl.setText("Базовое описание блоков")		
		elif int_lng == 'English':
			main_lbl.setText("Basic block description")	
			
		initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
		
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()		
			
			prs_grid_main = QtGui.QGridLayout()
	
			main_str = QtGui.QVBoxLayout()
			j = 1
			k = 0
			vrs_edit_list = []
			
			mg_edit_list = []
			mg_lbl_list = []
			
			napr_lbl_list = []
			napr_edit_list = []
			ks_lbl_list = []
			ks_edit_list = []
			noeG_frame_list = []

			v_1_obsh_list = []
			v_2_obsh_list = []
			vrs_obj_list = []
			j_list = []

			while j <= obj['nob']:
			
				hex_lbl = QtGui.QLabel("hex")
				a_lbl = QtGui.QLabel("(")
				b_lbl = QtGui.QLabel(")")
				c_lbl = QtGui.QLabel("(")
				d_lbl = QtGui.QLabel(")")
				
				vrs_edit = QtGui.QComboBox()
				vrs_edit.setFixedSize(100, 25)
				vrs_list = ["simpleGrading", "edgeGrading"]
				vrs_edit.addItems(vrs_list)
				vrs_edit_list.append(vrs_edit)
				if blocks_1_obj != None:
					for bvc in range(vrs_edit.count()):
						if vrs_edit.itemText(bvc) == blocks_1_obj[k]['srya_' + str(j)]:
							vrs_edit.setCurrentIndex(bvc)
					
				mg_lbl = QtGui.QLabel()
				mg_lbl_list.append(mg_lbl)
				mg_edit = QtGui.QCheckBox()
				
				if blocks_1_obj != None :
					mg_edit.setChecked(blocks_1_obj[k]['mg_' + str(j)])
				mg_edit_list.append(mg_edit)
				
				if int_lng == 'Russian':
					vrs_edit.setToolTip("Тип описания градуировки")	
					mg_lbl.setText("Мультиградуировка")
					mg_edit.setToolTip("Установите флажок для указания опции мультиградуировки") 
				elif int_lng == 'English':
					vrs_edit.setToolTip("Type of grading")	
					mg_lbl.setText("Multigrading")
					mg_edit.setToolTip("Check the box to specify the multigrading option") 
				
				nov_str = QtGui.QHBoxLayout()
				nos_str = QtGui.QHBoxLayout()
				noeG_str = QtGui.QHBoxLayout()
				
				n = 1
				p = 0
				v_1_list = []
				while n <= 8:
					
					v_1_edit = QtGui.QLineEdit()
					if int_lng == 'Russian':
						v_1_edit.setToolTip("Метка вершины " + str(n) + " - неотрицательное число")
					elif int_lng == 'English':
						v_1_edit.setToolTip("Label of the vertex " + str(n) + " - nonnegative number")
						
					v_1_edit.setFixedSize(30, 21)
					if blocks_1_obj != None:
						v_1_edit.setText(blocks_1_obj[k]['versh_' + str(j)][p])
					validator = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+"))
					v_1_edit.setValidator(validator)
					nov_str.insertWidget(n, v_1_edit)
					v_1_list.append(v_1_edit)
					n = n + 1
					p = p + 1
					
				v_1_obsh_list.append(v_1_list)
					
				n = 1
				p = 0
				v_2_list = []
				while n <= 3:
					
					v_2_edit = QtGui.QLineEdit()
					if n == 1:
						if int_lng == 'Russian':
							v_2_edit.setToolTip("Число ячеек в направлении x1" + " - неотрицательное число")
						elif int_lng == 'English':
							v_2_edit.setToolTip("Number of cells in x1 direction" + " - nonnegative number")
					elif n == 2:
						if int_lng == 'Russian':
							v_2_edit.setToolTip("Число ячеек в направлении x2" + " - неотрицательное число")
						elif int_lng == 'English':
							v_2_edit.setToolTip("Number of cells in x2 direction" + " - nonnegative number")
					elif n == 3:
						if int_lng == 'Russian':
							v_2_edit.setToolTip("Число ячеек в направлении x3" + " - неотрицательное число")
						elif int_lng == 'English':
							v_2_edit.setToolTip("Number of cells in x3 direction" + " - nonnegative number")
					v_2_edit.setFixedSize(30, 21)
					if blocks_1_obj != None:
						v_2_edit.setText(blocks_1_obj[k]['yach_' + str(j)][p])
					v_2_edit.setValidator(validator)
					nos_str.insertWidget(n, v_2_edit)
					v_2_list.append(v_2_edit)
					n = n + 1
					p = p + 1
				
				v_2_obsh_list.append(v_2_list)
					
				napr_lbl = QtGui.QLabel()
				napr_lbl_list.append(napr_lbl)
				napr_edit = QtGui.QComboBox()
				if blocks_1_obj != None and blocks_1_obj[k]['mg_' + str(j)] == True:
					napr_edit_mas = napr_edit.count() 
					for bvc in range(napr_edit_mas):
						if napr_edit.itemText(bvc) == blocks_1_obj[k]['napr_' + str(j)]:
							napr_edit.setCurrentIndex(bvc)
					
				napr_edit.setFixedSize(50, 25)
				napr_list = ["x", "y", "z"]
				napr_edit.addItems(napr_list)
				napr_edit_list.append(napr_edit)
				
				ks_lbl = QtGui.QLabel()
				ks_lbl_list.append(ks_lbl)
				ks_edit = QtGui.QSpinBox()
				if blocks_1_obj != None and blocks_1_obj[k]['mg_' + str(j)] == True:
					ks_edit.setValue(blocks_1_obj[k]['ks_' + str(j)])
				ks_edit.setRange(1,10)
				ks_edit.setFixedSize(50, 25)
				ks_edit_list.append(ks_edit)	
					
				prs_grid = QtGui.QGridLayout()
				prs_grid.addWidget(hex_lbl, 0, 0)
				prs_grid.addWidget(a_lbl, 0, 1)
				prs_grid.addLayout(nov_str, 0, 2)
				prs_grid.addWidget(b_lbl, 0, 3)
				
				prs_grid.addWidget(c_lbl, 0, 4)
				prs_grid.addLayout(nos_str, 0, 5)
				prs_grid.addWidget(d_lbl, 0, 6)
				
				prs_grid.addWidget(vrs_edit, 0, 7)
				prs_grid.addWidget(mg_edit, 0, 8)
				prs_grid.addWidget(mg_lbl, 0, 9)
				
				noeG_str.insertWidget(0, napr_lbl)	
				noeG_str.insertWidget(1, napr_edit)	
				noeG_str.insertWidget(2, ks_lbl)	
				noeG_str.insertWidget(3, ks_edit)	
				
				main_str.addLayout(prs_grid)
				noeG_frame = QtGui.QFrame()
				noeG_frame.setFixedSize(370, 40)
				noeG_frame.setLayout(noeG_str)
				noeG_frame_list.append(noeG_frame)
				noeG_frame.setVisible(False)
				if blocks_1_obj != None and blocks_1_obj[k]['mg_' + str(j)] == True:
					noeG_frame.setVisible(True)
				main_str.addWidget(noeG_frame)
				noeG_str.setAlignment(QtCore.Qt.AlignCenter)
				
				if int_lng == 'Russian':
					napr_lbl.setText("Направление")
					napr_edit.setToolTip("Направление, в котором выполняется градуировка")
					ks_lbl.setText("Количество секторов")
					ks_edit.setToolTip("Количество секторов разбиения должно быть не менее одного")
				elif int_lng == 'English':
					napr_lbl.setText("Direction")
					napr_edit.setToolTip("The direction in which the grading is performed")
					ks_lbl.setText("Number of sectors")
					ks_edit.setToolTip("The number of sectors of the grading must be at least one")

				j = j + 1
				k = k + 1
				
				j_list.append(j)
		
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(main_str)
		
		

        # --------------------------------Кнопка сохранения-------------------------#

		blocks_1_btnSave = QtGui.QPushButton()
		blocks_1_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(blocks_1_btnSave)
		
		if int_lng == 'Russian':
			blocks_1_btnSave.setText("Записать")
		elif int_lng == 'English':
			blocks_1_btnSave.setText("Write")

        # -------------------------Групповой элемент формы--------------------------#

		blocks_1_grid = QtGui.QGridLayout()
		blocks_1_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		blocks_1_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		blocks_1_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		blocks_1_grid.setRowStretch(3, 6)
		blocks_1_group = QtGui.QGroupBox()
		blocks_1_group.setLayout(blocks_1_grid)
		
		return blocks_1_group, blocks_1_btnSave, obj, vrs_edit_list, mg_edit_list, mg_lbl_list, napr_lbl_list, napr_edit_list, ks_lbl_list, ks_edit_list, noeG_frame_list, j_list, v_1_obsh_list, v_2_obsh_list

	