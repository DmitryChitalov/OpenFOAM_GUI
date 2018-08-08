# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil
import re

class msh_functions_class():		
	
	###..............................Функция вывода результатов потока t1..........................### 
	
	def on_msh_finished(return_code, prj_path_val_th, mesh_name_txt_val_th, par, int_lng, msh_t):

		msh_read_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th + "/mesh_out.log")
		data = msh_read_file.read()

		if int_lng == 'Russian':
			par.outf_lbl.setText('Результаты генерации сетки типа ' + msh_t) 
		elif int_lng == 'English':
			par.outf_lbl.setText('Generation results of mesh of type ' + msh_t) 
		par.cdw.setWidget(par.outf_scroll)
		par.cdw.setTitleBarWidget(par.cdw_frame)
		par.outf_edit.setText(data)

		if return_code == 0:
			if int_lng == 'Russian':
				msg = "Расчетная сетка типа " + msh_t + " успешно сгенерирована"
			elif int_lng == 'English':
				msg = "Mesh of type " + msh_t + " was successfully generated"
			color = QtGui.QColor("green")
			
			par.msh_visual.setEnabled(True)
			
			if os.path.exists(par.full_dir + "/0") == False:

				shutil.copytree("./matches/0", par.full_dir + "/0")
				
				#---0---
				dir_0_path = par.full_dir + '/0'
				if dir_0_path:
					dir_0_name = os.path.basename(par.full_dir + '/0')	

					files_0 = ['p', 'T', 'U']

					item_0 = QtGui.QStandardItem(dir_0_name)
					par.treeview.model.insertRow(2, item_0)
					j = 0
					index = par.treeview.model.index(2, 0)
					par.treeview.expand(index) 
					for el_0 in files_0:
						child_item_0 = QtGui.QStandardItem(el_0)
						child_item_0.setForeground(QtGui.QColor('navy'))
						item_0.setChild(j, 0, child_item_0)
						j = j + 1
				
				file = open(par.full_dir + "/constant/polyMesh/boundary", 'r') 
				data = file.read()
				file.close()

				struct_reg = re.compile(r"\S*\n\s*(?=[{])")
				struct_mas = struct_reg.findall(data)

				i = 1
				mas = []
				for elem in range(len(struct_mas)-1):
					div = struct_mas[i].split("\n")
					i = i + 1
					mas.append(div[0])

				file_U = open(par.full_dir + "/0/U", 'a')                 
				file_U.write("\n{\n")
				for el in range(len(mas)):
					file_U.write("    " + mas[el] + "\n    {\n        type            empty;\n    }\n")
					print(mas[el])
				file_U.write("}")
				file_U.close()

				file_T = open(par.full_dir + "/0/T", 'a')                 
				file_T.write("\n{\n")
				for el in range(len(mas)):
					file_T.write("    " + mas[el] + "\n    {\n        type            empty;\n    }\n")
				file_T.write("}")
				file_T.close()

				file_p = open(par.full_dir + "/0/p", 'a')                 
				file_p.write("\n{\n")
				for el in range(len(mas)):
					file_p.write("    " + mas[el] + "\n    {\n        type            empty;\n    }\n")
				file_p.write("}")
				file_p.close()

		else:
			if int_lng == 'Russian':
				msg = "Расчетная сетка типа " + msh_t + " сгенерирована c ошибками"
			elif int_lng == 'English':
				msg = "Mesh of type " + msh_t + " was generated with errors"
			color = QtGui.QColor("red")

		par.listWidget.clear()
		par.item = QtGui.QListWidgetItem(msg, par.listWidget)
		par.item.setTextColor(color)
		par.listWidget.addItem(par.item)
		
		if os.path.exists(par.full_dir + '/mesh_script'):
			os.remove(par.full_dir + '/mesh_script')
		if os.path.exists(par.full_dir + '/mesh_out.log'):
			os.remove(par.full_dir + '/mesh_out.log')
		
	def on_msh_visual_run(par, int_lng):
		
		if int_lng == 'Russian':
			msg = "Визуализация сетки типа " + msh_t + "запущена"
		elif int_lng == 'English':
			msg = "Visualisation of the mesh of type " + msh_t + " is started"
		color = QtGui.QColor("blue")

		par.listWidget.clear()
		par.item = QtGui.QListWidgetItem(msg, par.listWidget)
		par.item.setTextColor(color)
		par.listWidget.addItem(par.item)
		
	def on_msh_visual_finished(return_code, prj_path_val_th, mesh_name_txt_val_th, par, int_lng):

		msh_read_file = open(prj_path_val_th + '/' + mesh_name_txt_val_th + "/mesh_visual_out.log")
		data = msh_read_file.read()

		if int_lng == 'Russian':
			par.outf_lbl.setText('Результаты визуализации сетки типа ' + msh_t) 
		elif int_lng == 'English':
			par.outf_lbl.setText('Vizualization results of mesh of type ' + msh_t) 
		par.cdw.setWidget(par.outf_scroll)
		par.cdw.setTitleBarWidget(par.cdw_frame)
		par.outf_edit.setText(data)

		if return_code == 0:
			if int_lng == 'Russian':
				msg = "Визуализация сетки " + msh_t + " завершена"
			elif int_lng == 'English':
				msg = "Mesh visualisation of type " + msh_t + " complete"
			color = QtGui.QColor("green")

		else:
			if int_lng == 'Russian':
				msg = "При отображении расчетной сетки " + msh_t + " возникли проблемы"
			elif int_lng == 'English':
				msg = "Mesh visualisation of type " + msh_t + " complete with errors"
			color = QtGui.QColor("red")

		par.listWidget.clear()
		par.item = QtGui.QListWidgetItem(msg, par.listWidget)
		par.item.setTextColor(color)
		par.listWidget.addItem(par.item)	
		
		if os.path.exists(par.full_dir + '/mesh_visual_script'):
			os.remove(par.full_dir + '/mesh_visual_script')
		if os.path.exists(par.full_dir + '/mesh_visual_out.log'):
			os.remove(par.full_dir + '/mesh_visual_out.log')