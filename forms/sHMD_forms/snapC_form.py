# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class snapC_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, snapC_visible): 
		snapC_obj = None
		
		#----------------Если файл snapC.pkl существует, получаем данные из него для вывода в форму---------------#

		if snapC_visible == True:
			snapC_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'snapC.pkl'
			if os.path.exists(snapC_path_file):
		
				input = open(snapC_path_file, 'rb')
				snapC_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла snapC.pkl на основе данных файла initial.pkl-------------#
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Настройки для привязки")
		elif int_lng == 'English':
			main_lbl.setText("Settings for the snapping")
			
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'

		if os.path.exists(initial_path_file):
			
			prs_grid = QtGui.QGridLayout()

			snapC_prs_table = QtGui.QTableWidget()
			snapC_prs_table.setFixedSize(695, 270)
			snapC_prs_table.setRowCount(8)
			snapC_prs_table.setColumnCount(4)
			snapC_prs_table.verticalHeader().hide()

			snapC_prs_table.horizontalHeader().resizeSection(0, 50)
			snapC_prs_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
			column_1 = QtGui.QTableWidgetItem()
			snapC_prs_table.setHorizontalHeaderItem(0, column_1)
			snapC_prs_table.horizontalHeader().setStyleSheet("color: steelblue")

			snapC_prs_table.horizontalHeader().resizeSection(1, 150)
			snapC_prs_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
			column_2 = QtGui.QTableWidgetItem()
			snapC_prs_table.setHorizontalHeaderItem(1, column_2)
			snapC_prs_table.horizontalHeader().setStyleSheet("color: steelblue")

			snapC_prs_table.horizontalHeader().resizeSection(2, 380)
			snapC_prs_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
			column_3 = QtGui.QTableWidgetItem()
			snapC_prs_table.setHorizontalHeaderItem(2, column_3)
			snapC_prs_table.horizontalHeader().setStyleSheet("color: steelblue")

			snapC_prs_table.horizontalHeader().resizeSection(3, 110)
			snapC_prs_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
			column_4 = QtGui.QTableWidgetItem()
			snapC_prs_table.setHorizontalHeaderItem(3, column_4)
			snapC_prs_table.horizontalHeader().setStyleSheet("color: steelblue")

			if int_lng == 'Russian':
				column_1.setText("Флаг")
				column_2.setText("Параметр")
				column_3.setText("Описание")	
				column_4.setText("Значение")
			elif int_lng == 'English':
				column_1.setText("Flag")
				column_2.setText("Parameter")
				column_3.setText("Definition")	
				column_4.setText("Value")
				
			snapC_chcks_list = []
			snapC_prs_list = []
			snapC_def_list = []
			snapC_val_list = []
			
			#1)nSmoothPatch
			nSP_val_pr = QtGui.QLabel()
			nSP_val_pr.setText('nSmoothPatch')
			snapC_prs_table.setCellWidget(0, 1, nSP_val_pr)
			nSP_val_def = QtGui.QLabel()
			snapC_prs_table.setCellWidget(0, 2, nSP_val_def)
			nSP_val = QtGui.QSpinBox()
			nSP_val.setFixedSize(70, 25)
			nSP_val.setRange(1, 1000000)
			nSP_val_hbox = QtGui.QHBoxLayout()
			nSP_val_hbox.setContentsMargins(0, 0, 0, 0)
			nSP_val_hbox.addWidget(nSP_val)
			nSP_val_cell_widget = QtGui.QWidget()
			nSP_val_cell_widget.setLayout(nSP_val_hbox)
			snapC_prs_table.setCellWidget(0, 3, nSP_val_cell_widget)
			if int_lng == 'Russian':
				nSP_val_def.setText("Количество итераций сглаживания патчей")
				nSP_val.setToolTip("Введите целое число") 
			elif int_lng == 'English':
				nSP_val_def.setText("Number of patch smoothing iterations")
				nSP_val.setToolTip("Enter the integer number") 
			if snapC_obj != None:
				nSP_val.setValue(snapC_obj['nSmoothPatch'])
	
			#2)tolerance
			t_val_pr = QtGui.QLabel()
			t_val_pr.setText('tolerance')
			snapC_prs_table.setCellWidget(1, 1, t_val_pr)
			t_val_def = QtGui.QLabel()
			snapC_prs_table.setCellWidget(1, 2, t_val_def)
			t_val = QtGui.QDoubleSpinBox()
			t_val.setFixedSize(70, 25)
			t_val.setRange(1, 1000000)
			t_val_hbox = QtGui.QHBoxLayout()
			t_val_hbox.setContentsMargins(0, 0, 0, 0)
			t_val_hbox.addWidget(t_val)
			t_val_cell_widget = QtGui.QWidget()
			t_val_cell_widget.setLayout(t_val_hbox)
			snapC_prs_table.setCellWidget(1, 3, t_val_cell_widget)
			if int_lng == 'Russian':
				t_val_def.setText("Относительное расстояние для точек")
				t_val.setToolTip("Введите число двойной точности") 
			elif int_lng == 'English':
				t_val_def.setText("Relative distance for points")
				t_val.setToolTip("Enter the double-precision number") 
			if snapC_obj != None:
				t_val.setValue(snapC_obj['tolerance'])

			#3)nSolveIter
			nSI_val_pr = QtGui.QLabel()
			nSI_val_pr.setText('nSolveIter')
			snapC_prs_table.setCellWidget(2, 1, nSI_val_pr)
			nSI_val_def = QtGui.QLabel()
			snapC_prs_table.setCellWidget(2, 2, nSI_val_def)
			nSI_val = QtGui.QSpinBox()
			nSI_val.setFixedSize(70, 25)
			nSI_val.setRange(1, 1000000)
			nSI_val_hbox = QtGui.QHBoxLayout()
			nSI_val_hbox.setContentsMargins(0, 0, 0, 0)
			nSI_val_hbox.addWidget(nSI_val)
			nSI_val_cell_widget = QtGui.QWidget()
			nSI_val_cell_widget.setLayout(nSI_val_hbox)
			snapC_prs_table.setCellWidget(2, 3, nSI_val_cell_widget)
			if int_lng == 'Russian':
				nSI_val_def.setText("Количество итераций релаксации смещения сетки")
				nSI_val.setToolTip("Введите целое число") 
			elif int_lng == 'English':
				nSI_val_def.setText("Number of mesh displacement relaxation iterations")
				nSI_val.setToolTip("Enter the integer number") 
			if snapC_obj != None:
				nSI_val.setValue(snapC_obj['nSolveIter'])

			#4)nRelaxIter
			nRI_val_pr = QtGui.QLabel()
			nRI_val_pr.setText('nRelaxIter')
			snapC_prs_table.setCellWidget(3, 1, nRI_val_pr)
			nRI_val_def = QtGui.QLabel()
			snapC_prs_table.setCellWidget(3, 2, nRI_val_def)
			nRI_val = QtGui.QSpinBox()
			nRI_val.setFixedSize(70, 25)
			nRI_val.setRange(1, 1000000)
			nRI_val_hbox = QtGui.QHBoxLayout()
			nRI_val_hbox.setContentsMargins(0, 0, 0, 0)
			nRI_val_hbox.addWidget(nRI_val)
			nRI_val_cell_widget = QtGui.QWidget()
			nRI_val_cell_widget.setLayout(nRI_val_hbox)
			snapC_prs_table.setCellWidget(3, 3, nRI_val_cell_widget)
			if int_lng == 'Russian':
				nRI_val_def.setText("Макc. количество релаксационных итераций привязки")
				nRI_val.setToolTip("Введите целое число") 
			elif int_lng == 'English':
				nRI_val_def.setText("Maximum number of snapping relaxation iterations")
				nRI_val.setToolTip("Enter the integer number") 
			if snapC_obj != None:
				nRI_val.setValue(snapC_obj['nRelaxIter'])

			#5)nFeatureSnapIter
			nFSI_chck = QtGui.QCheckBox()
			nFSI_chck_hbox = QtGui.QHBoxLayout()
			nFSI_chck_hbox.setContentsMargins(0, 0, 0, 0)
			nFSI_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			nFSI_chck_hbox.addWidget(nFSI_chck)
			nFSI_chck_cell_widget = QtGui.QWidget()
			nFSI_chck_cell_widget.setLayout(nFSI_chck_hbox)
			snapC_prs_table.setCellWidget(4, 0, nFSI_chck_cell_widget)
			nFSI_val_pr = QtGui.QLabel()
			nFSI_val_pr.setEnabled(False)
			nFSI_val_pr.setText('nFeatureSnapIter')
			snapC_prs_table.setCellWidget(4, 1, nFSI_val_pr)
			nFSI_val_def = QtGui.QLabel()
			nFSI_val_def.setEnabled(False)
			snapC_prs_table.setCellWidget(4, 2, nFSI_val_def)
			nFSI_val = QtGui.QSpinBox()
			nFSI_val.setFixedSize(70, 25)
			nFSI_val.setRange(1, 1000000)
			nFSI_val_hbox = QtGui.QHBoxLayout()
			nFSI_val_hbox.setContentsMargins(0, 0, 0, 0)
			nFSI_val_hbox.addWidget(nFSI_val)
			nFSI_val_cell_widget = QtGui.QWidget()
			nFSI_val_cell_widget.setLayout(nFSI_val_hbox)
			nFSI_val.setEnabled(False)
			snapC_prs_table.setCellWidget(4, 3, nFSI_val_cell_widget)
			if int_lng == 'Russian':
				nFSI_val_def.setText("Количество итераций привязки края объекта")
				nFSI_val.setToolTip("Введите целое число") 
			elif int_lng == 'English':
				nFSI_val_def.setText("Number of feature edge snapping iterations")	
				nFSI_val.setToolTip("Enter the integer number") 
				
			snapC_chcks_list.append(nFSI_chck)
			snapC_prs_list.append(nFSI_val_pr) 
			snapC_def_list.append(nFSI_val_def) 
			snapC_val_list.append(nFSI_val) 
			
			if snapC_obj != None:
				if snapC_obj['nFeatureSnapIter']:
					nFSI_chck.setChecked(True)
					nFSI_val_pr.setEnabled(True)
					nFSI_val_def.setEnabled(True)
					nFSI_val.setEnabled(True)
					nFSI_val.setValue(snapC_obj['nFeatureSnapIter'])
			
			#6)implicitFeatureSnap
			iFS_chck = QtGui.QCheckBox()
			iFS_chck_hbox = QtGui.QHBoxLayout()
			iFS_chck_hbox.setContentsMargins(0, 0, 0, 0)
			iFS_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			iFS_chck_hbox.addWidget(iFS_chck)
			iFS_chck_cell_widget = QtGui.QWidget()
			iFS_chck_cell_widget.setLayout(iFS_chck_hbox)
			snapC_prs_table.setCellWidget(5, 0, iFS_chck_cell_widget)
			iFS_val_pr = QtGui.QLabel()
			iFS_val_pr.setEnabled(False)
			iFS_val_pr.setText('implicitFeatureSnap')
			snapC_prs_table.setCellWidget(5, 1, iFS_val_pr)
			iFS_val_def = QtGui.QLabel()
			iFS_val_def.setEnabled(False)
			snapC_prs_table.setCellWidget(5, 2, iFS_val_def)
			iFS_val = QtGui.QComboBox()
			iFS_val.setEnabled(False)
			iFS_val.setFixedSize(70, 25)
			iFS_val_list = ['true', 'false']
			iFS_val.addItems(iFS_val_list)
			iFS_val_hbox = QtGui.QHBoxLayout()
			iFS_val_hbox.setContentsMargins(0, 0, 0, 0)
			iFS_val_hbox.addWidget(iFS_val)
			iFS_val_cell_widget = QtGui.QWidget()
			iFS_val_cell_widget.setLayout(iFS_val_hbox)
			snapC_prs_table.setCellWidget(5, 3, iFS_val_cell_widget)
			if int_lng == 'Russian':
				iFS_val_def.setText("Определять характеристики путем отбора проб поверхности")
			elif int_lng == 'English':
				iFS_val_def.setText("Detect (geometric) features by sampling the surface")
				
			snapC_chcks_list.append(iFS_chck)
			snapC_prs_list.append(iFS_val_pr) 
			snapC_def_list.append(iFS_val_def) 
			snapC_val_list.append(iFS_val) 
					
			if snapC_obj != None:
				if 'implicitFeatureSnap' in snapC_obj:
					iFS_val_mas = iFS_val.count()  
					for t in range(iFS_val_mas):
						if iFS_val.itemText(t) == snapC_obj['implicitFeatureSnap']:
							iFS_val.setCurrentIndex(t)

					iFS_chck.setChecked(True)
					iFS_val_pr.setEnabled(True)
					iFS_val_def.setEnabled(True)
					iFS_val.setEnabled(True)

			#7)explicitFeatureSnap
			eFS_chck = QtGui.QCheckBox()
			eFS_chck_hbox = QtGui.QHBoxLayout()
			eFS_chck_hbox.setContentsMargins(0, 0, 0, 0)
			eFS_chck_hbox.addWidget(eFS_chck)
			eFS_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			eFS_chck_cell_widget = QtGui.QWidget()
			eFS_chck_cell_widget.setLayout(eFS_chck_hbox)
			snapC_prs_table.setCellWidget(6, 0, eFS_chck_cell_widget)
			eFS_val_pr = QtGui.QLabel()
			eFS_val_pr.setEnabled(False)
			eFS_val_pr.setText('explicitFeatureSnap')
			snapC_prs_table.setCellWidget(6, 1, eFS_val_pr)
			eFS_val_def = QtGui.QLabel()
			eFS_val_def.setEnabled(False)
			snapC_prs_table.setCellWidget(6, 2, eFS_val_def)
			eFS_val = QtGui.QComboBox()
			eFS_val.setEnabled(False)
			eFS_val.setFixedSize(70, 25)
			eFS_val_list = ['true', 'false']
			eFS_val.addItems(eFS_val_list)
			eFS_val_hbox = QtGui.QHBoxLayout()
			eFS_val_hbox.setContentsMargins(0, 0, 0, 0)
			eFS_val_hbox.addWidget(eFS_val)
			eFS_val_cell_widget = QtGui.QWidget()
			eFS_val_cell_widget.setLayout(eFS_val_hbox)
			snapC_prs_table.setCellWidget(6, 3, eFS_val_cell_widget)
			if int_lng == 'Russian':
				eFS_val_def.setText("Использовать castellatedMeshControls::features")
			elif int_lng == 'English':
				eFS_val_def.setText("Use castellatedMeshControls::features")
			
			snapC_chcks_list.append(eFS_chck)
			snapC_prs_list.append(eFS_val_pr) 
			snapC_def_list.append(eFS_val_def) 
			snapC_val_list.append(eFS_val) 
			
			if snapC_obj != None:
				if 'explicitFeatureSnap' in snapC_obj:
					eFS_val_mas = eFS_val.count()  
					for t in range(eFS_val_mas):
						if eFS_val.itemText(t) == snapC_obj['explicitFeatureSnap']:
							eFS_val.setCurrentIndex(t)
		
					eFS_chck.setChecked(True)
					eFS_val_pr.setEnabled(True)
					eFS_val_def.setEnabled(True)
					eFS_val.setEnabled(True)
			
			#8)multiRegionFeatureSnap
			mRFS_chck = QtGui.QCheckBox()
			mRFS_chck = QtGui.QCheckBox()
			mRFS_chck_hbox = QtGui.QHBoxLayout()
			mRFS_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mRFS_chck_hbox.addWidget(mRFS_chck)
			mRFS_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mRFS_chck_cell_widget = QtGui.QWidget()
			mRFS_chck_cell_widget.setLayout(mRFS_chck_hbox)
			snapC_prs_table.setCellWidget(7, 0, mRFS_chck_cell_widget)			
			mRFS_val_pr = QtGui.QLabel()
			mRFS_val_pr.setEnabled(False)
			mRFS_val_pr.setText('multiRegionFeatureSnap')
			snapC_prs_table.setCellWidget(7, 1, mRFS_val_pr)
			mRFS_val_def = QtGui.QLabel()
			mRFS_val_def.setEnabled(False)
			snapC_prs_table.setCellWidget(7, 2, mRFS_val_def)
			mRFS_val = QtGui.QComboBox()
			mRFS_val.setEnabled(False)
			mRFS_val.setFixedSize(70, 25)
			mRFS_val_list = ['true', 'false']
			mRFS_val.addItems(mRFS_val_list)
			mRFS_val_hbox = QtGui.QHBoxLayout()
			mRFS_val_hbox.setContentsMargins(0, 0, 0, 0)
			mRFS_val_hbox.addWidget(mRFS_val)
			mRFS_val_cell_widget = QtGui.QWidget()
			mRFS_val_cell_widget.setLayout(mRFS_val_hbox)
			snapC_prs_table.setCellWidget(7, 3, mRFS_val_cell_widget)
			if int_lng == 'Russian':
				mRFS_val_def.setText("Определять признаки между несколькими поверхностями")
			elif int_lng == 'English':
				mRFS_val_def.setText("Detect features between multiple surfaces")

			snapC_chcks_list.append(mRFS_chck)
			snapC_prs_list.append(mRFS_val_pr) 
			snapC_def_list.append(mRFS_val_def) 
			snapC_val_list.append(mRFS_val) 
			
			if snapC_obj != None:
				if 'multiRegionFeatureSnap' in snapC_obj:
					mRFS_val_mas = mRFS_val.count()  
					for t in range(mRFS_val_mas):
						if mRFS_val.itemText(t) == snapC_obj['multiRegionFeatureSnap']:
							mRFS_val.setCurrentIndex(t)
			
					mRFS_chck.setChecked(True)
					mRFS_val_pr.setEnabled(True)
					mRFS_val_def.setEnabled(True)
					mRFS_val.setEnabled(True)
				
			prs_grid.addWidget(snapC_prs_table, 0, 0)	
				
			prs_frame = QtGui.QFrame()
			prs_frame.setLayout(prs_grid)

			# -------------------------Кнопка сохранения --------------------------#

			snapC_btnSave = QtGui.QPushButton()
			snapC_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(snapC_btnSave)
			if int_lng == 'Russian':
				snapC_btnSave.setText("Записать")
			elif int_lng == 'English':
				snapC_btnSave.setText("Write")

			# -----------------------Групповой элемент формы-----------------------#

			snapC_grid = QtGui.QGridLayout()
			snapC_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			snapC_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			snapC_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			snapC_grid.setRowStretch(3, 6)
			snapC_group = QtGui.QGroupBox()
			snapC_group.setLayout(snapC_grid)

			return snapC_group, snapC_btnSave, snapC_prs_table, snapC_chcks_list, snapC_prs_list, snapC_def_list, snapC_val_list
	