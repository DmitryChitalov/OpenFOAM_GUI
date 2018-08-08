# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class initial_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt): 
		obj = None
		
		#----------------Если файл initial.pkl существует, получаем данные из него для вывода в форму---------------#

		initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()

			vertices_visible = True
			blocks_visible = True
			
			if obj['spe'] == True:
				edges_visible = True
			else:
				edges_visible = False
				
			if obj['spp'] == True:
				patches_visible = True
			else:
				patches_visible = False
				
			if obj['mpp'] == True:
				mergepatchpairs_visible = True
			else:
				mergepatchpairs_visible = False	
		else:
			vertices_visible = False
			blocks_visible = False
			edges_visible = False
			patches_visible = False
			mergepatchpairs_visible = False	
			
		#-----------------------Формируем внешний вид формы для файла initial.pkl----------------------#	

		main_lbl = QtGui.QLabel()

		cTM_lbl = QtGui.QLabel()
		cTM_edit = QtGui.QDoubleSpinBox()
		cTM_edit.setFixedSize(100, 22)
		if obj != None:
			cTM_edit.setValue(obj['cTM'])
			
		nov_lbl = QtGui.QLabel()
		nov_edit = QtGui.QSpinBox()
		nov_edit.setFixedSize(100, 22)
		nov_edit.setRange(1, 1000)
		if obj != None:
			nov_edit.setValue(obj['nov'])
		
		nob_lbl = QtGui.QLabel()
		nob_edit = QtGui.QSpinBox() 
		nob_edit.setFixedSize(100, 22)
		nob_edit.setRange(1, 1000)
		if obj != None:
			nob_edit.setValue(obj['nob'])
		
		spe_lbl = QtGui.QLabel()
		spe_edit = QtGui.QCheckBox()
		if obj != None:
			if obj['spe'] == True:
				spe_edit.setChecked(True)
			elif obj['spe'] == False:
				spe_edit.setChecked(False)
						
		nospe_lbl = QtGui.QLabel()
		nospe_lbl.setEnabled(False)
		nospe_edit = QtGui.QSpinBox() 
		nospe_edit.setFixedSize(100, 22)
		nospe_edit.setRange(1,100)
		nospe_edit.setEnabled(False)
		if obj != None:
			if spe_edit.isChecked() == True:
				nospe_edit.setEnabled(True)
				nospe_edit.setValue(obj['nospe'])
				nospe_lbl.setEnabled(True)
				
		spp_lbl = QtGui.QLabel()
		spp_edit = QtGui.QCheckBox()
		if obj != None:
			if obj['spp'] == True:
				spp_edit.setChecked(True)
			elif obj['spp'] == False:
				spp_edit.setChecked(False)		

		nop_lbl = QtGui.QLabel()
		nop_lbl.setEnabled(False)
		nop_edit = QtGui.QSpinBox()
		nop_edit.setFixedSize(100, 22)
		nop_edit.setRange(1, 1000)
		nop_edit.setEnabled(False)
		if obj != None:
			if spp_edit.isChecked() == True:
				nop_edit.setEnabled(True)
				nop_edit.setValue(obj['nop'])
				nop_lbl.setEnabled(True)	
								
		mpp_lbl = QtGui.QLabel()
		mpp_lbl.setEnabled(False)
		mpp_edit = QtGui.QCheckBox()
		mpp_edit.setEnabled(False)
		if obj != None:
			if obj['mpp'] == True:
				mpp_lbl.setEnabled(True)
				mpp_edit.setEnabled(True)
				mpp_edit.setChecked(True)
				
		nompp_lbl = QtGui.QLabel()
		nompp_lbl.setEnabled(False)
		nompp_edit = QtGui.QSpinBox()
		nompp_edit.setFixedSize(100, 22)
		nompp_edit.setRange(1, 1000)
		nompp_edit.setEnabled(False)
		if obj != None:
			if mpp_edit.isChecked() == True:
				nompp_edit.setEnabled(True)
				nompp_edit.setValue(obj['nompp'])
				nompp_lbl.setEnabled(True)			
					
		prs_grid = QtGui.QGridLayout()
		prs_grid.addWidget(cTM_lbl, 0, 0)
		prs_grid.addWidget(cTM_edit, 0, 1)
		
		prs_grid.addWidget(nov_lbl, 1, 0)
		prs_grid.addWidget(nov_edit, 1, 1)
		
		prs_grid.addWidget(nob_lbl, 2, 0)
		prs_grid.addWidget(nob_edit, 2, 1)
		
		prs_grid.addWidget(spe_lbl, 3, 0)
		prs_grid.addWidget(spe_edit, 3, 1)
		prs_grid.addWidget(nospe_lbl, 3, 2)
		prs_grid.addWidget(nospe_edit, 3, 3)
		
		prs_grid.addWidget(spp_lbl, 4, 0)
		prs_grid.addWidget(spp_edit, 4, 1)
		prs_grid.addWidget(nop_lbl, 4, 2)
		prs_grid.addWidget(nop_edit, 4, 3)
		
		prs_grid.addWidget(mpp_lbl, 5, 0)
		prs_grid.addWidget(mpp_edit, 5, 1)
		prs_grid.addWidget(nompp_lbl, 5, 2)
		prs_grid.addWidget(nompp_edit, 5, 3)
				
		prs_frame = QtGui.QFrame()
		prs_frame.setFixedSize(500, 150)
		prs_frame.setLayout(prs_grid)

        # -----------------------------Кнопка сохранения--------------------------#

		initial_btnSave = QtGui.QPushButton()
		initial_btnSave.setFixedSize(80, 25)

		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(initial_btnSave)
		
		# --------------------Определяем параметры интерфейса окна---------#
		
		if int_lng == 'Russian':
			main_lbl.setText("Начальные данные")
			
			cTM_lbl.setText("Масштабный коэффициент:")
			cTM_edit.setToolTip("Введите положительное, отрицательное целое или дробное число")
			
			nov_lbl.setText("Количество вершин:")
			nov_edit.setToolTip("Количество вершин должно быть не меньше одной")
			
			nob_lbl.setText("Количество блоков:")
			nob_edit.setToolTip("Количество блоков должно быть не менее одного")
			
			spe_lbl.setText("Изогнутые ребра:")
			spe_edit.setToolTip("Установите флажок при наличии изогнутых ребер") 
			nospe_lbl.setText("Количество:")
			nospe_edit.setToolTip("Количество изогнутых ребер должно быть не менее одного")
			
			spp_lbl.setText("Патчи:")
			spp_edit.setToolTip("Установите флажок при наличии патчей") 
			nop_lbl.setText("Количество:")
			nop_edit.setToolTip("Количество патчей должно быть не менее одного") 
			
			mpp_lbl.setText("Слияние граней:")
			mpp_edit.setToolTip("Установите флажок при слиянии патчей блоков") 
			nompp_lbl.setText("Количество:")
			nompp_edit.setToolTip("Количество слияний должно быть не менее одного") 
			
			initial_btnSave.setText("Записать")
			
		elif int_lng == 'English':
			main_lbl.setText("Initial data")
			
			cTM_lbl.setText("Scale factor:")
			cTM_edit.setToolTip("Enter a positive, negative integer or a fractional number")
			
			nov_lbl.setText("Number of vertices:")
			nov_edit.setToolTip("The number of vertices must be at least one")
			
			nob_lbl.setText("Number of blocks:")
			nob_edit.setToolTip("The number of blocks must be at least one")
			
			spe_lbl.setText("Curved edges:")
			spe_edit.setToolTip("Check the box if you have curved edges") 
			nospe_lbl.setText("Number:")
			nospe_edit.setToolTip("The number of curved edges must be at least one")
			
			spp_lbl.setText("Patches:")
			spp_edit.setToolTip("Check the box if you have patches") 
			nop_lbl.setText("Number:")
			nop_edit.setToolTip("The number of patches must be at least one") 
			
			mpp_lbl.setText("Merging faces:")
			mpp_edit.setToolTip("Check the box when merging patch blocks") 
			nompp_lbl.setText("Number:")
			nompp_edit.setToolTip("The number of mergers must be at least one") 
			
			initial_btnSave.setText("Write")
			
			
        # -------------------------Групповой элемент формы---------------------------#

		initial_grid = QtGui.QGridLayout()
		initial_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		initial_grid.setRowStretch(3, 6)

		initial_group = QtGui.QGroupBox()
		initial_group.setLayout(initial_grid)
			
		return initial_group, spe_edit, nospe_lbl, nospe_edit, initial_btnSave, cTM_edit, nov_edit, spp_edit, nop_lbl, nop_edit, nob_edit, mpp_lbl, mpp_edit, nompp_lbl, nompp_edit, vertices_visible, blocks_visible, edges_visible, patches_visible, mergepatchpairs_visible 
	
