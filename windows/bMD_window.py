import sys, re
import os

from PyQt4 import QtCore, QtGui

import pickle
import glob

from forms.bMD_forms.initial_form import initial_class
from forms.bMD_forms.vertices_form import vertices_class
from forms.bMD_forms.blocks_1_form import blocks_1_class
from forms.bMD_forms.blocks_2_form import blocks_2_class
from forms.bMD_forms.edges_1_form import edges_1_class
from forms.bMD_forms.edges_2_form import edges_2_class
from forms.bMD_forms.patches_1_form import patches_1_class
from forms.bMD_forms.patches_2_form import patches_2_class
from forms.bMD_forms.mergepatchpairs_form import mergepatchpairs_class
from functions.blockMeshDict_generation import blockMeshDict_generation_class

class bmd_window_class(QtGui.QWidget):
	def __init__(self, parent, par, prj_path_cur, mesh_name_txt_cur, pd_2_cur):
		QtGui.QWidget.__init__(self, parent)
	
		global tab
		global initial_group, spe_edit, nospe_lbl, nospe_edit, initial_btnSave, cTM_edit, nov_edit, spp_edit, nop_lbl, nop_edit, nob_edit, mpp_lbl, mpp_edit, nompp_lbl, nompp_edit, vertices_visible, blocks_visible, edges_visible, patches_visible, mergepatchpairs_visible
		global vertices_group, vert_list_main, vertices_btnSave, obj, vert_list, i_list, vert_list_main
		global blocks_1_group, blocks_1_btnSave, obj, vrs_edit_list, mg_edit_list, mg_lbl_list, napr_lbl_list, napr_edit_list, ks_lbl_list, ks_edit_list, noeG_frame_list, j_list, v_1_obsh_list, v_2_obsh_list
		global blocks_2_group, blocks_2_btnSave, obj_list, grad_type, sg_eg_obsh_list
		global patches_1_group, patches_1_btnSave, pne_list, pte_list, cnl_list, cne_list, fne_list, patch_def_list
		global patches_2_group, patches_2_btnSave, p_list, fe_main_list
		global edges_1_group, edges_1_btnSave, obj, edge_1_list, dots_quant_list, dots_quant_lbl_list
		global edges_2_group, edges_2_btnSave, nod_lbl_list, nod_main_list, nod_metk_list
		global mergepatchpairs_group, mergepatchpairs_btnSave, master_patch_list, slave_patch_list
		
		global vertices_path, blocks_1_path, blocks_2_path, edges_1_path, edges_2_path, patches_1_path, patches_2_path, mergepatchpairs_path, mergepatchpairs_visible
		
		global int_lng
		global mg_bool_old_mas
		global edg_txt_old_mas
		global dots_vls_old_mas
		global vrs_txt_old_mas
		global napr_txt_old_mas
		global ks_val_old_mas
		
		global pte_txt_old_mas
		global cne_txt_old_mas
		global fne_val_old_mas
		
		global parn
		parn = par
		
		int_lng = parent.int_lng_path_return()
		global prj_path, mesh_name_txt, pd_2 
		prj_path = prj_path_cur
		mesh_name_txt = mesh_name_txt_cur
		pd_2 = pd_2_cur
		

		#-------------------------------Загружаем вкладки для имеющегося файла----------------------------------#
		
		#------------------------------initial----------------------------------#
		
		tab = QtGui.QTabWidget()
		initial_group, spe_edit, nospe_lbl, nospe_edit, initial_btnSave, cTM_edit, nov_edit, spp_edit, nop_lbl, nop_edit, nob_edit, mpp_lbl, mpp_edit, nompp_lbl, nompp_edit, vertices_visible, blocks_visible, edges_visible, patches_visible, mergepatchpairs_visible = initial_class.out_frame_func(int_lng, prj_path, mesh_name_txt)
		tab.insertTab(0, initial_group, "&initial")
		spe_edit.stateChanged.connect(self.spe_state_changed)
		spp_edit.stateChanged.connect(self.spp_state_changed)
		mpp_edit.stateChanged.connect(self.mpp_state_changed)
		initial_btnSave.clicked.connect(self.on_initial_btnSave_clicked)
				
		#------------------------------vertices---------------------------------#

		vertices_path = prj_path + '/' + mesh_name_txt + '/' + 'vertices.pkl' 
		if vertices_visible == True:
			vertices_group, vertices_btnSave, obj, vert_list, i_list, vert_list_main = vertices_class.out_frame_func(int_lng, prj_path, mesh_name_txt, vertices_visible)
			vertices_btnSave.clicked.connect(self.on_vertices_btnSave_clicked)
			tab.insertTab(1, vertices_group, "&vertices")
		else:
			vertices_null_lbl = QtGui.QLabel()
			tab.insertTab(1, vertices_null_lbl, "&vertices")
			tab.setTabEnabled(1, False)
				
		#-------------------------------blocks_1--------------------------------#
	
		blocks_1_path = prj_path + '/' + mesh_name_txt + '/' + 'blocks_1.pkl'
		if blocks_visible == True:
			blocks_1_group, blocks_1_btnSave, obj, vrs_edit_list, mg_edit_list, mg_lbl_list, napr_lbl_list, napr_edit_list, ks_lbl_list, ks_edit_list, noeG_frame_list, j_list, v_1_obsh_list, v_2_obsh_list = blocks_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, blocks_visible)
			tab.insertTab(2, blocks_1_group, "&blocks_1")
			blocks_1_btnSave.clicked.connect(self.on_blocks_1_btnSave_clicked)

			mg_bool_old_mas = []
			vrs_txt_old_mas = []
			napr_txt_old_mas = []
			ks_val_old_mas = []
			
			for bvc in range(len(vrs_edit_list)):
				vrs_txt_old = vrs_edit_list[bvc].currentText()
				vrs_txt_old_mas.append(vrs_txt_old)
			
			for bvc in range(len(mg_edit_list)):	
				mg_bool_old = mg_edit_list[bvc].isChecked()
				mg_bool_old_mas.append(mg_bool_old)
				
			for bvc in range(len(napr_edit_list)):	
				napr_txt_old = napr_edit_list[bvc].currentText()
				napr_txt_old_mas.append(napr_txt_old)
			
			for bvc in range(len(ks_edit_list)):
				ks_val_old = ks_edit_list[bvc].value()
				ks_val_old_mas.append(ks_val_old)
				
		else:
			blocks_1_null_lbl = QtGui.QLabel()
			tab.insertTab(2, blocks_1_null_lbl, "&blocks_1")
			tab.setTabEnabled(2, False)
		
		#-------------------------------blocks_2------------------------------------#
	
		blocks_2_path = prj_path + '/' + mesh_name_txt + '/' + 'blocks_2.pkl'
		#and os.path.exists(blocks_2_path)
		if blocks_visible == True and os.path.exists(blocks_2_path):       
			blocks_2_group, blocks_2_btnSave, obj_list, grad_type, sg_eg_obsh_list = blocks_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, blocks_visible)
			tab.insertTab(3, blocks_2_group, "&blocks_2")
			blocks_2_btnSave.clicked.connect(self.on_blocks_2_btnSave_clicked)		
		else:
			blocks_2_null_lbl = QtGui.QLabel()
			tab.insertTab(3, blocks_2_null_lbl, "&blocks_2")
			tab.setTabEnabled(3, False)
		
		#--------------------------------edges_1------------------------------------#

		edges_1_path = prj_path + '/' + mesh_name_txt + '/' + 'edges_1.pkl'	
		#and os.path.exists(edges_1_path)
		if edges_visible == True:
			edges_1_group, edges_1_btnSave, obj, edge_1_list, dots_quant_list, dots_quant_lbl_list = edges_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, edges_visible)
			tab.insertTab(4, edges_1_group, "&edges_1")
			edges_1_btnSave.clicked.connect(self.on_edges_1_btnSave_clicked)
			edg_txt_old_mas = []
			dots_vls_old_mas = []
			for bvc in range(len(edge_1_list)):	
				edg_txt_old = edge_1_list[bvc].currentText()
				edg_txt_old_mas.append(edg_txt_old)
			
			for bvc in range(len(dots_quant_list)):		
				dots_vls_old = dots_quant_list[bvc].value()
				dots_vls_old_mas.append(dots_vls_old)

		else:
			edges_1_null_lbl = QtGui.QLabel()
			tab.insertTab(4, edges_1_null_lbl, "&edges_1")
			tab.setTabEnabled(4, False)
		
		#--------------------------------edges_2------------------------------------#
	
		edges_2_path = prj_path + '/' + mesh_name_txt + '/' + 'edges_2.pkl'
		#and os.path.exists(edges_2_path)
		if edges_visible == True and os.path.exists(edges_2_path):
			edges_2_group, edges_2_btnSave, nod_lbl_list, nod_main_list, nod_metk_list = edges_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, edges_visible)
			tab.insertTab(5, edges_2_group, "&edges_2")
			edges_2_btnSave.clicked.connect(self.on_edges_2_btnSave_clicked)
		else:
			edges_2_null_lbl = QtGui.QLabel()
			tab.insertTab(5, edges_2_null_lbl, "&edges_2")
			tab.setTabEnabled(5, False)
		
		#--------------------------------patches_1--------------------------------#

		patches_1_path = prj_path + '/' + mesh_name_txt + '/' + 'patches_1.pkl'
		#and os.path.exists(patches_1_path)
		if patches_visible == True:
			patches_1_group, patches_1_btnSave, pne_list, pte_list, cnl_list, cne_list, fne_list, patch_def_list = patches_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, patches_visible)
			tab.insertTab(6, patches_1_group, "&patches_1")
			patches_1_btnSave.clicked.connect(self.on_patches_1_btnSave_clicked)
			pte_txt_old_mas = []
			cne_txt_old_mas = []
			fne_val_old_mas = []
			for bvc in range(len(pte_list)):
				pte_txt_old = pte_list[bvc].currentText()
				pte_txt_old_mas.append(pte_txt_old)
			
			for bvc in range(len(cne_list)):
				cne_txt_old = cne_list[bvc].text()
				cne_txt_old_mas.append(cne_txt_old)
				
			for bvc in range(len(fne_list)):
				fne_val_old = fne_list[bvc].value()
				fne_val_old_mas.append(fne_val_old)
		else:
			patches_1_null_lbl = QtGui.QLabel()
			tab.insertTab(6, patches_1_null_lbl, "&patches_1")
			tab.setTabEnabled(6, False)
		
		#--------------------------------patches_2--------------------------------#

		patches_2_path = prj_path + '/' + mesh_name_txt + '/' + 'patches_2.pkl'
		#and os.path.exists(patches_2_path)
		if patches_visible == True and os.path.exists(patches_2_path):
			patches_2_group, patches_2_btnSave, p_list, fe_main_list = patches_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, patches_visible)
			tab.insertTab(7, patches_2_group, "&patches_2")
			patches_2_btnSave.clicked.connect(self.on_patches_2_btnSave_clicked)
		else:
			patches_2_null_lbl = QtGui.QLabel()
			tab.insertTab(7, patches_2_null_lbl, "&patches_2")
			tab.setTabEnabled(7, False)
			
		#--------------------------------mergepatchpairs------------------------------------#

		mergepatchpairs_path = prj_path + '/' + mesh_name_txt + '/' + 'mergepatchpairs.pkl'	
		#and os.path.exists(mergepatchpairs_path)
		if mergepatchpairs_visible == True and os.path.exists(patches_2_path):
			mergepatchpairs_group, mergepatchpairs_btnSave, master_patch_list, slave_patch_list = mergepatchpairs_class.out_frame_func(int_lng, prj_path, mesh_name_txt, mergepatchpairs_visible)
			tab.insertTab(8, mergepatchpairs_group, "&mergepatchpairs")
			mergepatchpairs_btnSave.clicked.connect(self.on_mergepatchpairs_btnSave_clicked)
			master_txt_old_mas = []
			slave_txt_old_mas = []
			for bvc in range(len(master_patch_list)):	
				master_txt_old = master_patch_list[bvc].currentText()
				master_txt_old_mas.append(master_txt_old)
				
			for bvc in range(len(slave_patch_list)):	
				slave_txt_old = slave_patch_list[bvc].currentText()
				slave_txt_old_mas.append(slave_txt_old)
		else:
			mergepatchpairs_null_lbl = QtGui.QLabel()
			tab.insertTab(8, mergepatchpairs_null_lbl, "&mergepatchpairs")
			tab.setTabEnabled(8, False)	
		
		#-------------------------Главный фрейм формы с элементами--------------------------#

		btnSave = QtGui.QPushButton("Сохранить")
		btnSave.setFixedSize(80, 25)
		btnSave.clicked.connect(self.on_btnSave_clicked)
		btnCancel = QtGui.QPushButton("Отмена")
		btnCancel.setFixedSize(80, 25)
		buttons_hbox = QtGui.QHBoxLayout()
		buttons_hbox.addWidget(btnSave)
		buttons_hbox.addWidget(btnCancel)
		if int_lng == 'Russian':
			btnSave.setText("Сохранить")
			btnCancel.setText("Отмена")
		elif int_lng == 'English':	
			btnSave.setText("Save")
			btnCancel.setText("Cancel")
   
		scrollLayout = QtGui.QFormLayout()
		scrollArea = QtGui.QScrollArea()
		scrollArea.setWidgetResizable(True) 
		scrollArea.setWidget(tab)
		scrollArea.setFixedSize(800, 600)	
			
		bMD_grid = QtGui.QGridLayout()
		bMD_grid.addWidget(scrollArea, 0, 0, alignment=QtCore.Qt.AlignCenter)
		bMD_grid.addLayout(buttons_hbox, 1, 0, alignment=QtCore.Qt.AlignCenter)
		bMD_frame = QtGui.QFrame()
		bMD_frame.setStyleSheet(open("./styles/properties_form_style.qss","r").read())
		bMD_frame.setFrameShape(QtGui.QFrame.Panel)
		bMD_frame.setFrameShadow(QtGui.QFrame.Sunken)
		bMD_frame.setLayout(bMD_grid)

		fvS_vbox = QtGui.QVBoxLayout() 
		fvS_vbox.addWidget(bMD_frame)

		# ---------------------Размещение на форме всех компонентов-------------------------#

		form = QtGui.QFormLayout()
		form.addRow(fvS_vbox)
		self.setLayout(form)
		
		#---------------------Привязываем к элементам формы обработчики, если изменяем имеющийся файл сетки----------------#
		
		if blocks_visible == True and os.path.exists(blocks_1_path):
						
			for bvc in range(len(vrs_edit_list)):
				self.vrs_control_chng(vrs_edit_list, bvc)	

			for bvc in range(len(mg_edit_list)):	
				self.mg_control_chng(mg_edit_list, bvc)	
				
		if spe_edit.isChecked() == True and edges_visible == True and os.path.exists(edges_1_path):
				
			for bvc in range(len(edge_1_list)):	
				self.edge_control_chng(edge_1_list, bvc)	
				
		if spp_edit.isChecked() == True and patches_visible == True and os.path.exists(patches_1_path):
				
			for bvc in range(len(pte_list)):	
				self.pte_control_chng(pte_list, bvc)	
			
	#------------------------------Связываем элементы управления с функциями----------------------------#
	
	def vrs_control_chng(self, vrs_edit_list, bvc):
		vrs_edit_list[bvc].activated.connect(lambda: self.vrs_on_change(bvc))
	
	def mg_control_chng(self, mg_edit_list, bvc):
		mg_edit_list[bvc].stateChanged.connect(lambda: self.mg_on_change(bvc))

	def edge_control_chng(self, edge_1_list, bvc):
		edge_1_list[bvc].activated.connect(lambda: self.edge_on_change(bvc))
		
	def pte_control_chng(self, pte_list, bvc):
		pte_list[bvc].activated.connect(lambda: self.pte_on_change(bvc))	

	#------------------------------Функции, связанные с элементами формы--------------------------------#

	def spe_state_changed(self):
		if spe_edit.isChecked() == False:
			nospe_lbl.setEnabled(False)
			nospe_edit.setEnabled(False)
		elif spe_edit.isChecked() == True:
			nospe_lbl.setEnabled(True)
			nospe_edit.setEnabled(True)
			
	def spp_state_changed(self):
		if spp_edit.isChecked() == False:
			nop_lbl.setEnabled(False)
			nop_edit.setEnabled(False)
			mpp_lbl.setEnabled(False)
			mpp_edit.setEnabled(False)
			mpp_edit.setChecked(False)
		elif spp_edit.isChecked() == True:
			nop_lbl.setEnabled(True)
			nop_edit.setEnabled(True)	
			mpp_lbl.setEnabled(True)
			mpp_edit.setEnabled(True)
			
	def mpp_state_changed(self):
		if mpp_edit.isChecked() == False:
			nompp_lbl.setEnabled(False)
			nompp_edit.setEnabled(False)
		elif mpp_edit.isChecked() == True:
			nompp_lbl.setEnabled(True)
			nompp_edit.setEnabled(True)
		
	def vrs_on_change(self, bvc):	
		vrs_txt = vrs_edit_list[bvc].currentText()
		if vrs_txt == "simpleGrading":
			mg_edit_list[bvc].setVisible(True)
			mg_lbl_list[bvc].setVisible(True)
			mg_edit_list[bvc].setChecked(False)
		if vrs_txt == "edgeGrading":
			mg_edit_list[bvc].setVisible(False)
			mg_lbl_list[bvc].setVisible(False)
			noeG_frame_list[bvc].setVisible(False)
				
	def mg_on_change(self, bvc):
		if mg_edit_list[bvc].isChecked() == False:
			noeG_frame_list[bvc].setVisible(False)

		if mg_edit_list[bvc].isChecked() == True:
			noeG_frame_list[bvc].setVisible(True)
				
	def edge_on_change(self, bvc):
		edge_txt = edge_1_list[bvc].currentText()
		if int_lng == 'Russian':
			if edge_txt == "Сплайновая кривая" or edge_txt == "Набор линий" or edge_txt == "B-сплайновая кривая":
				dots_quant_lbl_list[bvc].setVisible(True)
				dots_quant_list[bvc].setVisible(True)
			elif edge_txt == "Дуга окружности":
				dots_quant_lbl_list[bvc].setVisible(False)
				dots_quant_list[bvc].setVisible(False)
		elif int_lng == 'English':
			if edge_txt == "Spline curve" or edge_txt == "Set of lines" or edge_txt == "B-spline curve":
				dots_quant_lbl_list[bvc].setVisible(True)
				dots_quant_list[bvc].setVisible(True)
			elif edge_txt == "Arc of a circle":
				dots_quant_lbl_list[bvc].setVisible(False)
				dots_quant_list[bvc].setVisible(False)
				
	def pte_on_change(self, bvc):
		vrs_txt = pte_list[bvc].currentText()
		if vrs_txt == "cyclic":
			cnl_list[bvc].setVisible(True)
			cne_list[bvc].setVisible(True)
			if int_lng == 'Russian':
				definit = "Циклическая плоскость"	
			elif int_lng == 'English':
				definit = "Cyclic plane"
		elif vrs_txt == "patch":
			cnl_list[bvc].setVisible(False)
			cne_list[bvc].setVisible(False)
			if int_lng == 'Russian':
				definit = "Универсальный патч"
			elif int_lng == 'English':
				definit = "Universal patch"
		elif vrs_txt == "symmetryPlane":
			cnl_list[bvc].setVisible(False)
			cne_list[bvc].setVisible(False)
			if int_lng == 'Russian':
				definit = "Плоскость симметрии"
			elif int_lng == 'English':
				definit = "Plane of symmetry"
		elif vrs_txt == "empty":
			cnl_list[bvc].setVisible(False)
			cne_list[bvc].setVisible(False)
			if int_lng == 'Russian':
				definit = "Передняя и задняя плоскости двумерной геометрии"
			elif int_lng == 'English':
				definit = "Front and back planes of two-dimensional geometry"
		elif vrs_txt == "wedge":
			cnl_list[bvc].setVisible(False)
			cne_list[bvc].setVisible(False)
			if int_lng == 'Russian':
				definit = "Передняя и задняя поверхность клина для осесимметричной геометрии"
			elif int_lng == 'English':
				definit = "The front and back surfaces of the wedge for axially symmetric geometry"
		elif vrs_txt == "wall":
			cnl_list[bvc].setVisible(False)
			cne_list[bvc].setVisible(False)
			if int_lng == 'Russian':
				definit = "Стенка — используется для функций стенки в турбулентных потоках"	
			elif int_lng == 'English':
				definit = "Wall - used for wall functions in turbulent flows"	
		elif vrs_txt == "processor":	
			cnl_list[bvc].setVisible(False)
			cne_list[bvc].setVisible(False)
			if int_lng == 'Russian':
				definit = "Граница между процессорами"
			elif int_lng == 'English':
				definit = "Border between processors"
				
		patch_def_list[bvc].setText(definit)
			
	###---------------------Сохранение вкладки initial-------------------------###	
						
	def on_initial_btnSave_clicked(self):
		global vrs_ed_el, vrs_edit_list, mg_edit_list, mg_lbl_list, napr_lbl_list, napr_edit_list, ks_lbl_list, ks_edit_list, noeG_frame_list, j_list, v_1_obsh_list, v_2_obsh_list
		global i_list, vert_list_main
		global edges_1_group, edges_1_btnSave, obj, edge_1_list, dots_quant_list, dots_quant_lbl_list
		global blocks_1_group, blocks_1_btnSave, obj, vrs_edit_list, mg_edit_list, mg_lbl_list, napr_lbl_list, napr_edit_list, ks_lbl_list, ks_edit_list, noeG_frame_list, j_list, v_1_obsh_list, v_2_obsh_list
		global vertices_group, vertices_btnSave, obj, vert_list, i_list, vert_list_main
		global patches_1_group, patches_1_btnSave, pne_list, pte_list, cnl_list, cne_list, fne_list, patch_def_list
		global mergepatchpairs_group, mergepatchpairs_btnSave, master_patch_list, slave_patch_list
		global nospe_old, nospe_v, spe_old, spe_v, spp_old, spp_v, nop_old, nop_v, mpp_old, mpp_v, nompp_old, nompp_v
		
		#global initial_group, spe_edit, nospe_lbl, nospe_edit, initial_btnSave, cTM_edit, nov_edit, spp_edit, nop_lbl, nop_edit, nob_edit, mpp_lbl, mpp_edit, nompp_lbl, nompp_edit, vertices_visible, blocks_visible, edges_visible, patches_visible, mergepatchpairs_visible

		
		#------------------------------Получаем текущие значения полей вкладки initial--------------------------------------#

		cTM_v = cTM_edit.value()
		nob_v = nob_edit.value()
		nov_v = nov_edit.value()
		spe_v = spe_edit.isChecked()
		nospe_v = nospe_edit.value()
		spp_v = spp_edit.isChecked()
		nop_v = nop_edit.value()
		mpp_v = mpp_edit.isChecked()
		nompp_v = nompp_edit.value()
		
		#-------------------------------Сохраняем файл сетки если создаем новый----------------------------------------------#
		
		#initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
		#if sum(os.path.isfile(f) for f in glob.glob(prj_path + '/' + mesh_name_txt + '/')) == 1 and initial_path_file:
			#print()
			#os.remove(initial_path_file)
			#tab = QtGui.QTabWidget()
			#initial_group, spe_edit, nospe_lbl, nospe_edit, initial_btnSave, cTM_edit, nov_edit, spp_edit, nop_lbl, nop_edit, nob_edit, mpp_lbl, mpp_edit, nompp_lbl, nompp_edit, vertices_visible, blocks_visible, edges_visible, patches_visible, mergepatchpairs_visible = initial_class.out_frame_func(int_lng, prj_path, mesh_name_txt)
			#tab.insertTab(0, initial_group, "&initial")
			#spe_edit.stateChanged.connect(self.spe_state_changed)
			#spp_edit.stateChanged.connect(self.spp_state_changed)
			#mpp_edit.stateChanged.connect(self.mpp_state_changed)
			#initial_btnSave.clicked.connect(self.on_initial_btnSave_clicked)
		
		if vertices_visible == False and blocks_visible == False and edges_visible == False and patches_visible == False and mergepatchpairs_visible == False:
			
			initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
			###если initial сущ, а другие нет, то его удаляем
			if os.path.exists(initial_path_file) == True:
				#if sum(os.path.isfile(f) for f in glob.glob(prj_path + '/' + mesh_name_txt + '/')) == 1 and initial_path_file:
					#os.remove(initial_path_file)
					
				input = open(initial_path_file, 'rb')
				obj = pickle.load(input)
				input.close()
				
				nospe_old = None
				
				nov_old = obj['nov']
				nob_old = obj['nob']
				
				spe_old = obj['spe']
				if spe_old == True:
					nospe_old = obj['nospe']
					
				spp_old = obj['spp']
				if spp_old == True:
					nop_old = obj['nop']
					
				mpp_old = obj['mpp']
				if mpp_old == True:
					nompp_old = obj['nompp']	
				
			else:
				nov_old = nov_v
				nob_old = nob_v
				
				spe_old = spe_v
				if spe_old == True:
					nospe_old = nospe_v
				else:
					nospe_old = None
				
				spp_old = spp_v
				if spp_old == True:
					nop_old = nop_v
				else:
					nop_old = None
					
				mpp_old = mpp_v
				if mpp_old == True:
					nompp_old = nompp_v
				else:
					nompp_old = None	
										
			if spe_v == True and spp_v == True and mpp_v == True:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "nospe": nospe_v, "spp": spp_v, "nop": nop_v, "mpp": mpp_v, "nompp": nompp_v}
			
			elif spe_v == False and spp_v == True and mpp_v == True:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "spp": spp_v, "nop": nop_v, "mpp": mpp_v, "nompp": nompp_v}	
			elif spe_v == False and spp_v == False and mpp_v == True:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "spp": spp_v, "mpp": mpp_v, "nompp": nompp_v}
				
			elif spe_v == True and spp_v == False and mpp_v == False:	
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "nospe": nospe_v, "spp": spp_v, "mpp": mpp_v}	
			elif spe_v == True and spp_v == True and mpp_v == False:	
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "nospe": nospe_v, "spp": spp_v, "nop": nop_v, "mpp": mpp_v}	
				
			elif spe_v == True and spp_v == False and mpp_v == True:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "nospe": nospe_v, "spp": spp_v, "mpp": mpp_v, "nompp": nompp_v}		
			elif spe_v == False and spp_v == True and mpp_v == False:	
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "spp": spp_v, "nop": nop_v, "mpp": mpp_v}	
				
			else:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "spp": spp_v, "mpp": mpp_v}
		
			prj_path_dir = prj_path + '/' + mesh_name_txt

			if os.path.exists(prj_path_dir) == False:
				os.mkdir(prj_path_dir) 
		
			output = open(initial_path_file, 'wb')

			pickle.dump(obj, output)
			output.close()
			
		#-------------------------------Сохраняем файл сетки если пересохраняем имеющийся------------------------------------#
			
		if vertices_visible == True and blocks_visible == True and edges_visible == True or patches_visible == True or mergepatchpairs_visible == True:
			initial_path_file = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
			
			input = open(initial_path_file, 'rb')
			obj = pickle.load(input)
			input.close()

			nov_old = obj['nov']
			nob_old = obj['nob']
			
			spe_old = obj['spe']
			if spe_old == True:
				nospe_old = obj['nospe']
				
			spp_old = obj['spp']
			if spp_old == True:	
				nop_old = obj['nop']
				
			mpp_old = obj['mpp']
			if mpp_old == True:	
				nompp_old = obj['nompp']	
				
			if spe_v == True and spp_v == True and mpp_v == True:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "nospe": nospe_v, "spp": spp_v, "nop": nop_v, "mpp": mpp_v, "nompp": nompp_v}
			
			elif spe_v == False and spp_v == True and mpp_v == True:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "spp": spp_v, "nop": nop_v, "mpp": mpp_v, "nompp": nompp_v}	
			elif spe_v == False and spp_v == False and mpp_v == True:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "spp": spp_v, "mpp": mpp_v, "nompp": nompp_v}
				
			elif spe_v == True and spp_v == False and mpp_v == False:	
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "nospe": nospe_v, "spp": spp_v, "mpp": mpp_v}	
			elif spe_v == True and spp_v == True and mpp_v == False:	
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "nospe": nospe_v, "spp": spp_v, "nop": nop_v, "mpp": mpp_v}	
				
			elif spe_v == True and spp_v == False and mpp_v == True:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "nospe": nospe_v, "spp": spp_v, "mpp": mpp_v, "nompp": nompp_v}		
			elif spe_v == False and spp_v == True and mpp_v == False:	
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "spp": spp_v, "nop": nop_v, "mpp": mpp_v}	
				
			else:
				obj = {"cTM": cTM_v, "nov": nov_v, "nob": nob_v, "spe": spe_v, "spp": spp_v, "mpp": mpp_v}
			
			
			output = open(initial_path_file, 'wb')
			
			pickle.dump(obj, output)
			output.close()
			
		#----------------------------Формируем каждую из последующих вкладок если пересохраняем имеющийся файл-------------------------#
			
		if vertices_visible == True:
			if nov_v != nov_old:

				if os.path.exists(vertices_path) == True:
					os.remove(vertices_path)
					
				tab.removeTab(1)
			
				vertices_group, vertices_btnSave, obj, vert_list, i_list, vert_list_main = vertices_class.out_frame_func(int_lng, prj_path, mesh_name_txt, vertices_visible)
				vertices_btnSave.clicked.connect(self.on_vertices_btnSave_clicked)
			
				tab.insertTab(1, vertices_group, "&vertices")
			
		if blocks_visible == True:
			if nob_v != nob_old:
				
				if os.path.exists(blocks_1_path) == True: 
					os.remove(blocks_1_path)
				if os.path.exists(blocks_2_path) == True:
					os.remove(blocks_2_path)
				
				tab.removeTab(2)
			
				blocks_1_group, blocks_1_btnSave, obj, vrs_edit_list, mg_edit_list, mg_lbl_list, napr_lbl_list, napr_edit_list, ks_lbl_list, ks_edit_list, noeG_frame_list, j_list, v_1_obsh_list, v_2_obsh_list = blocks_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, blocks_visible)
				blocks_1_btnSave.clicked.connect(self.on_blocks_1_btnSave_clicked)
			
				tab.insertTab(2, blocks_1_group, "&blocks_1")
			
				for bvc in range(len(vrs_edit_list)):
					self.vrs_control_chng(vrs_edit_list, bvc)	

				for bvc in range(len(mg_edit_list)):	
					self.mg_control_chng(mg_edit_list, bvc)
			
				tab.removeTab(3)
				blocks_2_null_lbl = QtGui.QLabel()
				tab.insertTab(3, blocks_2_null_lbl, "&blocks_2")
				tab.setTabEnabled(3, False)
								
		if edges_visible == True:
			
			if spe_v == True and spe_v != spe_old or spe_v == True and spe_v == spe_old and nospe_v != nospe_old:
				
				if os.path.exists(edges_1_path):
					os.remove(edges_1_path)
				if os.path.exists(edges_2_path):
					os.remove(edges_2_path)
				
				tab.removeTab(4)
			
				edges_1_group, edges_1_btnSave, obj, edge_1_list, dots_quant_list, dots_quant_lbl_list = edges_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, edges_visible)
				edges_1_btnSave.clicked.connect(self.on_edges_1_btnSave_clicked)

				tab.insertTab(4, edges_1_group, "&edges_1")
			
				tab.removeTab(5)
				edges_2_null_lbl = QtGui.QLabel()
				tab.insertTab(5, edges_2_null_lbl, "&edges_2")
				tab.setTabEnabled(5, False)
			
				for bvc in range(len(edge_1_list)):	
					self.edge_control_chng(edge_1_list, bvc)	
			
			elif spe_v == False and spe_v != spe_old:
				
				if os.path.exists(edges_1_path):
					os.remove(edges_1_path)
				if os.path.exists(edges_2_path):
					os.remove(edges_2_path)
			
				tab.removeTab(4)
				edges_1_null_lbl = QtGui.QLabel()
				tab.insertTab(4, edges_1_null_lbl, "&edges_1")
				tab.setTabEnabled(4, False)
				
				tab.removeTab(5)
				edges_2_null_lbl = QtGui.QLabel()
				tab.insertTab(5, edges_2_null_lbl, "&edges_2")
				tab.setTabEnabled(5, False)
								
		if patches_visible == True:

			if spp_v == True and spp_v != spp_old or spp_v == True and spp_v == spp_old and nop_v != nop_old:
				
				if os.path.exists(patches_1_path) == True:
					os.remove(patches_1_path)
				if os.path.exists(patches_2_path) == True:
					os.remove(patches_2_path)
				
				tab.removeTab(6)
					
				patches_1_group, patches_1_btnSave, pne_list, pte_list, cnl_list, cne_list, fne_list, patch_def_list = patches_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, patches_visible)		
				patches_1_btnSave.clicked.connect(self.on_patches_1_btnSave_clicked)
			
				tab.insertTab(6, patches_1_group, "&patches_1")
			
				tab.removeTab(7)
				patches_2_null_lbl = QtGui.QLabel()
				tab.insertTab(7, patches_2_null_lbl, "&patches_2")
				tab.setTabEnabled(7, False)
			
				for bvc in range(len(pte_list)):	
					self.pte_control_chng(pte_list, bvc)
					
			elif spp_v == False and spp_v != spp_old:
				
				if os.path.exists(patches_1_path):
					os.remove(patches_1_path)
				if os.path.exists(patches_2_path):
					os.remove(patches_2_path)
			
				tab.removeTab(6)
				patches_1_null_lbl = QtGui.QLabel()
				tab.insertTab(6, patches_1_null_lbl, "&patches_1")
				tab.setTabEnabled(6, False)
				
				tab.removeTab(7)
				patches_2_null_lbl = QtGui.QLabel()
				tab.insertTab(7, patches_2_null_lbl, "&patches_2")
				tab.setTabEnabled(7, False)
				
				tab.removeTab(8)
				mergepatchpairs_null_lbl = QtGui.QLabel()
				tab.insertTab(8, mergepatchpairs_null_lbl, "&mergepatchpairs")
				tab.setTabEnabled(8, False)
				
		if mergepatchpairs_visible == True:
			
			if mpp_v == True and mpp_v == mpp_old and nompp_v != nompp_old or spp_v == True and spp_v == spp_old and nop_v == nop_old and mpp_v == True and mpp_v != mpp_old:
				
				if os.path.exists(mergepatchpairs_path):
					os.remove(mergepatchpairs_path)
				
				tab.removeTab(8)
			
				mergepatchpairs_group, mergepatchpairs_btnSave, master_patch_list, slave_patch_list = mergepatchpairs_class.out_frame_func(int_lng, prj_path, mesh_name_txt, mergepatchpairs_visible)
				mergepatchpairs_btnSave.clicked.connect(self.on_mergepatchpairs_btnSave_clicked)

				tab.insertTab(8, mergepatchpairs_group, "&mergepatchpairs")	
			
			elif mpp_v == False and mpp_v != mpp_old:
				
				if os.path.exists(mergepatchpairs_path):
					os.remove(mergepatchpairs_path)
				
				tab.removeTab(8)
				mergepatchpairs_null_lbl = QtGui.QLabel()
				tab.insertTab(8, mergepatchpairs_null_lbl, "&mergepatchpairs")
				tab.setTabEnabled(8, False)
				
		#----------------------------Формируем каждую из последующих вкладок если сохраняем новый файл-------------------------#

		if vertices_visible == False:
			if nov_v != nov_old or os.path.exists(vertices_path) == False:
				
				if os.path.exists(vertices_path) == True:
					os.remove(vertices_path)
				
				vertices_group, vertices_btnSave, obj, vert_list, i_list, vert_list_main = vertices_class.out_frame_func(int_lng, prj_path, mesh_name_txt, vertices_visible)
				vertices_btnSave.clicked.connect(self.on_vertices_btnSave_clicked)
				tab.setTabEnabled(1, True)
				tab.removeTab(1)
				tab.insertTab(1, vertices_group, "&vertices")
										
		if blocks_visible == False:
			if nob_v != nob_old or os.path.exists(blocks_1_path) == False:
				
				if os.path.exists(blocks_1_path) == True:
					os.remove(blocks_1_path)
				if os.path.exists(blocks_2_path) == True:
					os.remove(blocks_2_path)	
				
				blocks_1_group, blocks_1_btnSave, obj, vrs_edit_list, mg_edit_list, mg_lbl_list, napr_lbl_list, napr_edit_list, ks_lbl_list, ks_edit_list, noeG_frame_list, j_list, v_1_obsh_list, v_2_obsh_list = blocks_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, blocks_visible)
				blocks_1_btnSave.clicked.connect(self.on_blocks_1_btnSave_clicked)
								
				for bvc in range(len(vrs_edit_list)):
					self.vrs_control_chng(vrs_edit_list, bvc)	

				for bvc in range(len(mg_edit_list)):	
					self.mg_control_chng(mg_edit_list, bvc)
					
				tab.setTabEnabled(2, True)
				tab.removeTab(2)
				tab.insertTab(2, blocks_1_group, "&blocks_1")

				tab.removeTab(3)
				blocks_2_null_lbl = QtGui.QLabel()
				tab.insertTab(3, blocks_2_null_lbl, "&blocks_2")
				tab.setTabEnabled(3, False)
								
		if edges_visible == False:

			if spe_v == True and spe_v != spe_old or spe_v == True and os.path.exists(edges_1_path) == False or spe_v == True and spe_v == spe_old and nospe_v != nospe_old:
				
				if os.path.exists(edges_1_path) == True:
					os.remove(edges_1_path)
				if os.path.exists(edges_2_path) == True:
					os.remove(edges_2_path)	
				
				edges_1_group, edges_1_btnSave, obj, edge_1_list, dots_quant_list, dots_quant_lbl_list = edges_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, edges_visible)
				edges_1_btnSave.clicked.connect(self.on_edges_1_btnSave_clicked)

				for bvc in range(len(edge_1_list)):	
					self.edge_control_chng(edge_1_list, bvc)	

				tab.setTabEnabled(4, True)
				tab.removeTab(4)
				tab.insertTab(4, edges_1_group, "&edges_1")

				tab.removeTab(5)
				edges_2_null_lbl = QtGui.QLabel()
				tab.insertTab(5, edges_2_null_lbl, "&edges_2")
				tab.setTabEnabled(5, False)
			elif spe_v == False and spe_v != spe_old:
				if os.path.exists(edges_1_path) == True:
					os.remove(edges_1_path)
				if os.path.exists(edges_2_path) == True:
					os.remove(edges_2_path)	
				
				tab.removeTab(4)
				edges_1_null_lbl = QtGui.QLabel()
				tab.insertTab(4, edges_1_null_lbl, "&edges_1")
				tab.setTabEnabled(4, False)

				tab.removeTab(5)
				edges_2_null_lbl = QtGui.QLabel()
				tab.insertTab(5, edges_2_null_lbl, "&edges_2")
				tab.setTabEnabled(5, False)
		
		if patches_visible == False:

			if spp_v == True and spp_v != spp_old or spp_v == True and os.path.exists(patches_1_path) == False or spp_v == True and spp_v == spp_old and nop_v != nop_old:

				if os.path.exists(patches_1_path) == True:
					os.remove(patches_1_path)
				if os.path.exists(patches_2_path) == True:
					os.remove(patches_2_path)

				patches_1_group, patches_1_btnSave, pne_list, pte_list, cnl_list, cne_list, fne_list, patch_def_list = patches_1_class.out_frame_func(int_lng, prj_path, mesh_name_txt, patches_visible)		
				patches_1_btnSave.clicked.connect(self.on_patches_1_btnSave_clicked)
				
				for bvc in range(len(pte_list)):	
					self.pte_control_chng(pte_list, bvc)	

				tab.setTabEnabled(6, True)
				tab.removeTab(6)
				tab.insertTab(6, patches_1_group, "&patches_1")

				tab.removeTab(7)
				patches_2_null_lbl = QtGui.QLabel()
				tab.insertTab(7, patches_2_null_lbl, "&patches_2")
				tab.setTabEnabled(7, False)
				
				tab.removeTab(8)
				mergepatchpairs_null_lbl = QtGui.QLabel()
				tab.insertTab(8, mergepatchpairs_null_lbl, "&mergepatchpairs")
				tab.setTabEnabled(8, False)
				
			elif spp_v == False and spp_v != spp_old:
				if os.path.exists(patches_1_path) == True:
					os.remove(patches_1_path)
				if os.path.exists(patches_2_path) == True:
					os.remove(patches_2_path)	
				
				tab.removeTab(6)
				patches_1_null_lbl = QtGui.QLabel()
				tab.insertTab(6, patches_1_null_lbl, "&patches_1")
				tab.setTabEnabled(6, False)

				tab.removeTab(7)
				patches_2_null_lbl = QtGui.QLabel()
				tab.insertTab(7, patches_2_null_lbl, "&patches_2")
				tab.setTabEnabled(7, False)	
				
				tab.removeTab(8)
				mergepatchpairs_null_lbl = QtGui.QLabel()
				tab.insertTab(8, mergepatchpairs_null_lbl, "&mergepatchpairs")
				tab.setTabEnabled(8, False)
				
		if mergepatchpairs_visible == False:

			if mpp_v == True and mpp_v == mpp_old and nompp_v != nompp_old or spp_v == True and spp_v == spp_old and nop_v == nop_old and mpp_v == True and mpp_v != mpp_old:
				
				if os.path.exists(mergepatchpairs_path) == True:
					os.remove(mergepatchpairs_path)

				mergepatchpairs_group, mergepatchpairs_btnSave, master_patch_list, slave_patch_list = mergepatchpairs_class.out_frame_func(int_lng, prj_path, mesh_name_txt, mergepatchpairs_visible)
				mergepatchpairs_btnSave.clicked.connect(self.on_mergepatchpairs_btnSave_clicked)
	
				tab.setTabEnabled(8, True)
				tab.removeTab(8)
				tab.insertTab(8, mergepatchpairs_group, "&mergepatchpairs")

			elif mpp_v == False and mpp_v != mpp_old:
				if os.path.exists(mergepatchpairs_path) == True:
					os.remove(mergepatchpairs_path)
	
				tab.removeTab(8)
				mergepatchpairs_null_lbl = QtGui.QLabel()
				tab.insertTab(8, mergepatchpairs_null_lbl, "&mergepatchpairs")
				tab.setTabEnabled(8, False)

		if int_lng == 'Russian':
			msg = "Начальные данные успешно сохранены"
		elif int_lng == 'English':
			msg = "Initial data saved successfully"
		self.on_msg_correct(msg)

	###---------------------Сохранение вкладки vertices-------------------------###		

	def on_vertices_btnSave_clicked(self):
				
		main_value_list = []
		msg_list = []
		k = 0
		for el_m in vert_list_main:
		
			m = 0
			value_list = []
			for el_n in el_m:
	
				if el_n.text() == "" and m == 0:
					if int_lng == 'Russian':
						msg = "Укажите координату 'x1' для вершины " + str(k)
					elif int_lng == 'English':
						msg = "Specify the 'x1' coordinate for the vertex " + str(k)
					msg_list.append(msg)
				elif el_n.text() == "" and m == 1:
					if int_lng == 'Russian':
						msg = "Укажите координату 'x2' для вершины " + str(k)
					elif int_lng == 'English':
						msg = "Specify the 'x2' coordinate for the vertex " + str(k)
					msg_list.append(msg)
				elif el_n.text() == "" and m == 2:
					if int_lng == 'Russian':
						msg = "Укажите координату 'x3' для вершины " + str(k)
					elif int_lng == 'English':
						msg = "Specify the 'x3' coordinate for the vertex " + str(k)
					msg_list.append(msg)
				
				value_list.append(el_n.text())				
				m = m + 1
							
			if not "" in value_list:
				main_value_list.append(value_list)
			
			k = k + 1
				
		self.on_msg_error(msg_list)
		
		if len(vert_list_main) == len(main_value_list):
			l = 0
			vertices_obj_list = []
			for e in main_value_list:
				obj = {"vertex_" + str(l): e}
				vertices_obj_list.append(obj)
				l = l + 1
						
			output = open(prj_path + '/' + mesh_name_txt + '/' + 'vertices.pkl', 'wb')
			pickle.dump(vertices_obj_list, output)
			output.close()
			
			if int_lng == 'Russian':
				msg = "Данные vertices успешно сохранены"	
			elif int_lng == 'English':
				msg = "The vertices data was successfully saved"	
			self.on_msg_correct(msg)
			
	###---------------------Сохранение вкладки blocks_1-------------------------###	
			
	def on_blocks_1_btnSave_clicked(self):
		global blocks_2_group, blocks_2_btnSave, obj_list, grad_type, sg_eg_obsh_list
		global mg_bool_old_mas
		global vrs_txt_old_mas
		global napr_txt_old_mas
		global ks_val_old_mas
			
		versh_list_main = []
		msg_list = []
		i = 1
		for el_m in v_1_obsh_list:
			versh_list = []
			for el_n in el_m:
				versh_list.append(el_n.text())
				
			if "" in versh_list:
				if int_lng == 'Russian':
					msg = "Укажите корректный список вершин для блока " + str(i)
				elif int_lng == 'English':
					msg = "Specify the correct vertex list for the block " + str(i)
				msg_list.append(msg)
				
			else:
				versh_list_main.append(versh_list)
				
			i = i + 1	
		
		yach_list_main = []
		i = 1
		for el_m in v_2_obsh_list:
			
			yach_list = []
			for el_n in el_m:
				yach_list.append(el_n.text())
			
			j = 1	
			for el_yach in yach_list:

				if el_yach == "" in yach_list and j == 1:
					if int_lng == 'Russian':
						msg = "Укажите корректное число ячеек для направления 'x1' блока " + str(i)
					elif int_lng == 'English':
						msg = "Specify the correct number of cells for the 'x1' direction of the block " + str(i)
					msg_list.append(msg)
				elif el_yach == "" in yach_list and j == 2:
					if int_lng == 'Russian':
						msg = "Укажите корректное число ячеек для направления 'x2' блока " + str(i)
					elif int_lng == 'English':
						msg = "Specify the correct number of cells for the 'x2' direction of the block " + str(i)
					msg_list.append(msg)
				elif el_yach == "" in yach_list and j == 3:
					if int_lng == 'Russian':
						msg = "Укажите корректное число ячеек для направления 'x3' блока " + str(i)
					elif int_lng == 'English':
						msg = "Specify the correct number of cells for the 'x3' direction of the block " + str(i)
					msg_list.append(msg)
				
				j = j + 1
			
			if not "" in yach_list:
				yach_list_main.append(yach_list)
			
			i = i + 1	
		
		self.on_msg_error(msg_list)
		
		srya_list = []
		for el_k in vrs_edit_list:
			srya_list.append(el_k.currentText())	
		
		mg_list = []
		napr_list = []
		ks_list = []
		i = 0
		for mg_el in mg_edit_list:
			if vrs_edit_list[i].currentText() == "simpleGrading" and noeG_frame_list[i].isVisible() == True:
				mg_list.append(True)
				napr_list.append(napr_edit_list[i].currentText())
				ks_list.append(ks_edit_list[i].value())
			elif vrs_edit_list[i].currentText() == "simpleGrading" and noeG_frame_list[i].isVisible() == False:
				mg_list.append(False)
				napr_list.append(False)
				ks_list.append(False)
			elif vrs_edit_list[i].currentText() == "edgeGrading":
				mg_list.append(False)
				napr_list.append(False)
				ks_list.append(False)
			i = i + 1
			
		if len(versh_list_main) == len(v_1_obsh_list) and len(yach_list_main) == len(v_2_obsh_list) and len(srya_list) == len(vrs_edit_list):
			i = 0
			n = 1
						
			obj_list = []
			
			for el_m in j_list:
				obj = {"versh_" + str(n): versh_list_main[i], "yach_" + str(n): yach_list_main[i], "srya_" + str(n): srya_list[i], "mg_" + str(n): mg_list[i], "napr_" + str(n): napr_list[i], "ks_" + str(n): ks_list[i]}
				obj_list.append(obj)
				i = i + 1
				n = n + 1

			output = open(prj_path + '/' + mesh_name_txt + '/' + 'blocks_1.pkl', 'wb')
			pickle.dump(obj_list, output)
			output.close()
			
			if int_lng == 'Russian':
				msg = "Данные blocks_1 успешно сохранены"
			elif int_lng == 'English':
				msg = "The blocks_1 data was successfully saved"
			self.on_msg_correct(msg)

					        
			if blocks_visible == False:
				if os.path.exists(blocks_2_path) == True:
					os.remove(blocks_2_path)
					
				blocks_2_group, blocks_2_btnSave, obj_list, grad_type, sg_eg_obsh_list = blocks_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, blocks_visible)
	
				blocks_2_btnSave.clicked.connect(self.on_blocks_2_btnSave_clicked)
			
				tab.setTabEnabled(3, True)
				tab.removeTab(3)
				tab.insertTab(3, blocks_2_group, "&blocks_2")
			
			if blocks_visible == True:				
				vrs_txt_new_mas = []
				mg_bool_new_mas = []
				napr_txt_new_mas = []
				ks_val_new_mas = []
				
				for bvc in range(len(vrs_edit_list)):
					vrs_txt_new = vrs_edit_list[bvc].currentText()
					vrs_txt_new_mas.append(vrs_txt_new)
					
				for bvc in range(len(mg_edit_list)):
					mg_bool_new = mg_edit_list[bvc].isChecked()
					mg_bool_new_mas.append(mg_bool_new)
				
				for bvc in range(len(napr_edit_list)):
					napr_txt_new = napr_edit_list[bvc].currentText()
					napr_txt_new_mas.append(napr_txt_new)
					
				for bvc in range(len(ks_edit_list)):
					ks_val_new = ks_edit_list[bvc].value()
					ks_val_new_mas.append(ks_val_new)
					
				if vrs_txt_old_mas != vrs_txt_new_mas or mg_bool_old_mas != mg_bool_new_mas or napr_txt_old_mas != napr_txt_new_mas or ks_val_old_mas != ks_val_new_mas or os.path.exists(blocks_2_path) == False:
					if os.path.exists(blocks_2_path) == True:
						os.remove(blocks_2_path)
					blocks_2_group, blocks_2_btnSave, obj_list, grad_type, sg_eg_obsh_list = blocks_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, blocks_visible)
					blocks_2_btnSave.clicked.connect(self.on_blocks_2_btnSave_clicked)
					tab.setTabEnabled(3, True)
					tab.removeTab(3)
					tab.insertTab(3, blocks_2_group, "&blocks_2")
				
				vrs_txt_old_mas = vrs_txt_new_mas
				mg_bool_old_mas = mg_bool_new_mas
				napr_txt_old_mas = napr_txt_new_mas
				mg_bool_old_mas = mg_bool_new_mas
				ks_val_old_mas = ks_val_new_mas
			
	###---------------------Сохранение вкладки blocks_2-------------------------###				
		
	def on_blocks_2_btnSave_clicked(self):
		
		bbk = []
		msg_list = []
		
		i = 1
		w = 0
		for el_gt in sg_eg_obsh_list:
			if grad_type[w] == "simpleGrading":
				j = 1
				sg_value_list = []
				for rt in el_gt:
					if rt.text() == "" and j == 1:
						if int_lng == 'Russian':
							msg = "Укажите корректную степень для направления 'x1' блока " + str(i)
						elif int_lng == 'English':
							msg = "Specify the correct degree for the 'x1' direction of the block " + str(i)
						msg_list.append(msg)
					elif rt.text() == "" and j == 2:
						if int_lng == 'Russian':
							msg = "Укажите корректную степень для направления 'x2' блока " + str(i)
						elif int_lng == 'English':
							msg = "Specify the correct degree for the 'x2' direction of the block " + str(i)
						msg_list.append(msg)
					elif rt.text() == "" and j == 3:
						if int_lng == 'Russian':
							msg = "Укажите корректную степень для направления 'x3' блока " + str(i)
						elif int_lng == 'English':
							msg = "Specify the correct degree for the 'x3' direction of the block " + str(i)
						msg_list.append(msg)
					else:
						sg_value_list.append(rt.text())
					
					j = j + 1
					
				if len(sg_value_list) == 3:
					bbk.append(sg_value_list)
					
			#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

			if grad_type[w] == "edgeGrading":
				j = 1
				eg_value_list = []
				for rt in el_gt:
					if rt.text() == "":
						if int_lng == 'Russian':
							msg = "Укажите корректную степень для ребра " + str(j) + " блока " + str(i)
						elif int_lng == 'English':
							msg = "Specify the correct degree for the edge " + str(j) + " of the block " + str(i)
						msg_list.append(msg)
					else:
						eg_value_list.append(rt.text())
					j = j + 1
					
				if len(eg_value_list) == 12:
					bbk.append(eg_value_list)
					
			#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
						
			if grad_type[w] == "simpleGrading_mg":
				
				sg_mg_value_list = []
				j = 1
				for napr in el_gt:
					if j == 1 and type(napr) == list:
						x_napr = {}
						
						k = 1
						napr_val_list = []
						for sect in napr:
							b = 1
							sect_val_list = []
							for stepen in sect:
								if stepen.text() == "":
									if int_lng == 'Russian':
										msg = "Укажите корректное значение для степени " + str(b) + " сектора " + str(k) + " направления 'x'" + " блока " + str(i)
									elif int_lng == 'English':
										msg = "Please enter a valid value for the degree " + str(b) + " of the sector " + str(k) + " of the direction 'x'" + " of the block " + str(i)
									msg_list.append(msg)
								else:
									sect_val_list.append(stepen.text())
								b = b + 1
							x_obj = {"sekt_" + str(k): sect_val_list}
							napr_val_list.append(x_obj)
							k = k + 1
						
						x_napr_list = []
						if len(sect) == len(sect_val_list) and len(napr) == len(napr_val_list):
							x_napr = {"x": napr_val_list}
							
					if j == 1 and type(napr) != list:
						x_napr = {}
						if napr.text() == "":
							if int_lng == 'Russian':
								msg = "Укажите корректное значение для степени направления 'x'" + " блока " + str(i)
							elif int_lng == 'English':
								msg = "Specify the correct value for the degree of direction 'x'" + " of the block " + str(i)
							msg_list.append(msg)
						else:
							x_napr = {"x": napr.text()}
							
					#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#	
						
					if j == 2 and type(napr) == list:
						y_napr = {}
						
						k = 1
						napr_val_list = []
						for sect in napr:
							b = 1
							sect_val_list = []
							for stepen in sect:
								if stepen.text() == "":
									if int_lng == 'Russian':
										msg = "Укажите корректное значение для степени " + str(b) + " сектора " + str(k) + " направления 'y'" + " блока " + str(i)
									elif int_lng == 'English':
										msg = "Please enter a valid value for the degree " + str(b) + " of the sector " + str(k) + " of the direction 'y'" + " of the block " + str(i)
									msg_list.append(msg)
								else:
									sect_val_list.append(stepen.text())
								b = b + 1
							y_obj = {"sekt_" + str(k): sect_val_list}
							napr_val_list.append(y_obj)
							k = k + 1	
							
						y_napr_list = []
						if len(sect) == len(sect_val_list) and len(napr) == len(napr_val_list):
							y_napr = {"y": napr_val_list}
							
					if j == 2 and type(napr) != list:
						y_napr = {}
						if napr.text() == "":
							if int_lng == 'Russian':
								msg = "Укажите корректное значение для степени направления 'y'" + " блока " + str(i)
							elif int_lng == 'English':
								msg = "Specify the correct value for the degree of direction 'y'" + " блока " + str(i)
							msg_list.append(msg)
						else:
							y_napr = {"y": napr.text()}
					
					#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
							
					if j == 3 and type(napr) == list:
						z_napr = {}
						k = 1
						napr_val_list = []
						for sect in napr:
							b = 1
							sect_val_list = []
							for stepen in sect:
								if stepen.text() == "":
									if int_lng == 'Russian':
										msg = "Укажите корректное значение для степени " + str(b) + " сектора " + str(k) + " направления 'z'" + " блока " + str(i)
									elif int_lng == 'English':
										msg = "Please enter a valid value for the degree " + str(b) + " of the sector " + str(k) + " of the direction 'z'" + " of the block " + str(i)
									msg_list.append(msg)
								else:
									sect_val_list.append(stepen.text())
								b = b + 1
							z_obj = {"sekt_" + str(k): sect_val_list}
							napr_val_list.append(z_obj)
							k = k + 1	
							
						y_napr_list = []
						if len(sect) == len(sect_val_list) and len(napr) == len(napr_val_list):
							z_napr = {"z": napr_val_list}
							
					if j == 3 and type(napr) != list:
						z_napr = {}
						if napr.text() == "":
							if int_lng == 'Russian':
								msg = "Укажите корректное значение для степени направления 'z'" + " блока " + str(i)
							elif int_lng == 'English':
								msg = "Specify the correct value for the degree of 'z' direction" + " of the block " + str(i)
							msg_list.append(msg)
						else:
							z_napr = {"z": napr.text()}
							
					j = j + 1
					
				if x_napr != {} and y_napr != {} and z_napr != {}:

					xyz_value_list = []
					xyz_value_list.append(x_napr)
					xyz_value_list.append(y_napr)
					xyz_value_list.append(z_napr)
					
					obj_sg_mg = {"mg_blocks_" + str(i): xyz_value_list}
					
					sg_mg_value_list.append(obj_sg_mg)
					
					bbk.append(sg_mg_value_list)
						
			i = i + 1
			w = w + 1

		self.on_msg_error(msg_list)

		if len(grad_type) == len(bbk):
			itog_list = []
			w = 0
			for it_el in grad_type:
				obj_itog = {it_el: bbk[w]}
			
				itog_list.append(obj_itog)
				w = w + 1
			
			output = open(prj_path + '/' + mesh_name_txt + '/' + 'blocks_2.pkl', 'wb')
			pickle.dump(itog_list, output)
			output.close()
			
			if int_lng == 'Russian':
				msg = "Данные blocks_2 успешно сохранены"
			elif int_lng == 'English':
				msg = "The blocks_2 data was successfully saved"
			self.on_msg_correct(msg)
			
	###---------------------Сохранение вкладки edge_1-------------------------###			
		
	def on_edges_1_btnSave_clicked(self):
		global edges_2_group, edges_2_btnSave, nod_lbl_list, nod_main_list, nod_metk_list
		global edg_txt_old_mas
		global dots_vls_old_mas
		
		i = 0
				
		obj_list = []
			
		for el_m in edge_1_list:
			if int_lng == 'Russian':
				if el_m.currentText() == "Дуга окружности":
					obj = {el_m.currentText(): None}
				else:
					obj = {el_m.currentText(): dots_quant_list[i].value()}
			elif int_lng == 'English':
				if el_m.currentText() == "Arc of a circle":
					obj = {el_m.currentText(): None}
				else:
					obj = {el_m.currentText(): dots_quant_list[i].value()}
			obj_list.append(obj)
			i = i + 1
			
		output = open(prj_path + '/' + mesh_name_txt + '/' + 'edges_1.pkl', 'wb')
		pickle.dump(obj_list, output)
		output.close()
			
		if int_lng == 'Russian':
			msg = "Данные edges_1 успешно сохранены"
		elif int_lng == 'English':
			msg = "The edges_1 data was successfully saved"
		self.on_msg_correct(msg)
	
		if edges_visible == False:
			if os.path.exists(edges_2_path) == True:
				os.remove(edges_2_path)	
			
			edges_2_group, edges_2_btnSave, nod_lbl_list, nod_main_list, nod_metk_list = edges_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, edges_visible)
			edges_2_btnSave.clicked.connect(self.on_edges_2_btnSave_clicked)
			tab.setTabEnabled(5, True)
			tab.removeTab(5)
			tab.insertTab(5, edges_2_group, "&edges_2")
			
		if edges_visible == True:
			edg_txt_new_mas = []
			dots_vls_new_mas = []
			for bvc in range(len(edge_1_list)):	
				edg_txt_new = edge_1_list[bvc].currentText()
				edg_txt_new_mas.append(edg_txt_new)
			for bvc in range(len(dots_quant_list)):		
				dots_vls_new = dots_quant_list[bvc].value()
				dots_vls_new_mas.append(dots_vls_new)
					
			if edg_txt_old_mas != edg_txt_new_mas or dots_vls_old_mas != dots_vls_new_mas or nospe_old != nospe_v or nospe_old == nospe_v and spe_old != spe_v or os.path.exists(edges_2_path) == False:

				if os.path.exists(edges_2_path) == True:
					os.remove(edges_2_path)
						
				edges_2_group, edges_2_btnSave, nod_lbl_list, nod_main_list, nod_metk_list = edges_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, edges_visible)
				edges_2_btnSave.clicked.connect(self.on_edges_2_btnSave_clicked)
				tab.setTabEnabled(5, True)
				tab.removeTab(5)
				tab.insertTab(5, edges_2_group, "&edges_2")
				
			edg_txt_old_mas = edg_txt_new_mas
			dots_vls_old_mas = dots_vls_new_mas		
		
	###---------------------Сохранение вкладки edge_2-------------------------###		
		
	def on_edges_2_btnSave_clicked(self):
		obj_list = []
		i = 0
		j = 1

		common_list = []
		msg_list = []
		
		for el_m in nod_lbl_list:			
			metk_value_list = []
			common_obj = {}

			n = 1
			for metk in nod_metk_list[i]:
				metk_value = metk.text()
				if metk_value != '':
					metk_value_list.append(metk_value)
				else:
					if int_lng == 'Russian':
						msg = "Укажите корректные значения метки вершины " + str(n) + " ребра " + str(j)
					elif int_lng == 'English':
						msg = "Specify the correct values for the vertex label " + str(n) + " of the edge " + str(j)
					msg_list.append(msg)
				n = n + 1
							
			if len(metk_value_list) == 2:
				common_obj['metk_' + str(j)] = metk_value_list
				
			if el_m == 'Дуга окружности' or el_m == 'Arc of a circle':		
				do_value_list = []
				for do in nod_main_list[i]:
					do_value = do.text()
					if do_value != '':
						do_value_list.append(do_value)
						
				if len(do_value_list) == 3:	
					common_obj['values_' + str(j)] = do_value_list
				else:
					if int_lng == 'Russian':
						msg = "Укажите корректные значения координат точки для ребра " + str(j)
					elif int_lng == 'English':
						msg = "Specify the correct coordinates for the point for the edge " + str(j)
					msg_list.append(msg)
								
			elif el_m == 'Сплайновая кривая' or el_m == 'Набор линий' or el_m == 'B-сплайновая кривая' or el_m == "Spline curve" or el_m == "Set of lines" or el_m == "B-spline curve":
				do_ext_list = []
				k = 1
				for do_ext in nod_main_list[i]:
					do_int_list = []
					for do_int in do_ext:
						do_int_value = do_int.text()
						if do_int_value != '':
							do_int_list.append(do_int_value)
					
					if len(do_int_list) == 3:
						do_ext_list.append(do_int_list)
					else:
						if int_lng == 'Russian':
							msg = "Укажите корректные значения координат точки " + str(k) + " для ребра " + str(j)
						elif int_lng == 'English':
							msg = "Specify the correct values for the coordinates of the point " + str(k) + " for the edge " + str(j)
						msg_list.append(msg)
						
					k = k + 1	
				if len(nod_main_list[i]) == len(do_ext_list):
					common_obj['values_' + str(j)] = do_ext_list

			if len(common_obj) == 2:
				common_list.append(common_obj)

			i = i + 1
			j = j + 1
	
		self.on_msg_error(msg_list)

		if len(nod_lbl_list) == len(common_list):
		
			output = open(prj_path + '/' + mesh_name_txt + '/' + 'edges_2.pkl', 'wb')
			pickle.dump(common_list, output)
			output.close()
				
			if int_lng == 'Russian':
				msg = "Данные edges_2 успешно сохранены"
			elif int_lng == 'English':
				msg = "The edges_2 data was successfully saved"

			self.on_msg_correct(msg)
		
	###---------------------Сохранение вкладки patches_1-------------------------###
		
	def on_patches_1_btnSave_clicked(self):
		
		
		global patches_2_group, patches_2_btnSave, p_list, fe_main_list
		global mergepatchpairs_group, mergepatchpairs_btnSave, master_patch_list, slave_patch_list
		global pte_txt_old_mas
		global cne_txt_old_mas 
		global fne_val_old_mas 
		
		k = 1
		pne_incor_list = []
		msg_list = []
		for el_m in pne_list:
			if el_m.text() == "":
				if int_lng == 'Russian':
					msg = "Укажите корректное название патча " + str(k)
				elif int_lng == 'English':
					msg = "Please enter a valid patch name " + str(k)
				msg_list.append(msg)
				pne_incor_list.append(None)
			else:
				pne_incor_list.append("")
				
			k = k + 1
			
		m = 0
		l = 1
		pte_incor_list = []
		for el_m in pte_list:
			if el_m.currentText() == 'cyclic':
				if cne_list[m].text() == "":
					if int_lng == 'Russian':
						msg = "Укажите корректное имя циклического патча " + str(l)
					elif int_lng == 'English':
						msg = "Please enter a valid cyclical patch name " + str(l)
					msg_list.append(msg)
					pte_incor_list.append(None)
				else:
					pte_incor_list.append("")
			else:
				pte_incor_list.append("")
			m = m + 1
			l = l + 1
			
		self.on_msg_error(msg_list)
		
		if not None in pte_incor_list and not None in pne_incor_list:
			obj_list = []
			i = 1
			j = 0
			for el_m in pte_list:
				if el_m.currentText() != 'cyclic':
					obj = {"patch_" + str(i): pne_list[j].text(), "type_" + str(i): el_m.currentText(), "faces_" + str(i): fne_list[j].value()}
					
				if el_m.currentText() == 'cyclic':
					obj = {"patch_" + str(i): pne_list[j].text(), "type_" + str(i): el_m.currentText(), "neighb_" + str(i): cne_list[j].text(), "faces_" + str(i): fne_list[j].value()}
				
				obj_list.append(obj)
				i = i + 1
				j = j + 1

			output = open(prj_path + '/' + mesh_name_txt + '/' + 'patches_1.pkl', 'wb')
			pickle.dump(obj_list, output)
			output.close()
			
			if int_lng == 'Russian':
				msg = "Данные patches_1 успешно сохранены"
			elif int_lng == 'English':
				msg = "The patches_1 data was successfully saved"
			self.on_msg_correct(msg)
			
			if patches_visible == False:
				if os.path.exists(patches_2_path) == True:
					os.remove(patches_2_path)
					
				patches_2_group, patches_2_btnSave, p_list, fe_main_list = patches_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, patches_visible)
				patches_2_btnSave.clicked.connect(self.on_patches_2_btnSave_clicked)
				tab.setTabEnabled(7, True)
				tab.removeTab(7)
				tab.insertTab(7, patches_2_group, "&patches_2")

			if patches_visible == True:
				
				pte_txt_new_mas = []
				cne_txt_new_mas = []
				fne_val_new_mas = []
				for bvc in range(len(pte_list)):
					pte_txt_new = pte_list[bvc].currentText()
					pte_txt_new_mas.append(pte_txt_new)
					
				for bvc in range(len(cne_list)):
					cne_txt_new = cne_list[bvc].text()
					cne_txt_new_mas.append(cne_txt_new)
				
				for bvc in range(len(fne_list)):
					fne_val_new = fne_list[bvc].value()
					fne_val_new_mas.append(fne_val_new)

				if pte_txt_old_mas != pte_txt_new_mas or cne_txt_old_mas != cne_txt_new_mas or fne_val_old_mas != fne_val_new_mas or os.path.exists(patches_2_path) == False:
					if os.path.exists(patches_2_path) == True:
						os.remove(patches_2_path)

					patches_2_group, patches_2_btnSave, p_list, fe_main_list = patches_2_class.out_frame_func(int_lng, prj_path, mesh_name_txt, patches_visible)
					patches_2_btnSave.clicked.connect(self.on_patches_2_btnSave_clicked)
					tab.setTabEnabled(7, True)
					tab.removeTab(7)
					tab.insertTab(7, patches_2_group, "&patches_2")	
				
				pte_txt_old_mas = pte_txt_new_mas
				cne_txt_old_mas = cne_txt_new_mas
				fne_val_old_mas = fne_val_new_mas
			
			if mpp_v == True:
				
				if os.path.exists(mergepatchpairs_path):
					os.remove(mergepatchpairs_path)

				tab.removeTab(8)

				mergepatchpairs_group, mergepatchpairs_btnSave, master_patch_list, slave_patch_list = mergepatchpairs_class.out_frame_func(int_lng, prj_path, mesh_name_txt, mergepatchpairs_visible)
				mergepatchpairs_btnSave.clicked.connect(self.on_mergepatchpairs_btnSave_clicked)

				tab.insertTab(8, mergepatchpairs_group, "&mergepatchpairs")	

			elif mpp_v == False:

				if os.path.exists(mergepatchpairs_path):
					os.remove(mergepatchpairs_path)

				tab.removeTab(8)
				mergepatchpairs_null_lbl = QtGui.QLabel()
				tab.insertTab(8, mergepatchpairs_null_lbl, "&mergepatchpairs")
				tab.setTabEnabled(8, False)			
								
	###---------------------Сохранение вкладки patches_2-------------------------###			
	
	def on_patches_2_btnSave_clicked(self):
		
		i = 0
		n = 1
		msg_list = []
		f3_list = []

		for f_el in fe_main_list:

			f1_list = []
			fd_list = []
			y = 1
			for el_m in f_el:
				
				if type(el_m) != list:
					flag = True
					if el_m.text() == "":
						fd_list.append(None)
					else:
						fd_list.append(el_m.text())
						
				if type(el_m) == list:
					fk_list  = []
					for e_m in el_m:
						if e_m.text() == "":
							fk_list.append(None)
						else:
							fk_list.append(e_m.text())
					if fk_list != [] and not None in fk_list:
						f1_list.append(fk_list) 
					else:
						f1_list.append(None) 
									
					if fk_list != [] and None in fk_list:
						if int_lng == 'Russian':
							msg = "Укажите корректный список вершин грани " + str(y) + " патча " + str(n)	
						elif int_lng == 'English':
							msg = "Specify the correct vertex list of the face " + str(y) + " of the patch " + str(n)
						msg_list.append(msg)
					
					y = y + 1
					
			if fd_list != [] and not None in fd_list and flag == True:
				f1_list.append(fd_list) 
			elif None in fd_list and flag == True:
				f1_list.append(None) 
					
			if fd_list != [] and None in fd_list:
				msg = "Укажите корректный список вершин грани патча " + str(n)	
				msg_list.append(msg)
				
			if not None in f1_list and f1_list != []:
				f3_list.append(f1_list)
				
			i = i + 1
			n = n + 1
							
		self.on_msg_error(msg_list)
								
		if len(f3_list) == len(fe_main_list):
			obj_list = []
			i = 0
			for el_m in p_list:
				obj = {el_m: f3_list[i]}
				obj_list.append(obj)
				
				i = i + 1
			
			output = open(prj_path + '/' + mesh_name_txt + '/' + 'patches_2.pkl', 'wb')
			pickle.dump(obj_list, output)
			output.close()
			
			if int_lng == 'Russian':
				msg = "Данные patches_2 успешно сохранены"
			elif int_lng == 'English':
				msg = "The patches_2 data was successfully saved"
				
			self.on_msg_correct(msg)
							
	###---------------------Сохранение вкладки mergepatchpairs-------------------------###
	
	def on_mergepatchpairs_btnSave_clicked(self):

		i = 0
		k = 1
		obj_list = []
		for mp_el in master_patch_list:
			obj = {'master_' + str(k): mp_el.currentText(), 'slave_' + str(k): slave_patch_list[i].currentText()}
			obj_list.append(obj)
			i = i + 1
			k = k + 1
			
		output = open(prj_path + '/' + mesh_name_txt + '/' + 'mergepatchpairs.pkl', 'wb')
		pickle.dump(obj_list, output)
		output.close()

		if int_lng == 'Russian':
			msg = "Данные mergepatchpairs успешно сохранены"
		elif int_lng == 'English':
			msg = "The mergepatchpairs data was successfully saved"

		self.on_msg_correct(msg)
		

	###--------------------Функции вывода служебных сообщений-------------------------------#
			
	def on_msg_correct(self, msg):
		parn.listWidget.clear()
		parn.item = QtGui.QListWidgetItem(msg, parn.listWidget)
		color = QtGui.QColor("green")
		parn.item.setTextColor(color)
		parn.listWidget.addItem(parn.item)		
	def on_msg_error(self, msg_list):
		parn.listWidget.clear()
		for msg in msg_list:
			parn.item = QtGui.QListWidgetItem(msg, parn.listWidget)
			color = QtGui.QColor("red")
			parn.item.setTextColor(color)
			parn.listWidget.addItem(parn.item)

	###---------------------Запуск сохранения файла blocksMeshDict-------------------------###			
			
	def on_btnSave_clicked(self):
		blockMeshDict_generation_class.blockMeshDict_func(int_lng, parn, tab, spe_edit, spp_edit, mpp_edit, prj_path, mesh_name_txt, self)
	             
