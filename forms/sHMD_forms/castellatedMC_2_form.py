# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os

class castellatedMC_2_class():
	def out_frame_func(int_lng, prj_path, mesh_name_txt, pd_2, castellatedMC_visible): 
		castellatedMC_2_obj = None
		
		#----------------Если файл castellatedMC_2.pkl существует, получаем данные из него для вывода в форму---------------#
		
		prs_lvl_grid = QtGui.QGridLayout()
		prs_lvl_frame = QtGui.QFrame()
		prs_lvl_frame.setLayout(prs_lvl_grid)

		if castellatedMC_visible == True:
			castellatedMC_2_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_2.pkl'
			if os.path.exists(castellatedMC_2_path_file):
		
				input = open(castellatedMC_2_path_file, 'rb')
				castellatedMC_2_obj = pickle.load(input)
				input.close()
				
		castellatedMC_1_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_1.pkl'
		if os.path.exists(castellatedMC_1_path_file):
		
			input = open(castellatedMC_1_path_file, 'rb')
			castellatedMC_1_obj = pickle.load(input)
			input.close()
				
		initial_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path_file):
	
			input = open(initial_path_file, 'rb')
			obj_initial = pickle.load(input)
			input.close()
			
		geometry_2_path_file = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if os.path.exists(geometry_2_path_file):

			input = open(geometry_2_path_file, 'rb')
			obj_2_geometry = pickle.load(input)
			input.close()
			
			tri_distirbTri_list = []
			tri_distirbTri_geometry_list = []
			other_geometry_list = []
			other_geometry_list_geom = []
			i = 1			
			for el in obj_2_geometry:
				if el['geometry_' + str(i)] == 'Tri-surface' or el['geometry_' + str(i)] == 'Три-поверхность' or el['geometry_' + str(i)] == 'Distributed tri-surface' or el['geometry_' + str(i)] == 'Распределенная три-поверхность':
					tri_distirbTri_list.append(True)
					tri_distirbTri_geometry_list.append(el['file'])
					other_geometry_list.append(False)
					other_geometry_list_geom.append(el['file'])
				elif el['geometry_' + str(i)] == 'Base shape complex' or el['geometry_' + str(i)] == 'Набор базовых фигур':
					other_geometry_list_geom.append(el['name'])
					other_geometry_list.append(True)
				elif el['geometry_' + str(i)] == 'Base shape' or el['geometry_' + str(i)] == 'Базовая фигура':
					other_geometry_list_geom.append(el['shape'])
					other_geometry_list.append(True)
				i = i + 1
		
		f_level_single_list = []
		if obj_initial['f'] == True and True in tri_distirbTri_list:
		
		##-------------------------------------Первая таблица---------------------------------------------##
		
			cMC_f_lvl_lbl = QtGui.QLabel()	
			if int_lng == 'Russian':
				cMC_f_lvl_lbl.setText("Параметры уровней для ячеек при измельчении")
			elif int_lng == 'English':
				cMC_f_lvl_lbl.setText("Level parameters for cells in grinding")
				
			cMC_features_obj_list = castellatedMC_1_obj['features']

			f_level_multi_val_list = []
			el_CMC_f_list = []
			for el_CMC_f in cMC_features_obj_list:
				f_level_single = el_CMC_f['f_level_single']
				
				el_CMC_f_list.append(el_CMC_f['f_geometry'])
				
				if f_level_single == False:
					f_level_multi_val = el_CMC_f['f_level_multi_val']
					f_level_multi_val_list.append(f_level_multi_val)
					f_level_single_list.append(f_level_single)
				else:
					f_level_single_list.append(f_level_single)
					
			if False in f_level_single_list:
				max_val = max(f_level_multi_val_list)
			else:
				max_val = 1
				
			cMC_f_lvl_table = QtGui.QTableWidget()
			
			width = 150 + 250*max_val
			height = 30 + len(cMC_features_obj_list)*30

			cMC_f_lvl_table.setFixedSize(width, height)
			cMC_f_lvl_table.setRowCount(obj_initial['f_val'])
			if f_level_multi_val_list == []:
				cMC_f_lvl_table.setColumnCount(2)
			else:
				cMC_f_lvl_table.setColumnCount(max_val+1)
			cMC_f_lvl_table.verticalHeader().hide()

			cMC_f_lvl_table.horizontalHeader().resizeSection(0, 150)
			cMC_f_lvl_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
			column_1 = QtGui.QTableWidgetItem()
			cMC_f_lvl_table.setHorizontalHeaderItem(0, column_1)
			cMC_f_lvl_table.horizontalHeader().setStyleSheet("color: steelblue")
			
			if int_lng == 'Russian':
				column_1.setText("Три-поверхность")
			elif int_lng == 'English':
				column_1.setText("Tri-surface")
				
			q = 0

			for el_CMC_f in cMC_features_obj_list:
				#geometry#
				f_geometry_edit = QtGui.QComboBox()
				f_geometry_edit.setFixedSize(110, 25)
				f_geometry_edit.addItems(el_CMC_f_list)
				f_geometry_hbox = QtGui.QHBoxLayout()
				f_geometry_hbox.setContentsMargins(0, 0, 0, 0)
				f_geometry_hbox.addWidget(f_geometry_edit)
				f_geometry_cell_widget = QtGui.QWidget()
				f_geometry_cell_widget.setLayout(f_geometry_hbox)
				if castellatedMC_2_obj != None:
					f_geometry_edit_mas = f_geometry_edit.count()  
					for t in range(f_geometry_edit_mas):
						if f_geometry_edit.itemText(t) == castellatedMC_2_obj['CM_features_lvl'][q]['geometry']:
							f_geometry_edit.setCurrentIndex(t)
					
				cMC_f_lvl_table.setCellWidget(q, 0, f_geometry_cell_widget)
				#level#
				f_level_single = el_CMC_f['f_level_single']
				if f_level_single == True:
					
					f_level_single_val = QtGui.QSpinBox()
					if castellatedMC_2_obj != None:
						f_level_single_val.setValue(castellatedMC_2_obj['CM_features_lvl'][q]['lvl_prs']['lvl_single'])
					f_level_single_val.setFixedSize(50, 25)
					f_level_single_val.setRange(0, 1000)
					f_level_single_val_hbox = QtGui.QHBoxLayout()
					f_level_single_val_hbox.setContentsMargins(0, 0, 0, 0)

					f_level_single_val_hbox.addWidget(f_level_single_val)
					f_level_cell_widget = QtGui.QWidget()
					f_level_cell_widget.setLayout(f_level_single_val_hbox)
					
					cMC_f_lvl_table.horizontalHeader().resizeSection(1, 245)
					cMC_f_lvl_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
					column_2 = QtGui.QTableWidgetItem()
					cMC_f_lvl_table.setHorizontalHeaderItem(1, column_2)
					cMC_f_lvl_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					if int_lng == 'Russian':
						column_2.setText("Уровень_1")	
					elif int_lng == 'English':
						column_2.setText("Level_1")
					
					cMC_f_lvl_table.setCellWidget(q, 1, f_level_cell_widget)
					
				elif f_level_single == False:
					
					f_level_multi_val = el_CMC_f['f_level_multi_val']
					r = 1
					l = 0

					while r <= f_level_multi_val:
						
						flmv_min_lbl = QtGui.QLabel()
						flmv_min = QtGui.QSpinBox()
						flmv_min.setFixedSize(50, 25)
						flmv_min.setRange(0, 1000)
						if castellatedMC_2_obj != None:
							flmv_min.setValue(castellatedMC_2_obj['CM_features_lvl'][q]['multi_prs'][l]['lvl_multi_' + str(r)][0])
							
						flmv_max_lbl = QtGui.QLabel()
						flmv_max = QtGui.QSpinBox()
						flmv_max.setFixedSize(50, 25)
						flmv_max.setRange(0, 1000)
						if castellatedMC_2_obj != None:
							flmv_min.setValue(castellatedMC_2_obj['CM_features_lvl'][q]['multi_prs'][l]['lvl_multi_' + str(r)][1])
						
						cMC_f_lvl_table.horizontalHeader().resizeSection(r, 245)
						cMC_f_lvl_table.horizontalHeader().setResizeMode(r, QtGui.QHeaderView.Fixed)
						column_2 = QtGui.QTableWidgetItem()
						cMC_f_lvl_table.setHorizontalHeaderItem(r, column_2)
						cMC_f_lvl_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						if int_lng == 'Russian':
							column_2.setText("Уровень_" + str(r))	
						elif int_lng == 'English':
							column_2.setText("Level_" + str(r))
						
						if int_lng == 'Russian':
							flmv_min_lbl.setText("Мин_" + str(r) + ":")
							flmv_max_lbl.setText("Макс_" + str(r) + ":")
						elif int_lng == 'English':
							flmv_min_lbl.setText("Min_" + str(r) + ":")
							flmv_max_lbl.setText("Max_" + str(r) + ":")
							
						flmv_min_max_hbox = QtGui.QHBoxLayout()
						flmv_min_max_hbox.setContentsMargins(0, 0, 0, 0)

						flmv_min_max_hbox.addWidget(flmv_min_lbl)
						flmv_min_max_hbox.addWidget(flmv_min)
						flmv_min_max_hbox.addWidget(flmv_max_lbl)
						flmv_min_max_hbox.addWidget(flmv_max)
						flmv_min_max_cell_widget = QtGui.QWidget()
						flmv_min_max_cell_widget.setLayout(flmv_min_max_hbox)
						
						cMC_f_lvl_table.setCellWidget(q, r, flmv_min_max_cell_widget)

						r = r + 1
						l = l + 1

				q = q + 1

			prs_lvl_grid.addWidget(cMC_f_lvl_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
			prs_lvl_grid.addWidget(cMC_f_lvl_table, 1, 0, alignment=QtCore.Qt.AlignCenter)
		
		#--------------------------------------Вторая таблица-----------------------------------#		
		
		el_CMC_rS_regions_list = []
		if obj_initial['rS'] == True and True in tri_distirbTri_list:

			cMC_refinementSurfaces_obj_list = castellatedMC_1_obj['refinementSurfaces']

			el_CMC_rS_list = []
			
			for el_CMC_rS in cMC_refinementSurfaces_obj_list:
				el_CMC_rS_list.append(el_CMC_rS['rS_surface'])
				el_CMC_rS_regions_list.append(el_CMC_rS['rS_regions'])	
			if obj_initial['rS'] == True and True in el_CMC_rS_regions_list:
				cMC_rS_lvl_lbl = QtGui.QLabel()	
				if int_lng == 'Russian':
					cMC_rS_lvl_lbl.setText("Параметры уровней для поверхностей")
				elif int_lng == 'English':
					cMC_rS_lvl_lbl.setText("Level parameters for surfaces")

				#Определям макс длину массива
				rS_level_multi_val_list = []
				for el_CMC_f in cMC_refinementSurfaces_obj_list:
					rS_level = el_CMC_f['rS_regions']
					if rS_level == True:
						rS_level_val = el_CMC_f['rS_regions_val']
						rS_level_multi_val_list.append(rS_level_val)	
				
				if rS_level == True:
					max_val = max(rS_level_multi_val_list)
				else:
					max_val = 1
					
				cMC_rS_lvl_table = QtGui.QTableWidget()
				width = 150 + 290*max_val + 5
				height = 30 + len(cMC_refinementSurfaces_obj_list)*30
				cMC_rS_lvl_table.setFixedSize(width, height)
	
				cMC_rS_lvl_table.setRowCount(obj_initial['rS_val'])
				cMC_rS_lvl_table.verticalHeader().hide()

				if rS_level_multi_val_list == []:
					cMC_rS_lvl_table.setColumnCount(2)
				else:
					cMC_rS_lvl_table.setColumnCount(max_val+1)
				cMC_rS_lvl_table.verticalHeader().hide()

				cMC_rS_lvl_table.horizontalHeader().resizeSection(0, 150)
				cMC_rS_lvl_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
				column_1 = QtGui.QTableWidgetItem()
				cMC_rS_lvl_table.setHorizontalHeaderItem(0, column_1)
				cMC_rS_lvl_table.horizontalHeader().setStyleSheet("color: steelblue")

				if int_lng == 'Russian':
					column_1.setText("Поверхность")

				elif int_lng == 'English':
					column_1.setText("Surface")

				q = 0

				for el_CMC_rS in cMC_refinementSurfaces_obj_list:
					#rS_surface#
					rS_geometry_edit = QtGui.QComboBox()
					rS_geometry_edit.setFixedSize(110, 25)
					rS_geometry_edit.addItems(el_CMC_rS_list)
					rS_geometry_hbox = QtGui.QHBoxLayout()
					rS_geometry_hbox.setContentsMargins(0, 0, 0, 0)
					rS_geometry_hbox.addWidget(rS_geometry_edit)
					rS_geometry_cell_widget = QtGui.QWidget()
					rS_geometry_cell_widget.setLayout(rS_geometry_hbox)
					
					if castellatedMC_2_obj != None:
						rS_geometry_edit_mas = rS_geometry_edit.count()  
						for t in range(rS_geometry_edit_mas):
							if rS_geometry_edit.itemText(t) == castellatedMC_2_obj['CM_refinementSurface_lvl'][q]['rS_surface']:
								f_geometry_edit.setCurrentIndex(t)

					cMC_rS_lvl_table.setCellWidget(q, 0, rS_geometry_cell_widget)
					rS_regions_val = el_CMC_rS['rS_regions_val']
					
					r = 1
					l = 0

					while r <= rS_regions_val:

						cMC_rS_lvl_table.horizontalHeader().resizeSection(r, 290)
						cMC_rS_lvl_table.horizontalHeader().setResizeMode(r, QtGui.QHeaderView.Fixed)
						column_2 = QtGui.QTableWidgetItem()
						cMC_rS_lvl_table.setHorizontalHeaderItem(r, column_2)
						cMC_rS_lvl_table.horizontalHeader().setStyleSheet("color: steelblue")
							
						rslmv_reg_edit = QtGui.QLineEdit()	
						rslmv_reg_edit.setFixedSize(100, 25)
						regexp = QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+')
						validator = QtGui.QRegExpValidator(regexp)
						rslmv_reg_edit.setValidator(validator)
						if castellatedMC_2_obj != None:
							rslmv_reg_edit.setText(castellatedMC_2_obj['CM_refinementSurface_lvl'][q]['rS_regions'][l])
						
						rslmv_min_lbl = QtGui.QLabel()
						rslmv_min = QtGui.QSpinBox()
						rslmv_min.setFixedSize(45, 25)
						rslmv_min.setRange(0, 1000)
						if castellatedMC_2_obj != None:
							rslmv_min.setValue(castellatedMC_2_obj['CM_refinementSurface_lvl'][q]['rS_levels'][l][0])

						rslmv_max_lbl = QtGui.QLabel()
						rslmv_max = QtGui.QSpinBox()
						rslmv_max.setFixedSize(45, 25)
						rslmv_max.setRange(0, 1000)
						if castellatedMC_2_obj != None:
							rslmv_max.setValue(castellatedMC_2_obj['CM_refinementSurface_lvl'][q]['rS_levels'][l][1])
						
						if int_lng == 'Russian':
							
							rslmv_min_lbl.setText("Мин:")
							rslmv_max_lbl.setText("Макс:")
							column_2.setText("Подобласть_" + str(r))
						elif int_lng == 'English':
							
							rslmv_min_lbl.setText("Min:")
							rslmv_max_lbl.setText("Max:")
							column_2.setText("Subregion_" + str(r))

						rslmv_min_max_hbox = QtGui.QHBoxLayout()
						rslmv_min_max_hbox.setContentsMargins(0, 0, 0, 0)

						rslmv_min_max_hbox.addWidget(rslmv_reg_edit)
						rslmv_min_max_hbox.addWidget(rslmv_min_lbl)
						rslmv_min_max_hbox.addWidget(rslmv_min)
						rslmv_min_max_hbox.addWidget(rslmv_max_lbl)
						rslmv_min_max_hbox.addWidget(rslmv_max)

						rslmv_min_max_cell_widget = QtGui.QWidget()
						rslmv_min_max_cell_widget.setLayout(rslmv_min_max_hbox)
						
						cMC_rS_lvl_table.setCellWidget(q, r, rslmv_min_max_cell_widget)	

						l = l + 1
						r = r + 1

					q = q + 1

				prs_lvl_grid.addWidget(cMC_rS_lvl_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
				prs_lvl_grid.addWidget(cMC_rS_lvl_table, 3, 0, alignment=QtCore.Qt.AlignCenter)
				
		rR_level_single_list = []
		if obj_initial['rR'] == True and True in other_geometry_list:
		
		##-------------------------------------Третья таблица---------------------------------------------##
				
			cMC_refinementRegions_obj_list = castellatedMC_1_obj['refinementRegions']
			
			el_CMC_rR_list = []
			for el_CMC_rR in cMC_refinementRegions_obj_list:
				el_CMC_rR_list.append(el_CMC_rR['rR_surface'])
				
			cMC_rR_lvl_lbl = QtGui.QLabel()	
			if int_lng == 'Russian':
				cMC_rR_lvl_lbl.setText("Параметры уровней для областей при измельчении")
			elif int_lng == 'English':
				cMC_rR_lvl_lbl.setText("Level parameters for regions in grinding")

			#Определям макс длину массива
			rR_level_multi_val_list = []
			for el_CMC_rR in cMC_refinementRegions_obj_list:
				rR_level_single = el_CMC_rR['rR_level_single']
				
				if rR_level_single == False:
					rR_level_multi_val = el_CMC_rR['rR_level_multi_val']
					rR_level_multi_val_list.append(rR_level_multi_val)
					rR_level_single_list.append(rR_level_single)
				else:
					rR_level_single_list.append(rR_level_single)
					
			if False in rR_level_single_list:
				max_val = max(rR_level_multi_val_list)
			else:
				max_val = 1
				
			cMC_rR_lvl_table = QtGui.QTableWidget()
			
			width = 150 + 213*max_val
			height = 30 + len(cMC_refinementRegions_obj_list)*30

			cMC_rR_lvl_table.setFixedSize(width, height)
			cMC_rR_lvl_table.setRowCount(obj_initial['rR_val'])
			if rR_level_multi_val_list == []:
				cMC_rR_lvl_table.setColumnCount(2)
			else:
				cMC_rR_lvl_table.setColumnCount(max_val+1)
			cMC_rR_lvl_table.verticalHeader().hide()

			cMC_rR_lvl_table.horizontalHeader().resizeSection(0, 150)
			cMC_rR_lvl_table.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Fixed)
			column_1 = QtGui.QTableWidgetItem()
			cMC_rR_lvl_table.setHorizontalHeaderItem(0, column_1)
			cMC_rR_lvl_table.horizontalHeader().setStyleSheet("color: steelblue")
			
			if int_lng == 'Russian':
				column_1.setText("Поверхность")
			elif int_lng == 'English':
				column_1.setText("Surface")
				
			q = 0

			for el_CMC_rR in cMC_refinementRegions_obj_list:
				#rR_surface#
				rR_geometry_edit = QtGui.QComboBox()
				rR_geometry_edit.setFixedSize(110, 25)
				rR_geometry_edit.addItems(el_CMC_rR_list)
				rR_geometry_hbox = QtGui.QHBoxLayout()
				rR_geometry_hbox.setContentsMargins(0, 0, 0, 0)
				rR_geometry_hbox.addWidget(rR_geometry_edit)
				rR_geometry_cell_widget = QtGui.QWidget()
				rR_geometry_cell_widget.setLayout(rR_geometry_hbox)
				if castellatedMC_2_obj != None:
					rR_geometry_edit_mas = rR_geometry_edit.count()  
					for t in range(rR_geometry_edit_mas):
						if rR_geometry_edit.itemText(t) == castellatedMC_2_obj['CM_refinementRegions_lvl'][q]['rR_surface']:
							rR_geometry_edit.setCurrentIndex(t)
					
				cMC_rR_lvl_table.setCellWidget(q, 0, rR_geometry_cell_widget)
				#level#
				rR_level_single = el_CMC_rR['rR_level_single']
				
				if rR_level_single == True:
										
					rR_level_single_min_val_lbl = QtGui.QLabel()
					rR_level_single_min_val = QtGui.QSpinBox()
					rR_level_single_min_val.setFixedSize(50, 25)
					rR_level_single_min_val.setRange(0, 1000000000000000)
					if castellatedMC_2_obj != None:
						rR_level_single_min_val.setValue(castellatedMC_2_obj['CM_refinementRegions_lvl'][q]['lvl_prs']['lvl_single_min'])
					
					rR_level_single_max_val_lbl = QtGui.QLabel()
					rR_level_single_max_val = QtGui.QSpinBox()
					rR_level_single_max_val.setFixedSize(50, 25)
					rR_level_single_max_val.setRange(0, 1000000000000000)
					if castellatedMC_2_obj != None:
						rR_level_single_max_val.setValue(castellatedMC_2_obj['CM_refinementRegions_lvl'][q]['lvl_prs']['lvl_single_max'])
					
					rR_level_single_val_hbox = QtGui.QHBoxLayout()
					rR_level_single_val_hbox.setContentsMargins(0, 0, 0, 0)

					rR_level_single_val_hbox.addWidget(rR_level_single_min_val_lbl)
					rR_level_single_val_hbox.addWidget(rR_level_single_min_val)
					rR_level_single_val_hbox.addWidget(rR_level_single_max_val_lbl)
					rR_level_single_val_hbox.addWidget(rR_level_single_max_val)

					rR_level_cell_widget = QtGui.QWidget()
					rR_level_cell_widget.setLayout(rR_level_single_val_hbox)
					
					cMC_rR_lvl_table.horizontalHeader().resizeSection(1, 210)
					cMC_rR_lvl_table.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
					column_2 = QtGui.QTableWidgetItem()
					cMC_rR_lvl_table.setHorizontalHeaderItem(1, column_2)
					cMC_rR_lvl_table.horizontalHeader().setStyleSheet("color: steelblue")
					
					if int_lng == 'Russian':
						column_2.setText("Уровень_1")
						rR_level_single_min_val_lbl.setText("Мин" + ":")
						rR_level_single_max_val_lbl.setText("Макс" + ":")
					elif int_lng == 'English':
						column_2.setText("Level_1")
						rR_level_single_min_val_lbl.setText("Min" + ":")
						rR_level_single_max_val_lbl.setText("Max" + ":")
					
					cMC_rR_lvl_table.setCellWidget(q, 1, rR_level_cell_widget)
					
				elif rR_level_single == False:
					
					rR_level_multi_val = el_CMC_rR['rR_level_multi_val']
					r = 1
					l = 0

					while r <= rR_level_multi_val:
						
						rRlmv_min_lbl = QtGui.QLabel()
						rRlmv_min = QtGui.QSpinBox()
						rRlmv_min.setFixedSize(50, 25)
						rRlmv_min.setRange(0, 1000)
						if castellatedMC_2_obj != None:
							rRlmv_min.setValue(castellatedMC_2_obj['CM_refinementRegions_lvl'][q]['multi_prs'][l]['lvl_multi_' + str(r)][0])
							
						rRlmv_max_lbl = QtGui.QLabel()
						rRlmv_max = QtGui.QSpinBox()
						rRlmv_max.setFixedSize(50, 25)
						rRlmv_max.setRange(0, 1000)
						if castellatedMC_2_obj != None:
							rRlmv_max.setValue(castellatedMC_2_obj['CM_refinementRegions_lvl'][q]['multi_prs'][l]['lvl_multi_' + str(r)][1])
						
						cMC_rR_lvl_table.horizontalHeader().resizeSection(r, 205)
						cMC_rR_lvl_table.horizontalHeader().setResizeMode(r, QtGui.QHeaderView.Fixed)
						column_2 = QtGui.QTableWidgetItem()
						cMC_rR_lvl_table.setHorizontalHeaderItem(r, column_2)
						cMC_rR_lvl_table.horizontalHeader().setStyleSheet("color: steelblue")
						
						if int_lng == 'Russian':
							column_2.setText("Уровень_" + str(r))	
						elif int_lng == 'English':
							column_2.setText("Level_" + str(r))
						
						if int_lng == 'Russian':
							rRlmv_min_lbl.setText("Мин_" + str(r) + ":")
							rRlmv_max_lbl.setText("Макс_" + str(r) + ":")
						elif int_lng == 'English':
							rRlmv_min_lbl.setText("Min_" + str(r) + ":")
							rRlmv_max_lbl.setText("Max_" + str(r) + ":")
							
						rRlmv_min_max_hbox = QtGui.QHBoxLayout()
						rRlmv_min_max_hbox.setContentsMargins(0, 0, 0, 0)

						rRlmv_min_max_hbox.addWidget(rRlmv_min_lbl)
						rRlmv_min_max_hbox.addWidget(rRlmv_min)
						rRlmv_min_max_hbox.addWidget(rRlmv_max_lbl)
						rRlmv_min_max_hbox.addWidget(rRlmv_max)
						rRlmv_min_max_cell_widget = QtGui.QWidget()
						rRlmv_min_max_cell_widget.setLayout(rRlmv_min_max_hbox)
						
						cMC_rR_lvl_table.setCellWidget(q, r, rRlmv_min_max_cell_widget)

						r = r + 1
						l = l + 1

				q = q + 1

			prs_lvl_grid.addWidget(cMC_rR_lvl_lbl, 4, 0, alignment=QtCore.Qt.AlignCenter)
			prs_lvl_grid.addWidget(cMC_rR_lvl_table, 5, 0, alignment=QtCore.Qt.AlignCenter)
		
		# -------------------------Кнопка сохранения --------------------------#

		castellatedMC_2_btnSave = QtGui.QPushButton()
		castellatedMC_2_btnSave.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(castellatedMC_2_btnSave)
		if int_lng == 'Russian':
			castellatedMC_2_btnSave.setText("Записать")
		elif int_lng == 'English':
			castellatedMC_2_btnSave.setText("Write")

		# -----------------------Групповой элемент формы-----------------------#

		castellatedMC_2_grid = QtGui.QGridLayout()
		castellatedMC_2_grid.addWidget(prs_lvl_frame, 0, 0, alignment=QtCore.Qt.AlignCenter)
		castellatedMC_2_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		castellatedMC_2_grid.setRowStretch(3, 6)
		castellatedMC_2_group = QtGui.QGroupBox()
		castellatedMC_2_group.setLayout(castellatedMC_2_grid)
		return castellatedMC_2_group, castellatedMC_2_btnSave, prs_lvl_grid, f_level_single_list, rR_level_single_list, el_CMC_rS_regions_list



