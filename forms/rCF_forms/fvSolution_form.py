# -*- coding: utf-8 -*-
# -----------------------------Импорт модулей-----------------------------------

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path

# -----------------------------------Форма--------------------------------------

class fvSolution_form(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
		
        full_dir = parent.full_dir
        interface_lng_val = parent.interface_lng_val

# ------------------------Функции связанные с формой-----------------------------
        def on_btnSave_clicked():
            solver_txt = solver_name.currentText()
            
            solv_txt = solv_name.currentText()
            smooth_txt = smooth_name.currentText()
            nS_txt = str(nS_name.value())
            tol_txt = tol_name.text()
            relTol_txt = relTol_name.text()
            
            toler_txt = toler_name.text()
            rT_txt = rT_name.text()
       
            file = open(full_dir+"/system/fvSolution", 'r') 
            data = file.read()
            file.close()

            slvrs_reg = re.compile(r"\s*\{\n\s*\S*\s*\S*\n\s*\}")
            slvrs_mas = slvrs_reg.findall(data)
            slvrs_txt_add = "\n"+"    "+"{"+"\n"+"        "+"solver"+"          "+solver_txt+";"+"\n"+"    "+"}"
            data = data.replace(slvrs_mas[0], slvrs_txt_add)

            U_reg = re.compile(r"\s*U\n\s*\{\n\s*\S*\s*\S*\n\s*\S*\s*\S*\n\s*\S*\s*\S*\n\s*\S*\s*\S*\n\s*\S*\s*\S*\n\s*\}")
            U_mas = U_reg.findall(data)
            U1="solver"+"          "+solv_txt+";"+"\n"+"        "
            U2="smoother"+"        "+smooth_txt+";"+"\n"+"        "
            U3="nSweeps"+"         "+nS_txt+";"+"\n"+"        "
            U4="tolerance"+"       "+tol_txt+";"+"\n"+"    "+"    "
            U5="relTol"+"          "+relTol_txt+";"+"\n"+"    "
            U_txt_add = "\n"+"\n"+"    "+"U"+"\n"+"    "+"{"+"\n"+"        "+U1+U2+U3+U4+U5+"}"
            data = data.replace(U_mas[0], U_txt_add)

            h_reg = re.compile(r"\s*h\n\s*\{\n\s*\S*\n\s*\S*\s*\S*\n\s*\S*\s*\S*\n\s*\}")
            h_mas = h_reg.findall(data)
            h1="$U;"+"\n"+"        "
            h2="tolerance"+"       "+toler_txt+";"+"\n"+"        "
            h3="relTol"+"          "+rT_txt+";"+"\n"+"    "
            h_txt_add = "\n"+"\n"+"    "+"h"+"\n"+"    "+"{"+"\n"+"        "+h1+h2+h3+"}"
            data = data.replace(h_mas[0], h_txt_add)

            file = open(full_dir+"/system/fvSolution", 'w')  
            file.write(data)
            file.close()
            
            if interface_lng_val == 'Russian':
                msg = "Сохранен файл: fvSolution"
            elif interface_lng_val == 'English':
                msg = "Saved file: fvSolution"
            color = QtGui.QColor("green")
            #parent.item.setTextColor(parent.color)
            #parent.listWidget.addItem(parent.item)
            parent.listWidget.clear()
            parent.item = QtGui.QListWidgetItem(msg, parent.listWidget)
            parent.item.setTextColor(color)
            parent.listWidget.addItem(parent.item)
			
            if interface_lng_val == 'Russian':
                parent.outf_lbl.setText("Структура файла: " + "<font color='peru'>" + 'fvSolution' + "</font>") 
            elif interface_lng_val == 'English':
                parent.outf_lbl.setText("The structure of file: " + "<font color='peru'>" + 'fvSolution' + "</font>")

            file_form_path = full_dir + '/system/fvSolution'
            outf = open(file_form_path)
            data = outf.read()    
            parent.outf_edit.setText(data)
            parent.cdw.setWidget(parent.outf_scroll)
            parent.cdw.setTitleBarWidget(parent.cdw_frame)

        def on_btnCancel_clicked():
            self.clear_label = QtGui.QLabel()
            parent.ffw.setTitleBarWidget(self.clear_label)
            self.close()

# -------------------------------Разметка формы----------------------------------
        
        # ---------------------Решатели---------------------

        slvrs_lbl = QtGui.QLabel("Solvers")

        # ---------------------Solver---------------------

        solver_lbl = QtGui.QLabel("solver: ")
        solver_name = QtGui.QComboBox()
        solver_name.setFixedSize(100, 25)
        solver_list = ["diagonal"]
        solver_name.addItems(solver_list)
        solver_grid = QtGui.QGridLayout()
        solver_grid.addWidget(solver_lbl, 0, 0)
        solver_grid.addWidget(solver_name, 0, 1)
        solver_frame = QtGui.QFrame()
        solver_frame.setFixedSize(190, 40)
        solver_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        solver_frame.setLayout(solver_grid)
        solver_hbox = QtGui.QHBoxLayout()
        solver_hbox.addWidget(solver_frame)
        
        # ---------------------U---------------------
        
        U_lbl = QtGui.QLabel("U:")
        U_lbl.setStyleSheet("qproperty-alignment: AlignCenter;")
        U_lbl_hbox = QtGui.QHBoxLayout()
        U_lbl_hbox.addWidget(U_lbl)
        solv_lbl = QtGui.QLabel("solver: ")
        solv_name = QtGui.QComboBox()
        solv_name.setFixedSize(100, 25)
        solv_list = ["smoothSolver"]
        solv_name.addItems(solv_list)
        smooth_lbl = QtGui.QLabel("smoother: ")
        smooth_name = QtGui.QComboBox()
        smooth_name.setFixedSize(100, 25)
        smooth_list = ["GaussSeidel"]
        smooth_name.addItems(smooth_list)
        nS_lbl = QtGui.QLabel("nSweeps: ")
        nS_name = QtGui.QSpinBox()
        nS_name.setFixedSize(100, 25)
        tol_lbl = QtGui.QLabel("tolerance: ")
        tol_name = QtGui.QLineEdit()
        tol_name.setFixedSize(100, 25)
        #tol_name.setInputMask("9e-99;_")
        relTol_lbl = QtGui.QLabel("relTol: ")
        relTol_name = QtGui.QLineEdit()
        relTol_name.setFixedSize(100, 25)
        valid = QtGui.QRegExpValidator(QtCore.QRegExp("\S*"))
        relTol_name.setValidator(valid)
        U_grid = QtGui.QGridLayout()
        U_grid.addWidget(solv_lbl, 0, 0)
        U_grid.addWidget(solv_name, 0, 1)
        U_grid.addWidget(smooth_lbl, 1, 0)
        U_grid.addWidget(smooth_name, 1, 1)
        U_grid.addWidget(nS_lbl, 2, 0)
        U_grid.addWidget(nS_name, 2, 1)
        U_grid.addWidget(tol_lbl, 3, 0)
        U_grid.addWidget(tol_name, 3, 1)
        U_grid.addWidget(relTol_lbl, 4, 0)
        U_grid.addWidget(relTol_name, 4, 1)
        U_frame = QtGui.QFrame()
        U_frame.setFixedSize(190, 170)
        U_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        U_frame.setLayout(U_grid)
        U_hbox = QtGui.QHBoxLayout()
        U_hbox.addWidget(U_frame)

        # ---------------------e---------------------
       
        e_lbl = QtGui.QLabel("h:")
        e_lbl.setStyleSheet("qproperty-alignment: AlignCenter;")
        e_lbl_hbox = QtGui.QHBoxLayout()
        e_lbl_hbox.addWidget(e_lbl)
        toler_lbl = QtGui.QLabel("tolerance: ")
        toler_name = QtGui.QLineEdit()
        toler_name.setFixedSize(100, 25)
        #toler_name.setInputMask("9e-99;_")
        rT_lbl = QtGui.QLabel("relTol: ")
        rT_name = QtGui.QLineEdit()
        rT_name.setFixedSize(100, 25)
        valid = QtGui.QRegExpValidator(QtCore.QRegExp("\S*"))
        rT_name.setValidator(valid)
        e_grid = QtGui.QGridLayout()
        e_grid.addWidget(toler_lbl, 0, 0)
        e_grid.addWidget(toler_name, 0, 1)
        e_grid.addWidget(rT_lbl, 1, 0)
        e_grid.addWidget(rT_name, 1, 1)
        e_frame = QtGui.QFrame()
        e_frame.setFixedSize(190, 80)
        e_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        e_frame.setLayout(e_grid)
        e_hbox = QtGui.QHBoxLayout()
        e_hbox.addWidget(e_frame)

        # ---------------------Кнопки-----------------------

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

        # --------------------------------------------------

        fvSolution_grid = QtGui.QGridLayout()
        fvSolution_grid.addWidget(slvrs_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
        fvSolution_grid.addLayout(solver_hbox, 1, 0)
        fvSolution_grid.addLayout(U_lbl_hbox, 2, 0)
        fvSolution_grid.addLayout(U_hbox, 3, 0)
        fvSolution_grid.addLayout(e_lbl_hbox, 4, 0)
        fvSolution_grid.addLayout(e_hbox, 5, 0)
        fvSolution_grid.addLayout(buttons_hbox, 6, 0, alignment=QtCore.Qt.AlignCenter)
        fvSolution_frame = QtGui.QFrame()
        fvSolution_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        fvSolution_frame.setFrameShape(QtGui.QFrame.Panel)
        fvSolution_frame.setFrameShadow(QtGui.QFrame.Sunken)
        fvSolution_frame.setLayout(fvSolution_grid)
        fvSolution_vbox = QtGui.QVBoxLayout() 
        fvSolution_vbox.addWidget(fvSolution_frame)

# ---------------------Размещение на форме всех компонентов-------------------------

        form_1 = QtGui.QFormLayout()
        form_1.addRow(fvSolution_vbox)
        self.setLayout(form_1)

# --------------------------Функции связанные c выводом-----------------------------
        

        file = open(full_dir+"/system/fvSolution", 'r') 
        data = file.read()
        file.close()

        s_reg = re.compile(r"solver\s*\S*(?=[;])")
        s_mas = s_reg.findall(data) 
        
        solver_name_div = s_mas[0].split()
        solver_name_mas = solver_name.count()   
        for i in range(solver_name_mas):
            if solver_name.itemText(i) == solver_name_div[1]:
                solver_name.setCurrentIndex(i)

        solv_name_div = s_mas[1].split()
        solv_name_mas = solv_name.count()   
        for i in range(solv_name_mas):
            if solv_name.itemText(i) == solv_name_div[1]:
                solv_name.setCurrentIndex(i)

        nS_reg = re.compile(r"nSweeps\s*\S*(?=[;])")
        nS_mas = nS_reg.findall(data)
        nS_div = nS_mas[0].split("         ")
        nS_name.setValue(int(nS_div[1]))
        
        tol_reg = re.compile(r"tolerance\s*\S*(?=[;])")
        tol_mas = tol_reg.findall(data)
        tol_div = tol_mas[0].split("       ")
        tol_name.setText(tol_div[1])
        toler_div = tol_mas[1].split("       ")
        toler_name.setText(toler_div[1])

        relTol_reg = re.compile(r"relTol\s*\S*(?=[;])")
        relTol_mas = relTol_reg.findall(data)
        relTol_div = relTol_mas[0].split("          ")
        relTol_name.setText(relTol_div[1])
        rT_div = relTol_mas[1].split("          ")
        rT_name.setText(rT_div[1])

