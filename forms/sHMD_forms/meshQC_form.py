# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class meshQC_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, meshQC_visible): 
		meshQC_obj = None
		
		#----------------Если файл meshQC.pkl существует, получаем данные из него для вывода в форму---------------#

		if meshQC_visible == True:
			meshQC_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'meshQC.pkl'
			if os.path.exists(meshQC_path_file):
		
				input = open(meshQC_path_file, 'rb')
				meshQC_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла meshQC.pkl на основе данных файла initial.pkl-------------#
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Общие настройки качества сетки")
		elif int_lng == 'English':
			main_lbl.setText("Generic mesh quality settings")
			
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'

		if os.path.exists(initial_path_file):
	
			input = open(initial_path_file, 'rb')
			obj_initial = pickle.load(input)
			input.close()
			
			prs_grid = QtGui.QGridLayout()
			
			##################################Дополнительные параметры#########################################
			
			meshQC_prs_add_table = QtGui.QTableWidget()
			meshQC_prs_add_table.setFixedSize(685, 508)
			meshQC_prs_add_table.setRowCount(16)
			meshQC_prs_add_table.setColumnCount(4)
			meshQC_prs_add_table.verticalHeader().hide()

			meshQC_prs_add_table.horizontalHeader().resizeSection(0, 50)
			meshQC_prs_add_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
			column_1 = QtGui.QTableWidgetItem()
			meshQC_prs_add_table.setHorizontalHeaderItem(0, column_1)
			meshQC_prs_add_table.horizontalHeader().setStyleSheet("color: steelblue")

			meshQC_prs_add_table.horizontalHeader().resizeSection(1, 150)
			meshQC_prs_add_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
			column_2 = QtGui.QTableWidgetItem()
			meshQC_prs_add_table.setHorizontalHeaderItem(1, column_2)
			meshQC_prs_add_table.horizontalHeader().setStyleSheet("color: steelblue")

			meshQC_prs_add_table.horizontalHeader().resizeSection(2, 360)
			meshQC_prs_add_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
			column_3 = QtGui.QTableWidgetItem()
			meshQC_prs_add_table.setHorizontalHeaderItem(2, column_3)
			meshQC_prs_add_table.horizontalHeader().setStyleSheet("color: steelblue")

			meshQC_prs_add_table.horizontalHeader().resizeSection(3, 110)
			meshQC_prs_add_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
			column_4 = QtGui.QTableWidgetItem()
			meshQC_prs_add_table.setHorizontalHeaderItem(3, column_4)
			meshQC_prs_add_table.horizontalHeader().setStyleSheet("color: steelblue")
			
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
				
			meshQC_chcks_list = []
			meshQC_prs_list = []
			meshQC_def_list = []
			meshQC_val_list = []
			
			#1)relaxedMaxNonOrtho		
			rMNO_chck = QtGui.QCheckBox()
			rMNO_chck_hbox = QtGui.QHBoxLayout()
			rMNO_chck_hbox.setContentsMargins(0, 0, 0, 0)
			rMNO_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			rMNO_chck_hbox.addWidget(rMNO_chck)
			rMNO_chck_cell_widget = QtGui.QWidget()
			rMNO_chck_cell_widget.setLayout(rMNO_chck_hbox)
			meshQC_prs_add_table.setCellWidget(0, 0, rMNO_chck_cell_widget)
			rMNO_val_pr = QtGui.QLabel()
			rMNO_val_pr.setEnabled(False)
			rMNO_val_pr.setText('relaxed maxNonOrtho')
			meshQC_prs_add_table.setCellWidget(0, 1, rMNO_val_pr)
			rMNO_val_def = QtGui.QLabel()
			rMNO_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(0, 2, rMNO_val_def)
			rMNO_val = QtGui.QSpinBox()
			rMNO_val.setEnabled(False)
			rMNO_val.setFixedSize(70, 25)
			rMNO_val_hbox = QtGui.QHBoxLayout()
			rMNO_val_hbox.setContentsMargins(0, 0, 0, 0)
			rMNO_val_hbox.addWidget(rMNO_val)
			rMNO_val_cell_widget = QtGui.QWidget()
			rMNO_val_cell_widget.setLayout(rMNO_val_hbox)
			meshQC_prs_add_table.setCellWidget(0, 3, rMNO_val_cell_widget)
			if int_lng == 'Russian':
				rMNO_val_def.setText("Максимальная неортогональность для свойств relaxed")
				rMNO_val.setToolTip("Введите целое число") 
			elif int_lng == 'English':
				rMNO_val_def.setText("Maximum non-orthogonality for relaxed parameters")
				rMNO_val.setToolTip("Enter the integer number") 
			
			meshQC_chcks_list.append(rMNO_chck)
			meshQC_prs_list.append(rMNO_val_pr) 
			meshQC_def_list.append(rMNO_val_def) 
			meshQC_val_list.append(rMNO_val)
			
			if meshQC_obj != None:
				if 'relaxed_maxNonOrtho' in meshQC_obj['meshQC_add']:
					rMNO_val.setValue(meshQC_obj['meshQC_add']['relaxed_maxNonOrtho'])	
					rMNO_chck.setChecked(True)
					rMNO_val_pr.setEnabled(True)
					rMNO_val_def.setEnabled(True)
					rMNO_val.setEnabled(True)

			#2)nSmoothScale			
			nSS_val_pr = QtGui.QLabel()
			nSS_val_pr.setText('nSmoothScale')
			meshQC_prs_add_table.setCellWidget(1, 1, nSS_val_pr)
			nSS_val_def = QtGui.QLabel()
			meshQC_prs_add_table.setCellWidget(1, 2, nSS_val_def)
			nSS_val = QtGui.QSpinBox()
			nSS_val.setFixedSize(70, 25)
			nSS_val_hbox = QtGui.QHBoxLayout()
			nSS_val_hbox.setContentsMargins(0, 0, 0, 0)
			nSS_val_hbox.addWidget(nSS_val)
			nSS_val_cell_widget = QtGui.QWidget()
			nSS_val_cell_widget.setLayout(nSS_val_hbox)
			meshQC_prs_add_table.setCellWidget(1, 3, nSS_val_cell_widget)
			if int_lng == 'Russian':
				nSS_val_def.setText("Количество итераций распространения ошибок")
				nSS_val.setToolTip("Введите целое число") 
			elif int_lng == 'English':
				nSS_val_def.setText("Number of error distribution iterations")
				nSS_val.setToolTip("Enter the integer number") 
			if meshQC_obj != None:
				nSS_val.setValue(meshQC_obj['meshQC_add']['nSmoothScale'])	
			
			#3)errorReduction		
			eR_val_pr = QtGui.QLabel()
			eR_val_pr.setText('errorReduction')
			meshQC_prs_add_table.setCellWidget(2, 1, eR_val_pr)
			eR_val_def = QtGui.QLabel()
			meshQC_prs_add_table.setCellWidget(2, 2, eR_val_def)
			eR_val = QtGui.QDoubleSpinBox()
			eR_val.setFixedSize(70, 25)
			eR_val_hbox = QtGui.QHBoxLayout()
			eR_val_hbox.setContentsMargins(0, 0, 0, 0)
			eR_val_hbox.addWidget(eR_val)
			eR_val_cell_widget = QtGui.QWidget()
			eR_val_cell_widget.setLayout(eR_val_hbox)
			meshQC_prs_add_table.setCellWidget(2, 3, eR_val_cell_widget)
			if int_lng == 'Russian':
				eR_val_def.setText("Величина уменьшения смещения в точке ошибки")
				eR_val.setToolTip("Введите число двойной точности") 
			elif int_lng == 'English':
				eR_val_def.setText("Amount to scale back displacement at error points")
				eR_val.setToolTip("Enter the double-precision number") 
			if meshQC_obj != None:
				eR_val.setValue(meshQC_obj['meshQC_add']['errorReduction'])	
				
			#4)maxNonOrtho
			mNO_chck = QtGui.QCheckBox()
			mNO_chck_hbox = QtGui.QHBoxLayout()
			mNO_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mNO_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mNO_chck_hbox.addWidget(mNO_chck)
			mNO_chck_cell_widget = QtGui.QWidget()
			mNO_chck_cell_widget.setLayout(mNO_chck_hbox)
			meshQC_prs_add_table.setCellWidget(3, 0, mNO_chck_cell_widget)
			mNO_val_pr = QtGui.QLabel()
			mNO_val_pr.setEnabled(False)
			mNO_val_pr.setText('maxNonOrtho')
			meshQC_prs_add_table.setCellWidget(3, 1, mNO_val_pr)
			mNO_val_def = QtGui.QLabel()
			mNO_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(3, 2, mNO_val_def)
			mNO_val = QtGui.QSpinBox()
			mNO_val.setEnabled(False)
			mNO_val.setFixedSize(70, 25)
			mNO_val_hbox = QtGui.QHBoxLayout()
			mNO_val_hbox.setContentsMargins(0, 0, 0, 0)
			mNO_val_hbox.addWidget(mNO_val)
			mNO_val_cell_widget = QtGui.QWidget()
			mNO_val_cell_widget.setLayout(mNO_val_hbox)
			meshQC_prs_add_table.setCellWidget(3, 3, mNO_val_cell_widget)
			if int_lng == 'Russian':
				mNO_val_def.setText("Максимальная ортогональность")
				mNO_val.setToolTip("Введите целое число") 
			elif int_lng == 'English':
				mNO_val_def.setText("Maximum orthogonality")
				mNO_val.setToolTip("Enter the integer number") 
			
			meshQC_chcks_list.append(mNO_chck)
			meshQC_prs_list.append(mNO_val_pr) 
			meshQC_def_list.append(mNO_val_def) 
			meshQC_val_list.append(mNO_val)
			
			if meshQC_obj != None:
				if 'maxNonOrtho' in meshQC_obj['meshQC_add']:
					mNO_val.setValue(meshQC_obj['meshQC_add']['maxNonOrtho'])	
					mNO_chck.setChecked(True)
					mNO_val_pr.setEnabled(True)
					mNO_val_def.setEnabled(True)
					mNO_val.setEnabled(True)
				
			#5)maxBoundarySkewness
			mBS_chck = QtGui.QCheckBox()
			mBS_chck_hbox = QtGui.QHBoxLayout()
			mBS_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mBS_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mBS_chck_hbox.addWidget(mBS_chck)
			mBS_chck_cell_widget = QtGui.QWidget()
			mBS_chck_cell_widget.setLayout(mBS_chck_hbox)
			meshQC_prs_add_table.setCellWidget(4, 0, mBS_chck_cell_widget)
			mBS_val_pr = QtGui.QLabel()
			mBS_val_pr.setEnabled(False)
			mBS_val_pr.setText('maxBoundarySkewness')
			meshQC_prs_add_table.setCellWidget(4, 1, mBS_val_pr)
			mBS_val_def = QtGui.QLabel()
			mBS_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(4, 2, mBS_val_def)
			mBS_val = QtGui.QSpinBox()
			mBS_val.setEnabled(False)
			mBS_val.setFixedSize(70, 25)
			mBS_val_hbox = QtGui.QHBoxLayout()
			mBS_val_hbox.setContentsMargins(0, 0, 0, 0)
			mBS_val_hbox.addWidget(mBS_val)
			mBS_val_cell_widget = QtGui.QWidget()
			mBS_val_cell_widget.setLayout(mBS_val_hbox)
			meshQC_prs_add_table.setCellWidget(4, 3, mBS_val_cell_widget)
			if int_lng == 'Russian':
				mBS_val_def.setText("Максимальная асимметрия границы")
				mBS_val.setToolTip("Введите целое число")
			elif int_lng == 'English':
				mBS_val_def.setText("Maximum boundary skewness")
				mBS_val.setToolTip("Enter the integer number") 
				
			meshQC_chcks_list.append(mBS_chck)
			meshQC_prs_list.append(mBS_val_pr) 
			meshQC_def_list.append(mBS_val_def) 
			meshQC_val_list.append(mBS_val)
			
			if meshQC_obj != None:
				if 'maxBoundarySkewness' in meshQC_obj['meshQC_add']:
					mBS_val.setValue(meshQC_obj['meshQC_add']['maxBoundarySkewness'])	
					mBS_chck.setChecked(True)
					mBS_val_pr.setEnabled(True)
					mBS_val_def.setEnabled(True)
					mBS_val.setEnabled(True)
				
			#6)maxInternalSkewness
			mIS_chck = QtGui.QCheckBox()
			mIS_chck = QtGui.QCheckBox()
			mIS_chck_hbox = QtGui.QHBoxLayout()
			mIS_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mIS_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mIS_chck_hbox.addWidget(mIS_chck)
			mIS_chck_cell_widget = QtGui.QWidget()
			mIS_chck_cell_widget.setLayout(mIS_chck_hbox)
			meshQC_prs_add_table.setCellWidget(5, 0, mIS_chck_cell_widget)
			mIS_val_pr = QtGui.QLabel()
			mIS_val_pr.setEnabled(False)
			mIS_val_pr.setText('maxInternalSkewness')
			meshQC_prs_add_table.setCellWidget(5, 1, mIS_val_pr)
			mIS_val_def = QtGui.QLabel()
			mIS_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(5, 2, mIS_val_def)
			mIS_val = QtGui.QSpinBox()
			mIS_val.setEnabled(False)
			mIS_val.setFixedSize(70, 25)
			mIS_val_hbox = QtGui.QHBoxLayout()
			mIS_val_hbox.setContentsMargins(0, 0, 0, 0)
			mIS_val_hbox.addWidget(mIS_val)
			mIS_val_cell_widget = QtGui.QWidget()
			mIS_val_cell_widget.setLayout(mIS_val_hbox)
			meshQC_prs_add_table.setCellWidget(5, 3, mIS_val_cell_widget)
			if int_lng == 'Russian':
				mIS_val_def.setText("Максимальная внутренняя асимметрия")
				mIS_val.setToolTip("Введите целое число")
			elif int_lng == 'English':
				mIS_val_def.setText("Maximum Internal Skewness")
				mIS_val.setToolTip("Enter the integer number") 
				
			meshQC_chcks_list.append(mIS_chck)
			meshQC_prs_list.append(mIS_val_pr) 
			meshQC_def_list.append(mIS_val_def) 
			meshQC_val_list.append(mIS_val)
			
			if meshQC_obj != None:
				if 'maxInternalSkewness' in meshQC_obj['meshQC_add']:
					mIS_val.setValue(meshQC_obj['meshQC_add']['maxInternalSkewness'])	
					mIS_chck.setChecked(True)
					mIS_val_pr.setEnabled(True)
					mIS_val_def.setEnabled(True)
					mIS_val.setEnabled(True)
				
			#7)maxConcave
			mC_chck = QtGui.QCheckBox()
			mC_chck_hbox = QtGui.QHBoxLayout()
			mC_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mC_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mC_chck_hbox.addWidget(mC_chck)
			mC_chck_cell_widget = QtGui.QWidget()
			mC_chck_cell_widget.setLayout(mC_chck_hbox)
			meshQC_prs_add_table.setCellWidget(6, 0, mC_chck_cell_widget)
			mC_val_pr = QtGui.QLabel()
			mC_val_pr.setEnabled(False)
			mC_val_pr.setText('maxConcave')
			meshQC_prs_add_table.setCellWidget(6, 1, mC_val_pr)
			mC_val_def = QtGui.QLabel()
			mC_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(6, 2, mC_val_def)
			mC_val = QtGui.QSpinBox()
			mC_val.setEnabled(False)
			mC_val.setFixedSize(70, 25)
			mC_val_hbox = QtGui.QHBoxLayout()
			mC_val_hbox.setContentsMargins(0, 0, 0, 0)
			mC_val_hbox.addWidget(mC_val)
			mC_val_cell_widget = QtGui.QWidget()
			mC_val_cell_widget.setLayout(mC_val_hbox)
			meshQC_prs_add_table.setCellWidget(6, 3, mC_val_cell_widget)
			if int_lng == 'Russian':
				mC_val_def.setText("Максимальная вогнутость")
				mC_val.setToolTip("Введите целое число")
			elif int_lng == 'English':
				mC_val_def.setText("Maximum concaveness")
				mC_val.setToolTip("Enter the integer number")
				
			meshQC_chcks_list.append(mC_chck)
			meshQC_prs_list.append(mC_val_pr) 
			meshQC_def_list.append(mC_val_def) 
			meshQC_val_list.append(mC_val)
			
			if meshQC_obj != None:
				if 'maxConcave' in meshQC_obj['meshQC_add']:
					mC_val.setValue(meshQC_obj['meshQC_add']['maxConcave'])	
					mC_chck.setChecked(True)
					mC_val_pr.setEnabled(True)
					mC_val_def.setEnabled(True)
					mC_val.setEnabled(True)
				
			#8)minVol
			mV_chck = QtGui.QCheckBox()
			mV_chck_hbox = QtGui.QHBoxLayout()
			mV_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mV_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mV_chck_hbox.addWidget(mV_chck)
			mV_chck_cell_widget = QtGui.QWidget()
			mV_chck_cell_widget.setLayout(mV_chck_hbox)
			meshQC_prs_add_table.setCellWidget(7, 0, mV_chck_cell_widget)
			mV_val_pr = QtGui.QLabel()
			mV_val_pr.setEnabled(False)
			mV_val_pr.setText('minVol')
			meshQC_prs_add_table.setCellWidget(7, 1, mV_val_pr)
			mV_val_def = QtGui.QLabel()
			mV_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(7, 2, mV_val_def)
			mV_val = QtGui.QLineEdit()
			mV_val.setEnabled(False)
			mV_val.setFixedSize(70, 25)
			mV_val.setInputMask("9e-99;_")
			mV_val_hbox = QtGui.QHBoxLayout()
			mV_val_hbox.setContentsMargins(0, 0, 0, 0)
			mV_val_hbox.addWidget(mV_val)
			mV_val_cell_widget = QtGui.QWidget()
			mV_val_cell_widget.setLayout(mV_val_hbox)
			meshQC_prs_add_table.setCellWidget(7, 3, mV_val_cell_widget)
			if int_lng == 'Russian':
				mV_val_def.setText("Минимальный объем пирамиды")
				mV_val.setToolTip("Введите число в экспоненциальном формате")
			elif int_lng == 'English':
				mV_val_def.setText("Minimum pyramid volume")
				mV_val.setToolTip("Enter the number in exponential format")
				
			meshQC_chcks_list.append(mV_chck)
			meshQC_prs_list.append(mV_val_pr) 
			meshQC_def_list.append(mV_val_def) 
			meshQC_val_list.append(mV_val)
			
			if meshQC_obj != None:
				if 'minVol' in meshQC_obj['meshQC_add']:
					mV_val.setText(meshQC_obj['meshQC_add']['minVol'])	
					mV_chck.setChecked(True)
					mV_val_pr.setEnabled(True)
					mV_val_def.setEnabled(True)
					mV_val.setEnabled(True)
				
			#9)minArea
			mA_chck = QtGui.QCheckBox()
			mA_chck_hbox = QtGui.QHBoxLayout()
			mA_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mA_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mA_chck_hbox.addWidget(mA_chck)
			mA_chck_cell_widget = QtGui.QWidget()
			mA_chck_cell_widget.setLayout(mA_chck_hbox)
			meshQC_prs_add_table.setCellWidget(8, 0, mA_chck_cell_widget)
			mA_val_pr = QtGui.QLabel()
			mA_val_pr.setEnabled(False)
			mA_val_pr.setText('minArea')
			meshQC_prs_add_table.setCellWidget(8, 1, mA_val_pr)
			mA_val_def = QtGui.QLabel()
			mA_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(8, 2, mA_val_def)
			mA_val = QtGui.QLineEdit()
			mA_val.setEnabled(False)
			mA_val.setFixedSize(70, 25)
			regexp = QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+')
			validator = QtGui.QRegExpValidator(regexp)
			mA_val.setValidator(validator)
			
			mA_val_hbox = QtGui.QHBoxLayout()
			mA_val_hbox.setContentsMargins(0, 0, 0, 0)
			mA_val_hbox.addWidget(mA_val)
			mA_val_cell_widget = QtGui.QWidget()
			mA_val_cell_widget.setLayout(mA_val_hbox)
			meshQC_prs_add_table.setCellWidget(8, 3, mA_val_cell_widget)
			if int_lng == 'Russian':
				mA_val_def.setText("Минимальная площадь грани")
				mA_val.setToolTip("Введите число в экспоненциальном формате")
			elif int_lng == 'English':
				mA_val_def.setText("Minimum face area")
				mA_val.setToolTip("Enter the number in exponential format")
				
			meshQC_chcks_list.append(mA_chck)
			meshQC_prs_list.append(mA_val_pr) 
			meshQC_def_list.append(mA_val_def) 
			meshQC_val_list.append(mA_val)
			
			if meshQC_obj != None:
				if 'minVol' in meshQC_obj['meshQC_add']:
					mA_val.setText(meshQC_obj['meshQC_add']['minVol'])	
					mA_chck.setChecked(True)
					mA_val_pr.setEnabled(True)
					mA_val_def.setEnabled(True)
					mA_val.setEnabled(True)
				
			#10)minTetQuality
			mTQ_chck = QtGui.QCheckBox()
			mTQ_chck_hbox = QtGui.QHBoxLayout()
			mTQ_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mTQ_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mTQ_chck_hbox.addWidget(mTQ_chck)
			mTQ_chck_cell_widget = QtGui.QWidget()
			mTQ_chck_cell_widget.setLayout(mTQ_chck_hbox)
			meshQC_prs_add_table.setCellWidget(9, 0, mTQ_chck_cell_widget)
			mTQ_val_pr = QtGui.QLabel()
			mTQ_val_pr.setEnabled(False)
			mTQ_val_pr.setText('minTetQuality')
			meshQC_prs_add_table.setCellWidget(9, 1, mTQ_val_pr)
			mTQ_val_def = QtGui.QLabel()
			mTQ_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(9, 2, mTQ_val_def)
			mTQ_val = QtGui.QLineEdit()
			mTQ_val.setEnabled(False)
			mTQ_val.setFixedSize(70, 25)
			mTQ_val.setInputMask("9e-99;_")
			mTQ_val_hbox = QtGui.QHBoxLayout()
			mTQ_val_hbox.setContentsMargins(0, 0, 0, 0)
			mTQ_val_hbox.addWidget(mTQ_val)
			mTQ_val_cell_widget = QtGui.QWidget()
			mTQ_val_cell_widget.setLayout(mTQ_val_hbox)
			meshQC_prs_add_table.setCellWidget(9, 3, mTQ_val_cell_widget)
			if int_lng == 'Russian':
				mTQ_val_def.setText("Минимальное качество тетраэдра")
				mTQ_val.setToolTip("Введите число в экспоненциальном формате")
			elif int_lng == 'English':
				mTQ_val_def.setText("Minimum quality of the tetrahedron")
				mTQ_val.setToolTip("Enter the number in exponential format")
				
			meshQC_chcks_list.append(mTQ_chck)
			meshQC_prs_list.append(mTQ_val_pr) 
			meshQC_def_list.append(mTQ_val_def) 
			meshQC_val_list.append(mTQ_val)
			
			if meshQC_obj != None:
				if 'minTetQuality' in meshQC_obj['meshQC_add']:
					mTQ_val.setText(meshQC_obj['meshQC_add']['minTetQuality'])	
					mTQ_chck.setChecked(True)
					mTQ_val_pr.setEnabled(True)
					mTQ_val_def.setEnabled(True)
					mTQ_val.setEnabled(True)
			
			#11)minTwist
			mT_chck = QtGui.QCheckBox()
			mT_chck_hbox = QtGui.QHBoxLayout()
			mT_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mT_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mT_chck_hbox.addWidget(mT_chck)
			mT_chck_cell_widget = QtGui.QWidget()
			mT_chck_cell_widget.setLayout(mT_chck_hbox)
			meshQC_prs_add_table.setCellWidget(10, 0, mT_chck_cell_widget)
			mT_val_pr = QtGui.QLabel()
			mT_val_pr.setEnabled(False)
			mT_val_pr.setText('minTwist')
			meshQC_prs_add_table.setCellWidget(10, 1, mT_val_pr)
			mT_val_def = QtGui.QLabel()
			mT_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(10, 2, mT_val_def)
			mT_val = QtGui.QDoubleSpinBox()
			mT_val.setEnabled(False)
			mT_val.setFixedSize(70, 25)
			mT_val_hbox = QtGui.QHBoxLayout()
			mT_val_hbox.setContentsMargins(0, 0, 0, 0)
			mT_val_hbox.addWidget(mT_val)
			mT_val_cell_widget = QtGui.QWidget()
			mT_val_cell_widget.setLayout(mT_val_hbox)
			meshQC_prs_add_table.setCellWidget(10, 3, mT_val_cell_widget)
			if int_lng == 'Russian':
				mT_val_def.setText("Минимальное скручивание грани")
				mT_val.setToolTip("Введите число двойной точности") 
			elif int_lng == 'English':
				mT_val_def.setText("Minimum face twist")
				mT_val.setToolTip("Enter the double-precision number") 
				
			meshQC_chcks_list.append(mT_chck)
			meshQC_prs_list.append(mT_val_pr) 
			meshQC_def_list.append(mT_val_def) 
			meshQC_val_list.append(mT_val)
			
			if meshQC_obj != None:
				if 'minTwist' in meshQC_obj['meshQC_add']:
					mT_val.setValue(meshQC_obj['meshQC_add']['minTwist'])	
					mT_chck.setChecked(True)
					mT_val_pr.setEnabled(True)
					mT_val_def.setEnabled(True)
					mT_val.setEnabled(True)
				
			#12)minDeterminant
			mD_chck = QtGui.QCheckBox()
			mD_chck_hbox = QtGui.QHBoxLayout()
			mD_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mD_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mD_chck_hbox.addWidget(mD_chck)
			mD_chck_cell_widget = QtGui.QWidget()
			mD_chck_cell_widget.setLayout(mD_chck_hbox)
			meshQC_prs_add_table.setCellWidget(11, 0, mD_chck_cell_widget)
			mD_val_pr = QtGui.QLabel()
			mD_val_pr.setEnabled(False)
			mD_val_pr.setText('minDeterminant')
			meshQC_prs_add_table.setCellWidget(11, 1, mD_val_pr)
			mD_val_def = QtGui.QLabel()
			mD_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(11, 2, mD_val_def)
			mD_val = QtGui.QLineEdit()
			mD_val.setEnabled(False)
			mD_val.setValidator(QtGui.QDoubleValidator(0.0, 999.0, 3, mD_val))
			mD_val.setFixedSize(70, 25)
			mD_val_hbox = QtGui.QHBoxLayout()
			mD_val_hbox.setContentsMargins(0, 0, 0, 0)
			mD_val_hbox.addWidget(mD_val)
			mD_val_cell_widget = QtGui.QWidget()
			mD_val_cell_widget.setLayout(mD_val_hbox)
			meshQC_prs_add_table.setCellWidget(11, 3, mD_val_cell_widget)
			if int_lng == 'Russian':
				mD_val_def.setText("Минимальная нормированная детерминанта ячейки")
				mD_val.setToolTip("Введите число тройной точности")
			elif int_lng == 'English':
				mD_val_def.setText("Minimum normalised cell determinant")
				mD_val.setToolTip("Enter the triple precision number")
				
			meshQC_chcks_list.append(mD_chck)
			meshQC_prs_list.append(mD_val_pr) 
			meshQC_def_list.append(mD_val_def) 
			meshQC_val_list.append(mD_val)	
			
			if meshQC_obj != None:
				if 'minDeterminant' in meshQC_obj['meshQC_add']:
					mD_val.setText(meshQC_obj['meshQC_add']['minDeterminant'])	
					mD_chck.setChecked(True)
					mD_val_pr.setEnabled(True)
					mD_val_def.setEnabled(True)
					mD_val.setEnabled(True)
				
			#13)minFaceWeight
			mFW_chck = QtGui.QCheckBox()
			mFW_chck_hbox = QtGui.QHBoxLayout()
			mFW_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mFW_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mFW_chck_hbox.addWidget(mFW_chck)
			mFW_chck_cell_widget = QtGui.QWidget()
			mFW_chck_cell_widget.setLayout(mFW_chck_hbox)
			meshQC_prs_add_table.setCellWidget(12, 0, mFW_chck_cell_widget)
			mFW_val_pr = QtGui.QLabel()
			mFW_val_pr.setEnabled(False)
			mFW_val_pr.setText('minFaceWeight')
			meshQC_prs_add_table.setCellWidget(12, 1, mFW_val_pr)
			mFW_val_def = QtGui.QLabel()
			mFW_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(12, 2, mFW_val_def)
			mFW_val = QtGui.QDoubleSpinBox()
			mFW_val.setEnabled(False)
			mFW_val.setFixedSize(70, 25)
			mFW_val_hbox = QtGui.QHBoxLayout()
			mFW_val_hbox.setContentsMargins(0, 0, 0, 0)
			mFW_val_hbox.addWidget(mFW_val)
			mFW_val_cell_widget = QtGui.QWidget()
			mFW_val_cell_widget.setLayout(mFW_val_hbox)
			meshQC_prs_add_table.setCellWidget(12, 3, mFW_val_cell_widget)
			if int_lng == 'Russian':
				mFW_val_def.setText("Минимальный вес грани")
				mFW_val.setToolTip("Введите число двойной точности") 
			elif int_lng == 'English':
				mFW_val_def.setText("Minimum face weight")
				mFW_val.setToolTip("Enter the double-precision number") 
				
			meshQC_chcks_list.append(mFW_chck)
			meshQC_prs_list.append(mFW_val_pr) 
			meshQC_def_list.append(mFW_val_def) 
			meshQC_val_list.append(mFW_val)	
			
			if meshQC_obj != None:
				if 'minFaceWeight' in meshQC_obj['meshQC_add']:
					mFW_val.setValue(meshQC_obj['meshQC_add']['minFaceWeight'])	
					mFW_chck.setChecked(True)
					mFW_val_pr.setEnabled(True)
					mFW_val_def.setEnabled(True)
					mFW_val.setEnabled(True)
				
			#14)minVolRatio
			mVR_chck = QtGui.QCheckBox()
			mVR_chck_hbox = QtGui.QHBoxLayout()
			mVR_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mVR_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mVR_chck_hbox.addWidget(mVR_chck)
			mVR_chck_cell_widget = QtGui.QWidget()
			mVR_chck_cell_widget.setLayout(mVR_chck_hbox)
			meshQC_prs_add_table.setCellWidget(13, 0, mVR_chck_cell_widget)
			mVR_val_pr = QtGui.QLabel()
			mVR_val_pr.setEnabled(False)
			mVR_val_pr.setText('minVolRatio')
			meshQC_prs_add_table.setCellWidget(13, 1, mVR_val_pr)
			mVR_val_def = QtGui.QLabel()
			mVR_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(13, 2, mVR_val_def)
			mVR_val = QtGui.QDoubleSpinBox()
			mVR_val.setEnabled(False)
			mVR_val.setFixedSize(70, 25)
			mVR_val_hbox = QtGui.QHBoxLayout()
			mVR_val_hbox.setContentsMargins(0, 0, 0, 0)
			mVR_val_hbox.addWidget(mVR_val)
			mVR_val_cell_widget = QtGui.QWidget()
			mVR_val_cell_widget.setLayout(mVR_val_hbox)
			meshQC_prs_add_table.setCellWidget(13, 3, mVR_val_cell_widget)
			if int_lng == 'Russian':
				mVR_val_def.setText("Минимальное объемное соотношение соседних ячеек")
				mVR_val.setToolTip("Введите число двойной точности") 
			elif int_lng == 'English':
				mVR_val_def.setText("Minimum volume ratio of neighbouring cells")
				mVR_val.setToolTip("Enter the double-precision number") 
				
			meshQC_chcks_list.append(mVR_chck)
			meshQC_prs_list.append(mVR_val_pr) 
			meshQC_def_list.append(mVR_val_def) 
			meshQC_val_list.append(mVR_val)	
			
			if meshQC_obj != None:
				if 'minVolRatio' in meshQC_obj['meshQC_add']:
					mVR_val.setValue(meshQC_obj['meshQC_add']['minVolRatio'])	
					mVR_chck.setChecked(True)
					mVR_val_pr.setEnabled(True)
					mVR_val_def.setEnabled(True)
					mVR_val.setEnabled(True)
				
			#15)minTriangleTwist
			mTT_chck = QtGui.QCheckBox()
			mTT_chck_hbox = QtGui.QHBoxLayout()
			mTT_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mTT_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mTT_chck_hbox.addWidget(mTT_chck)
			mTT_chck_cell_widget = QtGui.QWidget()
			mTT_chck_cell_widget.setLayout(mTT_chck_hbox)
			meshQC_prs_add_table.setCellWidget(14, 0, mTT_chck_cell_widget)
			mTT_val_pr = QtGui.QLabel()
			mTT_val_pr.setEnabled(False)
			mTT_val_pr.setText('minTriangleTwist')
			meshQC_prs_add_table.setCellWidget(14, 1, mTT_val_pr)
			mTT_val_def = QtGui.QLabel()
			mTT_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(14, 2, mTT_val_def)
			mTT_val = QtGui.QLineEdit()
			mTT_val.setEnabled(False)
			mTT_val.setValidator(QtGui.QDoubleValidator(-999.0, 999.0, 1, mTT_val))
			mTT_val.setFixedSize(70, 25)
			mTT_val.setEnabled(False)
			mTT_val.setFixedSize(70, 25)
			mTT_val_hbox = QtGui.QHBoxLayout()
			mTT_val_hbox.setContentsMargins(0, 0, 0, 0)
			mTT_val_hbox.addWidget(mTT_val)
			mTT_val_cell_widget = QtGui.QWidget()
			mTT_val_cell_widget.setLayout(mTT_val_hbox)
			meshQC_prs_add_table.setCellWidget(14, 3, mTT_val_cell_widget)
			if int_lng == 'Russian':
				mTT_val_def.setText("Минимальное треугольное скручивание")
				mTT_val.setToolTip("Введите целое число, отрицательное или положительное") 
			elif int_lng == 'English':
				mTT_val_def.setText("Minimum triangle twist")
				mTT_val.setToolTip("Enter an integer, negative or positive")
				
			meshQC_chcks_list.append(mTT_chck)
			meshQC_prs_list.append(mTT_val_pr) 
			meshQC_def_list.append(mTT_val_def) 
			meshQC_val_list.append(mTT_val)	
			
			if meshQC_obj != None:
				if 'minTriangleTwist' in meshQC_obj['meshQC_add']:
					mTT_val.setText(meshQC_obj['meshQC_add']['minTriangleTwist'])	
					mTT_chck.setChecked(True)
					mTT_val_pr.setEnabled(True)
					mTT_val_def.setEnabled(True)
					mTT_val.setEnabled(True)
					
			#16)minVolCollapseRatio
			mVCR_chck = QtGui.QCheckBox()
			mVCR_chck_hbox = QtGui.QHBoxLayout()
			mVCR_chck_hbox.setContentsMargins(0, 0, 0, 0)
			mVCR_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
			mVCR_chck_hbox.addWidget(mVCR_chck)
			mVCR_chck_cell_widget = QtGui.QWidget()
			mVCR_chck_cell_widget.setLayout(mVCR_chck_hbox)
			meshQC_prs_add_table.setCellWidget(15, 0, mVCR_chck_cell_widget)
			mVCR_val_pr = QtGui.QLabel()
			mVCR_val_pr.setEnabled(False)
			mVCR_val_pr.setText('minVolCollapseRatio')
			meshQC_prs_add_table.setCellWidget(15, 1, mVCR_val_pr)
			mVCR_val_def = QtGui.QLabel()
			mVCR_val_def.setEnabled(False)
			meshQC_prs_add_table.setCellWidget(15, 2, mVCR_val_def)
			mVCR_val = QtGui.QDoubleSpinBox()
			mVCR_val.setEnabled(False)
			mVCR_val.setFixedSize(70, 25)
			mVCR_val_hbox = QtGui.QHBoxLayout()
			mVCR_val_hbox.setContentsMargins(0, 0, 0, 0)
			mVCR_val_hbox.addWidget(mVCR_val)
			mVCR_val_cell_widget = QtGui.QWidget()
			mVCR_val_cell_widget.setLayout(mVCR_val_hbox)
			meshQC_prs_add_table.setCellWidget(15, 3, mVCR_val_cell_widget)
			if int_lng == 'Russian':
				mVCR_val_def.setText("Минимальный коэффициент сглаживания объема")
				mVCR_val.setToolTip("Введите дробное или целое число") 
			elif int_lng == 'English':
				mVCR_val_def.setText("Minimum volume smoothing ratio")
				mVCR_val.setToolTip("Enter a fractional or an integer value") 
				
			meshQC_chcks_list.append(mVCR_chck)
			meshQC_prs_list.append(mVCR_val_pr) 
			meshQC_def_list.append(mVCR_val_def) 
			meshQC_val_list.append(mVCR_val)	
			
			if meshQC_obj != None:
				if 'minVolCollapseRatio' in meshQC_obj['meshQC_add']:
					mVCR_val.setValue(meshQC_obj['meshQC_add']['minVolCollapseRatio'])	
					mVCR_chck.setChecked(True)
					mVCR_val_pr.setEnabled(True)
					mVCR_val_def.setEnabled(True)
					mVCR_val.setEnabled(True)
			
			prs_grid.addWidget(meshQC_prs_add_table, 0, 0, alignment=QtCore.Qt.AlignCenter)
			
			prs_frame = QtGui.QFrame()
			prs_frame.setLayout(prs_grid)

			# -------------------------Кнопка сохранения --------------------------#

			meshQC_btnSave = QtGui.QPushButton()
			meshQC_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(meshQC_btnSave)
			if int_lng == 'Russian':
				meshQC_btnSave.setText("Записать")
			elif int_lng == 'English':
				meshQC_btnSave.setText("Write")

			# -----------------------Групповой элемент формы-----------------------#

			meshQC_grid = QtGui.QGridLayout()
			meshQC_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			meshQC_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			meshQC_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			meshQC_grid.setRowStretch(3, 6)
			meshQC_group = QtGui.QGroupBox()
			meshQC_group.setLayout(meshQC_grid)

			return meshQC_group, meshQC_btnSave, meshQC_prs_add_table, meshQC_chcks_list, meshQC_prs_list, meshQC_def_list, meshQC_val_list
		


