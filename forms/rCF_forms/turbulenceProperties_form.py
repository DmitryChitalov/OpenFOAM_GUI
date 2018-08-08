# -*- coding: utf-8 -*-
# -----------------------------Импорт модулей-----------------------------------

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path

# -----------------------------------Форма--------------------------------------

class turbulenceProperties_form(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
		
        full_dir = parent.full_dir
        interface_lng_val = parent.interface_lng_val

# ------------------------Функции связанные с формой-----------------------------
        def on_btnSave_clicked():
            sT_txt = sT_name.currentText()
       
            file = open(full_dir+"/constant/turbulenceProperties", 'r') 
            data = file.read()
            file.close()

            sT_reg = re.compile(r"simulationType\s*\S*(?=[;])")
            sT_mas = sT_reg.findall(data)
            sT_txt_add = "simulationType  "+sT_txt
            data = data.replace(sT_mas[0], sT_txt_add)

            file = open(full_dir+"/constant/turbulenceProperties", 'w')  
            file.write(data)
            file.close()

            if interface_lng_val == 'Russian':
                msg = "Сохранен файл: turbulenceProperties"
            elif interface_lng_val == 'English':
                msg = "Saved file: turbulenceProperties"
            color = QtGui.QColor("green")
				
            if interface_lng_val == 'Russian':
                parent.outf_lbl.setText("Структура файла: " + "<font color='peru'>" + 'turbulenceProperties' + "</font>") 
            elif interface_lng_val == 'English':
                parent.outf_lbl.setText("The structure of file: " + "<font color='peru'>" + 'turbulenceProperties' + "</font>")
				
            file_form_path = full_dir + '/constant/turbulenceProperties'
            outf = open(file_form_path)
            data = outf.read()    
            parent.outf_edit.setText(data)
            parent.cdw.setWidget(parent.outf_scroll)
            parent.cdw.setTitleBarWidget(parent.cdw_frame)
			
            #parent.color = QtGui.QColor("green")
            #parent.item.setTextColor(parent.color)
            #parent.listWidget.addItem(parent.item)
            parent.listWidget.clear()
            parent.item = QtGui.QListWidgetItem(msg, parent.listWidget)
            parent.item.setTextColor(color)
            parent.listWidget.addItem(parent.item)

        def on_btnCancel_clicked():
            self.clear_label = QtGui.QLabel()
            parent.ffw.setTitleBarWidget(self.clear_label)
            self.close()

# -------------------------------Разметка формы----------------------------------

        sT_lbl = QtGui.QLabel("simulationType: ")
        sT_name = QtGui.QComboBox()
        sT_name.setFixedSize(100, 25)
        sT_list = ["demo", "laminar"]
        sT_name.addItems(sT_list)
        sT_grid = QtGui.QGridLayout()
        sT_grid.addWidget(sT_lbl, 0, 0)
        sT_grid.addWidget(sT_name, 0, 1)
        sT_frame = QtGui.QFrame()
        sT_frame.setFixedSize(210, 40)
        sT_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        sT_frame.setLayout(sT_grid)
        sT_hbox = QtGui.QHBoxLayout()
        sT_hbox.addWidget(sT_frame)

        # ---------------------Кнопки сохранения и отмены-----------------------

        btnSave = QtGui.QPushButton()
        btnSave.setFixedSize(80, 25)
        btnSave.clicked.connect(on_btnSave_clicked)
        btnCancel = QtGui.QPushButton()
        btnCancel.setFixedSize(80, 25)
        btnCancel.clicked.connect(on_btnCancel_clicked)
        buttons_hbox = QtGui.QHBoxLayout()
        buttons_hbox.addWidget(btnSave)
        buttons_hbox.addWidget(btnCancel)
		
        if interface_lng_val == 'Russian':
            btnSave.setText("Сохранить")
            btnCancel.setText("Отмена")
        elif interface_lng_val == 'English':
            btnSave.setText("Save")
            btnCancel.setText("Cancel")

        # --------------------Фрейм элементов управления------------------------

        turbProp_grid = QtGui.QGridLayout()
        turbProp_grid.addLayout(sT_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
        turbProp_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        turbProp_frame = QtGui.QFrame()
        turbProp_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        turbProp_frame.setFrameShape(QtGui.QFrame.Panel)
        turbProp_frame.setFrameShadow(QtGui.QFrame.Sunken)
        turbProp_frame.setLayout(turbProp_grid)
        turbProp_vbox = QtGui.QVBoxLayout() 
        turbProp_vbox.addWidget(turbProp_frame)

# ---------------------Размещение на форме всех компонентов-------------------------

        form_1 = QtGui.QFormLayout()
        form_1.addRow(turbProp_vbox)
        self.setLayout(form_1)

# --------------------------Функции связанные c выводом-----------------------------

        file = open(full_dir+"/constant/turbulenceProperties", 'r') 
        data = file.read()
        file.close()

        sT_reg = re.compile(r"simulationType\s*\S*(?=[;])")
        sT_mas = sT_reg.findall(data) 
        
        sT_name_div = sT_mas[0].split()
        sT_name_mas = sT_name.count()   
        for i in range(sT_name_mas):
            if sT_name.itemText(i) == sT_name_div[1]:
                sT_name.setCurrentIndex(i)

