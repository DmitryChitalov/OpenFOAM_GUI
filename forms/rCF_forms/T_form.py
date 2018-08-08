# -*- coding: utf-8 -*-
# -----------------------------Импорт модулей-----------------------------------

from PyQt4 import QtCore, QtGui
import shutil
import sys
import re
import os
import os.path

# -----------------------------------Форма--------------------------------------

class T_form(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)
		
        full_dir = parent.full_dir
        interface_lng_val = parent.interface_lng_val

        global types_mas
        global mas
        global c_txt_mas
        global un_txt_mas
        global fw_mas
        global frame_mas
        global fixedV
        global unifs_mas
        global val_mas
        global vali_mas
        global un_txt_mas
        global values
        global perem1_mas
        global nv_mas 

#-------------------Обработчики выпадающих списков-----------------------
        def iF_on_change():
            iF_txt = iF_name.currentText()
            if iF_txt == "uniform":
                iF_name.setVisible(True)
                iF_val.setVisible(True)
                iF_frame.setFixedSize(230, 40)
            else:
                iF_val.setVisible(False)
                iF_frame.setFixedSize(170, 40)

        def on_change():
            w = 0
            c_txt_mas = []
            for w in range(len(types_mas)):
                c_txt = types_mas[w].currentText()
                c_txt_mas.append(c_txt)
                w = w + 1

            for h in range(len(c_txt_mas)):
                if c_txt_mas[h] == "fixedValue":
                    unifs_mas[h].setVisible(True)
                else:
                    unifs_mas[h].setVisible(False)
                    vali_mas[h].setVisible(False)

        def on_change_unif():
            e = 0
            un_txt_mas = []
            for e in range(len(unifs_mas)):
                un_txt = unifs_mas[e].currentText()
                un_txt_mas.append(un_txt)
                e = e + 1
            for b in range(len(un_txt_mas)):
                if un_txt_mas[b] == "uniform" and unifs_mas[b].isVisible() == True:
                    vali_mas[b].setVisible(True)
                else:
                    vali_mas[b].setVisible(False)

#--------------------------------Первый блок.Разметка и вывод данных----------------------------------

        p1 = QtGui.QLineEdit()
        p1.setFixedSize(30, 25)
        valid = QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]|-[0-9]"), self)
        p1.setValidator(valid)

        p2 = QtGui.QLineEdit()
        p2.setFixedSize(30, 25)
        p2.setValidator(valid)
        
        p3 = QtGui.QLineEdit()
        p3.setFixedSize(30, 25)
        p3.setValidator(valid)

        p4 = QtGui.QLineEdit()
        p4.setFixedSize(30, 25)
        p4.setValidator(valid)

        p5 = QtGui.QLineEdit()
        p5.setFixedSize(30, 25)
        p5.setValidator(valid)
        
        p6 = QtGui.QLineEdit()
        p6.setFixedSize(30, 25)
        p6.setValidator(valid)
        
        p7 = QtGui.QLineEdit()
        p7.setFixedSize(30, 25)
        p7.setValidator(valid)

        dim_lbl = QtGui.QLabel("dimensions: ")
        dim_grid = QtGui.QGridLayout()

        dim_grid.addWidget(dim_lbl, 0, 1)
        dim_grid.addWidget(p1, 0, 2)
        dim_grid.addWidget(p2, 0, 3)
        dim_grid.addWidget(p3, 0, 4)
        dim_grid.addWidget(p4, 0, 5)
        dim_grid.addWidget(p5, 0, 6)
        dim_grid.addWidget(p6, 0, 7)
        dim_grid.addWidget(p7, 0, 8)

        dim_frame = QtGui.QFrame()
        dim_frame.setFixedSize(315, 40)
        dim_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        dim_frame.setLayout(dim_grid)
        dim_hbox = QtGui.QHBoxLayout()
        dim_hbox.addWidget(dim_frame)
		
        file = open(full_dir+"/0/T", 'r') 
        data = file.read()
        file.close()

        dim_reg = re.compile(r"(?<=[\[])\S*\s\S*\s\S*\s\S*\s\S*\s\S*\s\S*(?=[\]])")
        dim_mas = dim_reg.findall(data)
        dim_div = dim_mas[0].split(" ")
        p1.setText(dim_div[0])
        p2.setText(dim_div[1])
        p3.setText(dim_div[2])
        p4.setText(dim_div[3])
        p5.setText(dim_div[4])
        p6.setText(dim_div[5])
        p7.setText(dim_div[6])

