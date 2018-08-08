# -*- coding: utf-8 -*-
# -----------------------------Импорт модулей-----------------------------------

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path

# -----------------------------------Форма--------------------------------------

class thermophysicalProperties_form(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
		
        full_dir = parent.full_dir
        interface_lng_val = parent.interface_lng_val

# ------------------------Функции связанные с формой-----------------------------

        def on_btnSave_clicked():
            type_txt = type_name.currentText()
            mixture_txt = mixture_name.currentText()
            tr_txt = tr_name.currentText()
            th_txt = th_name.currentText()
            eOS_txt = eOS_name.currentText()
            s_txt = s_name.currentText()
            e_txt = e_name.currentText()

            nM_txt = nM_name.text()
            mW_txt = mW_name.text()
            Cp_txt = Cp_name.text()
            Hf_txt = Hf_name.text()
            #As_txt = As_name.text()
            #Ts_txt = Ts_name.text()
            mu_txt = mu_name.text()
            Pr_txt = Pr_name.text()
 
            file = open(full_dir+"/constant/thermophysicalProperties", 'r') 
            data = file.read()
            file.close()

            t_reg = re.compile(r"type\s*\S*(?=[;])")
            t_mas = t_reg.findall(data)
            t_txt_add = "type            "+type_txt
            data = data.replace(t_mas[0], t_txt_add)

            m_reg = re.compile(r"mixture\s*\S*(?=[;])")
            m_mas = m_reg.findall(data)
            m_txt_add = "mixture         "+mixture_txt
            data = data.replace(m_mas[0], m_txt_add)

            tr_reg = re.compile(r"transport\s*\S*(?=[;])")
            tr_mas = tr_reg.findall(data)
            tr_txt_add = "transport       "+tr_txt
            data = data.replace(tr_mas[0], tr_txt_add)

            th_reg = re.compile(r"thermo\s\s*\S*(?=[;])")
            th_mas = th_reg.findall(data)
            th_txt_add = "thermo          "+th_txt
            data = data.replace(th_mas[0], th_txt_add)

            eOS_reg = re.compile(r"equationOfState\s*\S*(?=[;])")
            eOS_mas = eOS_reg.findall(data)
            eOS_txt_add = "equationOfState "+eOS_txt
            data = data.replace(eOS_mas[0], eOS_txt_add)

            s_reg = re.compile(r"specie\s*\S*(?=[;])")
            s_mas = s_reg.findall(data)
            s_txt_add = "specie          "+s_txt
            data = data.replace(s_mas[0], s_txt_add)

            e_reg = re.compile(r"energy\s*\S*(?=[;])")
            e_mas = e_reg.findall(data)
            e_txt_add = "energy          "+e_txt
            data = data.replace(e_mas[0], e_txt_add)

            nM_reg = re.compile(r"nMoles\s*\S*(?=[;])")
            nM_mas = nM_reg.findall(data)
            nM_txt_add = "nMoles          "+nM_txt
            data = data.replace(nM_mas[0], nM_txt_add)

            mW_reg = re.compile(r"molWeight\s*\S*(?=[;])")
            mW_mas = mW_reg.findall(data)
            mW_txt_add = "molWeight       "+mW_txt
            data = data.replace(mW_mas[0], mW_txt_add)

            Cp_reg = re.compile(r"Cp\s*\S*(?=[;])")
            Cp_mas = Cp_reg.findall(data)
            Cp_txt_add = "Cp              "+Cp_txt
            data = data.replace(Cp_mas[0], Cp_txt_add)

            Hf_reg = re.compile(r"Hf\s*\S*(?=[;])")
            Hf_mas = Hf_reg.findall(data)
            Hf_txt_add = "Hf              "+Hf_txt
            data = data.replace(Hf_mas[0], Hf_txt_add)

            #As_reg = re.compile(r"As\s*\S*(?=[;])")
            #As_mas = As_reg.findall(data)
            #As_txt_add = "As              "+As_txt
            #data = data.replace(As_mas[0], As_txt_add)

            #Ts_reg = re.compile(r"Ts\s*\S*(?=[;])")
            #Ts_mas = Ts_reg.findall(data)
            #Ts_txt_add = "Ts              "+Ts_txt
            #data = data.replace(Ts_mas[0], Ts_txt_add)
			
            mu_reg = re.compile(r"mu\s*\S*(?=[;])")
            mu_mas = mu_reg.findall(data)
            mu_txt_add = "mu              "+mu_txt
            data = data.replace(mu_mas[0], mu_txt_add)

            Pr_reg = re.compile(r"Pr\s\s*\S*(?=[;])")
            Pr_mas = Pr_reg.findall(data)
            Pr_txt_add = "Pr              "+Pr_txt
            data = data.replace(Pr_mas[0], Pr_txt_add)

            file = open(full_dir+"/constant/thermophysicalProperties", 'w')  
            file.write(data)
            file.close()
            
            if interface_lng_val == 'Russian':
                msg = "Сохранен файл: thermophysicalProperties"
            elif interface_lng_val == 'English':
                msg = "Saved file: thermophysicalProperties"
            color = QtGui.QColor("green")
				
            if interface_lng_val == 'Russian':
                parent.outf_lbl.setText("Структура файла: " + "<font color='peru'>" + 'thermophysicalProperties' + "</font>") 
            elif interface_lng_val == 'English':
                parent.outf_lbl.setText("The structure of file: " + "<font color='peru'>" + 'thermophysicalProperties' + "</font>")
				
            file_form_path = full_dir + '/constant/thermophysicalProperties'
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
        
        # ---------------------thermoType---------------------
        
        tT_lbl = QtGui.QLabel("thermoType")
        tT_lbl.setStyleSheet("qproperty-alignment: AlignCenter;")
        tT_lbl_hbox = QtGui.QHBoxLayout()
        tT_lbl_hbox.addWidget(tT_lbl)
        type_lbl = QtGui.QLabel("type: ")
        type_name = QtGui.QComboBox()
        type_name.setFixedSize(100, 25)
        type_list = ["demo", "hePsiThermo"]
        type_name.addItems(type_list)
        mixture_lbl = QtGui.QLabel("mixture: ")
        mixture_name = QtGui.QComboBox()
        mixture_name.setFixedSize(100, 25)
        mixture_list = ["demo", "pureMixture"]
        mixture_name.addItems(mixture_list)
        tr_lbl = QtGui.QLabel("transport: ")
        tr_name = QtGui.QComboBox()
        tr_name.setFixedSize(100, 25)
        tr_list = ["demo", "sutherland", "const"]
        tr_name.addItems(tr_list)
        th_lbl = QtGui.QLabel("thermo: ")
        th_name = QtGui.QComboBox()
        th_name.setFixedSize(100, 25)
        th_list = ["demo", "hConst"]
        th_name.addItems(th_list)
        eOS_lbl = QtGui.QLabel("equationOfState: ")
        eOS_name = QtGui.QComboBox()
        eOS_name.setFixedSize(100, 25)
        eOS_list = ["demo", "perfectGas"]
        eOS_name.addItems(eOS_list)
        s_lbl = QtGui.QLabel("specie: ")
        s_name = QtGui.QComboBox()
        s_name.setFixedSize(100, 25)
        s_list = ["demo", "specie"]
        s_name.addItems(s_list)
        e_lbl = QtGui.QLabel("energy: ")
        e_name = QtGui.QComboBox()
        e_name.setFixedSize(100, 25)
        e_list = ["demo", "sensibleInternalEnergy"]
        e_name.addItems(e_list)
        tT_grid = QtGui.QGridLayout()
        tT_grid.addWidget(type_lbl, 0, 0)
        tT_grid.addWidget(type_name, 0, 1)
        tT_grid.addWidget(mixture_lbl, 1, 0)
        tT_grid.addWidget(mixture_name, 1, 1)
        tT_grid.addWidget(tr_lbl, 2, 0)
        tT_grid.addWidget(tr_name , 2, 1)
        tT_grid.addWidget(th_lbl, 3, 0)
        tT_grid.addWidget(th_name, 3, 1)
        tT_grid.addWidget(eOS_lbl, 4, 0)
        tT_grid.addWidget(eOS_name, 4, 1)
        tT_grid.addWidget(s_lbl, 5, 0)
        tT_grid.addWidget(s_name, 5, 1)
        tT_grid.addWidget(e_lbl, 6, 0)
        tT_grid.addWidget(e_name, 6, 1)
        tT_frame = QtGui.QFrame()
        tT_frame.setFixedSize(240, 200)
        tT_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        tT_frame.setLayout(tT_grid)
        tT_hbox = QtGui.QHBoxLayout()
        tT_hbox.addWidget(tT_frame)

        # ---------------------mixture----------------------

        m_lbl = QtGui.QLabel("mixture")
        m_lbl.setStyleSheet("qproperty-alignment: AlignCenter;")
        m_lbl_hbox = QtGui.QHBoxLayout()
        m_lbl_hbox.addWidget(m_lbl)
        spec_lbl = QtGui.QLabel("specie")
        spec_lbl.setStyleSheet("qproperty-alignment: AlignCenter;")
        spec_lbl_hbox = QtGui.QHBoxLayout()
        spec_lbl_hbox.addWidget(spec_lbl)
        validator = QtGui.QDoubleValidator(0.0, 999.0, 2, self)
        nM_lbl = QtGui.QLabel("nMoles: ")
        nM_name = QtGui.QLineEdit()
        nM_name.setValidator(validator)
        nM_name.setFixedSize(100, 25)
        nM_hbox = QtGui.QHBoxLayout()
        nM_hbox.addWidget(nM_lbl)
        nM_hbox.addWidget(nM_name)
        mW_lbl = QtGui.QLabel("molWeight: ")
        mW_name = QtGui.QLineEdit()
        mW_name.setValidator(validator)
        mW_name.setFixedSize(100, 25)
        mW_hbox = QtGui.QHBoxLayout()
        mW_hbox.addWidget(mW_lbl)
        mW_hbox.addWidget(mW_name)
        thd_lbl = QtGui.QLabel("thermodynamics")
        thd_lbl.setStyleSheet("qproperty-alignment: AlignCenter;")
        thd_lbl_hbox = QtGui.QHBoxLayout()
        thd_lbl_hbox.addWidget(thd_lbl)
        Cp_lbl = QtGui.QLabel("Cp: ")
        Cp_name = QtGui.QLineEdit()
        Cp_name.setValidator(validator)
        Cp_name.setFixedSize(100, 25)
        Cp_hbox = QtGui.QHBoxLayout()
        Cp_hbox.addWidget(Cp_lbl)
        Cp_hbox.addWidget(Cp_name)
        Hf_lbl = QtGui.QLabel("Hf: ")
        Hf_name = QtGui.QLineEdit()
        Hf_name.setValidator(validator)
        Hf_name.setFixedSize(100, 25)
        Hf_hbox = QtGui.QHBoxLayout()
        Hf_hbox.addWidget(Hf_lbl)
        Hf_hbox.addWidget(Hf_name)
        trt_lbl = QtGui.QLabel("transport")
        trt_lbl.setStyleSheet("qproperty-alignment: AlignCenter;")
        trt_lbl_hbox = QtGui.QHBoxLayout()
        trt_lbl_hbox.addWidget(trt_lbl)
		
        #As_lbl = QtGui.QLabel("As: ")
        #As_name = QtGui.QLineEdit()
        #valid = QtGui.QRegExpValidator(QtCore.QRegExp("\S*"), self)
        #As_name.setValidator(valid)
        #As_name.setFixedSize(100, 25)
        #As_hbox = QtGui.QHBoxLayout()
        #As_hbox.addWidget(As_lbl)
        #As_hbox.addWidget(As_name)
        #Ts_lbl = QtGui.QLabel("Ts: ")
        #Ts_name = QtGui.QLineEdit()
        #Ts_name.setValidator(validator)
        #Ts_name.setFixedSize(100, 25)
        #Ts_hbox = QtGui.QHBoxLayout()
        #Ts_hbox.addWidget(Ts_lbl)
        #Ts_hbox.addWidget(Ts_name)
		
        mu_lbl = QtGui.QLabel("mu: ")
        mu_name = QtGui.QLineEdit()
        mu_name.setValidator(validator)
        mu_name.setFixedSize(100, 25)
        mu_hbox = QtGui.QHBoxLayout()
        mu_hbox.addWidget(mu_lbl)
        mu_hbox.addWidget(mu_name)
		
		
		
        Pr_lbl = QtGui.QLabel("Pr: ")
        Pr_name = QtGui.QLineEdit()
        Pr_name.setValidator(validator)
        Pr_name.setFixedSize(100, 25)
        Pr_hbox = QtGui.QHBoxLayout()
        Pr_hbox.addWidget(Pr_lbl)
        Pr_hbox.addWidget(Pr_name)
        mix_grid = QtGui.QGridLayout()
        mix_grid.addLayout(spec_lbl_hbox, 0, 0)
        mix_grid.addLayout(nM_hbox, 1, 0)
        mix_grid.addLayout(mW_hbox, 2, 0)
        mix_grid.addLayout(thd_lbl_hbox, 3, 0)
        mix_grid.addLayout(Cp_hbox, 4, 0)
        mix_grid.addLayout(Hf_hbox, 5, 0)
        mix_grid.addLayout(trt_lbl_hbox, 6, 0)
        mix_grid.addLayout(mu_hbox, 7, 0)
        mix_grid.addLayout(Pr_hbox, 8, 0)
        #mix_grid.addLayout(Ts_hbox, 8, 0)
        #mix_grid.addLayout(Pr_hbox, 9, 0)
        mix_frame = QtGui.QFrame()
        mix_frame.setFixedSize(240, 270)
        mix_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        mix_frame.setLayout(mix_grid)
        mix_hbox = QtGui.QHBoxLayout()
        mix_hbox.addWidget(mix_frame)

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

        tProp_grid = QtGui.QGridLayout()
        tProp_grid.addLayout(tT_lbl_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
        tProp_grid.addLayout(tT_hbox, 1, 0)
        tProp_grid.addLayout(m_lbl_hbox, 2, 0, alignment=QtCore.Qt.AlignCenter)
        tProp_grid.addLayout(mix_hbox, 3, 0, alignment=QtCore.Qt.AlignCenter)
        tProp_grid.addLayout(buttons_hbox, 4, 0, alignment=QtCore.Qt.AlignCenter)
        tProp_frame = QtGui.QFrame()
        tProp_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        tProp_frame.setFrameShape(QtGui.QFrame.Panel)
        tProp_frame.setFrameShadow(QtGui.QFrame.Sunken)
        tProp_frame.setLayout(tProp_grid)
        tProp_vbox = QtGui.QVBoxLayout() 
        tProp_vbox.addWidget(tProp_frame)

# ---------------------Размещение на форме всех компонентов-------------------------

        form_1 = QtGui.QFormLayout()
        form_1.addRow(tProp_vbox)
        self.setLayout(form_1)

# --------------------------Функции связанные c выводом-----------------------------

        file = open(full_dir+"/constant/thermophysicalProperties", 'r') 
        data = file.read()
        file.close()

        t_reg = re.compile(r"type\s*\S*(?=[;])")
        t_mas = t_reg.findall(data)
        t_div = t_mas[0].split()
        t_edit_mas = type_name.count()   
        for i in range(t_edit_mas):
            if type_name.itemText(i) == t_div[1]:
                type_name.setCurrentIndex(i)

        m_reg = re.compile(r"mixture\s*\S*(?=[;])")
        m_mas = m_reg.findall(data)
        m_div = m_mas[0].split()
        m_edit_mas = mixture_name.count()   
        for i in range(m_edit_mas):
            if mixture_name.itemText(i) == m_div[1]:
                mixture_name.setCurrentIndex(i)

        tr_reg = re.compile(r"transport\s*\S*(?=[;])")
        tr_mas = tr_reg.findall(data)
        tr_div = tr_mas[0].split()
        tr_edit_mas = tr_name.count()   
        for i in range(tr_edit_mas):
            if tr_name.itemText(i) == tr_div[1]:
                tr_name.setCurrentIndex(i)

        th_reg = re.compile(r"thermo\s\s*\S*(?=[;])")
        th_mas = th_reg.findall(data)
        th_div = th_mas[0].split()
        th_edit_mas = th_name.count()   
        for i in range(th_edit_mas):
            if th_name.itemText(i) == th_div[1]:
                th_name.setCurrentIndex(i)

        eOS_reg = re.compile(r"equationOfState\s*\S*(?=[;])")
        eOS_mas = eOS_reg.findall(data)
        eOS_div = eOS_mas[0].split()
        eOS_edit_mas = eOS_name.count()   
        for i in range(eOS_edit_mas):
            if eOS_name.itemText(i) == eOS_div[1]:
                eOS_name.setCurrentIndex(i)

        s_reg = re.compile(r"specie\s*\S*(?=[;])")
        s_mas = s_reg.findall(data)
        s_div = s_mas[0].split()
        s_edit_mas = s_name.count()   
        for i in range(s_edit_mas):
            if s_name.itemText(i) == s_div[1]:
                s_name.setCurrentIndex(i)

        e_reg = re.compile(r"energy\s*\S*(?=[;])")
        e_mas = e_reg.findall(data)
        e_div = e_mas[0].split()
        e_edit_mas = e_name.count()   
        for i in range(e_edit_mas):
            if e_name.itemText(i) == e_div[1]:
                e_name.setCurrentIndex(i)

        nM_reg = re.compile(r"nMoles\s*\S*(?=[;])")
        nM_mas = nM_reg.findall(data)
        nM_div = nM_mas[0].split()
        nM_name.setText(nM_div[1])

        mW_reg = re.compile(r"molWeight\s*\S*(?=[;])")
        mW_mas = mW_reg.findall(data)
        mW_div = mW_mas[0].split()
        mW_name.setText(mW_div[1])

        Cp_reg = re.compile(r"Cp\s*\S*(?=[;])")
        Cp_mas = Cp_reg.findall(data)
        Cp_div = Cp_mas[0].split()
        Cp_name.setText(Cp_div[1])

        Hf_reg = re.compile(r"Hf\s*\S*(?=[;])")
        Hf_mas = Hf_reg.findall(data)
        Hf_div = Hf_mas[0].split()
        Hf_name.setText(Hf_div[1])

        #As_reg = re.compile(r"As\s*\S*(?=[;])")
        #As_mas = As_reg.findall(data)
        #As_div = As_mas[0].split()
        #As_name.setText(As_div[1])

        #Ts_reg = re.compile(r"Ts\s*\S*(?=[;])")
        #Ts_mas = Ts_reg.findall(data)
        #Ts_div = Ts_mas[0].split()
        #Ts_name.setText(Ts_div[1])
		
        mu_reg = re.compile(r"mu\s*\S*(?=[;])")
        mu_mas = mu_reg.findall(data)
        mu_div = mu_mas[0].split()
        mu_name.setText(mu_div[1])

        Pr_reg = re.compile(r"Pr\s\s*\S*(?=[;])")
        Pr_mas = Pr_reg.findall(data)
        Pr_div = Pr_mas[0].split()
        Pr_name.setText(Pr_div[1])


