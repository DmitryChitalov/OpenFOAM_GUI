# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------

from PyQt4 import QtCore, QtGui
import pickle
import os

class blocks_2_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, blocks_visible): 
		blocks_2_obj = None
		
		#----------------Если файл blocks_2.pkl существует, получаем данные из него для вывода в форму---------------#
		
		if blocks_visible == True:	
			blocks_2_path_file = prj_path + '/' + mesh_name_txt + '/' + 'blocks_2.pkl'
			if os.path.exists(blocks_2_path_file):
		
				input = open(blocks_2_path_file, 'rb')
				blocks_2_obj = pickle.load(input)
				input.close()
		
		main_lbl = QtGui.QLabel()
		
		if int_lng == 'Russian':
			main_lbl.setText("Дополнительное описание блоков")
		elif int_lng == 'English':
			main_lbl.setText("Additional block description")
			
		#---------------Формируем внешний вид формы для файла blocks_2.pkl на основе данных файла blocks_1.pkl-------------#
		
		blocks_1_path_file = prj_path + '/' + mesh_name_txt + '/' + 'blocks_1.pkl'
		if os.path.exists(blocks_1_path_file):
		
			input = open(blocks_1_path_file, 'rb')
			obj_list = pickle.load(input)
			input.close()
			
			srya_list = []
			mg_list = []
			napr_list = []
			ks_list = []
			
			blocks_2_grid = QtGui.QGridLayout()

			sg_eg_obsh_list = []
			
			grad_type = []
			
			i = 1
			h = 0
			nbl = 1
			
			q = 1
			for el in obj_list:
				
				srya_list.append(el['srya_' + str(q)])
				mg_list.append(el['mg_' + str(q)])
				napr_list.append(el['napr_' + str(q)])
				ks_list.append(el['ks_' + str(q)])
				
				blocks_lbl = QtGui.QLabel()
				blocks_2_grid.addWidget(blocks_lbl, i, 0, alignment=QtCore.Qt.AlignCenter)
				
				validator = QtGui.QRegExpValidator(QtCore.QRegExp("\\d*\\.\\d+"))
			
				el_srya_lbl = QtGui.QLabel(srya_list[h])
				
				if int_lng == 'Russian':
					blocks_lbl.setText("Мультиградуировка для блока " + str(nbl))
				elif int_lng == 'English':
					blocks_lbl.setText("Multigrading for the block " + str(nbl))
				###########################################################################
				if srya_list[h] == "simpleGrading" and mg_list[h] != True:
					
					n = 1
					p = 0
					sg_list = []
					nosg_str = QtGui.QHBoxLayout()
					while n <= 3:

						sg_edit = QtGui.QLineEdit()
						if n == 1:
							if int_lng == 'Russian':
								sg_edit.setToolTip("Степень расширения для направления x1 - неотрицательное число")
							elif int_lng == 'English':
								sg_edit.setToolTip("Degree of expansion for x1 direction - nonnegative number")
						elif n == 2:
							if int_lng == 'Russian':
								sg_edit.setToolTip("Степень расширения для направления x2 - неотрицательное число")
							elif int_lng == 'English':
								sg_edit.setToolTip("Degree of expansion for x2 direction - nonnegative number")
						elif n == 3:
							if int_lng == 'Russian':
								sg_edit.setToolTip("Степень расширения для направления x3 - неотрицательное число")
							elif int_lng == 'English':
								sg_edit.setToolTip("Degree of expansion for x3 direction - nonnegative number")
						if blocks_2_obj != None:
							sg_edit.setText(blocks_2_obj[h]['simpleGrading'][p])
						sg_edit.setFixedSize(30, 21)
						
						sg_edit.setValidator(validator)
						nosg_str.insertWidget(n, sg_edit)
						sg_list.append(sg_edit)
						n = n + 1
						p = p + 1

					sg_grid = QtGui.QGridLayout()
					sg_lbl = QtGui.QLabel(srya_list[h])
					sg_grid.addWidget(sg_lbl, 0, 0)
					sg_grid.addLayout(nosg_str, 0, 1)
					
					sg_frame = QtGui.QFrame()
					sg_frame.setLayout(sg_grid)
					
					grad_type.append("simpleGrading")
					sg_eg_obsh_list.append(sg_list)
					
				###########################################################################	
				if srya_list[h] == "simpleGrading" and mg_list[h] == True:
					if napr_list[h] == 'x':
						
						sg_mg_grid = QtGui.QGridLayout()
						sg_mg_lbl = QtGui.QLabel(srya_list[h])
						sg_mg_grid.addWidget(sg_mg_lbl, 0, 0)
						
						k = 0
						u = 1
						
						x_list = []
						sg_list_lvl = []
						while u <= ks_list[h]:
							l = 1
							x_str = QtGui.QHBoxLayout()
							sect_list = []
							p = 0
							while l <= 3:
								x_edit = QtGui.QLineEdit()
								if l == 1:
									if int_lng == 'Russian':
										x_edit.setToolTip("Доля сектора " + str(u) + " от длины блока для направления 'x' - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										x_edit.setToolTip("Share of the sector " + str(u) + " from the length of the block for the 'x' direction - in percent, fractions or absolute lengths")
								elif l == 2:
									if int_lng == 'Russian':
										x_edit.setToolTip("Доля ячеек в секторе " + str(u) + " - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										x_edit.setToolTip("The share of cells in the sector " + str(u) + " - in percent, fractions or absolute lengths")
								elif l == 3:
									if int_lng == 'Russian':
										x_edit.setToolTip("Расширение для сектора " + str(u) + " для направления 'x' - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										x_edit.setToolTip("Expansion for the sector " + str(u) + " for the 'x' direction - in percentages, fractions or absolute lengths")
								
								if blocks_2_obj != None:
									x_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][0]['x'][k]['sekt_' + str(u)][p])
								x_edit.setFixedSize(30, 21)
								x_edit.setValidator(validator)
								x_str.insertWidget(l, x_edit)
								sect_list.append(x_edit)
								l = l + 1
								p = p + 1
								
							x_list.append(sect_list)
							
							x_lbl = QtGui.QLabel()
							if int_lng == 'Russian':
								x_lbl.setText("// доля сектора в %, доля ячеек в %, расширение //" + " - сектор " + str(u) + " направления x")
							elif int_lng == 'English':
								x_lbl.setText("// sector share in %, percentage of cells in %, extension //" + " - sector " + str(u) + " direction x")
							
							
							sg_mg_grid.addLayout(x_str, k, 1)
							sg_mg_grid.addWidget(x_lbl, k, 2)
							
							k = k + 1
							u = u + 1
							
						y_edit = QtGui.QLineEdit()
						if blocks_2_obj != None:
							y_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][1]['y'])
						y_edit.setFixedSize(30, 21)
						y_edit.setValidator(validator)
						y_lbl = QtGui.QLabel()
						sg_mg_grid.addWidget(y_edit, k + 1, 1)
						sg_mg_grid.addWidget(y_lbl, k + 1, 2)
						
						
						z_edit = QtGui.QLineEdit()
						if blocks_2_obj != None:
							z_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][2]['z'])
						z_edit.setFixedSize(30, 21)
						z_edit.setValidator(validator)
						z_lbl = QtGui.QLabel()
						sg_mg_grid.addWidget(z_edit, k + 2, 1)
						sg_mg_grid.addWidget(z_lbl, k + 2, 2)
						
						
						if int_lng == 'Russian':
							y_edit.setToolTip("Степень расширения для направления 'y' - в процентах, долях или абсолютных длинах")
							y_lbl.setText("Cтепень расширения в направлении 'y'")
							z_edit.setToolTip("Степень расширения для направления 'z' - в процентах, долях или абсолютных длинах")
							z_lbl.setText("Cтепень расширения в направлении 'z'")
						elif int_lng == 'English':
							y_edit.setToolTip("The degree of expansion for the 'y' direction is in percentages, fractions or absolute lengths")
							y_lbl.setText("The degree of expansion in the 'y' direction")
							z_edit.setToolTip("The degree of expansion for the 'z' direction is in percentages, fractions or absolute lengths")
							z_lbl.setText("The degree of expansion in the 'z' direction")
						sg_list_lvl.append(x_list)
						sg_list_lvl.append(y_edit)
						sg_list_lvl.append(z_edit)
					#------------------------------------------	
					if napr_list[h] == 'y':
						sg_mg_grid = QtGui.QGridLayout()
						sg_mg_lbl = QtGui.QLabel(srya_list[h])
						sg_mg_grid.addWidget(sg_mg_lbl, 0, 0)
						
						x_edit = QtGui.QLineEdit()
						if blocks_2_obj != None:
							x_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][0]['x'])
						x_edit.setFixedSize(30, 21)
						x_edit.setValidator(validator)
						x_lbl = QtGui.QLabel()
						sg_mg_grid.addWidget(x_edit, 0, 1)
						sg_mg_grid.addWidget(x_lbl, 0, 2)
						
						k = 1
						u = 1
						o = 0
						
						y_list = []
						sg_list_lvl = []
						#print(ks_list[h])
						while u <= ks_list[h]:
							l = 1
							y_str = QtGui.QHBoxLayout()
							sect_list = []
							p = 0
							while l <= 3:
								y_edit = QtGui.QLineEdit()
								if l == 1:
									if int_lng == 'Russian':
										y_edit.setToolTip("Доля сектора " + str(u) + " от длины блока для направления 'y' - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										y_edit.setToolTip("Share of the sector " + str(u) + " from the length of the block for the 'y' direction - in percentages, fractions or absolute lengths")

								elif l == 2:
									if int_lng == 'Russian':
										y_edit.setToolTip("Доля ячеек в секторе " + str(u) + " - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										y_edit.setToolTip("The share of cells in the sector " + str(u) + " - in percentages, fractions or absolute lengths")

								elif l == 3:
									if int_lng == 'Russian':
										y_edit.setToolTip("Расширение для сектора " + str(u) + " для направления 'y' - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										y_edit.setToolTip("Expansion for the sector " + str(u) + " for the 'y' direction - in percentages, fractions or absolute lengths")

								if blocks_2_obj != None:
									y_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][1]['y'][o]['sekt_' + str(u)][p])
								y_edit.setFixedSize(30, 21)
								y_edit.setValidator(validator)
								y_str.insertWidget(l, y_edit)
								sect_list.append(y_edit)
								l = l + 1
								p = p + 1
								
							y_list.append(sect_list)
								
							y_lbl = QtGui.QLabel()
							if int_lng == 'Russian':
								y_lbl.setText("// доля сектора в %, доля ячеек в %, расширение //" + " - сектор " + str(u) + " направления 'y'")
							elif int_lng == 'English':
								y_lbl.setText("// sector share in %, percentage of cells in%, extension //" + " - sector " + str(u) + " 'y' direction")
							
							sg_mg_grid.addLayout(y_str, k, 1)
							sg_mg_grid.addWidget(y_lbl, k, 2)
							
							k = k + 1
							u = u + 1
							o = o + 1
						
						z_edit = QtGui.QLineEdit()
						if blocks_2_obj != None:
							z_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][2]['z'])
						z_edit.setFixedSize(30, 21)
						z_edit.setValidator(validator)
						z_lbl = QtGui.QLabel()
						sg_mg_grid.addWidget(z_edit, k + 1, 1)
						sg_mg_grid.addWidget(z_lbl, k + 1, 2)
						
						sg_list_lvl.append(x_edit)
						sg_list_lvl.append(y_list)
						sg_list_lvl.append(z_edit)
											  
						if int_lng == 'Russian':
							x_edit.setToolTip("Степень расширения для направления 'x' - в процентах, долях или абсолютных длинах")
							x_lbl.setText("Cтепень расширения в направлении 'x'")
							z_edit.setToolTip("Степень расширения для направления 'z' - в процентах, долях или абсолютных длинах")
							z_lbl.setText("Cтепень расширения в направлении 'z'")
						elif int_lng == 'English':
							x_edit.setToolTip("The degree of expansion for the 'x' direction is in percentages, fractions or absolute lengths")
							x_lbl.setText("The degree of expansion in the 'x' direction")
							z_edit.setToolTip("Degree of expansion for the 'z' direction - in percent, fractions or absolute lengths")
							z_lbl.setText("The degree of expansion in the 'z' direction")
					#--------------------------------------------
					if napr_list[h] == 'z':
						sg_mg_grid = QtGui.QGridLayout()
						sg_mg_lbl = QtGui.QLabel(srya_list[h])
						sg_mg_grid.addWidget(sg_mg_lbl, 0, 0)
						
						x_edit = QtGui.QLineEdit()
						if blocks_2_obj != None:
							x_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][0]['x'])
						x_edit.setFixedSize(30, 21)
						x_edit.setValidator(validator)
						x_lbl = QtGui.QLabel()
						sg_mg_grid.addWidget(x_edit, 0, 1)
						sg_mg_grid.addWidget(x_lbl, 0, 2)
						
						y_edit = QtGui.QLineEdit()
						if blocks_2_obj != None:
							y_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][1]['y'])
						y_edit.setFixedSize(30, 21)
						y_edit.setValidator(validator)
						y_lbl = QtGui.QLabel()
						sg_mg_grid.addWidget(y_edit, 1, 1)
						sg_mg_grid.addWidget(y_lbl, 1, 2)
						
						k = 2
						u = 1
	
						z_list = []
						sg_list_lvl = []
						while u <= ks_list[h]:
							l = 1
							z_str = QtGui.QHBoxLayout()
							sect_list = []
							p = 0
							while l <= 3:
								z_edit = QtGui.QLineEdit()
								if l == 1:
									if int_lng == 'Russian':
										z_edit.setToolTip("Доля сектора " + str(u) + " от длины блока для направления 'z' - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										z_edit.setToolTip("Share of the sector " + str(u) + " from the length of the block for the 'z' direction - in percentages, fractions or absolute lengths")	  
								elif l == 2:
									if int_lng == 'Russian':
										z_edit.setToolTip("Доля ячеек в секторе " + str(u) + " - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										z_edit.setToolTip("The share of cells in the sector " + str(u) + " - in percentages, fractions or absolute lengths")
								elif l == 3:
									if int_lng == 'Russian':
										z_edit.setToolTip("Расширение для сектора " + str(u) + " для направления 'z' - в процентах, долях или абсолютных длинах")
									elif int_lng == 'English':
										z_edit.setToolTip("Expansion for the sector " + str(u) + " for the 'z' direction - in percent, fractions or absolute lengths")
								if blocks_2_obj != None:
									z_edit.setText(blocks_2_obj[h]['simpleGrading_mg'][0]['mg_blocks_' + str(nbl)][2]['z'][k]['sekt_' + str(u)][p])
								z_edit.setFixedSize(30, 21)
								z_edit.setValidator(validator)
								z_str.insertWidget(l, z_edit)
								sect_list.append(z_edit)
								l = l + 1
								p = p + 1
								
							z_list.append(sect_list)
								
							z_lbl = QtGui.QLabel()
							if int_lng == 'Russian':
								z_lbl.setText("// доля сектора в %, доля ячеек в %, расширение //" + " - сектор " + str(u) + " направления 'z'")
							if int_lng == 'English':
								z_lbl.setText("// sector share in %, percentage of cells in %, extension //" + " - sector " + str(u) + " 'z' direction")
							
							sg_mg_grid.addLayout(z_str, k, 1)
							sg_mg_grid.addWidget(z_lbl, k, 2)
							
							k = k + 1
							u = u + 1
						
						sg_list_lvl.append(x_edit)
						sg_list_lvl.append(y_edit)
						sg_list_lvl.append(z_list)
						
						if int_lng == 'Russian':
							x_edit.setToolTip("Степень расширения для направления 'x' - в процентах, долях или абсолютных длинах")
							x_lbl.setText("Cтепень расширения в направлении 'x'")
							y_edit.setToolTip("Степень расширения для направления 'y' - в процентах, долях или абсолютных длинах")
							y_lbl.setText("Cтепень расширения в направлении 'y'")
						elif int_lng == 'English':
							x_edit.setToolTip("The degree of expansion for the 'x' direction is in percentages, fractions or absolute lengths")
							x_lbl.setText("The degree of expansion in the 'x' direction")				  
							y_edit.setToolTip("The degree of expansion for the 'y' direction is in percentages, fractions or absolute lengths")
							y_lbl.setText("The degree of expansion in the 'y' direction")				  
					sg_frame = QtGui.QFrame()
					sg_frame.setLayout(sg_mg_grid)
					
					grad_type.append("simpleGrading_mg")
					sg_eg_obsh_list.append(sg_list_lvl)
				###########################################################################	
				if srya_list[h] == "edgeGrading":
					
					n = 1
					p = 0
					eg_list = []
					noegr_str = QtGui.QHBoxLayout()
					while n <= 12:

						eg_edit = QtGui.QLineEdit()
						if int_lng == 'Russian':
							eg_edit.setToolTip("Степень расширения для ребра " + str(n) + " блока - неотрицательное число")
						elif int_lng == 'English':
							eg_edit.setToolTip("The degree of expansion for the edge " + str(n) + " block - nonnegative number")				  
						if blocks_2_obj != None:
							eg_edit.setText(blocks_2_obj[h]['edgeGrading'][p])
						eg_edit.setFixedSize(30, 21)
						eg_edit.setValidator(validator)
						noegr_str.insertWidget(n, eg_edit)
						eg_list.append(eg_edit)
						n = n + 1
						p = p + 1
					
					eg_grid = QtGui.QGridLayout()
					eg_lbl = QtGui.QLabel(srya_list[h])
					eg_grid.addWidget(eg_lbl, 0, 0)
					eg_grid.addLayout(noegr_str, 0, 1)
					
					sg_frame = QtGui.QFrame()
					sg_frame.setLayout(eg_grid)
					
					grad_type.append("edgeGrading")
					sg_eg_obsh_list.append(eg_list)
				
				blocks_2_grid.addWidget(sg_frame, i + 1, 0, alignment=QtCore.Qt.AlignCenter)
				
				i = i + 2
				h = h + 1
				nbl = nbl + 1
				q = q + 1
				
			# -----------------------Кнопка сохранения------------------------#	

			blocks_2_btnSave = QtGui.QPushButton("Записать")
			if int_lng == 'Russian':
				blocks_2_btnSave.setText("Записать")
			elif int_lng == 'English':
				blocks_2_btnSave.setText("Write")							  
			blocks_2_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(blocks_2_btnSave)

			blocks_2_grid.addLayout(buttons_hbox, i + 1, 0, alignment=QtCore.Qt.AlignCenter)
			blocks_2_grid.setRowStretch(i + 2, 6)
			
			# ---------------------Групповой элемент формы--------------------#
			
			blocks_2_group = QtGui.QGroupBox()
			blocks_2_group.setLayout(blocks_2_grid)

		return blocks_2_group, blocks_2_btnSave, obj_list, grad_type, sg_eg_obsh_list

	
	




