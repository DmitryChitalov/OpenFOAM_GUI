# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class layers_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, layers_visible): 
		layers_obj = None
		
		#----------------Если файл layers.pkl существует, получаем данные из него для вывода в форму---------------#

		if layers_visible == True:
			layers_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'layers.pkl'
			if os.path.exists(layers_path_file):
		
				input = open(layers_path_file, 'rb')
				layers_obj = pickle.load(input)
				input.close()
		
		#---------------Формируем внешний вид формы для файла layers.pkl на основе данных файла initial.pkl-------------#
		
		main_lbl = QtGui.QLabel()
		if int_lng == 'Russian':
			main_lbl.setText("Управление слоями")
		elif int_lng == 'English':
			main_lbl.setText("Layers control")
			
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'

		if os.path.exists(initial_path_file):
	
			input = open(initial_path_file, 'rb')
			obj_initial = pickle.load(input)
			input.close()
			
			prs_grid = QtGui.QGridLayout()
			
			###########################################Базовые параметры###################################################
			
			layers_prs_base_lbl = QtGui.QLabel()
			if int_lng == 'Russian':
				layers_prs_base_lbl.setText("Базовые параметры слоев:")
			elif int_lng == 'English':
				layers_prs_base_lbl.setText("Base layers parameters:")
			prs_grid.addWidget(layers_prs_base_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			
			layers_prs_base_table = QtGui.QTableWidget()
			
			layers_prs_base_table.setRowCount(obj_initial['l'])
			layers_prs_base_table.setColumnCount(2)
			layers_prs_base_table.verticalHeader().hide()

			layers_prs_base_table.horizontalHeader().resizeSection(0, 150)
			layers_prs_base_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
			column_1 = QtGui.QTableWidgetItem()
			layers_prs_base_table.setHorizontalHeaderItem(0, column_1)
			layers_prs_base_table.horizontalHeader().setStyleSheet("color: steelblue")

			layers_prs_base_table.horizontalHeader().resizeSection(1, 120)
			layers_prs_base_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
			column_2 = QtGui.QTableWidgetItem()
			layers_prs_base_table.setHorizontalHeaderItem(1, column_2)
			layers_prs_base_table.horizontalHeader().setStyleSheet("color: steelblue")
			
			if int_lng == 'Russian':
				column_1.setText("Название слоя")
				column_2.setText("Количество")	
			elif int_lng == 'English':
				column_1.setText("Layer name")
				column_2.setText("Number")	
				
			i = 1
			k = 0
			height = 60
			while i <= obj_initial['l']:
				layers_prs_base_table.setFixedSize(277, height)
				#layer#
				layer_edit = QtGui.QLineEdit()
				layer_edit.setFixedSize(120, 25)
				layer_hbox = QtGui.QHBoxLayout()
				layer_hbox.setContentsMargins(0, 0, 0, 0)
				layer_hbox.addWidget(layer_edit)
				layer_cell_widget = QtGui.QWidget()
				layer_cell_widget.setLayout(layer_hbox)
				if layers_obj != None:
					layer_edit.setText(layers_obj['layers_base'][k]['layer_' + str(i)])
				
				#nSurfaceLayers
				sSL_val = QtGui.QSpinBox()
				sSL_val.setFixedSize(70, 25)
				sSL_val.setRange(1, 1000)
				sSL_val_hbox = QtGui.QHBoxLayout()
				sSL_val_hbox.setContentsMargins(0, 0, 0, 0)
				sSL_val_hbox.addWidget(sSL_val)
				sSL_val_cell_widget = QtGui.QWidget()
				sSL_val_cell_widget.setLayout(sSL_val_hbox)
				if layers_obj != None:
					sSL_val.setValue(layers_obj['layers_base'][k]['layer_val_' + str(i)])

				layers_prs_base_table.setCellWidget(k, 0, layer_cell_widget)
				layers_prs_base_table.setCellWidget(k, 1, sSL_val_cell_widget)
				
				height = height + 30
				k = k + 1
				i = i + 1
			
			prs_grid.addWidget(layers_prs_base_table, 1, 0, alignment=QtCore.Qt.AlignCenter)
			
			##################################Дополнительные параметры#########################################
			layers_prs_add_lbl = QtGui.QLabel()
			if int_lng == 'Russian':
				layers_prs_add_lbl.setText("Дополнительные параметры слоев:")
			elif int_lng == 'English':
				layers_prs_add_lbl.setText("Additional layers parameters:")
			prs_grid.addWidget(layers_prs_add_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
			
			layers_prs_add_table = QtGui.QTableWidget()
			layers_prs_add_table.setFixedSize(695, 460)
			layers_prs_add_table.setRowCount(16)
			layers_prs_add_table.setColumnCount(3)
			layers_prs_add_table.verticalHeader().hide()

			layers_prs_add_table.horizontalHeader().resizeSection(0, 150)
			layers_prs_add_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
			column_3 = QtGui.QTableWidgetItem()
			layers_prs_add_table.setHorizontalHeaderItem(0, column_3)
			layers_prs_add_table.horizontalHeader().setStyleSheet("color: steelblue")

			layers_prs_add_table.horizontalHeader().resizeSection(1, 430)
			layers_prs_add_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
			column_4 = QtGui.QTableWidgetItem()
			layers_prs_add_table.setHorizontalHeaderItem(1, column_4)
			layers_prs_add_table.horizontalHeader().setStyleSheet("color: steelblue")
			
			layers_prs_add_table.horizontalHeader().resizeSection(2, 100)
			layers_prs_add_table.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
			column_5 = QtGui.QTableWidgetItem()
			layers_prs_add_table.setHorizontalHeaderItem(2, column_5)
			layers_prs_add_table.horizontalHeader().setStyleSheet("color: steelblue")
			
			if int_lng == 'Russian':
				column_3.setText("Параметр")
				column_4.setText("Описание")	
				column_5.setText("Значение")
			elif int_lng == 'English':
				column_3.setText("Parameter")
				column_4.setText("Definition")	
				column_5.setText("Value")
			
			#1)finalLayerThickness
			fLT_val_pr = QtGui.QLabel()
			fLT_val_pr.setText('finalLayerThickness')
			layers_prs_add_table.setCellWidget(0, 0, fLT_val_pr)
			fLT_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(0, 1, fLT_val_def)
			fLT_val = QtGui.QDoubleSpinBox()
			fLT_val.setFixedSize(70, 25)
			fLT_val_hbox = QtGui.QHBoxLayout()
			fLT_val_hbox.setContentsMargins(0, 0, 0, 0)
			fLT_val_hbox.addWidget(fLT_val)
			fLT_val_cell_widget = QtGui.QWidget()
			fLT_val_cell_widget.setLayout(fLT_val_hbox)
			layers_prs_add_table.setCellWidget(0, 2, fLT_val_cell_widget)
			if int_lng == 'Russian':
				fLT_val_def.setText("Толщина конечного слоя добавленной ячейки")
			elif int_lng == 'English':
				fLT_val_def.setText("Thickness of the final layer of the added cell")
			if layers_obj != None:
				fLT_val.setValue(layers_obj['layers_add']['finalLayerThickness'])
				
			#2)expansionRatio
			eR_val_pr = QtGui.QLabel()
			eR_val_pr.setText('expansionRatio')
			layers_prs_add_table.setCellWidget(1, 0, eR_val_pr)
			eR_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(1, 1, eR_val_def)
			eR_val = QtGui.QDoubleSpinBox()
			eR_val.setFixedSize(70, 25)
			eR_val_hbox = QtGui.QHBoxLayout()
			eR_val_hbox.setContentsMargins(0, 0, 0, 0)
			eR_val_hbox.addWidget(eR_val)
			eR_val_cell_widget = QtGui.QWidget()
			eR_val_cell_widget.setLayout(eR_val_hbox)
			layers_prs_add_table.setCellWidget(1, 2, eR_val_cell_widget)
			if int_lng == 'Russian':
				eR_val_def.setText("Коэффициент расширения для слоя")
			elif int_lng == 'English':
				eR_val_def.setText("Expansion factor for layer mesh")
			if layers_obj != None:
				eR_val.setValue(layers_obj['layers_add']['expansionRatio'])
				
			#3)minThickness
			mT_val_pr = QtGui.QLabel()
			mT_val_pr.setText('minThickness')
			layers_prs_add_table.setCellWidget(2, 0, mT_val_pr)
			mT_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(2, 1, mT_val_def)
			mT_val = QtGui.QDoubleSpinBox()
			mT_val.setFixedSize(70, 25)
			mT_val_hbox = QtGui.QHBoxLayout()
			mT_val_hbox.setContentsMargins(0, 0, 0, 0)
			mT_val_hbox.addWidget(mT_val)
			mT_val_cell_widget = QtGui.QWidget()
			mT_val_cell_widget.setLayout(mT_val_hbox)
			layers_prs_add_table.setCellWidget(2, 2, mT_val_cell_widget)
			if int_lng == 'Russian':
				mT_val_def.setText("Минимальная толщина клеточного слоя")
			elif int_lng == 'English':
				mT_val_def.setText("The minimum thickness of the cell layer")
			if layers_obj != None:
				mT_val.setValue(layers_obj['layers_add']['minThickness'])
			
			#4)relativeSizes
			rS_val_pr = QtGui.QLabel()
			rS_val_pr.setText('relativeSizes')
			layers_prs_add_table.setCellWidget(3, 0, rS_val_pr)
			rS_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(3, 1, rS_val_def)
			rS_val = QtGui.QComboBox()
			rS_val.setFixedSize(70, 25)
			rS_val_list = ['true', 'false']
			rS_val.addItems(rS_val_list)
			rS_val_hbox = QtGui.QHBoxLayout()
			rS_val_hbox.setContentsMargins(0, 0, 0, 0)
			rS_val_hbox.addWidget(rS_val)
			rS_val_cell_widget = QtGui.QWidget()
			rS_val_cell_widget.setLayout(rS_val_hbox)
			layers_prs_add_table.setCellWidget(3, 2, rS_val_cell_widget)
			if int_lng == 'Russian':
				rS_val_def.setText("Установить относительные размеры ячеек")
			elif int_lng == 'English':
				rS_val_def.setText("Set the relative sizes of cells")
			if layers_obj != None:
				rS_val_mas = rS_val.count()  
				for t in range(rS_val_mas):
					if rS_val.itemText(t) == layers_obj['layers_add']['relativeSizes']:
						rS_val.setCurrentIndex(t)
			
			#5)featureAngle
			fA_val_pr = QtGui.QLabel()
			fA_val_pr.setText('featureAngle')
			layers_prs_add_table.setCellWidget(4, 0, fA_val_pr)
			fA_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(4, 1, fA_val_def)
			fA_val = QtGui.QSpinBox()
			fA_val.setFixedSize(70, 25)
			fA_val_hbox = QtGui.QHBoxLayout()
			fA_val_hbox.setContentsMargins(0, 0, 0, 0)
			fA_val_hbox.addWidget(fA_val)
			fA_val_cell_widget = QtGui.QWidget()
			fA_val_cell_widget.setLayout(fA_val_hbox)
			layers_prs_add_table.setCellWidget(4, 2, fA_val_cell_widget)
			if int_lng == 'Russian':
				fA_val_def.setText("Угол обзора")
			elif int_lng == 'English':
				fA_val_def.setText("Viewing Angle")
			if layers_obj != None:
				fA_val.setValue(layers_obj['layers_add']['featureAngle'])
				
			#6)nSmoothSurfaceNormals
			nSSN_val_pr = QtGui.QLabel()
			nSSN_val_pr.setText('nSmoothSurfaceNormals')
			layers_prs_add_table.setCellWidget(5, 0, nSSN_val_pr)
			nSSN_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(5, 1, nSSN_val_def)
			nSSN_val = QtGui.QSpinBox()
			nSSN_val.setFixedSize(70, 25)
			nSSN_val_hbox = QtGui.QHBoxLayout()
			nSSN_val_hbox.setContentsMargins(0, 0, 0, 0)
			nSSN_val_hbox.addWidget(nSSN_val)
			nSSN_val_cell_widget = QtGui.QWidget()
			nSSN_val_cell_widget.setLayout(nSSN_val_hbox)
			layers_prs_add_table.setCellWidget(5, 2, nSSN_val_cell_widget)
			if int_lng == 'Russian':
				nSSN_val_def.setText("Число сглаживающих итераций поверхностных нормалей")
			elif int_lng == 'English':
				nSSN_val_def.setText("Number of smoothing iterations of surface normals")
			if layers_obj != None:
				nSSN_val.setValue(layers_obj['layers_add']['nSmoothSurfaceNormals'])
				
			#7)nSmoothNormals
			nSN_val_pr = QtGui.QLabel()
			nSN_val_pr.setText('nSmoothNormals')
			layers_prs_add_table.setCellWidget(6, 0, nSN_val_pr)
			nSN_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(6, 1, nSN_val_def)
			nSN_val = QtGui.QSpinBox()
			nSN_val.setFixedSize(70, 25)
			nSN_val_hbox = QtGui.QHBoxLayout()
			nSN_val_hbox.setContentsMargins(0, 0, 0, 0)
			nSN_val_hbox.addWidget(nSN_val)
			nSN_val_cell_widget = QtGui.QWidget()
			nSN_val_cell_widget.setLayout(nSN_val_hbox)
			layers_prs_add_table.setCellWidget(6, 2, nSN_val_cell_widget)
			if int_lng == 'Russian':
				nSN_val_def.setText("Количество сглаживающих итераций напр. движ. внутренней сетки")
			elif int_lng == 'English':
				nSN_val_def.setText("Number of smoothing iterations of interior mesh movement direction")
			if layers_obj != None:
				nSN_val.setValue(layers_obj['layers_add']['nSmoothNormals'])
			
			#8)nSmoothThickness
			nST_val_pr = QtGui.QLabel()
			nST_val_pr.setText('nSmoothThickness')
			layers_prs_add_table.setCellWidget(7, 0, nST_val_pr)
			nST_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(7, 1, nST_val_def)
			nST_val = QtGui.QSpinBox()
			nST_val.setFixedSize(70, 25)
			nST_val_hbox = QtGui.QHBoxLayout()
			nST_val_hbox.setContentsMargins(0, 0, 0, 0)
			nST_val_hbox.addWidget(nST_val)
			nST_val_cell_widget = QtGui.QWidget()
			nST_val_cell_widget.setLayout(nST_val_hbox)
			layers_prs_add_table.setCellWidget(7, 2, nST_val_cell_widget)
			if int_lng == 'Russian':
				nST_val_def.setText("Толщина слоя над поверхностными патчами")
			elif int_lng == 'English':
				nST_val_def.setText("Layer thickness over surface patches")
			if layers_obj != None:
				nST_val.setValue(layers_obj['layers_add']['nSmoothThickness'])
				
			#9)minMedianAxisAngle
			mMAA_val_pr = QtGui.QLabel()
			mMAA_val_pr.setText('minMedianAxisAngle')
			layers_prs_add_table.setCellWidget(8, 0, mMAA_val_pr)
			mMAA_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(8, 1, mMAA_val_def)
			mMAA_val = QtGui.QSpinBox()
			mMAA_val.setFixedSize(70, 25)
			mMAA_val_hbox = QtGui.QHBoxLayout()
			mMAA_val_hbox.setContentsMargins(0, 0, 0, 0)
			mMAA_val_hbox.addWidget(mMAA_val)
			mMAA_val_cell_widget = QtGui.QWidget()
			mMAA_val_cell_widget.setLayout(mMAA_val_hbox)
			layers_prs_add_table.setCellWidget(8, 2, mMAA_val_cell_widget)
			if int_lng == 'Russian':
				mMAA_val_def.setText("Угол, используемый для получения точек медиальной оси")
			elif int_lng == 'English':
				mMAA_val_def.setText("Angle used to pick up medial axis points")
			if layers_obj != None:
				mMAA_val.setValue(layers_obj['layers_add']['minMedianAxisAngle'])
				
			#10)maxThicknessToMedialRatio
			mTTMR_val_pr = QtGui.QLabel()
			mTTMR_val_pr.setText('maxThicknessToMedialRatio')
			layers_prs_add_table.setCellWidget(9, 0, mTTMR_val_pr)
			mTTMR_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(9, 1, mTTMR_val_def)
			mTTMR_val = QtGui.QDoubleSpinBox()
			mTTMR_val.setFixedSize(70, 25)
			mTTMR_val_hbox = QtGui.QHBoxLayout()
			mTTMR_val_hbox.setContentsMargins(0, 0, 0, 0)
			mTTMR_val_hbox.addWidget(mTTMR_val)
			mTTMR_val_cell_widget = QtGui.QWidget()
			mTTMR_val_cell_widget.setLayout(mTTMR_val_hbox)
			layers_prs_add_table.setCellWidget(9, 2, mTTMR_val_cell_widget)
			if int_lng == 'Russian':
				mTTMR_val_def.setText("Максимальная толщина слоя к медиальному расстоянию")
			elif int_lng == 'English':
				mTTMR_val_def.setText("Maximum layer thickness to the medial distance")
			if layers_obj != None:
				mTTMR_val.setValue(layers_obj['layers_add']['maxThicknessToMedialRatio'])
				
			#11)maxFaceThicknessRatio
			mFTR_val_pr = QtGui.QLabel()
			mFTR_val_pr.setText('maxFaceThicknessRatio')
			layers_prs_add_table.setCellWidget(10, 0, mFTR_val_pr)
			mFTR_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(10, 1, mFTR_val_def)
			mFTR_val = QtGui.QDoubleSpinBox()
			mFTR_val.setFixedSize(70, 25)
			mFTR_val_hbox = QtGui.QHBoxLayout()
			mFTR_val_hbox.setContentsMargins(0, 0, 0, 0)
			mFTR_val_hbox.addWidget(mFTR_val)
			mFTR_val_cell_widget = QtGui.QWidget()
			mFTR_val_cell_widget.setLayout(mFTR_val_hbox)
			layers_prs_add_table.setCellWidget(10, 2, mFTR_val_cell_widget)
			if int_lng == 'Russian':
				mFTR_val_def.setText("Максимальный рост слоя на деформированных клетках")
			elif int_lng == 'English':
				mFTR_val_def.setText("Maximum growth of a layer on deformed cells")
			if layers_obj != None:
				mFTR_val.setValue(layers_obj['layers_add']['maxFaceThicknessRatio'])
				
			#12)nLayerIter
			nLI_val_pr = QtGui.QLabel()
			nLI_val_pr.setText('nLayerIter')
			layers_prs_add_table.setCellWidget(11, 0, nLI_val_pr)
			nLI_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(11, 1, nLI_val_def)
			nLI_val = QtGui.QSpinBox()
			nLI_val.setFixedSize(70, 25)
			nLI_val_hbox = QtGui.QHBoxLayout()
			nLI_val_hbox.setContentsMargins(0, 0, 0, 0)
			nLI_val_hbox.addWidget(nLI_val)
			nLI_val_cell_widget = QtGui.QWidget()
			nLI_val_cell_widget.setLayout(nLI_val_hbox)
			layers_prs_add_table.setCellWidget(11, 2, nLI_val_cell_widget)
			if int_lng == 'Russian':
				nLI_val_def.setText("Общее максимальное количество итераций добавления слоев")
			elif int_lng == 'English':
				nLI_val_def.setText("Overall max number of layer addition iterations")
			if layers_obj != None:
				nLI_val.setValue(layers_obj['layers_add']['nLayerIter'])
				
			#13)nRelaxedIter
			nRI_val_pr = QtGui.QLabel()
			nRI_val_pr.setText('nRelaxedIter')
			layers_prs_add_table.setCellWidget(12, 0, nRI_val_pr)
			nRI_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(12, 1, nRI_val_def)
			nRI_val = QtGui.QSpinBox()
			nRI_val.setFixedSize(70, 25)
			nRI_val_hbox = QtGui.QHBoxLayout()
			nRI_val_hbox.setContentsMargins(0, 0, 0, 0)
			nRI_val_hbox.addWidget(nRI_val)
			nRI_val_cell_widget = QtGui.QWidget()
			nRI_val_cell_widget.setLayout(nRI_val_hbox)
			layers_prs_add_table.setCellWidget(12, 2, nRI_val_cell_widget)
			if int_lng == 'Russian':
				nRI_val_def.setText("Макс. кол-во итераций, после которых применимы узлы meshQuality")
			elif int_lng == 'English':
				nRI_val_def.setText("Max number of iter-s after which relaxed meshQuality controls get used")
			if layers_obj != None:
				nRI_val.setValue(layers_obj['layers_add']['nRelaxedIter'])
			
			#14)nRelaxIter
			nRiter_val_pr = QtGui.QLabel()
			nRiter_val_pr.setText('nRelaxIter')
			layers_prs_add_table.setCellWidget(13, 0, nRiter_val_pr)
			nRiter_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(13, 1, nRiter_val_def)
			nRiter_val = QtGui.QSpinBox()
			nRiter_val.setFixedSize(70, 25)
			nRiter_val_hbox = QtGui.QHBoxLayout()
			nRiter_val_hbox.setContentsMargins(0, 0, 0, 0)
			nRiter_val_hbox.addWidget(nRiter_val)
			nRiter_val_cell_widget = QtGui.QWidget()
			nRiter_val_cell_widget.setLayout(nRiter_val_hbox)
			layers_prs_add_table.setCellWidget(13, 2, nRiter_val_cell_widget)
			if int_lng == 'Russian':
				nRiter_val_def.setText("Максимальное количество релаксационных итераций привязки")
			elif int_lng == 'English':
				nRiter_val_def.setText("Maximum number of snapping relaxation iterations")
			if layers_obj != None:
				nRiter_val.setValue(layers_obj['layers_add']['nRelaxIter'])
				
			#15)nGrow
			nG_val_pr = QtGui.QLabel()
			nG_val_pr.setText('nGrow')
			layers_prs_add_table.setCellWidget(14, 0, nG_val_pr)
			nG_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(14, 1, nG_val_def)
			nG_val = QtGui.QSpinBox()
			nG_val.setFixedSize(70, 25)
			nG_val_hbox = QtGui.QHBoxLayout()
			nG_val_hbox.setContentsMargins(0, 0, 0, 0)
			nG_val_hbox.addWidget(nG_val)
			nG_val_cell_widget = QtGui.QWidget()
			nG_val_cell_widget.setLayout(nG_val_hbox)
			layers_prs_add_table.setCellWidget(14, 2, nG_val_cell_widget)
			if int_lng == 'Russian':
				nG_val_def.setText("Конвергенция для слоя")
			elif int_lng == 'English':
				nG_val_def.setText("Convergence for the layer")
			if layers_obj != None:
				nG_val.setValue(layers_obj['layers_add']['nGrow'])
				
			#16)nBufferCellsNoExtrude
			nBCNE_val_pr = QtGui.QLabel()
			nBCNE_val_pr.setText('nBufferCellsNoExtrude')
			layers_prs_add_table.setCellWidget(15, 0, nBCNE_val_pr)
			nBCNE_val_def = QtGui.QLabel()
			layers_prs_add_table.setCellWidget(15, 1, nBCNE_val_def)
			nBCNE_val = QtGui.QSpinBox()
			nBCNE_val.setFixedSize(70, 25)
			nBCNE_val_hbox = QtGui.QHBoxLayout()
			nBCNE_val_hbox.setContentsMargins(0, 0, 0, 0)
			nBCNE_val_hbox.addWidget(nBCNE_val)
			nBCNE_val_cell_widget = QtGui.QWidget()
			nBCNE_val_cell_widget.setLayout(nBCNE_val_hbox)
			layers_prs_add_table.setCellWidget(15, 2, nBCNE_val_cell_widget)
			if int_lng == 'Russian':
				nBCNE_val_def.setText("Величина буферной области для завершения нового слоя")
			elif int_lng == 'English':
				nBCNE_val_def.setText("The value of the buffer area for completing a new layer")
			if layers_obj != None:
				nBCNE_val.setValue(layers_obj['layers_add']['nBufferCellsNoExtrude'])
			
			prs_grid.addWidget(layers_prs_add_table, 3, 0, alignment=QtCore.Qt.AlignCenter)
			
			prs_frame = QtGui.QFrame()
			prs_frame.setLayout(prs_grid)

			# -------------------------Кнопка сохранения --------------------------#

			layers_btnSave = QtGui.QPushButton()
			layers_btnSave.setFixedSize(80, 25)
			buttons_hbox = QtGui.QHBoxLayout()
			buttons_hbox.addWidget(layers_btnSave)
			if int_lng == 'Russian':
				layers_btnSave.setText("Записать")
			elif int_lng == 'English':
				layers_btnSave.setText("Write")

			# -----------------------Групповой элемент формы-----------------------#

			layers_grid = QtGui.QGridLayout()
			layers_grid.addWidget(main_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			layers_grid.addWidget(prs_frame, 1, 0, alignment=QtCore.Qt.AlignCenter)
			layers_grid.addLayout(buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
			layers_grid.setRowStretch(3, 6)
			layers_group = QtGui.QGroupBox()
			layers_group.setLayout(layers_grid)

			return layers_group, layers_btnSave, layers_prs_base_table, layers_prs_add_table
	

