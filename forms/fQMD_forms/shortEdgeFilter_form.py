# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class shortEdgeFilter_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, shortEdgeFilter_visible): 
		shortEdgeFilter_obj = None
		
		#----------------Если файл shortEdgeFilter_.pkl существует, получаем данные из него для вывода в форму---------------#

		if shortEdgeFilter_visible == True:
			shortEdgeFilter_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'shortEdgeFilter.pkl'
			if os.path.exists(shortEdgeFilter_path_file):
		
				input = open(shortEdgeFilter_path_file, 'rb')
				shortEdgeFilter_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла shortEdgeFilter.pkl на основе данных файла initial.pkl-------------#
		
		prs_grid = QtGui.QGridLayout()
		prs_frame = QtGui.QFrame()
		prs_frame.setLayout(prs_grid)
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Блок указания свойств короткого краевого фильтра")
		elif int_lng == 'English':
			main_lbl.setText("Block indicating the properties of the short edge filter")
		
		sEF_table = QtGui.QTableWidget()
		sEF_table.setFixedSize(705, 90)
		sEF_table.setRowCount(2)
		sEF_table.setColumnCount(3)
		sEF_table.verticalHeader().hide()

		sEF_table.horizontalHeader().resizeSection(0, 155)
		sEF_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
		column_1 = QtGui.QTableWidgetItem()
		sEF_table.setHorizontalHeaderItem(0, column_1)
		sEF_table.horizontalHeader().setStyleSheet("color: steelblue")

		sEF_table.horizontalHeader().resizeSection(1, 395)
		sEF_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
		column_2 = QtGui.QTableWidgetItem()
		sEF_table.setHorizontalHeaderItem(1, column_2)
		sEF_table.horizontalHeader().setStyleSheet("color: steelblue")
		
		sEF_table.horizontalHeader().resizeSection(2, 150)
		sEF_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
		column_3 = QtGui.QTableWidgetItem()
		sEF_table.setHorizontalHeaderItem(2, column_3)
		sEF_table.horizontalHeader().setStyleSheet("color: steelblue")
				
		if int_lng == 'Russian':
			column_1.setText("Параметр")
			column_2.setText("Описание")	
			column_3.setText("Значение")
		elif int_lng == 'English':
			column_1.setText("Parameter")
			column_2.setText("Definition")	
			column_3.setText("Value")
				
		#shortEdgeFilterFactor#		
		sEFF_val_pr = QtGui.QLabel()
		sEFF_val_pr.setText('shortEdgeFilterFactor')
		sEF_table.setCellWidget(0, 0, sEFF_val_pr)
		sEFF_val_def = QtGui.QLabel()
		sEF_table.setCellWidget(0, 1, sEFF_val_def)
		sEFF_val = QtGui.QDoubleSpinBox()
		sEFF_val.setFixedSize(100, 25)
		sEFF_val_hbox = QtGui.QHBoxLayout()
		sEFF_val_hbox.setContentsMargins(0, 0, 0, 0)
		sEFF_val_hbox.addWidget(sEFF_val)
		sEFF_val_cell_widget = QtGui.QWidget()
		sEFF_val_cell_widget.setLayout(sEFF_val_hbox)
		sEF_table.setCellWidget(0, 2, sEFF_val_cell_widget)
		if int_lng == 'Russian':
			sEFF_val_def.setText("Фактор умножения среднего значения на длину ребра")
			sEFF_val.setToolTip("Введите число двойной точности") 
		elif int_lng == 'English':
			sEFF_val_def.setText("The multiplication factor of the mean value by the length of the edge")
			sEFF_val.setToolTip("Enter the double-precision number") 
		if shortEdgeFilter_obj != None:
			sEFF_val.setValue(shortEdgeFilter_obj['sEFF'])
			
		#edgeAttachedToBoundaryFactor#		
		eATBF_val_pr = QtGui.QLabel()
		eATBF_val_pr.setText('edgeAttachedToBoundaryFactor')
		sEF_table.setCellWidget(1, 0, eATBF_val_pr)
		eATBF_val_def = QtGui.QLabel()
		sEF_table.setCellWidget(1, 1, eATBF_val_def)
		eATBF_val = QtGui.QDoubleSpinBox()
		eATBF_val.setFixedSize(100, 25)
		eATBF_val_hbox = QtGui.QHBoxLayout()
		eATBF_val_hbox.setContentsMargins(0, 0, 0, 0)
		eATBF_val_hbox.addWidget(eATBF_val)
		eATBF_val_cell_widget = QtGui.QWidget()
		eATBF_val_cell_widget.setLayout(eATBF_val_hbox)
		sEF_table.setCellWidget(1, 2, eATBF_val_cell_widget)
		if int_lng == 'Russian':
			eATBF_val_def.setText("Взвешенное значение для длин ребер, прикрепл. к границам")
			eATBF_val.setToolTip("Введите число двойной точности") 
		elif int_lng == 'English':
			eATBF_val_def.setText("Weighted value for the lengths of edges attached to the boundaries")
			eATBF_val.setToolTip("Enter the double-precision number") 
		if shortEdgeFilter_obj != None:
			eATBF_val.setValue(shortEdgeFilter_obj['eATBF'])
				
		prs_grid.addWidget(sEF_table, 0, 0, alignment=QtCore.Qt.AlignCenter)

		# -------------------------Кнопка сохранения --------------------------#

		shortEdgeFilter_btnSave = QtGui.QPushButton()
		shortEdgeFilter_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(shortEdgeFilter_btnSave)
		if int_lng == 'Russian':
			shortEdgeFilter_btnSave.setText("Записать")
		elif int_lng == 'English':
			shortEdgeFilter_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		shortEdgeFilter_grid = QtGui.QGridLayout()
		shortEdgeFilter_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
		shortEdgeFilter_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
		shortEdgeFilter_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		shortEdgeFilter_grid.setRowStretch(3, 6)
		shortEdgeFilter_group = QtGui.QGroupBox()
		shortEdgeFilter_group.setLayout(shortEdgeFilter_grid)
		return shortEdgeFilter_group, shortEdgeFilter_btnSave, sEFF_val, eATBF_val

