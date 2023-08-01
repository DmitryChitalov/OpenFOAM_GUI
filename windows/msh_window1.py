# -*- coding: utf-8 -*-
# -------------------------------Импорт модулей----------------------------------#

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path
import subprocess
import time
import getpass

from windows.bMD_window import bmd_window_class
from windows.sHMD_window import shmd_window_class
from windows.fQMD_window import fqmd_window_class

# -----------Дочерний поток для запуска процесса генерации сетки-----------------

class MyThread(QtCore.QThread):
    def __init__(self, full_dir, parent=None):
        QtCore.QThread.__init__(self, parent)
        global fd
        fd = full_dir
    def run(self):
        global proc

        file = open(fd+"/out_mesh.log", "w")
        proc = subprocess.Popen(["bash "+fd+"/MESH_BASH"], cwd = fd, shell = True, stdout=file, stderr=file)
        while proc.poll() is None:
            time.sleep(0.5)

# ---------------------------Главная форма проекта-------------------------------#
		
class msh_window_class(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
		self.setWindowModality(QtCore.Qt.WindowModal)

		global par
		par = parent
		
		global int_lng
		int_lng = par.interface_lng_val	
		
		global full_dir
		full_dir = parent.full_dir
		self.t1 = MyThread(full_dir)
		
		self.connect(self.t1, QtCore.SIGNAL("finished()"), self.on_finished)
		
# ------------------------------------Первый блок формы--------------------------------------#

		self.mesh_choose_lbl = QtGui.QLabel()
		self.mesh_choose_lbl_hbox = QtGui.QHBoxLayout()
		self.mesh_choose_lbl_hbox.addWidget(self.mesh_choose_lbl)
		self.radio_1 = QtGui.QRadioButton()
		self.radio_1.toggled.connect(self.on_radio_1_clicked)
		self.radio_2 = QtGui.QRadioButton()
		self.radio_2.toggled.connect(self.on_radio_2_clicked)
		self.mesh_choose_grid = QtGui.QGridLayout()
		self.mesh_choose_grid.addWidget(self.radio_1, 0, 0)
		self.mesh_choose_grid.addWidget(self.radio_2, 0, 1)
		self.mesh_choose_frame = QtGui.QFrame()
		self.mesh_choose_frame.setLayout(self.mesh_choose_grid)
		self.mesh_choose_hbox = QtGui.QHBoxLayout() 
		self.mesh_choose_hbox.addWidget(self.mesh_choose_frame)
		
# ------------------------------------Второй блок формы--------------------------------------#

		self.fmtf_radio = QtGui.QRadioButton("Импорт 2D-сетки")
		self.f3Dmtf_radio = QtGui.QRadioButton("Импорт 3D-сетки")
		self.import_hbox = QtGui.QHBoxLayout()
		self.import_hbox.addWidget(self.fmtf_radio)
		self.import_hbox.addWidget(self.f3Dmtf_radio)
		
		self.mesh_label = QtGui.QLabel("Путь: ")
		self.mesh_edit = QtGui.QLineEdit()
		self.mesh_edit.setEnabled(False)
		self.mesh_edit.setFixedSize(290, 25)
		self.path_button = QtGui.QPushButton("...")
		self.path_button.setFixedSize(25, 25)
		
		self.import_prs_hbox = QtGui.QHBoxLayout()
		self.import_prs_hbox.addWidget(self.mesh_label)
		self.import_prs_hbox.addWidget(self.mesh_edit)
		self.import_prs_hbox.addWidget(self.path_button)
		self.path_button.clicked.connect(self.on_path_choose)

		self.prs_grid = QtGui.QGridLayout()
		self.prs_grid.addLayout(self.import_hbox, 0, 0)
		self.prs_grid.addLayout(self.import_prs_hbox, 1, 0)
		self.prs_frame = QtGui.QFrame()
		self.prs_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
		self.prs_frame.setLayout(self.prs_grid)
		self.prs_frame.setEnabled(False)
		self.prs_frame.setStyleSheet("border-color: darkgray;")
		self.prs_hbox = QtGui.QHBoxLayout() 
		self.prs_hbox.addWidget(self.prs_frame)

		# ------------------------------------Третий блок формы--------------------------------------#

		self.chc_label = QtGui.QLabel()
		self.chc_label.setEnabled(False)
		self.chc_lbl_hbox = QtGui.QHBoxLayout()
		self.chc_lbl_hbox.addWidget(self.chc_label)
		self.nf_radio = QtGui.QRadioButton()
		self.nf_radio.toggled.connect(self.on_nf_clicked)
		self.cf_radio = QtGui.QRadioButton()
		self.cf_radio.toggled.connect(self.on_cf_clicked)
		self.icon = self.style().standardIcon(QtGui.QStyle.SP_DirOpenIcon)
		self.chc_button = QtGui.QPushButton()
		self.chc_button.setFixedSize(30, 30)
		self.chc_button.setIcon(self.icon)
		self.chc_button.setEnabled(False)
		self.chc_button.clicked.connect(self.on_chc_clicked)
		self.chc_grid = QtGui.QGridLayout()
		self.chc_grid.addWidget(self.nf_radio, 0, 0)
		self.chc_grid.addWidget(self.cf_radio, 0, 1)
		self.chc_grid.addWidget(self.chc_button, 0, 2)
		self.chc_frame = QtGui.QFrame()
		self.chc_frame.setFixedWidth(400)
		self.chc_frame.setEnabled(False)
		self.chc_frame.setStyleSheet("border-color: darkgray;")
		self.chc_frame.setLayout(self.chc_grid)
		self.chc_hbox = QtGui.QHBoxLayout() 
		self.chc_hbox.addWidget(self.chc_frame)
		
		# ------------------------------------Четвертый блок формы--------------------------------------#

		self.mesh_type_label = QtGui.QLabel('Выберите тип сетки:')
		self.bm = QtGui.QRadioButton("blockMesh")
		self.bm.setChecked(True)
		self.shm = QtGui.QRadioButton("snappyHexMesh")
		self.fqm = QtGui.QRadioButton("foamyQuadMesh")
		self.mesh_type_vbox = QtGui.QVBoxLayout()
		self.mesh_type_vbox.addWidget(self.bm)
		self.mesh_type_vbox.addWidget(self.shm)
		self.mesh_type_vbox.addWidget(self.fqm)
		
		self.mesh_label = QtGui.QLabel()
		self.mesh_name = QtGui.QLineEdit()
		
		self.mesh_name.setFixedSize(214, 25)
		regexp = QtCore.QRegExp('[А-яА-Яa-zA-Z0-9\_]+')
		validator = QtGui.QRegExpValidator(regexp)
		self.mesh_name.setValidator(validator)
		
		self.prj_path_label = QtGui.QLabel()
		self.prj_path_name = QtGui.QLineEdit()
		self.prj_path_name.setEnabled(False)
		self.prj_path_name.setFixedSize(214, 25)
				
		self.prj_grid = QtGui.QGridLayout()
		self.prj_grid.addWidget(self.mesh_type_label, 0, 0, alignment=QtCore.Qt.AlignCenter)
		self.prj_grid.addLayout(self.mesh_type_vbox, 0, 1, alignment=QtCore.Qt.AlignCenter)
		self.prj_grid.addWidget(self.mesh_label, 1, 0, alignment=QtCore.Qt.AlignCenter)
		self.prj_grid.addWidget(self.mesh_name, 1, 1, alignment=QtCore.Qt.AlignCenter)
		self.prj_grid.addWidget(self.prj_path_label, 2, 0, alignment=QtCore.Qt.AlignCenter)
		self.prj_grid.addWidget(self.prj_path_name, 2, 1, alignment=QtCore.Qt.AlignCenter)

		self.prj_frame = QtGui.QFrame()
		self.prj_frame.setFixedWidth(400)
		self.prj_frame.setEnabled(False)
		self.prj_frame.setStyleSheet("border-color: darkgray;")
		self.prj_frame.setFrameShape(QtGui.QFrame.Panel)
		self.prj_frame.setFrameShadow(QtGui.QFrame.Sunken)
		self.prj_frame.setLayout(self.prj_grid) 
		self.prj_grid_vbox = QtGui.QVBoxLayout() 
		self.prj_grid_vbox.addWidget(self.prj_frame)

		# ---------------------Кнопки сохранения и отмены и их блок-------------------------#

		self.save_button = QtGui.QPushButton()
		self.save_button.setFixedSize(80, 25)
		self.save_button.clicked.connect(self.on_save_clicked)
		self.save_button.setEnabled(False)
		self.cancel_button = QtGui.QPushButton()
		self.cancel_button.setFixedSize(80, 25)
		self.cancel_button.clicked.connect(self.on_cancel_clicked)
		self.buttons_hbox = QtGui.QHBoxLayout()
		self.buttons_hbox.addWidget(self.save_button)
		self.buttons_hbox.addWidget(self.cancel_button)

		# -------------------------Фрейм формы---------------------------#

		self.form_grid = QtGui.QGridLayout()
		self.form_grid.addLayout(self.mesh_choose_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
		self.form_grid.addLayout(self.prs_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		self.form_grid.addLayout(self.chc_lbl_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
		self.form_grid.addLayout(self.chc_hbox, 3, 0, alignment=QtCore.Qt.AlignCenter)
		self.form_grid.addLayout(self.prj_grid_vbox, 4, 0, alignment=QtCore.Qt.AlignCenter)
		self.form_grid.addLayout(self.buttons_hbox, 5, 0, alignment=QtCore.Qt.AlignCenter)
		self.form_frame = QtGui.QFrame()
		self.form_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
		self.form_frame.setLayout(self.form_grid)
		self.form_vbox = QtGui.QVBoxLayout() 
		self.form_vbox.addWidget(self.form_frame)

		# --------------------Размещение на форме всех компонентов---------#

		self.form = QtGui.QFormLayout()
		self.form.addRow(self.form_vbox)
		self.setLayout(self.form)
		
		# --------------------Определяем параметры интерфейса окна---------#
		
		if int_lng == 'Russian':
			self.radio_1.setText("Внешняя сетка")
			self.radio_2.setText("OpenFOAM-сетка")
			self.fmtf_radio.setText("Импорт 2D-сетки")
			self.f3Dmtf_radio.setText("Импорт 3D-сетки")
			self.chc_label.setText("Создайте новую сетку или откройте существующую")
			self.nf_radio.setText("Создать новую")
			self.cf_radio.setText("Открыть существующую")
			self.mesh_type_label.setText("Выберите тип сетки:")
			self.mesh_label.setText("Название сетки:")
			self.prj_path_label.setText("Путь:")
			self.save_button.setText("Сохранить")
			self.cancel_button.setText("Отмена")
		elif int_lng == 'English':
			self.radio_1.setText("External mesh")
			self.radio_2.setText("OpenFOAM-mesh")
			self.fmtf_radio.setText("2D-mesh import")
			self.f3Dmtf_radio.setText("3D-mesh import")
			self.chc_label.setText("Create a new mesh or open an existing mesh")
			self.nf_radio.setText("Create new mesh")
			self.cf_radio.setText("Open existing mesh")
			self.mesh_type_label.setText("Select mesh type:")
			self.mesh_label.setText("Mesh name:")
			self.prj_path_label.setText("Path:")
			self.save_button.setText("Save")
			self.cancel_button.setText("Cancel")
		
	# ------------------------Функции связанные с формой-----------------------------#
	
	# .....Функция, запускаемая при нажатии радио-кнопки "Внешняя сетка"......#
	
	def on_radio_1_clicked(self):
		self.prs_frame.setEnabled(True)
		self.chc_frame.setEnabled(False)
		self.prj_frame.setEnabled(False)
		self.chc_label.setEnabled(False)
		self.prs_frame.setStyleSheet("border-color: dimgray;")
		self.chc_frame.setStyleSheet("border-color: darkgray;")
		self.prj_frame.setStyleSheet("border-color: darkgray;")
		self.prj_path_name.setText("")
		
	# .....Функция, запускаемая при нажатии радио-кнопки "OpenFOAM сетка"......#
		
	def on_radio_2_clicked(self):
		self.prs_frame.setEnabled(False)
		self.chc_frame.setEnabled(True)
		self.chc_label.setEnabled(True)
		self.chc_frame.setStyleSheet("border-color: dimgray;")
		self.prs_frame.setStyleSheet("border-color: darkgray;")
		self.prj_path_name.setText(full_dir + '/system')
		self.save_button.setEnabled(True)
	
	# .....Функция определения пути до внешней сетки......#
	
	def on_path_choose(self):
		global mesh_dir
		user = getpass.getuser()
		mesh_dir = QtGui.QFileDialog.getOpenFileName(directory="/home/"+user)
		mesh_reg = re.compile(r"\S*(?<=[\/])\S*msh")
		mesh_mas = mesh_reg.findall(mesh_dir)

		if mesh_mas != []:
			self.mesh_edit.setText(mesh_dir)
		else:
			dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
				"Внимание!", "Это не файл сетки. Выберите другой файл",
				buttons = QtGui.QMessageBox.Ok)
			result = dialog.exec_()
			
		self.save_button.setEnabled(True)
		
    #......Функция по завершению генерации внешней сетки......#
	
	def on_finished(self):
		global mas

		if proc.returncode == 0:

			file = open(full_dir+"/constant/polyMesh/boundary", 'r') 
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

			file_U = open(full_dir+"/0/U", 'a')                 
			file_U.write("\n{\n")
			for el in range(len(mas)):
				file_U.write("    " + mas[el] + "\n    {\n        type            empty;\n    }\n")
			file_U.write("}")
			file_U.close()

			file_T = open(full_dir+"/0/T", 'a')                 
			file_T.write("\n{\n")
			for el in range(len(mas)):
				file_T.write("    " + mas[el] + "\n    {\n        type            empty;\n    }\n")
			file_T.write("}")
			file_T.close()

			file_p = open(full_dir+"/0/p", 'a')                 
			file_p.write("\n{\n")
			for el in range(len(mas)):
				file_p.write("    " + mas[el] + "\n    {\n        type            empty;\n    }\n")
			file_p.write("}")
			file_p.close()

			par.listWidget.clear()
			par.item = QtGui.QListWidgetItem("Расчетная сетка успешно сгенерирована", par.listWidget)
			par.color = QtGui.QColor("green")
			par.item.setTextColor(par.color)
			par.listWidget.addItem(par.item)
			
			par.task_open.setEnabled(True)
		
			self.close()
		else:
			par.item = QtGui.QListWidgetItem("Расчетная сетка не сгенерирована", par.listWidget)
			par.color = QtGui.QColor("red")
			par.item.setTextColor(par.color)
			par.listWidget.addItem(par.item)
		
	# .....Функция, запускаемая при нажатии радио-кнопки "создать новую сетку OpenFOAM"......#
	
	def on_nf_clicked(self):
		self.prj_path_label.setEnabled(True)
		self.prj_frame.setEnabled(True)
		self.prj_frame.setStyleSheet("border-color: dimgray;")
		self.chc_button.setEnabled(False)

	# .....Функция, запускаемая при нажатии радио-кнопки "открыть имеющуюся сетку OpenFOAM"......#

	def on_cf_clicked(self):
		self.prj_path_label.setEnabled(False)
		self.prj_frame.setEnabled(False)
		self.prj_frame.setStyleSheet("border-color: darkgray;")
		self.chc_button.setEnabled(True)
		self.prj_path_name.setText('')
			
	# .....Функция, запускаемая при нажатии кнопки "выбрать существующую"......#
		
	def on_chc_clicked(self):
		global prj_path_cur
		global pickles_dir
		global prj_dir
		global pd_2

		prj_dir = QtGui.QFileDialog.getExistingDirectory(directory=full_dir + '/system/')
		prj_path_cur, pickles_dir = os.path.split(prj_dir)
		
		pd_1, pd_2 = pickles_dir.split("_")

		initial_path = prj_dir + '/' + 'initial.pkl'
		if os.path.exists(initial_path) == True:
			self.prj_path_name.setText(prj_dir)
			self.save_button.setEnabled(True)
			self.mesh_name.setText(pickles_dir)
			if pd_2 == 'blockMesh':
				self.bm.setChecked(True)
				par.on_mesh_type_get(pd_2)
			elif pd_2 == 'snappyHexMesh':
				self.shm.setChecked(True)
				par.on_mesh_type_get(pd_2)
			elif pd_2 == 'foamyQuadMesh':
				self.fqm.setChecked(True)
				par.on_mesh_type_get(pd_2)
				
			self.prj_frame.setEnabled(True)
			self.prj_path_name.setEnabled(False)
		else:
			if int_lng == 'Russian':
				dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Внимание!", "Это не директория сетки или в ней отсутствуют все необходимые файлы", buttons = QtGui.QMessageBox.Ok)
			elif int_lng == 'English':
				dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Attention!", "This is not a grid directory, or all necessary files are missing in it", buttons = QtGui.QMessageBox.Ok)
			result = dialog.exec_()			
		
	# ....................Функция, запускаемая при нажатии кнопки "сохранить"....................#

	def on_save_clicked(self):

		msh_lbl_widget = par.tdw_grid.itemAtPosition(0, 2)
		msh_path_lbl_widget = par.tdw_grid.itemAtPosition(0, 3)

		if msh_lbl_widget != None:
			par.tdw_grid.removeWidget(msh_lbl_widget, 0, 2)
		if msh_path_lbl_widget != None:
			par.tdw_grid.removeWidget(msh_path_lbl_widget, 0, 3)
		
		full_dir = par.full_dir
		if self.radio_1.isChecked():
			
			f = open(full_dir+'/MESH_BASH', 'w')
			if self.fmtf_radio.isChecked():
				f.write('#!/bin/sh' + '\n' + '. /opt/openfoam4/etc/bashrc' + '\n' + 'fluentMeshToFoam ' + mesh_dir + '\n' + 'exit')
				f.close()

			elif self.f3Dmtf_radio.isChecked():
				f.write('#!/bin/sh' + '\n' + '. /opt/openfoam4/etc/bashrc' + '\n' + 'fluent3DMeshToFoam ' + mesh_dir + '\n' + 'exit')
				f.close()
                
			self.t1.start()

			shutil.copytree("./matches/0", full_dir + "/0")
			
			par.msh_visual.setEnabled(True)
		
		elif self.radio_2.isChecked():
			global mesh_name_txt_cur
			mesh_name_txt_cur = self.mesh_name.text()

			if int_lng == 'Russian':
				par.ffw_label.setText("Форма генерации расчетной сетки: " + "<font color='peru'>" + mesh_name_txt_cur + "</font>")
			elif int_lng == 'English':
				par.ffw_label.setText("Form of mesh generation: " + "<font color='peru'>" + mesh_name_txt_cur + "</font>")
				
			 
			par.ffw_label.setStyleSheet("border-style: none;" "font-size: 9pt;")
			
			par.ffw.setTitleBarWidget(par.ffw_frame)
			par.ffw_frame.setFixedSize(838, 44)
           
			msh_lbl = QtGui.QLabel()
			if int_lng == 'Russian':
				msh_lbl.setText('Путь до расчетной сетки:')
			elif int_lng == 'English':
				msh_lbl.setText('Path to mesh file:')

			msh_lbl.setStyleSheet("border-style: none;" "font-size: 10pt;")
			msh_path_lbl = QtGui.QLineEdit()
			msh_path_lbl.setStyleSheet("background-color: white;" "font-size: 10pt;" "color: green;")
			msh_path_lbl.setFixedSize(500, 25)
			msh_path_lbl.setText(full_dir + '/system/' + mesh_name_txt_cur)
			msh_path_lbl.setEnabled(False)

			par.tdw_grid.addWidget(msh_lbl, 0, 2, alignment=QtCore.Qt.AlignCenter)
			par.tdw_grid.addWidget(msh_path_lbl, 0, 3, alignment=QtCore.Qt.AlignCenter)
			
			if self.nf_radio.isChecked() == True:
				if self.mesh_name.text() == '':
					if int_lng == 'Russian':
						dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Внимание!", "Укажите название сетки", buttons = QtGui.QMessageBox.Ok)
					elif int_lng == 'English':
						dialog = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "Attention!", "Specify name mesh", buttons = QtGui.QMessageBox.Ok)
					result = dialog.exec_()
				else:
					
					if self.bm.isChecked() == True:
						pckls_path = full_dir + '/system/'
						pd_2_cur = 'blockMesh'
						bmd_form = bmd_window_class(self, par, pckls_path, mesh_name_txt_cur, pd_2_cur)
						par.ffw.setWidget(bmd_form)
						par.setCentralWidget(par.ffw)
						self.close()

					elif self.shm.isChecked() == True:
						pckls_path = full_dir + '/system/'
						pd_2_cur = 'snappyHexMesh'
						shmd_form = shmd_window_class(self, par, pckls_path, mesh_name_txt_cur, pd_2_cur)
						par.ffw.setWidget(shmd_form)
						par.setCentralWidget(par.ffw)
						self.close()

					elif self.fqm.isChecked() == True:
						pckls_path = full_dir + '/system/'
						pd_2_cur = 'foamyQuadMesh'
						fqmd_form = fqmd_window_class(self, par, pckls_path, mesh_name_txt_cur, pd_2_cur)
						par.ffw.setWidget(fqmd_form)
						par.setCentralWidget(par.ffw)
						self.close()
					
					if os.path.exists(pckls_path + self.mesh_name.text()) == True:
						msh_msg_box = QtGui.QMessageBox()
						if int_lng == 'Russian':
							msh_msg_box.setText("Расчетная сетка с таким именем существует")
							msh_msg_box.setInformativeText("Заменить существующую сетку?")
						elif int_lng == 'English':
							msh_msg_box.setText("A calculated mesh with this name exists")
							msh_msg_box.setInformativeText("Replace an existing mesh?")

						msh_msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
						msh_msg_box.setDefaultButton(QMessageBox.Save)
						ret = msh_msg_box.exec_()
						
						if ret == QMessageBox.Save:
    						# Save was clicked
							shutil.rmtree(pckls_path)
							self.close()
						elif ret == QMessageBox.Discard:
    						# Don't save was clicked
							self.close()
							
			elif self.cf_radio.isChecked() == True:	
				
				msh_name_div, msh_type_div = pickles_dir.split("_")
				if msh_type_div == 'blockMesh':
					pd_2_cur = 'blockMesh'
					bmd_form = bmd_window_class(self, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur)
					par.ffw.setWidget(bmd_form)
					par.setCentralWidget(par.ffw)

				elif msh_type_div == 'snappyHexMesh':
					pd_2_cur = 'snappyHexMesh'
					shmd_form = shmd_window_class(self, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur)
					par.ffw.setWidget(shmd_form)
					par.setCentralWidget(par.ffw)

				elif msh_type_div == 'foamyQuadMesh':
					pd_2_cur = 'foamyQuadMesh'
					fqmd_form = fqmd_window_class(self, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur)
					par.ffw.setWidget(fqmd_form)
					par.setCentralWidget(par.ffw)

				if int_lng == 'Russian':
					msg = 'Загружены параметры сетки ' + self.mesh_name.text() + '. Установите ее в качестве текущей, выполнив создание файла ' + msh_type_div + 'Dict' + ' и генерацию сетки'
				elif int_lng == 'English':
					msg = 'Mesh parameters are loaded ' + self.mesh_name.text() + '. Set it as current by creating a ' + msh_type_div + 'Dict' + ' file and mesh generation'
				par.listWidget.clear()
				par.item = QtGui.QListWidgetItem(msg, par.listWidget)
				color = QtGui.QColor("blue")
				par.item.setTextColor(color)
				par.listWidget.addItem(par.item)	

				self.close()

				par.msh_run.setEnabled(True)
				par.msh_visual.setEnabled(True)
				par.on_prj_path_get(prj_path_cur, mesh_name_txt_cur)

	def int_lng_path_return(self):
		return(int_lng)

# .....................Функция, запускаемая при нажатии кнопки "отмена"......................#
        
	def on_cancel_clicked(self):
		self.close()
		
		
		
		
		
