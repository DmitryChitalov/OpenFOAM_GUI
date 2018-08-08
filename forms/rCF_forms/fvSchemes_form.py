# -*- coding: utf-8 -*-
# -----------------------------Импорт модулей-----------------------------------

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path

# -----------------------------------Форма--------------------------------------

class fvSchemes_form(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
		
        full_dir = parent.full_dir
        interface_lng_val = parent.interface_lng_val

# ------------------------Функции связанные с формой-----------------------------

        def on_btnSave_clicked():
            fS_txt = fS_edit.currentText()
            ddtS_txt = ddtS_edit.currentText()
            gS_txt = gS_edit.currentText()
            dS_txt = dS_edit.currentText()
            dtMC_txt = dtMC_edit.currentText()
            lS_txt = lS_edit.currentText()
            iS_txt = iS_edit.currentText()
            rR_txt = rR_edit.currentText()
            rU_txt = rU_edit.currentText()
            rT_txt = rT_edit.currentText()
            sGS_txt = sGS_edit.currentText()
                     
            file = open(full_dir+"/system/fvSchemes", 'r') 
            data = file.read()
            file.close()

            fS_reg = re.compile(r"fluxScheme\s*\S*(?=[;])")
            fS_mas = fS_reg.findall(data)
            fS_txt_add = "fluxScheme      "+fS_txt
            data = data.replace(fS_mas[0], fS_txt_add)

            ddtS_reg = re.compile(r"ddtSchemes\s*\n\{\s*\n\s*default\s*\S*(?=[;])")
            ddtS_mas = ddtS_reg.findall(data)
            ddtS_txt_add = "ddtSchemes"+"\n"+"{"+"\n"+"    "+"default"+"         "+ddtS_txt
            data = data.replace(ddtS_mas[0], ddtS_txt_add)

            gS_reg = re.compile(r"gradSchemes\s*\n\{\s*\n\s*default\s*\S*(?=[;])|gradSchemes\s*\n\{\s*\n\s*default\s*\S*\s\S*(?=[;])|gradSchemes\s*\n\{\s*\n\s*default\s*\S*\s\S*\s\S*(?=[;])")
            gS_mas = gS_reg.findall(data)
            gS_txt_add = "gradSchemes"+"\n"+"{"+"\n"+"    "+"default"+"         "+gS_txt
            data = data.replace(gS_mas[0], gS_txt_add)

            dS_reg = re.compile(r"divSchemes\s*\n\{\s*\n\s*default\s*\S*(?=[;])")
            dS_mas = dS_reg.findall(data)
            dS_txt_add = "divSchemes"+"\n"+"{"+"\n"+"    "+"default"+"         "+dS_txt
            data = data.replace(dS_mas[0], dS_txt_add)

            dtMC_reg = re.compile(r"div\(tauMC\)\s*\S*(?=[;])|div\(tauMC\)\s*\S*\s\S*(?=[;])|div\(tauMC\)\s*\S*\s\S*\s\S*(?=[;])")
            dtMC_mas = dtMC_reg.findall(data)
            dtMC_txt_add = "div(tauMC)      "+dtMC_txt
            data = data.replace(dtMC_mas[0], dtMC_txt_add)

            lS_reg = re.compile(r"laplacianSchemes\s*\n\{\s*\n\s*default\s*\S*(?=[;])|laplacianSchemes\s*\n\{\s*\n\s*default\s*\S*\s\S*(?=[;])|laplacianSchemes\s*\n\{\s*\n\s*default\s*\S*\s\S*\s\S*(?=[;])")
            lS_mas = lS_reg.findall(data)
            lS_txt_add = "laplacianSchemes"+"\n"+"{"+"\n"+"    "+"default"+"         "+lS_txt
            data = data.replace(lS_mas[0], lS_txt_add)

            iS_reg = re.compile(r"interpolationSchemes\s*\n\{\s*\n\s*default\s*\S*(?=[;])")
            iS_mas = iS_reg.findall(data)
            iS_txt_add = "interpolationSchemes"+"\n"+"{"+"\n"+"    "+"default"+"          "+iS_txt
            data = data.replace(iS_mas[0], iS_txt_add)

            rR_reg = re.compile(r"reconstruct\(rho\)\s*\S*(?=[;])")
            rR_mas = rR_reg.findall(data)
            rR_txt_add = "reconstruct(rho)"+" "+rR_txt
            data = data.replace(rR_mas[0], rR_txt_add)

            rU_reg = re.compile(r"reconstruct\(U\)\s*\S*(?=[;])")
            rU_mas = rU_reg.findall(data)
            rU_txt_add = "reconstruct(U)"+"   "+rU_txt
            data = data.replace(rU_mas[0], rU_txt_add)

            rT_reg = re.compile(r"reconstruct\(T\)\s*\S*(?=[;])")
            rT_mas = rT_reg.findall(data)
            rT_txt_add = "reconstruct(T)"+"   "+rT_txt
            data = data.replace(rT_mas[0], rT_txt_add)

            sGS_reg = re.compile(r"snGradSchemes\s*\n\{\s*\n\s*default\s*\S*(?=[;])|snGradSchemes\s*\n\{\s*\n\s*default\s*\S*\s\S*(?=[;])|snGradSchemes\s*\n\{\s*\n\s*default\s*\S*\s\S*\s\S*(?=[;])")
            sGS_mas = sGS_reg.findall(data)
            sGS_txt_add = "snGradSchemes"+"\n"+"{"+"\n"+"    "+"default"+"         "+sGS_txt
            data = data.replace(sGS_mas[0], sGS_txt_add)

            file = open(full_dir+"/system/fvSchemes", 'w')  
            file.write(data)
            file.close()
            
            if interface_lng_val == 'Russian':
                msg = "Сохранен файл: fvSchemes"
            elif interface_lng_val == 'English':
                msg = "Saved file: fvSchemes"
            color = QtGui.QColor("green")
			
            parent.listWidget.clear()
            parent.item = QtGui.QListWidgetItem(msg, parent.listWidget)
            parent.item.setTextColor(color)
            parent.listWidget.addItem(parent.item)
			
            if interface_lng_val == 'Russian':
                parent.outf_lbl.setText("Структура файла: " + "<font color='peru'>" + 'fvSchemes' + "</font>") 
            elif interface_lng_val == 'English':
                parent.outf_lbl.setText("The structure of file: " + "<font color='peru'>" + 'fvSchemes' + "</font>")

            file_form_path = full_dir + '/system/fvSchemes'
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
        
        # -------------Элементы управления------------
        fS_lbl = QtGui.QLabel("fluxScheme:")
        fS_edit = QtGui.QComboBox()
        fS_edit.setFixedSize(150, 25)
        fS_list = ["Tadmor", "Kurganov"]
        fS_edit.addItems(fS_list)
        fS_hbox = QtGui.QHBoxLayout()
        fS_hbox.addWidget(fS_lbl)
        fS_hbox.addWidget(fS_edit)
        ddtS_lbl = QtGui.QLabel("ddtSchemes:")
        ddtS_edit = QtGui.QComboBox()
        ddtS_edit.setFixedSize(150, 25)
        ddtS_list = ["demo", "Euler"]
        ddtS_edit.addItems(ddtS_list)
        ddtS_hbox = QtGui.QHBoxLayout()
        ddtS_hbox.addWidget(ddtS_lbl)
        ddtS_hbox.addWidget(ddtS_edit)
        gS_lbl = QtGui.QLabel("gradSchemes:")
        gS_edit = QtGui.QComboBox()
        gS_edit.setFixedSize(150, 25)
        gS_list = ["Gauss linear corrected", "Gauss linear"]
        gS_edit.addItems(gS_list)
        gS_hbox = QtGui.QHBoxLayout()
        gS_hbox.addWidget(gS_lbl)
        gS_hbox.addWidget(gS_edit)
        dS_lbl = QtGui.QLabel("divSchemes:")
        dS_edit = QtGui.QComboBox()
        dS_edit.setFixedSize(150, 25)
        dS_list = ["demo", "none"]
        dS_edit.addItems(dS_list)
        dS_hbox = QtGui.QHBoxLayout()
        dS_hbox.addWidget(dS_lbl)
        dS_hbox.addWidget(dS_edit)
        dtMC_lbl = QtGui.QLabel("div(tauMC):")
        dtMC_edit = QtGui.QComboBox()
        dtMC_edit.setFixedSize(150, 25)
        dtMC_list = ["Gauss linear corrected", "Gauss linear"]
        dtMC_edit.addItems(dtMC_list)
        dtMC_hbox = QtGui.QHBoxLayout()
        dtMC_hbox.addWidget(dtMC_lbl)
        dtMC_hbox.addWidget(dtMC_edit)
        dS_grid = QtGui.QGridLayout()
        dS_grid.addLayout(dS_hbox, 0, 0)
        dS_grid.addLayout(dtMC_hbox, 1, 0)
        dS_frame = QtGui.QFrame()
        dS_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        dS_frame.setLayout(dS_grid)
        dS_vbox = QtGui.QVBoxLayout() 
        dS_vbox.addWidget(dS_frame)
        lS_lbl = QtGui.QLabel("laplacianSchemes:")
        lS_edit = QtGui.QComboBox()
        lS_edit.setFixedSize(150, 25)
        lS_list = ["Gauss linear", "Gauss linear corrected"]
        lS_edit.addItems(lS_list)
        lS_hbox = QtGui.QHBoxLayout()
        lS_hbox.addWidget(lS_lbl)
        lS_hbox.addWidget(lS_edit)
        iS_lbl = QtGui.QLabel("interpolationSchemes:")
        iS_edit = QtGui.QComboBox()
        iS_edit.setFixedSize(150, 25)
        iS_list = ["demo", "linear"]
        iS_edit.addItems(iS_list)
        iS_hbox = QtGui.QHBoxLayout()
        iS_hbox.addWidget(iS_lbl)
        iS_hbox.addWidget(iS_edit)
        rR_lbl = QtGui.QLabel("reconstruct(rho):")
        rR_edit = QtGui.QComboBox()
        rR_edit.setFixedSize(150, 25)
        rR_list = ["demo", "vanLeer"]
        rR_edit.addItems(rR_list)
        rR_hbox = QtGui.QHBoxLayout()
        rR_hbox.addWidget(rR_lbl)
        rR_hbox.addWidget(rR_edit)
        rU_lbl = QtGui.QLabel("reconstruct(U):")
        rU_edit = QtGui.QComboBox()
        rU_edit.setFixedSize(150, 25)
        rU_list = ["demo", "vanLeerV"]
        rU_edit.addItems(rU_list)
        rU_hbox = QtGui.QHBoxLayout()
        rU_hbox.addWidget(rU_lbl)
        rU_hbox.addWidget(rU_edit)
        rT_lbl = QtGui.QLabel("reconstruct(T):")
        rT_edit = QtGui.QComboBox()
        rT_edit.setFixedSize(150, 25)
        rT_list = ["demo", "vanLeer"]
        rT_edit.addItems(rT_list)
        rT_hbox = QtGui.QHBoxLayout()
        rT_hbox.addWidget(rT_lbl)
        rT_hbox.addWidget(rT_edit)
        iS_grid = QtGui.QGridLayout()
        iS_grid.addLayout(iS_hbox, 0, 0)
        iS_grid.addLayout(rR_hbox, 1, 0)
        iS_grid.addLayout(rU_hbox, 2, 0)
        iS_grid.addLayout(rT_hbox, 3, 0)
        iS_frame = QtGui.QFrame()
        iS_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        iS_frame.setLayout(iS_grid)
        iS_vbox = QtGui.QVBoxLayout() 
        iS_vbox.addWidget(iS_frame)
        sGS_lbl = QtGui.QLabel("snGradSchemes:")
        sGS_edit = QtGui.QComboBox()
        sGS_edit.setFixedSize(150, 25)
        sGS_list = ["demo", "corrected"]
        sGS_edit.addItems(sGS_list)
        sGS_hbox = QtGui.QHBoxLayout()
        sGS_hbox.addWidget(sGS_lbl)
        sGS_hbox.addWidget(sGS_edit)

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

        # -------------------Фрейм элементов управления---------------------

        prs_grid = QtGui.QGridLayout()
        prs_grid.addLayout(fS_hbox, 0, 0)
        prs_grid.addLayout(ddtS_hbox, 1, 0)
        prs_grid.addLayout(gS_hbox, 2, 0)
        prs_grid.addLayout(dS_vbox, 3, 0)
        prs_grid.addLayout(lS_hbox, 4, 0)
        prs_grid.addLayout(iS_vbox, 5, 0)
        prs_grid.addLayout(sGS_hbox, 6, 0)
        prs_frame = QtGui.QFrame()
        prs_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        prs_frame.setLayout(prs_grid)

        # -------------------------Фрейм формы---------------------------

        fvS_grid = QtGui.QGridLayout()
        fvS_grid.addWidget(prs_frame, 0, 0, alignment=QtCore.Qt.AlignCenter)
        fvS_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        fvS_frame = QtGui.QFrame()
        fvS_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        fvS_frame.setLayout(fvS_grid)
        fvS_vbox = QtGui.QVBoxLayout() 
        fvS_vbox.addWidget(fvS_frame)

# ---------------------Размещение на форме всех компонентов-------------------------

        form = QtGui.QFormLayout()
        form.addRow(fvS_vbox)
        self.setLayout(form)

# --------------------------Функции связанные c выводом-----------------------------
      
        file = open(full_dir+"/system/fvSchemes", 'r') 
        data = file.read()
        file.close()

        fS_reg = re.compile(r"fluxScheme\s*\S*(?=[;])")
        fS_mas = fS_reg.findall(data)
        fS_div = fS_mas[0].split()
        fS_edit_mas = fS_edit.count()   
        for i in range(fS_edit_mas):
            if fS_edit.itemText(i) == fS_div[1]:
                fS_edit.setCurrentIndex(i)

        def_reg = re.compile(r"default\s*\S*(?=[;])|default\s*\S*\s\S*(?=[;])|default\s*\S*\s\S*\s\S*(?=[;])")
        def_mas = def_reg.findall(data)
        
        ddtS_div = def_mas[0].split("         ")
        ddtS_edit_mas = ddtS_edit.count()   
        for i in range(ddtS_edit_mas):
            if ddtS_edit.itemText(i) == ddtS_div[1]:
                ddtS_edit.setCurrentIndex(i)

        gS_div = def_mas[1].split("         ")
        gS_edit_mas = gS_edit.count()   
        for i in range(gS_edit_mas):
            if gS_edit.itemText(i) == gS_div[1]:
                gS_edit.setCurrentIndex(i)

        dS_div = def_mas[2].split("         ")
        dS_edit_mas = dS_edit.count()   
        for i in range(dS_edit_mas):
            if dS_edit.itemText(i) == dS_div[1]:
                dS_edit.setCurrentIndex(i)

        lS_div = def_mas[3].split("         ")
        lS_edit_mas = lS_edit.count()   
        for i in range(lS_edit_mas):
            if lS_edit.itemText(i) == lS_div[1]:
                lS_edit.setCurrentIndex(i)
                
        iS_div = def_mas[4].split("          ")
        iS_edit_mas = iS_edit.count()   
        for i in range(iS_edit_mas):
            if iS_edit.itemText(i) == iS_div[1]:
                iS_edit.setCurrentIndex(i)

        sGS_div = def_mas[5].split("         ")
        sGS_edit_mas = sGS_edit.count()   
        for i in range(sGS_edit_mas):
            if sGS_edit.itemText(i) == sGS_div[1]:
                sGS_edit.setCurrentIndex(i)

        dtMC_reg = re.compile(r"div\(tauMC\)\s*\S*(?=[;])|div\(tauMC\)\s*\S*\s\S*(?=[;])|div\(tauMC\)\s*\S*\s\S*\s\S*(?=[;])")
        dtMC_mas = dtMC_reg.findall(data)
        dtMC_div = dtMC_mas[0].split("      ")
        dtMC_edit_mas = dtMC_edit.count()   
        for i in range(dtMC_edit_mas):
            if dtMC_edit.itemText(i) == dtMC_div[1]:
                dtMC_edit.setCurrentIndex(i)

        rR_reg = re.compile(r"reconstruct\(rho\)\s\S*(?=[;])")
        rR_mas = rR_reg.findall(data)
        rR_div = rR_mas[0].split(" ")
        rR_edit_mas = rR_edit.count()   
        for i in range(rR_edit_mas):
            if rR_edit.itemText(i) == rR_div[1]:
                rR_edit.setCurrentIndex(i)

        rU_reg = re.compile(r"reconstruct\(U\)\s*\S*(?=[;])")
        rU_mas = rU_reg.findall(data)
        rU_div = rU_mas[0].split("   ")
        rU_edit_mas = rU_edit.count()   
        for i in range(rU_edit_mas):
            if rU_edit.itemText(i) == rU_div[1]:
                rU_edit.setCurrentIndex(i)

        rT_reg = re.compile(r"reconstruct\(T\)\s*\S*(?=[;])")
        rT_mas = rT_reg.findall(data)
        rT_div = rT_mas[0].split("   ")
        rT_edit_mas = rT_edit.count()   
        for i in range(rT_edit_mas):
            if rT_edit.itemText(i) == rT_div[1]:
                rT_edit.setCurrentIndex(i)

