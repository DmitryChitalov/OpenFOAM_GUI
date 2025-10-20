#!/usr/bin/python3
# -*- coding: utf-8 -*--
###--------------------------------Импорт модулей------------------------------------###
# --- обновлен запускаемый файл--------

from PyQt4 import QtCore, QtGui                                                 
import sys, os
import subprocess
import time

from add_classes.file_form_class import file_form_class

from functions.first_toolbar_functions import first_toolbar_functions_class
from functions.second_toolbar_functions import second_toolbar_functions_class

###-------------------------Главное окно приложения-----------------------------###

class MainWindowClass(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.interface_lng_val = 'Russian'
        self.setWindowTitle("Графический интерфейс программы OpenFOAM")

        self.full_dir = ''
        self.prj_name = ''
        self.new_app = ''

        # ---------------------------Панель управления решением задачи МСС-----------------------------

        self.proj_open = QtGui.QAction(self)
        self.proj_open.setEnabled(True)
        proj_ico = self.style().standardIcon(QtGui.QStyle.SP_ArrowUp)
        self.proj_open.setIcon(proj_ico)
        self.proj_open.setToolTip('Открыть проект')

        self.task_open = QtGui.QAction(self)
        self.task_open.setEnabled(False)
        task_ico = self.style().standardIcon(QtGui.QStyle.SP_FileDialogStart)
        self.task_open.setIcon(task_ico)
        self.task_open.setToolTip('Запустить процесс решения')

        self.task_close = QtGui.QAction(self)
        self.task_close.setEnabled(False)
        close_ico = self.style().standardIcon(QtGui.QStyle.SP_DockWidgetCloseButton)
        self.task_close.setIcon(close_ico)
        self.task_close.setToolTip('Остановить процесс решения')

        self.view_open = QtGui.QAction(self)
        self.view_open.setEnabled(False)
        view_ico = self.style().standardIcon(QtGui.QStyle.SP_DriveNetIcon)
        self.view_open.setIcon(view_ico)
        self.view_open.setToolTip('Запустить ParaView')

        self.lng_chs = QtGui.QAction(self)
        self.lng_chs.setEnabled(True)
        lng_chs_ico = self.style().standardIcon(QtGui.QStyle.SP_FileDialogDetailedView)
        self.lng_chs.setIcon(lng_chs_ico)
        self.lng_chs.setToolTip('Выбрать язык интерфейса программы')

        self.toolBar_1 = QtGui.QToolBar("MyToolBar")
        self.toolBar_1.addAction(self.proj_open)
        self.toolBar_1.addAction(self.task_open)
        self.toolBar_1.addAction(self.task_close)
        self.toolBar_1.addAction(self.view_open)
        self.toolBar_1.addAction(self.lng_chs)

        self.proj_open.triggered.connect(lambda: first_toolbar_functions_class.on_proj_open(self))
        self.task_open.triggered.connect(lambda: first_toolbar_functions_class.on_task_open(self))
        self.task_close.triggered.connect(lambda: first_toolbar_functions_class.on_task_close(self))
        self.view_open.triggered.connect(lambda: first_toolbar_functions_class.on_view_open(self))
        self.lng_chs.triggered.connect(lambda: first_toolbar_functions_class.on_lng_chs(self))

        self.addToolBar(self.toolBar_1)
		
        ###----------------------Панель управления подготовкой расчетных сеток---------------------------###

        self.msh_open = QtGui.QAction(self)
        self.msh_open.setEnabled(False)
        msh_ico = self.style().standardIcon(QtGui.QStyle.SP_FileDialogNewFolder)
        self.msh_open.setIcon(msh_ico)
        self.msh_open.setToolTip('Открыть форму выбора расчетной сетки')

        self.msh_run = QtGui.QAction(self)
        self.msh_run.setEnabled(False)
        msh_ico = self.style().standardIcon(QtGui.QStyle.SP_ArrowRight)
        self.msh_run.setIcon(msh_ico)
        self.msh_run.setToolTip('Выполнить генерацию расчетной сетки')

        self.msh_visual = QtGui.QAction(self)
        self.msh_visual.setEnabled(False)
        msh_visual_ico = self.style().standardIcon(QtGui.QStyle.SP_MediaSeekForward)
        self.msh_visual.setIcon(msh_visual_ico)
        self.msh_visual.setToolTip('Выполнить визуализацию расчетной сетки')

        self.toolBar_2 = QtGui.QToolBar()
        self.toolBar_2.addAction(self.msh_open)
        self.toolBar_2.addAction(self.msh_run)
        self.toolBar_2.addAction(self.msh_visual)
       
        self.msh_open.triggered.connect(lambda: second_toolbar_functions_class.on_msh_open(self))
        self.msh_run.triggered.connect(lambda: second_toolbar_functions_class.on_msh_run(prj_path_val, mesh_name_txt_val, pp_dir, self, self.interface_lng_val, msh_type))
        self.msh_visual.triggered.connect(lambda: second_toolbar_functions_class.on_visual_msh_run(prj_path_val, mesh_name_txt_val, pp_dir, self, self.interface_lng_val))
        
        self.addToolBar(self.toolBar_2)
        self.insertToolBarBreak(self.toolBar_2)
                
        ###----------------Верхний виджет с полным путем до файла сетки----------------###

        self.tdw = QtGui.QDockWidget()
        self.tdw.setFixedSize(1400, 65)
        self.tdw.setFeatures(self.tdw.NoDockWidgetFeatures)       
        self.tdw_grid = QtGui.QGridLayout()
        self.tdw_grid.setColumnStretch(2, 1)
        self.tdw_frame = QtGui.QFrame()
        self.tdw_frame.setStyleSheet("background-color: ghostwhite;" "border-width: 0.5px;" "border-style: solid;" "border-color: silver;")
        self.tdw_frame.setLayout(self.tdw_grid)
        self.tdw.setWidget(self.tdw_frame)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.tdw)

        ###-----------------Левый виджет с файловой системой проекта---------------------###

        self.fsw = QtGui.QDockWidget()
        self.fsw.setFeatures(self.fsw.NoDockWidgetFeatures)
        self.fsw_label = QtGui.QLabel()
        self.fsw_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fsw_grid = QtGui.QGridLayout()
        self.fsw_grid.addWidget(self.fsw_label, 0, 0)
        self.fsw_frame = QtGui.QFrame()
        self.fsw_frame.setFixedSize(200, 35)
        self.fsw_frame.setStyleSheet("background-color: honeydew;" "border-width: 1px;" "border-style: solid;" "border-color: dimgray;" "border-radius: 4px;")
        self.fsw_frame.setLayout(self.fsw_grid)
        fs_lbl = "Файловая структура проекта"
        self.fsw_label.setText("<font color='SeaGreen'>" + fs_lbl + "</font>")
        self.fsw_label.setStyleSheet("border-style: none;" "font-size: 10pt;")
        self.fsw.setTitleBarWidget(self.fsw_frame)
        self.treeview = QtGui.QTreeView()
        self.treeview.setFixedSize(200, 660)
        self.treeview.model = QtGui.QStandardItemModel()
        self.treeview.setModel(self.treeview.model) 
        self.treeview.setColumnWidth(0, 100)  
        self.treeview.setColumnHidden(1, True)
        self.treeview.setColumnHidden(2, True)
        self.treeview.setColumnHidden(3, True)
        self.treeview.header().hide()
        self.treeview.setItemsExpandable(False) 
        self.treeview.clicked.connect(self.on_treeview_clicked)
        self.fsw.setWidget(self.treeview)

        ###-----------Правый виджет-----------###

        self.cdw = QtGui.QDockWidget()
        self.cdw.setFeatures(self.cdw.NoDockWidgetFeatures)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.cdw)

        self.cdw_grid = QtGui.QGridLayout()
        self.cdw_frame = QtGui.QFrame()
        self.cdw_frame.setFixedSize(495, 35)
        self.cdw_frame.setStyleSheet("border-width: 1px;" "border-style: solid;" "border-color: dimgray;" "border-radius: 4px;" "background-color: honeydew;")
        self.cdw_frame.setLayout(self.cdw_grid)

        self.outf_lbl = QtGui.QLabel()
        self.outf_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.outf_lbl.setStyleSheet("border-style: none;" "font-size: 9pt;")
		
        self.cdw_grid.addWidget(self.outf_lbl, 0, 0)

        self.outf_edit = QtGui.QTextEdit()
        self.outf_scroll = QtGui.QScrollArea()
        self.outf_scroll.setWidgetResizable(True) 
        self.outf_scroll.setWidget(self.outf_edit)
        self.outf_scroll.setFixedSize(495, 650)

        ###-----------------Центральный виджет с формой параметров---------------------###

        self.ffw = QtGui.QDockWidget()
        self.ffw.setFeatures(self.ffw.NoDockWidgetFeatures)
        self.ffw_label = QtGui.QLabel()
        self.ffw_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ffw_grid = QtGui.QGridLayout()
        self.ffw_grid.addWidget(self.ffw_label, 0, 0)
        self.ffw_frame = QtGui.QFrame()
        self.ffw_frame.setFixedSize(699, 44)
        self.ffw_frame.setStyleSheet("border-width: 1px;" "border-style: solid;" "border-color: dimgray;" "border-radius: 4px;" "background-color: honeydew;")
        self.ffw_frame.setLayout(self.ffw_grid)

        ###------------------Нижний виджет со служебными сообщениями------------------###

        self.serv_mes = QtGui.QDockWidget("Служебные сообщения")
        self.serv_mes.setFixedSize(1400, 160)
        self.serv_mes.setFeatures(self.serv_mes.NoDockWidgetFeatures)
        self.listWidget = QtGui.QListWidget()
        self.serv_mes.setWidget(self.listWidget)

    ###---------------------Функции, связанные с работой главного окна------------------------###

    # ...........................Функция клика по файлу из дерева.........................

    def on_treeview_clicked(self, index):
        global fileName
        indexItem = self.treeview.model.index(index.row(), 0, index.parent())
        file_name = self.treeview.model.itemFromIndex(indexItem).text()
        file_form_class.inp_file_form_func(self, file_name)
        file_name_title = file_form_class.out_file_name_func()
        self.clear_label = QtGui.QLabel()
        if file_name_title != None:
            self.cdw.setWidget(self.clear_label)
            self.cdw.setTitleBarWidget(self.clear_label)            
            
            self.setCentralWidget(self.ffw)

            file_form = file_form_class.out_file_form_func()
            file_form.setFixedWidth(700)
            self.ffw.setWidget(file_form)
            
            self.ffw.setTitleBarWidget(self.ffw_frame)
            self.ffw_label.setText("Форма параметров файла: " + "<font color='peru'>" + file_name_title + "</font>")
            self.ffw_label.setStyleSheet("border-style: none;" "font-size: 9pt;")
        else:
            
            self.ffw.setTitleBarWidget(self.clear_label)
            self.ffw.setWidget(self.clear_label)
            self.cdw.setWidget(self.clear_label)
            self.cdw.setTitleBarWidget(self.clear_label)            

    #.........................Функция получения языка интерфейса..........................      

    def on_lng_get(self, interface_lng):
        global interface_lng_val

        self.interface_lng_val = interface_lng

        if self.interface_lng_val == 'Russian':
            self.setWindowTitle("Генератор расчетных сеток")
            self.prj_open.setToolTip('Открыть проект')
            self.msh_run.setToolTip('Выполнить генерацию расчетной сетки')
            self.msh_visual.setToolTip('Выполнить визуализацию расчетной сетки')
            self.lng_chs.setToolTip('Выбрать язык интерфейса программы')
        elif self.interface_lng_val == 'English':
            self.setWindowTitle("Mesh generator")
            self.prj_open.setToolTip('Open project')
            self.msh_run.setToolTip('Run mesh generation')
            self.msh_visual.setToolTip('Run mesh vizualization')
            self.lng_chs.setToolTip('Select the interface language for the program')          

    #.........................Функция получения пути до директории..........................

    def on_prj_path_get(self, prj_path, mesh_name_txt):
        global prj_path_val
        global mesh_name_txt_val
        global pp_dir
        
        prj_path_val = prj_path
        mesh_name_txt_val = mesh_name_txt

        pp_dir, pp_sys = os.path.split(prj_path_val)

    #.............................Функция получения типа сетки..............................

    def on_mesh_type_get(self, pd_2):
        global msh_type
        msh_type = pd_2

###---------------------------Формирование главного окна программы-------------------------

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindowClass()
    window.setFixedSize(1400, 1000)
    window.setGeometry(200, 30, 0, 0)
    window.show()
    sys.exit(app.exec_())
       
