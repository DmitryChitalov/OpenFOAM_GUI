# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class mergepatchpairs_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, mergepatchpairs_visible): 
		mergepatchpairs_obj = None
		
		#----------------Если файл mergepatchpairs.pkl существует, получаем данные из него для вывода в форму---------------#
		
		if mergepatchpairs_visible == True:
		
			mergepatchpairs_path_file = prj_path + '/' + mesh_name_txt + '/' + 'mergepatchpairs.pkl'
			if os.path.exists(mergepatchpairs_path_file):
		
				input = open(mergepatchpairs_path_file, 'rb')
				mergepatchpairs_obj = pickle.load(input)
				input.close()
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Патчи для слияния")
		elif int_lng == 'English':
			main_lbl.setText("Patches to merge")
		
		#---------------Формируем внешний вид формы для файла mergepatchpairs.pkl на основе данных файла mergepatchpairs.pkl -------------#
		
		patches_1_path_file = prj_path + '/' + mesh_name_txt + '/' + 'patches_1.pkl'
		if os.path.exists(patches_1_path_file):
		
			input = open(patches_1_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			
			k = 1
			p_name_list = []
			for el_m in obj:
				p_name = el_m['patch_' + str(k)]
				p_name_list.append(p_name)
				k = k + 1
				
		initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
		
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()
			
			if obj['mpp'] == True:
				prs_grid = QtGui.QGridLayout()
			
				i = 0
				k = 1
				master_patch_list = []
				slave_patch_list = []
				while k <= obj['nompp']:
					master_patch_lbl = QtGui.QLabel()
					slave_lbl = QtGui.QLabel()
					mpp_lbl = QtGui.QLabel()
					
					master_patch_name = QtGui.QComboBox()
					master_patch_name.setFixedSize(150, 25)
					master_patch_name.addItems(p_name_list)
					master_patch_list.append(master_patch_name)
					
					if mergepatchpairs_obj != None:
						master_patch_name_mas = master_patch_name.count() 
						for bvc in range(master_patch_name_mas):
							if master_patch_name.itemText(bvc) == mergepatchpairs_obj[i]['master_' + str(k)]:
								master_patch_name.setCurrentIndex(bvc)
						
					slave_patch_name = QtGui.QComboBox()
					slave_patch_name.setFixedSize(150, 25)
					slave_patch_name.addItems(p_name_list)
					slave_patch_list.append(slave_patch_name)
					
					if mergepatchpairs_obj != None:
						slave_patch_name_mas = slave_patch_name.count() 
						for bvc in range(slave_patch_name_mas):
							if slave_patch_name.itemText(bvc) == mergepatchpairs_obj[i]['slave_' + str(k)]:
								slave_patch_name.setCurrentIndex(bvc)
					
					prs_grid.addWidget(master_patch_lbl, i, 0)
					prs_grid.addWidget(master_patch_name, i, 1)
					prs_grid.addWidget(slave_lbl, i, 2)
					prs_grid.addWidget(slave_patch_name, i, 3)
					prs_grid.addWidget(mpp_lbl, i, 4)
					
					if int_lng == 'Russian':
						master_patch_lbl.setText("Ведущий патч:")
						slave_lbl.setText("Ведомый патч:")
						mpp_lbl.setText("// слияние " + str(k))
						master_patch_name.setToolTip("Название ведущего патча")
						slave_patch_name.setToolTip("Название ведомого патча")
					elif int_lng == 'English':
						master_patch_lbl.setText("Lead patch:")	
						slave_lbl.setText("Slave patch:")
						mpp_lbl.setText("// merging " + str(k))
						master_patch_name.setToolTip("Name of the master patch")
						slave_patch_name.setToolTip("Name of the slave patch")
						
					i = i + 1
					k = k + 1
				
				prs_frame = QtGui.QFrame()
				prs_frame.setLayout(prs_grid)
				
			# --------------------Кнопка сохранения--------------------------#

			mergepatchpairs_btnSave = QtGui.QPushButton()
			mergepatchpairs_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(mergepatchpairs_btnSave)
			if int_lng == 'Russian':
				mergepatchpairs_btnSave.setText("Записать")
			elif int_lng == 'English':
				mergepatchpairs_btnSave.setText("Write")
			
			# -------------------Групповой элемент формы---------------------#

			mergepatchpairs_grid = QtGui.QGridLayout()
			mergepatchpairs_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			mergepatchpairs_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			mergepatchpairs_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			mergepatchpairs_grid.setRowStretch(3, 6)
			mergepatchpairs_group = QtGui.QGroupBox()
			mergepatchpairs_group.setLayout(mergepatchpairs_grid)
				
			return mergepatchpairs_group, mergepatchpairs_btnSave, master_patch_list, slave_patch_list


