# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class extrusion_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, extrusion_visible): 
		extrusion_obj = None
		
		#----------------Если файл extrusion.pkl существует, получаем данные из него для вывода в форму---------------#

		if extrusion_visible == True:
			extrusion_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'extrusion.pkl'
			if os.path.exists(extrusion_path_file):
		
				input = open(extrusion_path_file, 'rb')
				extrusion_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла extrusion.pkl на основе данных файла initial.pkl-------------#
		
		prs_grid = QtGui.QGridLayout()
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(prs_grid)
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Блок параметров вытеснения")
		elif int_lng == 'English':
			main_lbl.setText("Wave parameters block")
		
		extr_table = QtGui.QTableWidget()
		extr_table.setFixedSize(660, 330)
		extr_table.setRowCount(10)
		extr_table.setColumnCount(4)
		extr_table.verticalHeader().hide()

		extr_table.horizontalHeader().resizeSection(0, 60)
		extr_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
		column_1 = QtGui.QTableWidgetItem()
		extr_table.setHorizontalHeaderItem(0, column_1)
		extr_table.horizontalHeader().setStyleSheet("color: steelblue")

		extr_table.horizontalHeader().resizeSection(1, 100)
		extr_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
		column_2 = QtGui.QTableWidgetItem()
		extr_table.setHorizontalHeaderItem(1, column_2)
		extr_table.horizontalHeader().setStyleSheet("color: steelblue")
		
		extr_table.horizontalHeader().resizeSection(2, 195)
		extr_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
		column_3 = QtGui.QTableWidgetItem()
		extr_table.setHorizontalHeaderItem(2, column_3)
		extr_table.horizontalHeader().setStyleSheet("color: steelblue")
		
		extr_table.horizontalHeader().resizeSection(3, 300)
		extr_table.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Fixed)
		column_4 = QtGui.QTableWidgetItem()
		extr_table.setHorizontalHeaderItem(3, column_4)
		extr_table.horizontalHeader().setStyleSheet("color: steelblue")
				
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
			
		extrusion_checks_list = []	
		extrusion_values_list = []
		extrusion_val_pr_list = []
		extrusion_val_def_list = []
			
		#extrude#
		e_val_pr = QtGui.QLabel()
		e_val_pr.setText('extrude')
		extr_table.setCellWidget(0, 1, e_val_pr)
		e_val_def = QtGui.QLabel()
		extr_table.setCellWidget(0, 2, e_val_def)
		e_edit = QtGui.QComboBox()
		e_edit.setFixedSize(50, 25)
		e_list = ['on', 'off']
		e_edit.addItems(e_list)
		e_val_hbox = QtGui.QHBoxLayout()
		e_val_hbox.setContentsMargins(0, 0, 0, 0)
		e_val_hbox.addWidget(e_edit)
		e_val_cell_widget = QtGui.QWidget()
		e_val_cell_widget.setLayout(e_val_hbox)
		extr_table.setCellWidget(0, 3, e_val_cell_widget)
		if int_lng == 'Russian':
			e_val_def.setText("Установить опцию вытеснения")
		elif int_lng == 'English':
			e_val_def.setText("Set wipe option")
		if extrusion_obj != None:
			e_edit_mas = e_edit.count()  
			for t in range(e_edit_mas):
				if e_edit.itemText(t) == extrusion_obj['e']:
					e_edit.setCurrentIndex(t)
		
		#extrudeModel#			
		eM_val_pr = QtGui.QLabel()
		eM_val_pr.setText('extrudeModel')
		extr_table.setCellWidget(1, 1, eM_val_pr)
		eM_val_def = QtGui.QLabel()
		extr_table.setCellWidget(1, 2, eM_val_def)
		eM_edit = QtGui.QComboBox()
		eM_edit.setFixedSize(140, 25)
		eM_list = ['linearDirection', 'wedge']
		eM_edit.addItems(eM_list)
		eM_val_hbox = QtGui.QHBoxLayout()
		eM_val_hbox.setContentsMargins(0, 0, 0, 0)
		eM_val_hbox.addWidget(eM_edit)
		eM_val_cell_widget = QtGui.QWidget()
		eM_val_cell_widget.setLayout(eM_val_hbox)
		extr_table.setCellWidget(1, 3, eM_val_cell_widget)
		if int_lng == 'Russian':
			eM_val_def.setText("Модель вытеснения")
		elif int_lng == 'English':
			eM_val_def.setText("Model of extrusion")
			
		if extrusion_obj != None:
			eM_edit_mas = e_edit.count()  
			for t in range(e_edit_mas):
				if eM_edit.itemText(t) == extrusion_obj['eM']:
					eM_edit.setCurrentIndex(t)
						
		#patchType#			
		pT_val_pr = QtGui.QLabel()
		pT_val_pr.setText('patchType')
		extr_table.setCellWidget(2, 1, pT_val_pr)
		pT_val_def = QtGui.QLabel()
		extr_table.setCellWidget(2, 2, pT_val_def)
		pT_edit = QtGui.QComboBox()
		pT_edit.setFixedSize(140, 25)
		pT_list = ['linearDirection', 'wedge', 'empty']
		pT_edit.addItems(pT_list)
		pT_val_hbox = QtGui.QHBoxLayout()
		pT_val_hbox.setContentsMargins(0, 0, 0, 0)
		pT_val_hbox.addWidget(pT_edit)
		pT_val_cell_widget = QtGui.QWidget()
		pT_val_cell_widget.setLayout(pT_val_hbox)
		extr_table.setCellWidget(2, 3, pT_val_cell_widget)
		if int_lng == 'Russian':
			pT_val_def.setText("Тип патча")
		elif int_lng == 'English':
			pT_val_def.setText("Patch type")
			
		if extrusion_obj != None:
			pT_edit_mas = pT_edit.count()  
			for t in range(pT_edit_mas):
				if pT_edit.itemText(t) == extrusion_obj['pT']:
					pT_edit.setCurrentIndex(t)
		
		#nLayers
		nL_chck = QtGui.QCheckBox()
		nL_chck_hbox = QtGui.QHBoxLayout()
		nL_chck_hbox.setContentsMargins(0, 0, 0, 0)
		nL_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
		nL_chck_hbox.addWidget(nL_chck)
		nL_chck_cell_widget = QtGui.QWidget()
		nL_chck_cell_widget.setLayout(nL_chck_hbox)
		extr_table.setCellWidget(3, 0, nL_chck_cell_widget)
		nL_val_pr = QtGui.QLabel()
		nL_val_pr.setEnabled(False)
		nL_val_pr.setText('nLayers')
		extr_table.setCellWidget(3, 1, nL_val_pr)
		nL_val_def = QtGui.QLabel()
		nL_val_def.setEnabled(False)
		extr_table.setCellWidget(3, 2, nL_val_def)
		nL_val = QtGui.QSpinBox()
		nL_val.setEnabled(False)
		nL_val.setFixedSize(70, 25)
		nL_val_hbox = QtGui.QHBoxLayout()
		nL_val_hbox.setContentsMargins(0, 0, 0, 0)
		nL_val_hbox.addWidget(nL_val)
		nL_val_cell_widget = QtGui.QWidget()
		nL_val_cell_widget.setLayout(nL_val_hbox)
		extr_table.setCellWidget(3, 3, nL_val_cell_widget)
		if int_lng == 'Russian':
			nL_val_def.setText("Количество слоев")
			nL_val.setToolTip("Введите целое число") 
		elif int_lng == 'English':
			nL_val_def.setText("Number of layers")
			nL_val.setToolTip("Enter the integer number") 
		if extrusion_obj != None:
			nL_chck.setChecked(extrusion_obj['nL_chck'])
			if extrusion_obj['nL_chck'] == True:
				nL_val_pr.setEnabled(True)
				nL_val_def.setEnabled(True)
				nL_val.setEnabled(True)
				nL_val.setValue(extrusion_obj['nL_val'])	
					
		extrusion_checks_list.append(nL_chck)	
		extrusion_values_list.append(nL_val)	
		extrusion_val_pr_list.append(nL_val_pr)
		extrusion_val_def_list.append(nL_val_def)
		
		#expansionRatio
		eR_chck = QtGui.QCheckBox()
		eR_chck_hbox = QtGui.QHBoxLayout()
		eR_chck_hbox.setContentsMargins(0, 0, 0, 0)
		eR_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
		eR_chck_hbox.addWidget(eR_chck)
		eR_chck_cell_widget = QtGui.QWidget()
		eR_chck_cell_widget.setLayout(eR_chck_hbox)
		extr_table.setCellWidget(4, 0, eR_chck_cell_widget)
		eR_val_pr = QtGui.QLabel()
		eR_val_pr.setEnabled(False)
		eR_val_pr.setText('expansionRatio')
		extr_table.setCellWidget(4, 1, eR_val_pr)
		eR_val_def = QtGui.QLabel()
		eR_val_def.setEnabled(False)
		extr_table.setCellWidget(4, 2, eR_val_def)
		eR_val = QtGui.QDoubleSpinBox()
		eR_val.setEnabled(False)
		eR_val.setFixedSize(70, 25)
		eR_val_hbox = QtGui.QHBoxLayout()
		eR_val_hbox.setContentsMargins(0, 0, 0, 0)
		eR_val_hbox.addWidget(eR_val)
		eR_val_cell_widget = QtGui.QWidget()
		eR_val_cell_widget.setLayout(eR_val_hbox)
		if extrusion_obj != None:
			eR_chck.setChecked(extrusion_obj['eR_chck'])
			if extrusion_obj['eR_chck'] == True:
				eR_val_pr.setEnabled(True)
				eR_val_def.setEnabled(True)
				eR_val.setEnabled(True)
				eR_val.setValue(extrusion_obj['eR_val'])
	
		extr_table.setCellWidget(4, 3, eR_val_cell_widget)
		if int_lng == 'Russian':
			eR_val_def.setText("Cтепень расширения")
			eR_val.setToolTip("Введите целое или дробное число") 
		elif int_lng == 'English':
			eR_val_def.setText("Ratio of expansion")
			eR_val.setToolTip("Enter the fractional number") 
					
		extrusion_checks_list.append(eR_chck)	
		extrusion_values_list.append(eR_val)	
		extrusion_val_pr_list.append(eR_val_pr)
		extrusion_val_def_list.append(eR_val_def)
		
		#direction
		d_val_list = []
		d_chck = QtGui.QCheckBox()
		d_chck_hbox = QtGui.QHBoxLayout()
		d_chck_hbox.setContentsMargins(0, 0, 0, 0)
		d_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
		d_chck_hbox.addWidget(d_chck)
		d_chck_cell_widget = QtGui.QWidget()
		d_chck_cell_widget.setLayout(d_chck_hbox)
		extr_table.setCellWidget(5, 0, d_chck_cell_widget)
		d_val_pr = QtGui.QLabel()
		d_val_pr.setEnabled(False)
		d_val_pr.setText('direction')
		extr_table.setCellWidget(5, 1, d_val_pr)
		d_val_def = QtGui.QLabel()
		d_val_def.setEnabled(False)
		extr_table.setCellWidget(5, 2, d_val_def)
		d_x_lbl = QtGui.QLabel('x:')
		d_x_lbl.setEnabled(False)
		d_val_x = QtGui.QDoubleSpinBox()
		d_val_x.setEnabled(False)
		d_val_x.setFixedSize(70, 25)
		d_y_lbl = QtGui.QLabel('y:')
		d_y_lbl.setEnabled(False)
		d_val_y = QtGui.QDoubleSpinBox()
		d_val_y.setEnabled(False)
		d_val_y.setFixedSize(70, 25)
		d_z_lbl = QtGui.QLabel('z:')
		d_z_lbl.setEnabled(False)
		d_val_z = QtGui.QDoubleSpinBox()
		d_val_z.setEnabled(False)
		d_val_z.setFixedSize(70, 25)
		d_val_hbox = QtGui.QHBoxLayout()
		d_val_hbox.setContentsMargins(0, 0, 0, 0)
		d_val_hbox.addWidget(d_x_lbl)
		d_val_hbox.addWidget(d_val_x)
		d_val_hbox.addWidget(d_y_lbl)
		d_val_hbox.addWidget(d_val_y)
		d_val_hbox.addWidget(d_z_lbl)
		d_val_hbox.addWidget(d_val_z)
		d_val_cell_widget = QtGui.QWidget()
		d_val_cell_widget.setLayout(d_val_hbox)
		extr_table.setCellWidget(5, 3, d_val_cell_widget)
		if int_lng == 'Russian':
			d_val_def.setText("Направление")
			d_val_x.setToolTip("Введите вектор целых или дробных чисел") 
			d_val_y.setToolTip("Введите вектор целых или дробных чисел") 
			d_val_z.setToolTip("Введите вектор целых или дробных чисел") 
		elif int_lng == 'English':
			d_val_def.setText("Direction")
			d_val_x.setToolTip("Enter the vector of integer or fractional numbers") 
			d_val_y.setToolTip("Enter the vector of integer or fractional numbers") 
			d_val_z.setToolTip("Enter the vector of integer or fractional numbers") 
		
		d_val_list.append(d_x_lbl)
		d_val_list.append(d_y_lbl)
		d_val_list.append(d_z_lbl)
		d_val_list.append(d_val_x)
		d_val_list.append(d_val_y)
		d_val_list.append(d_val_z)
			
		extrusion_checks_list.append(d_chck)	
		extrusion_values_list.append(d_val_list)
		extrusion_val_pr_list.append(d_val_pr)
		extrusion_val_def_list.append(d_val_def)
		
		if extrusion_obj != None:
			d_chck.setChecked(extrusion_obj['d_chck'])
			if extrusion_obj['d_chck'] == True:
				d_val_pr.setEnabled(True)
				d_val_def.setEnabled(True)
				d_x_lbl.setEnabled(True)
				d_val_x.setEnabled(True)
				
				d_y_lbl.setEnabled(True)
				d_val_y.setEnabled(True)
				
				d_z_lbl.setEnabled(True)
				d_val_z.setEnabled(True)
				
				d_val_x.setValue(extrusion_obj['d_val'][0])
				d_val_y.setValue(extrusion_obj['d_val'][1])
				d_val_z.setValue(extrusion_obj['d_val'][2])
			
		
		#thickness
		t_chck = QtGui.QCheckBox()
		t_chck_hbox = QtGui.QHBoxLayout()
		t_chck_hbox.setContentsMargins(0, 0, 0, 0)
		t_chck_hbox.setAlignment(QtCore.Qt.AlignCenter)
		t_chck_hbox.addWidget(t_chck)
		t_chck_cell_widget = QtGui.QWidget()
		t_chck_cell_widget.setLayout(t_chck_hbox)
		extr_table.setCellWidget(6, 0, t_chck_cell_widget)
		t_val_pr = QtGui.QLabel()
		t_val_pr.setEnabled(False)
		t_val_pr.setText('thickness')
		extr_table.setCellWidget(6, 1, t_val_pr)
		t_val_def = QtGui.QLabel()
		t_val_def.setEnabled(False)
		extr_table.setCellWidget(6, 2, t_val_def)
		t_val = QtGui.QDoubleSpinBox()
		t_val.setEnabled(False)
		t_val.setFixedSize(70, 25)
		t_val_hbox = QtGui.QHBoxLayout()
		t_val_hbox.setContentsMargins(0, 0, 0, 0)
		t_val_hbox.addWidget(t_val)
		t_val_cell_widget = QtGui.QWidget()
		t_val_cell_widget.setLayout(t_val_hbox)
		extr_table.setCellWidget(6, 3, t_val_cell_widget)
		if int_lng == 'Russian':
			t_val_def.setText("Толщина")
			t_val.setToolTip("Введите целое или дробное число") 
		elif int_lng == 'English':
			t_val_def.setText("Thickness")
			t_val.setToolTip("Enter the integer or fractional number") 
		
		extrusion_checks_list.append(t_chck)	
		extrusion_values_list.append(t_val)
		extrusion_val_pr_list.append(t_val_pr)
		extrusion_val_def_list.append(t_val_def)
		
		if extrusion_obj != None:
			t_chck.setChecked(extrusion_obj['t_chck'])
			if extrusion_obj['t_chck'] == True:
				t_val_pr.setEnabled(True)
				t_val_def.setEnabled(True)
				t_val.setEnabled(True)
				t_val.setValue(extrusion_obj['t_val'])
		
		#axisPt
		axisPt_list = []
		aPt_val_pr = QtGui.QLabel()
		aPt_val_pr.setText('axisPt')
		extr_table.setCellWidget(7, 1, aPt_val_pr)
		aPt_val_def = QtGui.QLabel()
		extr_table.setCellWidget(7, 2, aPt_val_def)
		aPt_x_lbl = QtGui.QLabel('x:')
		aPt_val_x = QtGui.QDoubleSpinBox()
		aPt_val_x.setFixedSize(70, 25)
		aPt_y_lbl = QtGui.QLabel('y:')
		aPt_val_y = QtGui.QDoubleSpinBox()
		aPt_val_y.setFixedSize(70, 25)
		aPt_z_lbl = QtGui.QLabel('z:')
		aPt_val_z = QtGui.QDoubleSpinBox()
		aPt_val_z.setFixedSize(70, 25)
		aPt_val_hbox = QtGui.QHBoxLayout()
		aPt_val_hbox.setContentsMargins(0, 0, 0, 0)
		aPt_val_hbox.addWidget(aPt_x_lbl)
		aPt_val_hbox.addWidget(aPt_val_x)
		aPt_val_hbox.addWidget(aPt_y_lbl)
		aPt_val_hbox.addWidget(aPt_val_y)
		aPt_val_hbox.addWidget(aPt_z_lbl)
		aPt_val_hbox.addWidget(aPt_val_z)
		aPt_val_cell_widget = QtGui.QWidget()
		aPt_val_cell_widget.setLayout(aPt_val_hbox)
		extr_table.setCellWidget(7, 3, aPt_val_cell_widget)
		if int_lng == 'Russian':
			aPt_val_def.setText("Параметры оси Pt")
			aPt_val_x.setToolTip("Введите вектор целых или дробных чисел") 
			aPt_val_y.setToolTip("Введите вектор целых или дробных чисел") 
			aPt_val_z.setToolTip("Введите вектор целых или дробных чисел") 
		elif int_lng == 'English':
			aPt_val_def.setText("Parameters of Pt axis")
			aPt_val_x.setToolTip("Enter the vector of integer or fractional numbers") 
			aPt_val_y.setToolTip("Enter the vector of integer or fractional numbers") 
			aPt_val_z.setToolTip("Enter the vector of integer or fractional numbers") 
					
		axisPt_list.append(aPt_val_x)
		axisPt_list.append(aPt_val_y)
		axisPt_list.append(aPt_val_z)
		
		if extrusion_obj != None:
			aPt_val_x.setValue(extrusion_obj['axisPt'][0])
			aPt_val_y.setValue(extrusion_obj['axisPt'][1])
			aPt_val_z.setValue(extrusion_obj['axisPt'][2])
		
		#axis
		a_list = []
		a_val_pr = QtGui.QLabel()
		a_val_pr.setText('axis')
		extr_table.setCellWidget(8, 1, a_val_pr)
		a_val_def = QtGui.QLabel()
		extr_table.setCellWidget(8, 2, a_val_def)
		a_x_lbl = QtGui.QLabel('x:')
		a_val_x = QtGui.QDoubleSpinBox()
		a_val_x.setFixedSize(70, 25)
		a_y_lbl = QtGui.QLabel('y:')
		a_val_y = QtGui.QDoubleSpinBox()
		a_val_y.setFixedSize(70, 25)
		a_z_lbl = QtGui.QLabel('z:')
		a_val_z = QtGui.QDoubleSpinBox()
		a_val_z.setFixedSize(70, 25)
		a_val_hbox = QtGui.QHBoxLayout()
		a_val_hbox.setContentsMargins(0, 0, 0, 0)
		a_val_hbox.addWidget(a_x_lbl)
		a_val_hbox.addWidget(a_val_x)
		a_val_hbox.addWidget(a_y_lbl)
		a_val_hbox.addWidget(a_val_y)
		a_val_hbox.addWidget(a_z_lbl)
		a_val_hbox.addWidget(a_val_z)
		a_val_cell_widget = QtGui.QWidget()
		a_val_cell_widget.setLayout(a_val_hbox)
		extr_table.setCellWidget(8, 3, a_val_cell_widget)
		if int_lng == 'Russian':
			a_val_def.setText("Параметры базовой оси")
			a_val_x.setToolTip("Введите вектор целых или дробных чисел") 
			a_val_y.setToolTip("Введите вектор целых или дробных чисел") 
			a_val_z.setToolTip("Введите вектор целых или дробных чисел") 
		elif int_lng == 'English':
			a_val_def.setText("Parameters of base axis")
			a_val_x.setToolTip("Enter the vector of integer or fractional numbers") 
			a_val_y.setToolTip("Enter the vector of integer or fractional numbers") 
			a_val_z.setToolTip("Enter the vector of integer or fractional numbers") 
					
		a_list.append(a_val_x)
		a_list.append(a_val_y)
		a_list.append(a_val_z)
		
		if extrusion_obj != None:
			a_val_x.setValue(extrusion_obj['a'][0])
			a_val_y.setValue(extrusion_obj['a'][1])
			a_val_z.setValue(extrusion_obj['a'][2])
				
		#angle
		ang_val_pr = QtGui.QLabel()
		ang_val_pr.setText('angle')
		extr_table.setCellWidget(9, 1, ang_val_pr)
		ang_val_def = QtGui.QLabel()
		extr_table.setCellWidget(9, 2, ang_val_def)
		ang_val = QtGui.QDoubleSpinBox()
		ang_val.setFixedSize(70, 25)
		ang_val_hbox = QtGui.QHBoxLayout()
		ang_val_hbox.setContentsMargins(0, 0, 0, 0)
		ang_val_hbox.addWidget(ang_val)
		ang_val_cell_widget = QtGui.QWidget()
		ang_val_cell_widget.setLayout(ang_val_hbox)
		extr_table.setCellWidget(9, 3, ang_val_cell_widget)
		if int_lng == 'Russian':
			ang_val_def.setText("Величина угла")
			ang_val.setToolTip("Введите целое число") 
		elif int_lng == 'English':
			ang_val_def.setText("Angle value")
			ang_val.setToolTip("Enter the integer number") 
		
		if extrusion_obj != None:
			ang_val.setValue(extrusion_obj['ang'])
		
		prs_grid.addWidget(extr_table, 0, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

		extrusion_btnSave = QtGui.QPushButton()
		extrusion_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(extrusion_btnSave)
		if int_lng == 'Russian':
			extrusion_btnSave.setText("Записать")
		elif int_lng == 'English':
			extrusion_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		extrusion_grid = QtGui.QGridLayout()
		extrusion_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		extrusion_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		extrusion_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		extrusion_grid.setRowStretch(3, 6)
		extrusion_group = QtGui.QGroupBox()
		extrusion_group.setLayout(extrusion_grid)
		return extrusion_group, extrusion_btnSave, e_edit, eM_edit, pT_edit, extrusion_checks_list, extrusion_values_list, extrusion_val_pr_list, extrusion_val_def_list, axisPt_list, a_list, ang_val
	
