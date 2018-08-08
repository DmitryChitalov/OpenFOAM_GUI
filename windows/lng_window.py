# -*- coding: utf-8 -*-
# -------------------------------Импорт модулей----------------------------------#

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path

from windows.bMD_window import bmd_window_class

# ---------------------------Главная форма проекта-------------------------------#
		
class lng_form_class(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowSystemMenuHint)
		self.setWindowModality(QtCore.Qt.WindowModal)

		global par
		par = parent
		
		global int_lng
		int_lng = par.interface_lng_val

# ------------------------------------Первый блок формы--------------------------------------#

		self.lng_label = QtGui.QLabel()
		self.lng_lbl_hbox = QtGui.QHBoxLayout()
		self.lng_lbl_hbox.addWidget(self.lng_label)
		self.ru_radio = QtGui.QRadioButton("Ru")
		self.en_radio = QtGui.QRadioButton("En")
		
		self.lng_grid = QtGui.QGridLayout()
		self.lng_grid.addWidget(self.ru_radio, 0, 0)
		self.lng_grid.addWidget(self.en_radio, 1, 0)
		
		self.lng_frame = QtGui.QFrame()
		self.lng_frame.setFrameShape(QtGui.QFrame.Panel)
		self.lng_frame.setFrameShadow(QtGui.QFrame.Sunken)
		self.lng_frame.setLayout(self.lng_grid)
		self.lng_hbox = QtGui.QVBoxLayout() 
		self.lng_hbox.addWidget(self.lng_frame)

		# ---------------------Кнопки сохранения и отмены и их блок-------------------------#

		self.save_button = QtGui.QPushButton()
		self.save_button.setFixedSize(80, 25)
		self.save_button.clicked.connect(self.on_save_clicked)
		self.cancel_button = QtGui.QPushButton()
		self.cancel_button.setFixedSize(80, 25)
		self.cancel_button.clicked.connect(self.on_cancel_clicked)
		self.buttons_hbox = QtGui.QHBoxLayout()
		self.buttons_hbox.addWidget(self.save_button)
		self.buttons_hbox.addWidget(self.cancel_button)

		# -------------------------Фрейм формы---------------------------#

		self.form_grid = QtGui.QGridLayout()
		self.form_grid.addLayout(self.lng_lbl_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
		self.form_grid.addLayout(self.lng_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		self.form_grid.addLayout(self.buttons_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
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
			self.lng_label.setText("Выберите язык интерфейса программы")
			self.save_button.setText("Сохранить")
			self.cancel_button.setText("Отмена")
			self.ru_radio.setChecked(True)
			
		elif int_lng == 'English':
			self.lng_label.setText("Select the interface language for the program")
			self.save_button.setText("Save")
			self.cancel_button.setText("Cancel")
			self.en_radio.setChecked(True)
			
	# ------------------------Функции связанные с формой-----------------------------#		
		
	# ....................Функция, запускаемая при нажатии кнопки "сохранить"....................#

	def on_save_clicked(self):
		if self.ru_radio.isChecked() == True:
			interface_lng = 'Russian'
		elif self.en_radio.isChecked() == True:
			interface_lng = 'English'
			
		while par.tdw_grid.count():
			item = par.tdw_grid.takeAt(0)
			widget = item.widget()
			widget.deleteLater()
			
		ldw_default = QtGui.QLabel()
		par.ldw.setWidget(ldw_default)
		par.ldw.setTitleBarWidget(ldw_default)
		
		serv_mes_default = QtGui.QLabel()
		par.serv_mes.setWidget(serv_mes_default)
		par.serv_mes.setWindowTitle("")
		
		cdw_default = QtGui.QLabel()
		par.cdw.setWidget(cdw_default)
		par.cdw.setTitleBarWidget(cdw_default)
		
		par.on_lng_get(interface_lng)
		self.close()

# .....................Функция, запускаемая при нажатии кнопки "отмена"......................#
        
	def on_cancel_clicked(self):
		self.close()