#--------------------------------Второй блок.Разметка и вывод данных----------------------------------
        
        iF_lbl = QtGui.QLabel("internalField: ")
            
        iF_name = QtGui.QComboBox()
        iF_name.setFixedSize(80, 25)
        iF_list = ["nonuniform", "uniform"]
        iF_name.addItems(iF_list)
        iF_name.activated.connect(iF_on_change)

        iF_val = QtGui.QLineEdit()
        iF_val.setFixedSize(50, 25)
        val = QtGui.QDoubleValidator(0.0, 999.0, 2, self)
        iF_val.setValidator(val)
        iF_val.setVisible(False)

        iF_grid = QtGui.QGridLayout()
        iF_grid.addWidget(iF_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
        iF_grid.addWidget(iF_name, 0, 1, alignment=QtCore.Qt.AlignLeft)
        iF_grid.addWidget(iF_val, 0, 2, alignment=QtCore.Qt.AlignCenter)

        iF_frame = QtGui.QFrame()
        iF_frame.setFixedSize(330, 40)
        iF_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        iF_frame.setLayout(iF_grid)
        iF_hbox = QtGui.QHBoxLayout()
        iF_hbox.addWidget(iF_frame)

        file = open(full_dir+"/0/T", 'r') 
        data = file.read()
        file.close()

        iF_reg = re.compile(r"internalField\s*\S*\s\S*(?=[;])|internalField\s*\S*(?=[;])")
        iF_mas = iF_reg.findall(data)
        iF_div = iF_mas[0].split("   ")
        iF_part = iF_div[1].split(" ")

        iF_edit_mas = iF_name.count()   
        for bvc in range(iF_edit_mas):
            if iF_name.itemText(bvc) == iF_part[0]:
                iF_name.setCurrentIndex(bvc)

        if iF_part[0] == "uniform":
            iF_val.setVisible(True)
            iF_val.setText(iF_part[1])

#--------------------------------Третий блок.Разметка и вывод данных----------------------------------

        file = open(full_dir+"/0/T", 'r') 
        data = file.read()
        file.close()

        bF_lbl = QtGui.QLabel("boundaryField")
        str_grid = QtGui.QGridLayout()
   
        str_frame = QtGui.QFrame()
        str_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        str_frame.setFrameShape(QtGui.QFrame.Panel)
        str_frame.setFrameShadow(QtGui.QFrame.Sunken)
        str_frame.setLayout(str_grid)
        
        str_vbox = QtGui.QVBoxLayout() 
        str_vbox.addWidget(str_frame)

        struct_reg = re.compile(r"\S*\n\s*\{\s*\n\s*type")
        struct_mas = struct_reg.findall(data)

        type_reg = re.compile(r"type\s*\S*(?=[;])")
        type_mas = type_reg.findall(data)
      
        m = 0
        mas_type = []
        for variant in range(len(type_mas)):
            type_div = type_mas[m].split("            ")
            m = m + 1
            mas_type.append(type_div[1])

        i = 0
        mas = []
        for elem in range(len(struct_mas)):
            div = struct_mas[i].split("\n")
            i = i + 1
            mas.append(div[0])

        file = open(full_dir+"/0/T", 'r') 
        data = file.read()
        file.close()
        
        hr_reg = re.compile(r"\n\s*\S*\n\s*\{\n\s*type\s*fixedValue;\n\s*value\s*\S*\s\S*\n\s*\}|\n\s*\S*\n\s*\{\n\s*type\s*\S*\n\s*\}|\n\s*\S*\n\s*\{\n\s*type\s*fixedValue;\n\s*value\s*\S*\n\s*\}")
        hr_mas = hr_reg.findall(data)

        perem1_mas = []
        for cvde in range(len(hr_mas)):
            unit_reg = re.compile(r"value\s*\w*")
            lre_mas = unit_reg.findall(hr_mas[cvde])
            if len(lre_mas) == 1:
                dal_div = lre_mas[0].split("           ")
                if dal_div[1] == "uniform" or dal_div[1] == "nonuniform":
                    perem1_mas.append(dal_div[1])
            else:
                perem1_mas.append("none")

        perem2_mas = []
        for cvdm in range(len(hr_mas)):
            uniform_reg = re.compile(r"\suniform\s*\S*(?=[;])")
            mre_mas = uniform_reg.findall(hr_mas[cvdm])
            if len(mre_mas) == 1:
                mal_div = mre_mas[0].split(" ")
                perem2_mas.append(mal_div[2])
            else:
                perem2_mas.append("none")    

        n = 0
        types_mas = []
        grids_mas = []
        frame_mas = []
        unifs_mas = []
        vali_mas = []
        un_mas = []
        uv_mas = []
        for j in range(len(mas)):
            
            type_lbl = QtGui.QLabel("type: ")
            
            type_name = QtGui.QComboBox()
            type_name.setFixedSize(100, 25)
            type_list = ["fixedValue", "empty", "zeroGradient", "symmetryPlane"]
            type_name.addItems(type_list)

            unif_name = QtGui.QComboBox()
            unif_name.setFixedSize(80, 25)
            unif_list = ["nonuniform", "uniform"]
            unif_name.addItems(unif_list)
            unif_name.setVisible(False)

            unif_val = QtGui.QLineEdit()
            unif_val.setFixedSize(50, 25)
            #validator = QtGui.QDoubleValidator(0.0, 999.0, 2, self)
            #unif_val.setValidator(validator)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp("\-?\\d*\\.\\d+"))
            unif_val.setValidator(validator)
            unif_val.setVisible(False)
            
            type_grid = QtGui.QGridLayout()
            type_grid.addWidget(type_lbl, 0, 0, alignment=QtCore.Qt.AlignCenter)
            type_grid.addWidget(type_name, 0, 1, alignment=QtCore.Qt.AlignLeft)
            type_grid.addWidget(unif_name, 0, 2, alignment=QtCore.Qt.AlignCenter)
            type_grid.addWidget(unif_val, 0, 3, alignment=QtCore.Qt.AlignCenter)

            type_frame = QtGui.QFrame()
            type_frame.setFixedSize(330, 40)
            type_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
            type_frame.setLayout(type_grid)
            type_hbox = QtGui.QHBoxLayout()
            type_hbox.addWidget(type_frame)

            str_lbl = QtGui.QLabel(mas[j])
            str_grid.addWidget(str_lbl, j, 0, alignment=QtCore.Qt.AlignCenter)
            str_grid.addLayout(type_hbox, j, 1)
            
            for r in range(len(type_list)):
                if type_list[r] == mas_type[j]:
                    type_name.setCurrentIndex(r)
                    if type_name.currentText() == "fixedValue":
                        unif_name.setVisible(True)

                        for x in range(len(unif_list)):
                            if unif_list[x] == perem1_mas[j]:
                                unif_name.setCurrentIndex(x)
                                if unif_name.currentText() == "uniform":
                                    unif_val.setVisible(True)
                                    unif_val.setText(perem2_mas[j])
                        
            types_mas.append(type_name)
            frame_mas.append(type_frame)

            unifs_mas.append(unif_name)
            vali_mas.append(unif_val)
        
            types_mas[j].activated.connect(on_change)
            unifs_mas[j].activated.connect(on_change_unif)


#------------------------------------------------------------------------

        def on_btnCancel_clicked():
            self.clear_label = QtGui.QLabel()
            parent.ffw.setTitleBarWidget(self.clear_label)
            self.close()

        def on_btnSave_clicked():
            #----------Первый блок.Запись данных----------
            file = open(full_dir+"/0/T", 'r')
            data = file.read()
            file.close()

            p1_txt = p1.text()
            p2_txt = p2.text()
            p3_txt = p3.text()
            p4_txt = p4.text()
            p5_txt = p5.text()
            p6_txt = p6.text()
            p7_txt = p7.text()

            dim_reg = re.compile(r"(?<=[\[])\S*\s\S*\s\S*\s\S*\s\S*\s\S*\s\S*(?=[\]])")
            dim_mas = dim_reg.findall(data)
            dim_txt_add = p1_txt+" "+p2_txt+" "+p3_txt+" "+p4_txt+" "+p5_txt+" "+p6_txt+" "+p7_txt
            data = data.replace(dim_mas[0], dim_txt_add)

            file = open(full_dir+"/0/T", 'w')  
            file.write(data)
            file.close()

            #----------Второй блок.Запись данных----------

            file = open(full_dir+"/0/T", 'r') 
            data = file.read()
            file.close()

            iF_reg = re.compile(r"internalField\s*\S*\s\S*(?=[;])|internalField\s*\S*(?=[;])")
            iF_mas = iF_reg.findall(data)

            if iF_name.currentText() == "uniform":
                iF_txt_add = "internalField"+"   "+iF_name.currentText()+" "+iF_val.text()
            else:
                iF_txt_add = "internalField"+"   "+iF_name.currentText()

            data = data.replace(iF_mas[0], iF_txt_add)

            file = open(full_dir+"/0/T", 'w')  
            file.write(data)
            file.close()

            #----------Третий блок.Запись данных----------
            
            file = open(full_dir+"/0/T", 'r') 
            data = file.read()
            file.close()

            u = 0
            new_tn_mas = []
            for w in range(len(types_mas)):
                new_tn_mas.append(types_mas[w].currentText())
                u = u + 1

            for s in range(len(mas)):
                if new_tn_mas[s] == "fixedValue":
                    type_reg = re.compile(r"\n\s*"+mas[s]+r"\n\s*\{\n\s*type\s*fixedValue;\n\s*value\s*\S*\s\S*\n\s*\}|\n\s*"+mas[s]+r"\n\s*\{\n\s*type\s*fixedValue;\n\s*value\s*\S*\n\s*\}|\n\s*"+mas[s]+r"\n\s*\{\n\s*type\s*\S*\n\s*\}")
                    type_mas = type_reg.findall(data)
                    tn_txt_add = "\n"+"    "+mas[s]+"\n"+"    "+"{"+"\n"+"  "+"      "+"type            "+new_tn_mas[s]+";"+"\n"+"  "+"      "+"value"+"           "+"meaning"+"\n"+"    "+"}"
                    data = data.replace(type_mas[0], tn_txt_add)
                else:
                    dr_reg = re.compile(r"\n\s*"+mas[s]+r"\n\s*\{\n\s*type\s*fixedValue;\n\s*value\s*\S*\s\S*\n\s*\}|\n\s*"+mas[s]+r"\n\s*\{\n\s*type\s*fixedValue;\n\s*value\s*\S*\n\s*\}|\n\s*"+mas[s]+r"\n\s*\{\n\s*type\s*\S*\n\s*\}")
                    dr_mas = dr_reg.findall(data)
                    dr_txt_add = "\n"+"    "+mas[s]+"\n"+"    "+"{"+"\n"+"  "+"      "+"type            "+new_tn_mas[s]+";"+"\n"+"    "+"}"
                    data = data.replace(dr_mas[0], dr_txt_add)

                file = open(full_dir+"/0/T", 'w')  
                file.write(data)
                file.close()
                    
            z = 0
            un_vals = []
            for z in range(len(unifs_mas)):
                if unifs_mas[z].isVisible() == True:
                    un_vals.append(unifs_mas[z].currentText())
                    z = z + 1

            lk = 0
            uv_vals = []
            for lk in range(len(vali_mas)):
                if vali_mas[lk].isVisible() == True:
                    uv_vals.append(vali_mas[lk].text())
                    lk = lk + 1
  

            file = open(full_dir+"/0/T", 'r') 
            data = file.read()
            file.close()

            vals_reg = re.compile(r"value\s*meaning")
            vals_mas = vals_reg.findall(data)
  
            for v in range(len(un_vals)):
                if un_vals[v] == "uniform":
                    val1_txt_add = "value"+"           "+un_vals[v]+";"
                    data = data.replace(vals_mas[0], val1_txt_add, 1)
                else:
                    val2_txt_add = "value"+"           "+un_vals[v]+";"
                    data = data.replace(vals_mas[0], val2_txt_add, 1)

                file = open(full_dir+"/0/T", 'w')  
                file.write(data)
                file.close()
                
            file = open(full_dir+"/0/T", 'r') 
            data = file.read()
            file.close()

            val_un_reg = re.compile(r"value\s*uniform;")
            val_un_mas = val_un_reg.findall(data)
            for xr in range(len(uv_vals)):
                val_un_txt_add = "value"+"           "+"uniform"+" "+uv_vals[xr]+";"
                data = data.replace(val_un_mas[0], val_un_txt_add, 1)

                file = open(full_dir+"/0/T", 'w')  
                file.write(data)
                file.close()

            if interface_lng_val == 'Russian':
                msg = "Сохранен файл: T"
            elif interface_lng_val == 'English':
                msg = "Saved file: T"
            color = QtGui.QColor("green")
			
            if interface_lng_val == 'Russian':
                parent.outf_lbl.setText("Структура файла: " + "<font color='peru'>" + 'T' + "</font>") 
            elif interface_lng_val == 'English':
                parent.outf_lbl.setText("The structure of file: " + "<font color='peru'>" + 'T' + "</font>")
				
            file_form_path = full_dir + '/0/T'
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

# -------------------------Фрейм формы---------------------------

        bound_grid = QtGui.QGridLayout()
        bound_grid.addLayout(dim_hbox, 0, 0, alignment=QtCore.Qt.AlignCenter)
        bound_grid.addLayout(iF_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
        bound_grid.addWidget(bF_lbl, 2, 0, alignment=QtCore.Qt.AlignCenter)
        bound_grid.addLayout(str_vbox, 3, 0, alignment=QtCore.Qt.AlignCenter)
        bound_grid.addLayout(buttons_hbox, 4, 0, alignment=QtCore.Qt.AlignCenter)
        bound_frame = QtGui.QFrame()
        bound_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
        bound_frame.setLayout(bound_grid)
        bound_vbox = QtGui.QVBoxLayout() 
        bound_vbox.addWidget(bound_frame)

# ---------------------Размещение на форме всех компонентов-------------------------

        form_1 = QtGui.QFormLayout()
        form_1.addRow(bound_vbox)
        self.setLayout(form_1)

