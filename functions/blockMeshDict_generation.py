# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil

class blockMeshDict_generation_class:			
	def blockMeshDict_func(int_lng, parn, tab, spe_edit, spp_edit, mpp_edit, prj_path, mesh_name_txt, bmd_par): 
		def blockMeshDict_end(int_lng, prj_path, parn):
			bMD = open(prj_path + '/blockMeshDict', 'a')

			close_str = '// ************************************************************************* //'
			bMD.write(close_str)
			bMD.close()

			if int_lng == 'Russian':
				msg = "Файл blockMeshDict сохранен"
			elif int_lng == 'English':
				msg = "The 'blockMeshDict' file was saved"
			bmd_par.on_msg_correct(msg)

			parn.cdw.setWidget(parn.outf_scroll)
			parn.outf_scroll.setFixedSize(350, 660)
			parn.cdw_frame.setFixedSize(350, 35)
			
			parn.msh_run.setEnabled(True)

			prj_dir = prj_path + '/blockMeshDict'

			outf = open(prj_dir)
			data = outf.read()
			if int_lng == 'Russian':
				parn.outf_lbl.setText("Файл " + "<font color='peru'>" + 'blockMeshDict' + "</font>") 
			elif int_lng == 'English':
				parn.outf_lbl.setText("<font color='peru'>" + 'blockMeshDict' + "</font>" + " file") 
			parn.outf_edit.setText(data)
			parn.cdw.setWidget(parn.outf_scroll)

			parn.cdw.setTitleBarWidget(parn.cdw_frame)
	
		msg_list = []
		
		#проверяем на заполнение initial#
		initial_path = prj_path + '/' + mesh_name_txt + '/' + 'initial.pkl'
		if os.path.exists(initial_path):
			initial_vkl_arr = []
			
			initial_input = open(initial_path, 'rb')
			obj = pickle.load(initial_input)
			initial_input.close()
			
			cTM_v = obj['cTM']
			
			initial_vkl_arr.append('initial')
			
		else:
			initial_vkl_arr = []
			
			if int_lng == 'Russian':
				msg = "Заполните форму 'initial'"
			elif int_lng == 'English':
				msg = "Fill out the 'initial' form"
			msg_list.append(msg)
							
			initial_vkl_arr.append(None)
			
		#проверяем на заполнение vertices#
		vertices_path = prj_path + '/' + mesh_name_txt + '/' + 'vertices.pkl'
		if os.path.exists(vertices_path):	
			vertices_vkl_arr = []
			
			vertices_input = open(vertices_path, 'rb')
			vertices_obj = pickle.load(vertices_input)
			vertices_input.close()
			
			vertices_vkl_arr.append('vertices')
		else:
			vertices_vkl_arr = []
			
			if int_lng == 'Russian':
				msg = "Заполните форму 'vertices'"
			elif int_lng == 'English':
				msg = "Fill out the 'vertices' form"
				
			msg_list.append(msg)
			vertices_vkl_arr.append(None)
				
		#проверяем на заполнение blocks_1#
		blocks_1_path = prj_path + '/' + mesh_name_txt + '/' + 'blocks_1.pkl'
		if os.path.exists(blocks_1_path):	
			blocks_1_vkl_arr = []
			
			blocks_1_input = open(blocks_1_path, 'rb')
			blocks_1_obj = pickle.load(blocks_1_input)
			blocks_1_input.close()
			
			blocks_1_vkl_arr.append('blocks_1')
		else:
			blocks_1_vkl_arr = []
			
			if int_lng == 'Russian':
				msg = "Заполните форму 'blocks_1'"
			elif int_lng == 'English':
				msg = "Fill out the form 'blocks_1'"
			msg_list.append(msg)
			blocks_1_vkl_arr.append(None)
		
		#проверяем на заполнение block_2#
		blocks_2_path = prj_path + '/' + mesh_name_txt + '/' + 'blocks_2.pkl'
		if os.path.exists(blocks_2_path):	
			blocks_2_vkl_arr = []
			
			blocks_2_input = open(blocks_2_path, 'rb')
			blocks_2_obj = pickle.load(blocks_2_input)
			blocks_2_input.close()
			
			blocks_2_vkl_arr.append('blocks_2')
		else:
			blocks_2_vkl_arr = []
			
			if int_lng == 'Russian':
				msg = "Заполните форму 'blocks_2'"
			elif int_lng == 'English':
				msg = "Fill out the form 'blocks_2'"
			msg_list.append(msg)
			blocks_2_vkl_arr.append(None)
		
		edges_1_path = prj_path + '/' + mesh_name_txt + '/' + 'edges_1.pkl'
		edges_2_path = prj_path + '/' + mesh_name_txt + '/' + 'edges_2.pkl'
		if spe_edit.isChecked() == True:
			#проверяем на заполнение edges_1#
			
			if os.path.exists(edges_1_path):	
				edges_1_vkl_arr = []
			
				edges_1_input = open(edges_1_path, 'rb')
				edges_1_obj = pickle.load(edges_1_input)
				edges_1_input.close()
			
			
				edges_1_vkl_arr.append('edges_1')
			else:
				edges_1_vkl_arr = []
			
				if int_lng == 'Russian':
					msg = "Заполните форму 'edges_1'"
				elif int_lng == 'English':
					msg = "Fill out the form 'edges_1'"
				msg_list.append(msg)
				edges_1_vkl_arr.append(None)
			
			#проверяем на заполнение edges_2#
			
			if os.path.exists(edges_2_path):	
				edges_2_vkl_arr = []
			
				edges_2_input = open(edges_2_path, 'rb')
				edges_2_obj = pickle.load(edges_2_input)
				edges_2_input.close()
			
				edges_2_vkl_arr.append('edges_2')
			else:
				edges_2_vkl_arr = []
			
				if int_lng == 'Russian':
					msg = "Заполните вкладку 'edges_2'"
				elif int_lng == 'English':
					msg = "Fill out the form 'edges_2'"
				msg_list.append(msg)
				edges_2_vkl_arr.append(None)
		
		patches_1_path = prj_path + '/' + mesh_name_txt + '/' + 'patches_1.pkl'
		patches_2_path = prj_path + '/' + mesh_name_txt + '/' + 'patches_2.pkl'
		if spp_edit.isChecked() == True:
			#проверяем на заполнение patches_1#
			
			if os.path.exists(patches_1_path):	
				patches_1_vkl_arr = []
			
				patches_1_input = open(patches_1_path, 'rb')
				patches_1_obj = pickle.load(patches_1_input)
				patches_1_input.close()
			
				patches_1_vkl_arr.append('patches_1')
			else:
				patches_1_vkl_arr = []
				
				if int_lng == 'Russian':
					msg = "Заполните вкладку 'patches_1'"
				elif int_lng == 'English':
					msg = "Fill out the form 'patches_1'"
				msg_list.append(msg)
				patches_1_vkl_arr.append(None)
				
			#проверяем на заполнение patches_1#
			
			if os.path.exists(patches_2_path):	
				patches_2_vkl_arr = []
			
				patches_2_input = open(patches_2_path, 'rb')
				patches_2_obj = pickle.load(patches_2_input)
				patches_2_input.close()
			
				patches_2_vkl_arr.append('patches_2')
			else:
				patches_2_vkl_arr = []
			
				if int_lng == 'Russian':
					msg = "Заполните вкладку 'patches_2'"
				elif int_lng == 'English':
					msg = "Fill out the form 'patches_2'"
				msg_list.append(msg)
				patches_2_vkl_arr.append(None)
		
		mergepatchpairs_path = prj_path + '/' + mesh_name_txt + '/' + 'mergepatchpairs.pkl'
		if mpp_edit.isChecked() == True:
			#проверяем на заполнение mergepatchpairs#
			
			if os.path.exists(mergepatchpairs_path):	
				mergepatchpairs_vkl_arr = []
			
				mergepatchpairs_input = open(mergepatchpairs_path, 'rb')
				mergepatchpairs_obj = pickle.load(mergepatchpairs_input)
				mergepatchpairs_input.close()
			
				mergepatchpairs_vkl_arr.append('mergepatchpairs')
			else:
				mergepatchpairs_vkl_arr = []
			
				if int_lng == 'Russian':
					msg = "Заполните вкладку 'mergepatchpairs'"
				elif int_lng == 'English':
					msg = "Fill out the form 'mergepatchpairs'"
				msg_list.append(msg)
				mergepatchpairs_vkl_arr.append(None)
		
		bmd_par.on_msg_error(msg_list)	
		
		#########################################################################
		#Формируем блоки параметров для файла blockMeshDict#

		###convertToMeters###
		cTM_bl = 'convertToMeters ' + str(cTM_v) + ';' + '\n\n'

		###vertices###
		if os.path.exists(vertices_path):	
		
			vertices_pred_str = 'vertices' + '\n' + '(' + '\n'

			i = 0
			vert_eld_str_itog = ''
			for el_dict in vertices_obj:
				vertices_space_str = '    '
				skob_open_str = '('
				vertices_str = ' '.join(el_dict['vertex_' + str(i)])
				skob_close_str = ')' + '\n'
				vert_eld_str = vertices_space_str + skob_open_str + vertices_str + skob_close_str
				vert_eld_str_itog = vert_eld_str_itog + vert_eld_str
				i = i + 1

			vertices_post_str = ')' + ';' + '\n\n'
			vertices_bl = vertices_pred_str + vert_eld_str_itog + vertices_post_str

		###blocks###
		
		if os.path.exists(blocks_1_path) and os.path.exists(blocks_2_path):	

			blocks_pred_str = 'blocks' + '\n' + '(' + '\n'

			b = 1
			i = 0
			blocks_eld_str_itog = ''
			for el_dict in blocks_1_obj:
				blocks_1_space_str = '    hex'
				skob_open_str = ' ('
				versh_str = ' '.join(el_dict['versh_' + str(b)])
				skob_close_str = ')'
				yach_str = ' '.join(el_dict['yach_' + str(b)])

				hex_eld_str = blocks_1_space_str + skob_open_str + versh_str + skob_close_str + skob_open_str + yach_str + skob_close_str + ' ' 

				if el_dict['srya_' + str(b)] == 'simpleGrading' and el_dict['mg_' + str(b)] == False:
					srya_str = el_dict['srya_' + str(b)]
					blocks_2_str = ' '.join(blocks_2_obj[i]['simpleGrading'])
					grad_eld_str = srya_str + skob_open_str + blocks_2_str + skob_close_str + '\n'
				elif el_dict['srya_' + str(b)] == 'simpleGrading' and el_dict['mg_' + str(b)] == True:
					n_str = '    \n'
					srya_str = el_dict['srya_' + str(b)]
					bl_pred = '    (' + '\n'
					###
					if el_dict['napr_' + str(b)] == 'x':
						kos = 1
						sg_x_pred = '        (' + '\n'
						sG_dict = blocks_2_obj[i]['simpleGrading_mg']
						mg_blocks_dict = sG_dict[0]['mg_blocks_' + str(b)]
						x_dict = mg_blocks_dict[0]['x']
						h = 0
						x_el_pst_str_itog = ''
						while kos <= el_dict['ks_' + str(b)]:
							x_el_pred = '            ('
							x_el_str = ' '.join(x_dict[h]['sekt_' + str(kos)])
							x_el_post = ')' + '\n'
							x_el_pst = x_el_pred + x_el_str + x_el_post
							x_el_pst_str_itog = x_el_pst_str_itog + x_el_pst

							h = h + 1
							kos = kos + 1

						sg_x_post = '        )' + '\n'

						y_dict = mg_blocks_dict[1]['y'] + '\n'

						z_dict = mg_blocks_dict[2]['z'] + '\n'

						napr_str = sg_x_pred + x_el_pst_str_itog + sg_x_post + '        ' + y_dict + '        ' + z_dict
					###	
					elif el_dict['napr_' + str(b)] == 'y':

						sG_dict = blocks_2_obj[i]['simpleGrading_mg']
						mg_blocks_dict = sG_dict[0]['mg_blocks_' + str(b)]

						x_dict = mg_blocks_dict[0]['x'] + '\n'

						sg_y_pred = '        (' + '\n'

						y_dict = mg_blocks_dict[1]['y']
						kos = 1
						h = 0
						y_el_pst_str_itog = ''
						while kos <= el_dict['ks_' + str(b)]:

							y_el_pred = '            ('
							y_el_str = ' '.join(y_dict[h]['sekt_' + str(kos)])
							y_el_post = ')' + '\n'
							y_el_pst = y_el_pred + y_el_str + y_el_post
							y_el_pst_str_itog = y_el_pst_str_itog + y_el_pst

							h = h + 1
							kos = kos + 1

						sg_y_post = '        )' + '\n'

						z_dict = mg_blocks_dict[2]['z'] + '\n'

						napr_str = '        ' + x_dict + sg_y_pred + y_el_pst_str_itog + sg_y_post + '        ' + z_dict
					###	
					elif el_dict['napr_' + str(b)] == 'z':

						sG_dict = blocks_2_obj[i]['simpleGrading_mg']
						mg_blocks_dict = sG_dict[0]['mg_blocks_' + str(b)]

						x_dict = mg_blocks_dict[0]['x'] + '\n'

						y_dict = mg_blocks_dict[1]['y'] + '\n'

						sg_z_pred = '        (' + '\n'

						z_dict = mg_blocks_dict[2]['z']
						kos = 1
						h = 0
						z_el_pst_str_itog = ''
						while kos <= el_dict['ks_' + str(b)]:

							z_el_pred = '            ('
							z_el_str = ' '.join(z_dict[h]['sekt_' + str(kos)])
							z_el_post = ')' + '\n'
							z_el_pst = z_el_pred + z_el_str + z_el_post
							z_el_pst_str_itog = z_el_pst_str_itog + z_el_pst

							h = h + 1
							kos = kos + 1

						sg_z_post = '        )' + '\n'

						napr_str = '        ' + x_dict + '        ' + y_dict + sg_z_pred + z_el_pst_str_itog + sg_z_post

					bl_post = '    )'

					grad_eld_str = n_str + '    ' + srya_str + n_str + bl_pred + napr_str + bl_post + '\n'

				elif el_dict['srya_' + str(b)] == 'edgeGrading':
					srya_str = el_dict['srya_' + str(b)]
					blocks_2_str = ' '.join(blocks_2_obj[i]['edgeGrading'])

					grad_eld_str = srya_str + skob_open_str + blocks_2_str + skob_close_str + '\n'

				hex_eld_osch_str = hex_eld_str + grad_eld_str
				blocks_eld_str_itog = blocks_eld_str_itog + hex_eld_osch_str
				b = b + 1
				i = i + 1

			blocks_post_str = ')' + ';' + '\n\n'

			blocks_bl = blocks_pred_str + blocks_eld_str_itog + blocks_post_str

		###edges###
		
		if os.path.exists(edges_1_path) and os.path.exists(edges_2_path):	
		
			edges_pred_str = 'edges' + '\n' + '(' + '\n'

			i = 0
			b = 1
			edges_eld_str_itog = ''
			for el_m in edges_1_obj:
				for key in el_m.keys():

					if key == 'Дуга окружности' or key == 'Arc of a circle':
						edge_str = '    arc'

						do = edges_2_obj[i]

						for key in do.keys():							
							if key == 'metk_' + str(b):
								metk_list = do['metk_' + str(b)]
								metk_str = ' '.join(metk_list)

							if key == 'values_' + str(b):
								values_list = do['values_' + str(b)]
								values_str = ' '.join(values_list)
						itog_str = edge_str + ' ' + metk_str + ' (' + values_str + ')' + '\n'

					if key == 'Сплайновая кривая' or key == 'Spline curve':
						edge_str = '    spline'
						do = edges_2_obj[i]

						for key in do.keys():
							if key == 'metk_' + str(b):
								metk_list = do['metk_' + str(b)]
								metk_str = ' '.join(metk_list)
							if key == 'values_' + str(b):
								values_list = do['values_' + str(b)]
								values_str_list = ''
								for el_val in values_list:
									values_str = ' '.join(el_val)
									values_str_list = values_str_list + '(' + values_str + ')' + ' '

						itog_str = edge_str + ' ' + metk_str + ' ' + values_str_list + '\n'

					if key == 'B-сплайновая кривая' or key == 'B-spline curve':
						edge_str = '    BSpline'
						do = edges_2_obj[i]

						for key in do.keys():
							if key == 'metk_' + str(b):
								metk_list = do['metk_' + str(b)]
								metk_str = ' '.join(metk_list)
							if key == 'values_' + str(b):
								values_list = do['values_' + str(b)]
								values_str_list = ''
								for el_val in values_list:
									values_str = ' '.join(el_val)
									values_str_list = values_str_list + '(' + values_str + ')' + ' '

						itog_str = edge_str + ' ' + metk_str + ' ' + values_str_list + '\n'

					if key == 'Набор линий' or key == 'Set of lines':
						edge_str = '    polyLine'
						do = edges_2_obj[i]

						for key in do.keys():
							if key == 'metk_' + str(b):
								metk_list = do['metk_' + str(b)]
								metk_str = ' '.join(metk_list)
							if key == 'values_' + str(b):
								values_list = do['values_' + str(b)]
								values_str_list = ''
								for el_val in values_list:
									values_str = ' '.join(el_val)
									values_str_list = values_str_list + '(' + values_str + ')' + ' '

						itog_str = edge_str + ' ' + metk_str + ' ' + values_str_list + '\n'

				edges_eld_str_itog = edges_eld_str_itog + itog_str
				i = i + 1
				b = b + 1

			edges_post_str = ');' + '\n\n'

			edges_bl = edges_pred_str + edges_eld_str_itog + edges_post_str

		###edges_none###
		else:
			edges_none_pred_str = 'edges' + '\n' + '(' + '\n'
			edges_none_post_str = ');' + '\n\n'

			edges_none_bl = edges_none_pred_str + edges_none_post_str

		###patches###
		
		if os.path.exists(patches_1_path) and os.path.exists(patches_2_path):

			patches_pred_str = 'boundary' + '\n' + '(' + '\n'

			i = 0
			b = 1
			patches_eld_str_itog = ''
			
			for el_patch in patches_1_obj:
				
				patch_name = el_patch['patch_' + str(b)]
				el_patch_pred = '    ' + patch_name + '\n    {\n    '

				if el_patch['type_' + str(b)] == 'patch' or el_patch['type_' + str(b)] == 'wall' or el_patch['type_' + str(b)] == 'symmetryPlane' or el_patch['type_' + str(b)] == 'wedge' or el_patch['type_' + str(b)] == 'empty':
					type_name = el_patch['type_' + str(b)]

					type_str = '    type' + ' ' + type_name + ';\n'
					faces_pred_str = '        faces' + '\n' + '        ('

					p_val = patches_2_obj[i][patch_name]
					p_val_str_itog = ''
					for p_val_list in p_val:
						p_val_pred_str = '            ('
						p_val_str = ' '.join(p_val_list)
						p_val_post_str = ')'
						p_n = '\n'
						p_itog = p_n + p_val_pred_str + p_val_str + p_val_post_str
						p_val_str_itog = p_val_str_itog + p_itog

					faces_post_str = '\n' + '        );' + '\n'

					patch_str = type_str + faces_pred_str + '        ' + p_val_str_itog + faces_post_str

				if el_patch['type_' + str(b)] == 'cyclic':
					type_name = el_patch['type_' + str(b)]
					type_str = '    type' + ' ' + type_name + ';\n'

					neighb_name = el_patch['neighb_' + str(b)]
					neighb_str = '        neighbourPatch' + ' ' + neighb_name + ';\n'

					faces_pred_str = '        faces' + '\n' + '        (' 

					p_val = patches_2_obj[i][patch_name]

					p_val_str_itog = ''
					for p_val_list in p_val:

						p_val_pred_str = '    ('
						p_val_str = ' '.join(p_val_list)
						p_val_post_str = ')'
						p_n = '\n'
						p_itog = p_val_pred_str + p_val_str + p_val_post_str + p_n
						p_val_str_itog = p_val_str_itog + p_itog

					faces_post_str = '        );' + '\n'

					patch_str = type_str + neighb_str + faces_pred_str + '\n' +  '        ' + p_val_str_itog + faces_post_str

				el_patch_post = '    }\n'

				el_patch_str = el_patch_pred + patch_str + el_patch_post
				patches_eld_str_itog = patches_eld_str_itog + el_patch_str
			
				i = i + 1
				b = b + 1

			patches_post_str = ');\n\n'

			patches_bl = patches_pred_str + patches_eld_str_itog + patches_post_str

		###patches_none###
		else:
			patches_none_pred_str = 'patches' + '\n' + '(' + '\n'
			patches_none_post_str = ');' + '\n\n'

			patches_none_bl = patches_none_pred_str + patches_none_post_str
		
		###mergePatchPairs###
		if os.path.exists(mergepatchpairs_path):
		
			mergepatchpairs_pred_str = 'mergePatchPairs' + '\n' + '(' + '\n'
			b = 1
			mergepatchpairs_eld_str_itog = ''
			for el_patch in mergepatchpairs_obj:
				master_name = el_patch['master_' + str(b)]
				slave_name = el_patch['slave_' + str(b)]
				el_patch_pred = '    ' + '( ' + master_name + ' ' + slave_name + ' )\n'
				mergepatchpairs_eld_str_itog = mergepatchpairs_eld_str_itog + el_patch_pred
				b = b + 1

			mergepatchpairs_post_str = ');\n\n'

			mergepatchpairs_bl = mergepatchpairs_pred_str + mergepatchpairs_eld_str_itog + mergepatchpairs_post_str

		###mergePatchPairs_none###
		else:
			
			mergepatchpairs_none_pred_str = 'mergePatchPairs' + '\n' + '(' + '\n'
			mergepatchpairs_none_post_str = ');' + '\n\n'

			mergepatchpairs_none_bl = mergepatchpairs_none_pred_str + mergepatchpairs_none_post_str

		#########################################################################
		  			#Сохраняем файл при наличии различных опций#
		#########################################################################

		if not None in initial_vkl_arr \
		and not None in vertices_vkl_arr \
		and not None in blocks_1_vkl_arr \
		and not None in blocks_2_vkl_arr \
		and spe_edit.isChecked() == True and tab.isTabEnabled(4) == True and not None in edges_1_vkl_arr \
		and spe_edit.isChecked() == True and tab.isTabEnabled(5) == True and not None in edges_2_vkl_arr \
		and spp_edit.isChecked() == True and tab.isTabEnabled(6) == True and not None in patches_1_vkl_arr \
		and spp_edit.isChecked() == True and tab.isTabEnabled(7) == True and not None in patches_2_vkl_arr \
		and mpp_edit.isChecked() == True and tab.isTabEnabled(8) == True and not None in mergepatchpairs_vkl_arr:

			shutil.copyfile(r'./matches/blockMeshDict', prj_path + r'/blockMeshDict')
			bMD = open(prj_path + '/blockMeshDict', 'a')

			bMD.write(cTM_bl + vertices_bl + blocks_bl + edges_bl + patches_bl + mergepatchpairs_bl)
			bMD.close()

			blockMeshDict_end(int_lng, prj_path, parn)
			
		#########################################################################	
		
		if not None in initial_vkl_arr \
		and not None in vertices_vkl_arr \
		and not None in blocks_1_vkl_arr \
		and not None in blocks_2_vkl_arr \
		and spe_edit.isChecked() == False and tab.isTabEnabled(4) == False \
		and spe_edit.isChecked() == False and tab.isTabEnabled(5) == False \
		and spp_edit.isChecked() == True and tab.isTabEnabled(6) == True and not None in patches_1_vkl_arr \
		and spp_edit.isChecked() == True and tab.isTabEnabled(7) == True and not None in patches_2_vkl_arr \
		and mpp_edit.isChecked() == True and tab.isTabEnabled(8) == True and not None in mergepatchpairs_vkl_arr:
			
			shutil.copyfile(r'./matches/blockMeshDict', prj_path + r'/blockMeshDict')
			bMD = open(prj_path + '/blockMeshDict', 'a')
			
			bMD.write(cTM_bl + vertices_bl + blocks_bl + edges_none_bl + patches_bl + mergepatchpairs_bl)
			bMD.close()

			blockMeshDict_end(int_lng, prj_path, parn)
			
		#########################################################################	
		
		if not None in initial_vkl_arr \
		and not None in vertices_vkl_arr \
		and not None in blocks_1_vkl_arr \
		and not None in blocks_2_vkl_arr \
		and spe_edit.isChecked() == False and tab.isTabEnabled(4) == False \
		and spe_edit.isChecked() == False and tab.isTabEnabled(5) == False \
		and spp_edit.isChecked() == False and tab.isTabEnabled(6) == False \
		and spp_edit.isChecked() == False and tab.isTabEnabled(7) == False \
		and mpp_edit.isChecked() == True and tab.isTabEnabled(8) == True and not None in mergepatchpairs_vkl_arr:
			
			shutil.copyfile(r'./matches/blockMeshDict', prj_path + r'/blockMeshDict')
			bMD = open(prj_path + '/blockMeshDict', 'a')
			
			bMD.write(cTM_bl + vertices_bl + blocks_bl + edges_none_bl + patches_none_bl + mergepatchpairs_bl)
			bMD.close()

			blockMeshDict_end(int_lng, prj_path, parn)	
			
		#########################################################################	
		
		if not None in initial_vkl_arr \
		and not None in vertices_vkl_arr \
		and not None in blocks_1_vkl_arr \
		and not None in blocks_2_vkl_arr \
		and spe_edit.isChecked() == False and tab.isTabEnabled(4) == False \
		and spe_edit.isChecked() == False and tab.isTabEnabled(5) == False \
		and spp_edit.isChecked() == False and tab.isTabEnabled(6) == False \
		and spp_edit.isChecked() == False and tab.isTabEnabled(7) == False \
		and mpp_edit.isChecked() == False and tab.isTabEnabled(8) == False:
			
			shutil.copyfile(r'./matches/blockMeshDict', prj_path + r'/blockMeshDict')
			bMD = open(prj_path + '/blockMeshDict', 'a')
			
			bMD.write(cTM_bl + vertices_bl + blocks_bl + edges_none_bl + patches_none_bl + mergepatchpairs_none_bl)
			bMD.close()

			blockMeshDict_end(int_lng, prj_path, parn)	
	
		#########################################################################

		if not None in initial_vkl_arr \
		and not None in vertices_vkl_arr \
		and not None in blocks_1_vkl_arr \
		and not None in blocks_2_vkl_arr \
		and spe_edit.isChecked() == True and tab.isTabEnabled(4) == True and not None in edges_1_vkl_arr \
		and spe_edit.isChecked() == True and tab.isTabEnabled(5) == True and not None in edges_2_vkl_arr \
		and spp_edit.isChecked() == False and tab.isTabEnabled(6) == False \
		and spp_edit.isChecked() == False and tab.isTabEnabled(7) == False \
		and mpp_edit.isChecked() == False and tab.isTabEnabled(8) == False:

			shutil.copyfile(r'./matches/blockMeshDict', prj_path + r'/blockMeshDict')
			bMD = open(prj_path + '/blockMeshDict', 'a')

			bMD.write(cTM_bl + vertices_bl + blocks_bl + edges_bl + patches_none_bl + mergepatchpairs_none_bl)
			bMD.close()

			blockMeshDict_end(int_lng, prj_path, parn)
			
		#########################################################################

		if not None in initial_vkl_arr \
		and not None in vertices_vkl_arr \
		and not None in blocks_1_vkl_arr \
		and not None in blocks_2_vkl_arr \
		and spe_edit.isChecked() == True and tab.isTabEnabled(4) == True and not None in edges_1_vkl_arr \
		and spe_edit.isChecked() == True and tab.isTabEnabled(5) == True and not None in edges_2_vkl_arr \
		and spp_edit.isChecked() == True and tab.isTabEnabled(6) == True and not None in patches_1_vkl_arr \
		and spp_edit.isChecked() == True and tab.isTabEnabled(7) == True and not None in patches_2_vkl_arr \
		and mpp_edit.isChecked() == False and tab.isTabEnabled(8) == False:

			shutil.copyfile(r'./matches/blockMeshDict', prj_path + r'/blockMeshDict')
			bMD = open(prj_path + '/blockMeshDict', 'a')

			bMD.write(cTM_bl + vertices_bl + blocks_bl + edges_bl + patches_bl + mergepatchpairs_none_bl)
			bMD.close()

			blockMeshDict_end(int_lng, prj_path, parn)	
			
		#########################################################################

		if not None in initial_vkl_arr \
		and not None in vertices_vkl_arr \
		and not None in blocks_1_vkl_arr \
		and not None in blocks_2_vkl_arr \
		and spe_edit.isChecked() == True and tab.isTabEnabled(4) == True and not None in edges_1_vkl_arr \
		and spe_edit.isChecked() == True and tab.isTabEnabled(5) == True and not None in edges_2_vkl_arr \
		and spp_edit.isChecked() == False and tab.isTabEnabled(6) == False \
		and spp_edit.isChecked() == False and tab.isTabEnabled(7) == False \
		and mpp_edit.isChecked() == True and tab.isTabEnabled(8) == True and not None in mergepatchpairs_vkl_arr:

			shutil.copyfile(r'./matches/blockMeshDict', prj_path + r'/blockMeshDict')
			bMD = open(prj_path + '/blockMeshDict', 'a')

			bMD.write(cTM_bl + vertices_bl + blocks_bl + edges_bl + patches_none_bl + mergepatchpairs_bl)
			bMD.close()

			blockMeshDict_end(int_lng, prj_path, parn)
			
		#########################################################################

		if not None in initial_vkl_arr \
		and not None in vertices_vkl_arr \
		and not None in blocks_1_vkl_arr \
		and not None in blocks_2_vkl_arr \
		and spe_edit.isChecked() == False and tab.isTabEnabled(4) == False \
		and spe_edit.isChecked() == False and tab.isTabEnabled(5) == False \
		and spp_edit.isChecked() == True and tab.isTabEnabled(6) == True and not None in patches_1_vkl_arr \
		and spp_edit.isChecked() == True and tab.isTabEnabled(7) == True and not None in patches_2_vkl_arr \
		and mpp_edit.isChecked() == False and tab.isTabEnabled(8) == False:

			shutil.copyfile(r'./matches/blockMeshDict', prj_path + r'/blockMeshDict')
			bMD = open(prj_path + '/blockMeshDict', 'a')

			bMD.write(cTM_bl + vertices_bl + blocks_bl + edges_none_bl + patches_bl + mergepatchpairs_none_bl)
			bMD.close()

			blockMeshDict_end(int_lng, prj_path, parn)	
			
		



