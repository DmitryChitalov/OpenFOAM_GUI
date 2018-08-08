# -*- coding: utf-8 -*-
# -----------------------------Импорт модулей-----------------------------------

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path

# -----------------------------------Форма--------------------------------------

class controlDict_form(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
		
        full_dir = parent.full_dir
        interface_lng_val = parent.interface_lng_val

# ------------------------Функции связанные с формой-----------------------------

        def on_btnSave_clicked():
            sF_txt = sF_edit.currentText()
            sT_txt = sT_edit.value()
            sA_txt = sA_edit.currentText()
            eT_txt = eT_edit.text()
            dT_txt = dT_edit.text()
            wC_txt = wC_edit.currentText()
            wI_txt = wI_edit.text()
            pW_txt = pW_edit.value()
            wF_txt = wF_edit.currentText()
            wP_txt = wP_edit.value()
            wComp_txt = wComp_edit.currentText()
            tF_txt = tF_edit.currentText()
            tP_txt = tP_edit.value()
            gF_txt = gF_edit.currentText()
            rTM_txt = rTM_edit.currentText()
            aTS_txt = aTS_edit.currentText()
            mC_txt = mC_edit.text()
            mDT_txt = mDT_edit.text()
                        
            file = open(full_dir+"/system/controlDict", 'r') 
            data = file.read()
            file.close()

            sF_reg = re.compile(r"startFrom\s*\S*(?=[;])")
            sF_mas = sF_reg.findall(data)
            sF_txt_add = "startFrom       "+sF_txt
            data = data.replace(sF_mas[0], sF_txt_add)

            sT_reg = re.compile(r"startTime\s*\S*(?=[;])")
            sT_mas = sT_reg.findall(data)
            sT_txt_add = "startTime       "+str(sT_txt)
            data = data.replace(sT_mas[1], sT_txt_add)

            sA_reg = re.compile(r"stopAt\s*\S*(?=[;])")
            sA_mas = sA_reg.findall(data)
            sA_txt_add = "stopAt          "+sA_txt
            data = data.replace(sA_mas[0], sA_txt_add)

            eT_reg = re.compile(r"endTime\s*\S*(?=[;])")
            eT_mas = eT_reg.findall(data)
            eT_txt_add = "endTime         "+eT_txt
            data = data.replace(eT_mas[1], eT_txt_add)

            dT_reg = re.compile(r"deltaT\s*\S*(?=[;])")
            dT_mas = dT_reg.findall(data)
            dT_txt_add = "deltaT          "+dT_txt
            data = data.replace(dT_mas[0], dT_txt_add)

            wC_reg = re.compile(r"writeControl\s*\S*(?=[;])")
            wC_mas = wC_reg.findall(data)
            wC_txt_add = "writeControl    "+wC_txt
            data = data.replace(wC_mas[0], wC_txt_add)
            
            wI_reg = re.compile(r"writeInterval\s*\S*(?=[;])")
            wI_mas = wI_reg.findall(data)
            wI_txt_add = "writeInterval   "+wI_txt
            data = data.replace(wI_mas[0], wI_txt_add)

            pW_reg = re.compile(r"purgeWrite\s*\S*(?=[;])")
            pW_mas = pW_reg.findall(data)
            pW_txt_add = "purgeWrite      "+str(pW_txt)
            data = data.replace(pW_mas[0], pW_txt_add)

            wF_reg = re.compile(r"writeFormat\s*\S*(?=[;])")
            wF_mas = wF_reg.findall(data)
            wF_txt_add = "writeFormat     "+wF_txt
            data = data.replace(wF_mas[0], wF_txt_add)

            wP_reg = re.compile(r"writePrecision\s*\S*(?=[;])")
            wP_mas = wP_reg.findall(data)
            wP_txt_add = "writePrecision  "+str(wP_txt)
            data = data.replace(wP_mas[0], wP_txt_add)

            wComp_reg = re.compile(r"writeCompression\s*\S*(?=[;])")
            wComp_mas = wComp_reg.findall(data)
            wComp_txt_add = "writeCompression "+wComp_txt
            data = data.replace(wComp_mas[0], wComp_txt_add)

            tF_reg = re.compile(r"timeFormat\s*\S*(?=[;])")
            tF_mas = tF_reg.findall(data)
            tF_txt_add = "timeFormat      "+tF_txt
            data = data.replace(tF_mas[0], tF_txt_add)

            tP_reg = re.compile(r"timePrecision\s*\S*(?=[;])")
            tP_mas = tP_reg.findall(data)
            tP_txt_add = "timePrecision   "+str(tP_txt)
            data = data.replace(tP_mas[0], tP_txt_add)
			
            gF_reg = re.compile(r"graphFormat\s*\S*(?=[;])")
            gF_mas = gF_reg.findall(data)
            gF_txt_add = "graphFormat     "+str(gF_txt)
            data = data.replace(gF_mas[0], gF_txt_add)

            rTM_reg = re.compile(r"runTimeModifiable\s*\S*(?=[;])")
            rTM_mas = rTM_reg.findall(data)
            rTM_txt_add = "runTimeModifiable "+rTM_txt
            data = data.replace(rTM_mas[0], rTM_txt_add)

            aTS_reg = re.compile(r"adjustTimeStep\s*\S*(?=[;])")
            aTS_mas = aTS_reg.findall(data)
            aTS_txt_add = "adjustTimeStep  "+aTS_txt
            data = data.replace(aTS_mas[0], aTS_txt_add)

            mC_reg = re.compile(r"maxCo\s*\S*(?=[;])")
            mC_mas = mC_reg.findall(data)
            mC_txt_add = "maxCo           "+str(mC_txt)
            data = data.replace(mC_mas[0], mC_txt_add)

            mDT_reg = re.compile(r"maxDeltaT\s*\S*(?=[;])")
            mDT_mas = mDT_reg.findall(data)
            mDT_txt_add = "maxDeltaT       "+mDT_txt
            data = data.replace(mDT_mas[0], mDT_txt_add)

            file = open(full_dir+"/system/controlDict", 'w')  
            file.write(data)
            file.close()
            
            if interface_lng_val == 'Russian':
                msg = "Сохранен файл: controlDict"
            elif interface_lng_val == 'English':
                msg = "Saved file: controlDict"
            color = QtGui.QColor("green")
			
            parent.listWidget.clear()
            parent.item = QtGui.QListWidgetItem(msg, parent.listWidget)
            parent.item.setTextColor(color)
            parent.listWidget.addItem(parent.item)
			
            if interface_lng_val == 'Russian':
                parent.outf_lbl.setText("Структура файла: " + "<font color='peru'>" + 'controlDict' + "</font>") 
            elif interface_lng_val == 'English':
                parent.outf_lbl.setText("The structure of file: " + "<font color='peru'>" + 'controlDict' + "</font>")

            file_form_path = full_dir + '/system/controlDict'
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

        sF_lbl = QtGui.QLabel("startFrom:")
        sF_edit = QtGui.QComboBox()
        sF_edit.setFixedSize(100, 25)
        sF_list = ["startTime", "latestTime"]
        sF_edit.addItems(sF_list)
        sT_lbl = QtGui.QLabel("startTime:")
        sT_edit = QtGui.QSpinBox()
        sT_edit.setFixedSize(100, 25)
        sA_lbl = QtGui.QLabel("stopAt:")
        sA_edit = QtGui.QComboBox()
        sA_edit.setFixedSize(100, 25)
        sA_list = ["endTime"]
        sA_edit.addItems(sA_list)
        eT_lbl = QtGui.QLabel("endTime:")
        eT_edit = QtGui.QLineEdit()
        eT_edit.setFixedSize(100, 25)
        #eT_edit.setInputMask("9.9e-99;_")
        dT_lbl = QtGui.QLabel("deltaT:")
        dT_edit = QtGui.QLineEdit()
        dT_edit.setFixedSize(100, 25)
        #dT_edit.setInputMask("9.9e-99;_")
        wC_lbl = QtGui.QLabel("writeControl:")
        wC_edit = QtGui.QComboBox()
        wC_edit.setFixedSize(100, 25)
        wC_list = ["adjustableRunTime", "runTime"]
        wC_edit.addItems(wC_list)
        wI_lbl = QtGui.QLabel("writeInterval:")
        wI_edit = QtGui.QLineEdit()
        wI_edit.setFixedSize(100, 25)
        #wI_edit.setInputMask("9.9e-99;_")
        pW_lbl = QtGui.QLabel("purgeWrite:")
        pW_edit = QtGui.QSpinBox()
        pW_edit.setFixedSize(100, 25)
        wF_lbl = QtGui.QLabel("writeFormat:")
        wF_edit = QtGui.QComboBox()
        wF_edit.setFixedSize(100, 25)
        wF_list = ["ascii"]
        wF_edit.addItems(wF_list)
        wP_lbl = QtGui.QLabel("writePrecision:")
        wP_edit = QtGui.QSpinBox()
        wP_edit.setFixedSize(100, 25)
        wComp_lbl = QtGui.QLabel("writeCompression:")
        wComp_edit = QtGui.QComboBox()
        wComp_edit.setFixedSize(100, 25)
        wComp_list = ["on", "off"]
        wComp_edit.addItems(wComp_list)
        tF_lbl = QtGui.QLabel("timeFormat:")
        tF_edit = QtGui.QComboBox()
        tF_edit.setFixedSize(100, 25)
        tF_list = ["general"]
        tF_edit.addItems(tF_list)
        tP_lbl = QtGui.QLabel("timePrecision:")
        tP_edit = QtGui.QSpinBox()
        tP_edit.setFixedSize(100, 25)
		
        gF_lbl = QtGui.QLabel("graphFormat:")
        gF_edit = QtGui.QComboBox()
        gF_edit.setFixedSize(100, 25)
        gF_list = ["raw"]
        gF_edit.addItems(gF_list)
		
		
        rTM_lbl = QtGui.QLabel("runTimeModifiable:")
        rTM_edit = QtGui.QComboBox()
        rTM_edit.setFixedSize(100, 25)
        rTM_list = ["false", "true"]
        rTM_edit.addItems(rTM_list)
        aTS_lbl = QtGui.QLabel("adjustTimeStep:")
        aTS_edit = QtGui.QComboBox()
        aTS_edit.setFixedSize(100, 25)
        aTS_list = ["yes", "no"]
        aTS_edit.addItems(aTS_list)
        mC_lbl = QtGui.QLabel("maxCo:")
        mC_edit = QtGui.QLineEdit()
        mC_edit.setFixedSize(100, 25)
        mDT_lbl = QtGui.QLabel("maxDeltaT:")
        mDT_edit = QtGui.QLineEdit()
        mDT_edit.setFixedSize(100, 25)
        #mDT_edit.setInputMask("9.9e-99;_")
		
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
        prs_grid.addWidget(sF_lbl, 0, 0)
        prs_grid.addWidget(sF_edit, 0, 1)
        prs_grid.addWidget(sT_lbl, 1, 0)
        prs_grid.addWidget(sT_edit, 1, 1)
        prs_grid.addWidget(sA_lbl, 2, 0)
        prs_grid.addWidget(sA_edit, 2, 1)
        prs_grid.addWidget(eT_lbl, 3, 0)
        prs_grid.addWidget(eT_edit, 3, 1)
        prs_grid.addWidget(dT_lbl, 4, 0)
        prs_grid.addWidget(dT_edit, 4, 1)
        prs_grid.addWidget(wC_lbl, 5, 0)
        prs_grid.addWidget(wC_edit, 5, 1)
        prs_grid.addWidget(wI_lbl, 6, 0)
        prs_grid.addWidget(wI_edit, 6, 1)
        prs_grid.addWidget(pW_lbl, 7, 0)
        prs_grid.addWidget(pW_edit, 7, 1)
        prs_grid.addWidget(wF_lbl, 8, 0)
        prs_grid.addWidget(wF_edit, 8, 1)
        prs_grid.addWidget(wP_lbl, 9, 0)
        prs_grid.addWidget(wP_edit, 9, 1)
        prs_grid.addWidget(wComp_lbl, 10, 0)
        prs_grid.addWidget(wComp_edit, 10, 1)
        prs_grid.addWidget(tF_lbl, 11, 0)
        prs_grid.addWidget(tF_edit, 11, 1)
        prs_grid.addWidget(tP_lbl, 12, 0)
        prs_grid.addWidget(tP_edit, 12, 1)
		
        prs_grid.addWidget(gF_lbl, 13, 0)
        prs_grid.addWidget(gF_edit, 13, 1)
		
        prs_grid.addWidget(rTM_lbl, 14, 0)
        prs_grid.addWidget(rTM_edit, 14, 1)
        prs_grid.addWidget(aTS_lbl, 15, 0)
        prs_grid.addWidget(aTS_edit, 15, 1)
        prs_grid.addWidget(mC_lbl, 16, 0)
        prs_grid.addWidget(mC_edit, 16, 1)
        prs_grid.addWidget(mDT_lbl, 17, 0)
        prs_grid.addWidget(mDT_edit, 17, 1)
        prs_frame = QtGui.QFrame()
        prs_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        prs_frame.setLayout(prs_grid)

        # -------------------------Фрейм формы---------------------------

        fvS_grid = QtGui.QGridLayout()
        fvS_grid.addWidget(prs_frame, 0, 0, alignment=QtCore.Qt.AlignCenter)
        fvS_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        fvS_frame = QtGui.QFrame()
        fvS_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        fvS_frame.setFrameShape(QtGui.QFrame.Panel)
        fvS_frame.setFrameShadow(QtGui.QFrame.Sunken)
        fvS_frame.setLayout(fvS_grid)
        fvS_vbox = QtGui.QVBoxLayout() 
        fvS_vbox.addWidget(fvS_frame)

# ---------------------Размещение на форме всех компонентов-------------------------

        form = QtGui.QFormLayout()
        form.addRow(fvS_vbox)
        self.setLayout(form)

# --------------------------Функции связанные c выводом-----------------------------

        file = open(full_dir+"/system/controlDict", 'r') 
        data = file.read()
        file.close()

        sF_reg = re.compile(r"startFrom\s*\S*(?=[;])")
        sF_mas = sF_reg.findall(data)
        sF_div = sF_mas[0].split()
        sF_edit_mas = sF_edit.count()   
        for i in range(sF_edit_mas):
            if sF_edit.itemText(i) == sF_div[1]:
                sF_edit.setCurrentIndex(i)

        sT_reg = re.compile(r"startTime\s*\S*(?=[;])")
        sT_mas = sT_reg.findall(data)
        #print(sT_mas)
        sT_div = sT_mas[1].split()
        sT_edit.setValue(int(sT_div[1]))

        sA_reg = re.compile(r"stopAt\s*\S*(?=[;])")
        sA_mas = sA_reg.findall(data)
        sA_div = sA_mas[0].split()
        sA_edit_mas = sA_edit.count()   
        for i in range(sA_edit_mas):
            if sA_edit.itemText(i) == sA_div[1]:
                sA_edit.setCurrentIndex(i)

        eT_reg = re.compile(r"endTime\s*\S*(?=[;])")
        eT_mas = eT_reg.findall(data)
        eT_div = eT_mas[1].split()
        eT_edit.setText(eT_div[1])

        dT_reg = re.compile(r"deltaT\s*\S*(?=[;])")
        dT_mas = dT_reg.findall(data)
        dT_div = dT_mas[0].split()
        dT_edit.setText(dT_div[1])

        wC_reg = re.compile(r"writeControl\s*\S*(?=[;])")
        wC_mas = wC_reg.findall(data)
        wC_div = wC_mas[0].split()
        wC_edit_mas = wC_edit.count()   
        for i in range(wC_edit_mas):
            if wC_edit.itemText(i) == wC_div[1]:
                wC_edit.setCurrentIndex(i)

        wI_reg = re.compile(r"writeInterval\s*\S*(?=[;])")
        wI_mas = wI_reg.findall(data)
        wI_div = wI_mas[0].split()
        wI_edit.setText(wI_div[1])

        pW_reg = re.compile(r"purgeWrite\s*\S*(?=[;])")
        pW_mas = pW_reg.findall(data)
        pW_div = pW_mas[0].split()
        pW_edit.setValue(int(pW_div[1]))

        wF_reg = re.compile(r"writeFormat\s*\S*(?=[;])")
        wF_mas = wF_reg.findall(data)
        wF_div = wF_mas[0].split()
        wF_edit_mas = wF_edit.count()   
        for i in range(wC_edit_mas):
            if wF_edit.itemText(i) == wF_div[1]:
                wF_edit.setCurrentIndex(i)

        wP_reg = re.compile(r"writePrecision\s*\S*(?=[;])")
        wP_mas = wP_reg.findall(data)
        wP_div = wP_mas[0].split()
        wP_edit.setValue(int(wP_div[1]))

        wComp_reg = re.compile(r"writeCompression\s*\S*(?=[;])")
        wComp_mas = wComp_reg.findall(data)
        wComp_div = wComp_mas[0].split()
        wComp_edit_mas = wComp_edit.count()   
        for i in range(wComp_edit_mas):
            if wComp_edit.itemText(i) == wComp_div[1]:
                wComp_edit.setCurrentIndex(i)

        tF_reg = re.compile(r"timeFormat\s*\S*(?=[;])")
        tF_mas = tF_reg.findall(data)
        tF_div = tF_mas[0].split()
        tF_edit_mas = tF_edit.count()   
        for i in range(tF_edit_mas):
            if tF_edit.itemText(i) == tF_div[1]:
                tF_edit.setCurrentIndex(i)

        tP_reg = re.compile(r"timePrecision\s*\S*(?=[;])")
        tP_mas = tP_reg.findall(data)
        tP_div = tP_mas[0].split()
        tP_edit.setValue(int(tP_div[1]))
		
        gF_reg = re.compile(r"graphFormat\s*\S*(?=[;])")
        gF_mas = gF_reg.findall(data)
        #print(gF_mas[0])
        gF_div = gF_mas[0].split()
        gF_edit_mas = gF_edit.count()   
        for i in range(gF_edit_mas):
            if gF_edit.itemText(i) == gF_div[1]:
                gF_edit.setCurrentIndex(i)

        rTM_reg = re.compile(r"runTimeModifiable\s*\S*(?=[;])")
        rTM_mas = rTM_reg.findall(data)
        rTM_div = rTM_mas[0].split()
        rTM_edit_mas = rTM_edit.count()   
        for i in range(rTM_edit_mas):
            if rTM_edit.itemText(i) == rTM_div[1]:
                rTM_edit.setCurrentIndex(i)

        aTS_reg = re.compile(r"adjustTimeStep\s*\S*(?=[;])")
        aTS_mas = aTS_reg.findall(data)
        aTS_div = aTS_mas[0].split()
        aTS_edit_mas = aTS_edit.count()   
        for i in range(aTS_edit_mas):
            if aTS_edit.itemText(i) == aTS_div[1]:
                aTS_edit.setCurrentIndex(i)

        mC_reg = re.compile(r"maxCo\s*\S*(?=[;])")
        mC_mas = mC_reg.findall(data)
        mC_div = mC_mas[0].split()
        mC_edit.setText(mC_div[1])

        mDT_reg = re.compile(r"maxDeltaT\s*\S*(?=[;])")
        mDT_mas = mDT_reg.findall(data)
        mDT_div = mDT_mas[0].split()
        mDT_edit.setText(mDT_div[1])
        
