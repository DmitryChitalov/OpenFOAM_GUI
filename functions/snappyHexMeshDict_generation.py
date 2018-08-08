# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil

class snappyHexMeshDict_generation_class:			
	def snappyHexMeshDict_func(int_lng, parn, tab, f_edit, rS_edit, rR_edit, prj_path, mesh_name_txt, pd_2, shmd_par): 
		def snappyHexMeshDict_end(int_lng, prj_path, parn):
			sHMD = open(prj_path + '/snappyHexMeshDict', 'a')

			close_str = '// ************************************************************************* //'
			sHMD.write(close_str)
			sHMD.close()

			if int_lng == 'Russian':
				msg = "Файл 'snappyHexMeshDict' сохранен"
			elif int_lng == 'English':
				msg = "The 'snappyHexMeshDict' file was saved"
			shmd_par.on_msg_correct(msg)

			parn.cdw.setWidget(parn.outf_scroll)
			parn.outf_scroll.setFixedSize(350, 660)
			parn.cdw_frame.setFixedSize(350, 35)
			
			parn.msh_run.setEnabled(True)

			prj_dir = prj_path + '/snappyHexMeshDict'

			outf = open(prj_dir)
			data = outf.read()
			if int_lng == 'Russian':
				parn.outf_lbl.setText("Файл " + "<font color='peru'>" + 'snappyHexMeshDict' + "</font>") 
			elif int_lng == 'English':
				parn.outf_lbl.setText("<font color='peru'>" + 'snappyHexMeshDict' + "</font>" + " file") 
			parn.outf_edit.setText(data)
			parn.cdw.setWidget(parn.outf_scroll)

			parn.cdw.setTitleBarWidget(parn.cdw_frame)
			
		msg_list = []

		#проверяем на заполнение initial#
		initial_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'initial.pkl'
		if os.path.exists(initial_path):
			initial_vkl_arr = []

			initial_input = open(initial_path, 'rb')
			initial_obj = pickle.load(initial_input)
			initial_input.close()
			
			cM_v = initial_obj['cM']
			s_v = initial_obj['s']
			aL_v = initial_obj['al']
			mT_v = initial_obj['mT']
			
			f_v = initial_obj['f']
			rS_v = initial_obj['rS']
			rR_v = initial_obj['rR']
			
			initial_vkl_arr.append('initial')

		else:
			initial_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'initial'"
			elif int_lng == 'English':
				msg = "Fill out the 'initial' form"
			msg_list.append(msg)

			initial_vkl_arr.append(None)

		#проверяем на заполнение geometry_1#
		geometry_1_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_1.pkl'
		if os.path.exists(geometry_1_path):	
			geometry_1_vkl_arr = []

			geometry_1_input = open(geometry_1_path, 'rb')
			geometry_1_obj = pickle.load(geometry_1_input)
			geometry_1_input.close()

			geometry_1_vkl_arr.append('geometry_1')
		else:
			geometry_1_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'geometry_1'"
			elif int_lng == 'English':
				msg = "Fill out the form 'geometry_1'"
			msg_list.append(msg)
			geometry_1_vkl_arr.append(None)

		#проверяем на заполнение geometry_2#
		geometry_2_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'geometry_2.pkl'
		if os.path.exists(geometry_2_path):	
			geometry_2_vkl_arr = []

			geometry_2_input = open(geometry_2_path, 'rb')
			geometry_2_obj = pickle.load(geometry_2_input)
			geometry_2_input.close()

			geometry_2_vkl_arr.append('geometry_2')
		else:
			geometry_2_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'geometry_2'"
			elif int_lng == 'English':
				msg = "Fill out the form 'geometry_2'"
			msg_list.append(msg)
			geometry_2_vkl_arr.append(None)
		
		castellatedMC_1_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_1.pkl'
		castellatedMC_2_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'castellatedMC_2.pkl'
		if f_edit.isChecked() == True or rS_edit.isChecked() == True or rR_edit.isChecked() == True:
			#проверяем на заполнение castellatedMC_1#
			if os.path.exists(castellatedMC_1_path):	
				castellatedMC_1_vkl_arr = []

				castellatedMC_1_input = open(castellatedMC_1_path, 'rb')
				castellatedMC_1_obj = pickle.load(castellatedMC_1_input)
				castellatedMC_1_input.close()


				castellatedMC_1_vkl_arr.append('castellatedMC_1')
			else:
				castellatedMC_1_vkl_arr = []

				if int_lng == 'Russian':
					msg = "Заполните форму 'castellatedMC_1'"
				elif int_lng == 'English':
					msg = "Fill out the form 'castellatedMC_1'"
				msg_list.append(msg)
				castellatedMC_1_vkl_arr.append(None)

			#проверяем на заполнение castellatedMC_2#
			f_single_list = []
			f_multy_list = []
			rS_all_list = []
			rR_single_list = []
			rR_multy_list = []
			if 'features' in castellatedMC_1_obj:
				if castellatedMC_1_obj['features'] != False:
					for el_f in castellatedMC_1_obj['features']:
						f_single_list.append(el_f['f_level_single'])
						f_multy_list.append(el_f['f_level_multi'])
			if 'refinementSurfaces' in castellatedMC_1_obj:
				if castellatedMC_1_obj['refinementSurfaces'] != False:
					for el_rS in castellatedMC_1_obj['refinementSurfaces']:
						rS_all_list.append(el_rS['rS_regions'])
						
			if 'refinementRegions' in castellatedMC_1_obj:
				if castellatedMC_1_obj['refinementRegions'] != False:
					for el_rR in castellatedMC_1_obj['refinementRegions']:
						rR_single_list.append(el_rR['rR_level_single'])
						rR_multy_list.append(el_rR['rR_level_multi'])
					
			castellatedMC_2_vkl_arr = []
			if True in f_single_list or True in f_multy_list or True in rS_all_list or True in rR_single_list or True in rR_multy_list:
				if os.path.exists(castellatedMC_2_path):	
					castellatedMC_2_vkl_arr = []

					castellatedMC_2_input = open(castellatedMC_2_path, 'rb')
					castellatedMC_2_obj = pickle.load(castellatedMC_2_input)
					castellatedMC_2_input.close()

					castellatedMC_2_vkl_arr.append('castellatedMC_2')
				else:
					castellatedMC_2_vkl_arr = []

					if int_lng == 'Russian':
						msg = "Заполните вкладку 'castellatedMC_2'"
					elif int_lng == 'English':
						msg = "Fill out the form 'castellatedMC_2'"
					msg_list.append(msg)
					castellatedMC_2_vkl_arr.append(None)
			else:
				castellatedMC_2_vkl_arr.append('castellatedMC_2')
		else:
			castellatedMC_1_vkl_arr.append('castellatedMC_1')
			castellatedMC_2_vkl_arr.append(None)
			
		#проверяем на заполнение layers#
		layers_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'layers.pkl'
		if os.path.exists(layers_path):	
			layers_vkl_arr = []

			layers_input = open(layers_path, 'rb')
			layers_obj = pickle.load(layers_input)
			layers_input.close()

			layers_vkl_arr.append('layers')
		else:
			layers_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'layers'"
			elif int_lng == 'English':
				msg = "Fill out the 'layers' form"

			msg_list.append(msg)
			layers_vkl_arr.append(None)
		
		#проверяем на заполнение snapC#
		snapC_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'snapC.pkl'
		if os.path.exists(snapC_path):	
			snapC_vkl_arr = []

			snapC_input = open(snapC_path, 'rb')
			snapC_obj = pickle.load(snapC_input)
			snapC_input.close()

			snapC_vkl_arr.append('layers')
		else:
			snapC_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'snapC'"
			elif int_lng == 'English':
				msg = "Fill out the 'snapC' form"

			msg_list.append(msg)
			snapC_vkl_arr.append(None)
		
		#проверяем на заполнение meshQC#
		meshQC_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'meshQC.pkl'
		if os.path.exists(meshQC_path):	
			meshQC_vkl_arr = []

			meshQC_input = open(meshQC_path, 'rb')
			meshQC_obj = pickle.load(meshQC_input)
			meshQC_input.close()

			meshQC_vkl_arr.append('meshQC')
		else:
			meshQC_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'meshQC'"
			elif int_lng == 'English':
				msg = "Fill out the 'meshQC' form"

			msg_list.append(msg)
			meshQC_vkl_arr.append(None)
			
		shmd_par.on_msg_error(msg_list)	
		
		#########Формируем блоки параметров для файла snappyHexMeshDict##########
		
		###convertToMeters###
		cM_bl = 'castellatedMesh ' + str(cM_v) + ';' + '\n\n'
		
		###snap###
		s_bl = 'snap                        ' + str(s_v) + ';' + '\n\n'
		
		###addLayers###
		aL_bl = 'addLayers             ' + str(aL_v) + ';' + '\n\n'
		
		###mergeTolerance###
		mT_bl = 'mergeTolerance ' + str(mT_v) + ';' + '\n\n'
		
		###geometry###
		if os.path.exists(geometry_1_path) and os.path.exists(geometry_2_path):	

			geometry_pred_str = 'geometry' + '\n' + '{' + '\n'

			i = 1
			j = 0
			
			geometry_eld_str_itog = ''
			for el_dict in geometry_1_obj:
				
				tri_pred_str_1 = '    '
				tri_pred_str_2 = '        '
				tri_pred_str_3 = '            '
				tri_pred_str_4 = '                '
				tri_pred_str_5 = '                    '
				###Три-поверхность и распределенная три-поверхность###
				if el_dict['geometry_' + str(i)] == 'Три-поверхность' or el_dict['geometry_' + str(i)] == 'Tri-surface' or el_dict['geometry_' + str(i)] == 'Распределенная три-поверхность' or el_dict['geometry_' + str(i)] == 'Distributed tri-surface':

					tri_pred_main_name = geometry_2_obj[j]['file']
					tri_type_str = 'type ' + geometry_2_obj[j]['type']
					tri_pred_dop_name = 'name ' + geometry_2_obj[j]['name']
					tri_end = tri_pred_str_1 +  '}' + '\n'
					tri_itog = tri_pred_str_1 + tri_pred_main_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + tri_type_str + ';' + '\n' + tri_pred_str_2 + tri_pred_dop_name + ';'

					geometry_eld_str_itog = geometry_eld_str_itog + tri_itog

					###Три-поверхность и распределенная три-поверхность c областями###
					if el_dict['regions_number_' + str(i)] != 0:
						rn = el_dict['regions_number_' + str(i)]
						k = 1
						l = 0
						tri_reg_all = ''
						tri_reg_lbl = tri_pred_str_2 + 'regions' + '\n' + tri_pred_str_2 +'{' + '\n'
						while k <= rn:

							tri_reg = geometry_2_obj[j]['regions'][l]['region_' + str(k)][0]
							tri_reg_name = geometry_2_obj[j]['regions'][l]['region_' + str(k)][1]

							tri_reg_el = tri_pred_str_3 + tri_reg + '\n' + tri_pred_str_3 + '{' + '\n' + tri_pred_str_4 + 'name' + ' ' + tri_reg_name + ';' + '\n' + tri_pred_str_3 + '}' + '\n'

							tri_reg_all = tri_reg_all + tri_reg_el

							k = k + 1
							l = l + 1

						tri_reg_itog = tri_reg_lbl + tri_reg_all

						geometry_eld_str_itog = geometry_eld_str_itog + tri_reg_itog + tri_pred_str_2 + '}'

					geometry_eld_str_itog = geometry_eld_str_itog + '\n' + tri_pred_str_1 + '}' + '\n'

				###Базовая фигура###
				if el_dict['geometry_' + str(i)] == 'Базовая фигура' or el_dict['geometry_' + str(i)] == 'Base shape':
					#'шестигранник'#
					if el_dict['shape_type_' + str(i)] == 'шестигранник' or el_dict['shape_type_' + str(i)] == 'box':
						box_name = geometry_2_obj[j]['shape']
						box_type = geometry_2_obj[j]['type']
						box_max_x = geometry_2_obj[j]['max'][0]
						box_max_y = geometry_2_obj[j]['max'][1]
						box_max_z = geometry_2_obj[j]['max'][2]
						box_min_x = geometry_2_obj[j]['min'][0]
						box_min_y = geometry_2_obj[j]['min'][1]
						box_min_z = geometry_2_obj[j]['min'][2]

						box_itog_1 = tri_pred_str_1 + box_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + box_type + ';' + '\n'
						box_itog_2 = tri_pred_str_2 + 'min ' + '(' + box_min_x + ' ' + box_min_y + ' ' + box_min_z + ')' + ';' + '\n'
						box_itog_3 = tri_pred_str_2 + 'max ' + '(' + box_max_x + ' ' + box_max_y + ' ' + box_max_z + ')' + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

						box_itog = box_itog_1 + box_itog_2 + box_itog_3

						geometry_eld_str_itog = geometry_eld_str_itog + box_itog

					#'сфера'#	
					if el_dict['shape_type_' + str(i)] == 'сфера' or el_dict['shape_type_' + str(i)] == 'sphere':
						sphere_name = geometry_2_obj[j]['shape']
						sphere_type = geometry_2_obj[j]['type']
						sphere_centre_x = geometry_2_obj[j]['centre'][0]
						sphere_centre_y = geometry_2_obj[j]['centre'][1]
						sphere_centre_z = geometry_2_obj[j]['centre'][2]
						sphere_radius = geometry_2_obj[j]['radius']

						sphere_itog_1 = tri_pred_str_1 + sphere_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + sphere_type + ';' + '\n'
						sphere_itog_2 = tri_pred_str_2 + 'centre ' + '(' + sphere_centre_x + ' ' + sphere_centre_y + ' ' + sphere_centre_z + ')' + ';' + '\n'
						sphere_itog_3 = tri_pred_str_2 + 'radius ' + str(sphere_radius) + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

						sphere_itog = sphere_itog_1 + sphere_itog_2 + sphere_itog_3

						geometry_eld_str_itog = geometry_eld_str_itog + sphere_itog

					#'цилиндр'#
					if el_dict['shape_type_' + str(i)] == 'цилиндр' or el_dict['shape_type_' + str(i)] == 'cylinder':
						cylinder_name = geometry_2_obj[j]['shape']
						cylinder_type = geometry_2_obj[j]['type']

						cylinder_point1_x = geometry_2_obj[j]['point1'][0]
						cylinder_point1_y = geometry_2_obj[j]['point1'][1]
						cylinder_point1_z = geometry_2_obj[j]['point1'][2]

						cylinder_point2_x = geometry_2_obj[j]['point2'][0]
						cylinder_point2_y = geometry_2_obj[j]['point2'][1]
						cylinder_point2_z = geometry_2_obj[j]['point2'][2]

						cylinder_radius = geometry_2_obj[j]['radius']

						cylinder_itog_1 = tri_pred_str_1 + cylinder_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + cylinder_type + ';' + '\n'
						cylinder_itog_2 = tri_pred_str_2 + 'min ' + '(' + cylinder_point1_x + ' ' + cylinder_point1_y + ' ' + cylinder_point1_z + ')' + ';' + '\n'
						cylinder_itog_3 = tri_pred_str_2 + 'min ' + '(' + cylinder_point2_x + ' ' + cylinder_point2_y + ' ' + cylinder_point2_z + ')' + ';' + '\n'
						cylinder_itog_4 = tri_pred_str_2 + 'radius ' + str(cylinder_radius) + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

						cylinder_itog = cylinder_itog_1 + cylinder_itog_2 + cylinder_itog_3 + cylinder_itog_4

						geometry_eld_str_itog = geometry_eld_str_itog + cylinder_itog

					#'плоскость'#
					if el_dict['shape_type_' + str(i)] == 'плоскость' or el_dict['shape_type_' + str(i)] == 'plane':
						plane_name = geometry_2_obj[j]['shape']
						plane_type = geometry_2_obj[j]['type']
						plane_planeType = geometry_2_obj[j]['planeType']

						plane_basePoint_x = geometry_2_obj[j]['basePoint'][0]
						plane_basePoint_y = geometry_2_obj[j]['basePoint'][1]
						plane_basePoint_z = geometry_2_obj[j]['basePoint'][2]

						plane_normalVector_x = geometry_2_obj[j]['normalVector'][0]
						plane_normalVector_y = geometry_2_obj[j]['normalVector'][1]
						plane_normalVector_z = geometry_2_obj[j]['normalVector'][2]

						plane_itog_1 = tri_pred_str_1 + plane_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + plane_type + ';' + '\n'
						plane_itog_2 = tri_pred_str_2 + 'planeType' + ' ' + plane_planeType + ';' + '\n' + tri_pred_str_2 + 'pointAndNormalDict' + '\n' + tri_pred_str_2 + '{' + '\n'
						plane_itog_3 = tri_pred_str_3 + 'basePoint ' + '(' + plane_basePoint_x + ' ' + plane_basePoint_y + ' ' + plane_basePoint_z + ')' + ';' + '\n'
						plane_itog_4 = tri_pred_str_3 + 'normalVector ' + '(' + plane_normalVector_x + ' ' + plane_normalVector_y + ' ' + plane_normalVector_z + ')' + ';' + '\n'
						plane_itog_5 = tri_pred_str_2 + '}' + '\n'+ tri_pred_str_1 + '}' + '\n'

						plane_itog = plane_itog_1 + plane_itog_2 + plane_itog_3 + plane_itog_4 + plane_itog_5

						geometry_eld_str_itog = geometry_eld_str_itog + plane_itog

					#'пластина'#
					if el_dict['shape_type_' + str(i)] == 'пластина' or el_dict['shape_type_' + str(i)] == 'plate':
						plate_name = geometry_2_obj[j]['shape']
						plate_type = geometry_2_obj[j]['type']

						plate_origin_x = geometry_2_obj[j]['origin'][0]
						plate_origin_y = geometry_2_obj[j]['origin'][1]
						plate_origin_z = geometry_2_obj[j]['origin'][2]

						plate_span_x = geometry_2_obj[j]['span'][0]
						plate_span_y = geometry_2_obj[j]['span'][1]
						plate_span_z = geometry_2_obj[j]['span'][2]

						plate_itog_1 = tri_pred_str_1 + plate_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + plate_type + ';' + '\n'
						plate_itog_2 = tri_pred_str_2 + 'origin ' + '(' + plate_origin_x + ' ' + plate_origin_y + ' ' + plate_origin_z + ')' + ';' + '\n'
						plate_itog_3 = tri_pred_str_2 + 'span ' + '(' + plate_span_x + ' ' + plate_span_y + ' ' + plate_span_z + ')' + ';' + '\n' + tri_pred_str_1 + '}' + '\n'

						plate_itog = plate_itog_1 + plate_itog_2 + plate_itog_3

						geometry_eld_str_itog = geometry_eld_str_itog + plate_itog

				###Набор фигур###
				if el_dict['geometry_' + str(i)] == 'Набор базовых фигур' or el_dict['geometry_' + str(i)] == 'Base shape complex':

					complex_name = geometry_2_obj[j]['name']
					complex_type = geometry_2_obj[j]['type']
					complex_mSR = geometry_2_obj[j]['mergeSubRegions']

					complex_itog_1 = tri_pred_str_1 + complex_name + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'type' + ' ' + complex_type + ';' + '\n' + tri_pred_str_2 + 'mergeSubRegions' + ' ' + complex_mSR + ';' + '\n'

					sn = el_dict['shapes_number_' + str(i)]
					e = 1
					c = 0
					complex_itog_1 = complex_itog_1
					while e <= sn:
						shape_name = geometry_2_obj[j]['parameters'][c][0]

						if geometry_2_obj[j]['parameters'][c][1] == 'шестигранник':
							shape_type = 'box'
						elif geometry_2_obj[j]['parameters'][c][1] == 'цилиндр':
							shape_type = 'cylinder'
						elif geometry_2_obj[j]['parameters'][c][1] == 'сфера':
							shape_type = 'sphere'
						elif geometry_2_obj[j]['parameters'][c][1] == 'плоскость':
							shape_type = 'plane'
						elif geometry_2_obj[j]['parameters'][c][1] == 'пластина':
							shape_type = 'plate'
						else:
							shape_type = geometry_2_obj[j]['parameters'][c][1]

						shape_scale_x = geometry_2_obj[j]['parameters'][c][2][0]
						shape_scale_y = geometry_2_obj[j]['parameters'][c][2][1]
						shape_scale_z = geometry_2_obj[j]['parameters'][c][2][2]

						transform_type = geometry_2_obj[j]['parameters'][c][3]

						transform_origin_x = geometry_2_obj[j]['parameters'][c][4][0]
						transform_origin_y = geometry_2_obj[j]['parameters'][c][4][1]
						transform_origin_z = geometry_2_obj[j]['parameters'][c][4][2]

						transform_e1_x = geometry_2_obj[j]['parameters'][c][5][0]
						transform_e1_y = geometry_2_obj[j]['parameters'][c][5][1]
						transform_e1_z = geometry_2_obj[j]['parameters'][c][5][2]

						transform_e3_x = geometry_2_obj[j]['parameters'][c][6][0]
						transform_e3_y = geometry_2_obj[j]['parameters'][c][6][1]
						transform_e3_z = geometry_2_obj[j]['parameters'][c][6][2]

						sh_itog_1 = tri_pred_str_2 + shape_name + '\n' + tri_pred_str_2 + '{' + '\n' + tri_pred_str_3 + 'surface' + ' ' + shape_type + ';' + '\n'
						sh_itog_2 = tri_pred_str_3 + 'scale' + ' ' + '(' + shape_scale_x + ' ' + shape_scale_y + ' ' + shape_scale_z + ')' + ';' + '\n'
						sh_itog_3 = tri_pred_str_3 + 'transform' + '\n' + tri_pred_str_3 + '{' + '\n' + tri_pred_str_4 + 'type' + ' ' + transform_type + ';' + '\n'
						sh_itog_4 = tri_pred_str_4 + 'origin ' + '(' + transform_origin_x + ' ' + transform_origin_y + ' ' + transform_origin_z + ')' + ';' + '\n'
						sh_itog_5 = tri_pred_str_4 + 'e1 ' + '(' + transform_e1_x + ' ' + transform_e1_y + ' ' + transform_e1_z + ')' + ';' + '\n'
						sh_itog_6 = tri_pred_str_4 + 'e3 ' + '(' + transform_e3_x + ' ' + transform_e3_y + ' ' + transform_e3_z + ')' + ';' + '\n'
						sh_itog_7 = tri_pred_str_3 + '}' + '\n' + tri_pred_str_2 + '}' + '\n'

						sh_itog = sh_itog_1 + sh_itog_2 + sh_itog_3 + sh_itog_4 + sh_itog_5 + sh_itog_6 + sh_itog_7

						complex_itog_1 = complex_itog_1 + sh_itog

						e = e + 1
						c = c + 1

					geometry_eld_str_itog = geometry_eld_str_itog + complex_itog_1 + tri_pred_str_1 + '}' + '\n'

				i = i + 1
				j = j + 1				

			geometry_post_str = '}' + ';' + '\n\n'

			geometry_bl = geometry_pred_str + geometry_eld_str_itog + geometry_post_str
				
		###castellatedMeshControls###
		if os.path.exists(castellatedMC_1_path):	
			castellatedMC_pred_str = 'castellatedMeshControls' + '\n' + '{' + '\n'

			i = 1
			j = 0

			###Стартовые параметры###
			cMC_start_prs = castellatedMC_1_obj['cMC_start_prs']

			mGC_str = tri_pred_str_1 + 'maxGlobalCells' + ' ' + str(cMC_start_prs['mGC']) + ';' + '\n' + '\n'
			mLC_str = tri_pred_str_1 + 'maxLocalCells' + ' ' + str(cMC_start_prs['mLC']) + ';' + '\n' + '\n'
			mRC_str = tri_pred_str_1 + 'minRefinementCells' + ' ' + str(cMC_start_prs['mRC']) + ';' + '\n' + '\n'
			nCBL_str = tri_pred_str_1 + 'nCellsBetweenLevels' + ' ' + str(cMC_start_prs['nCBL']) + ';' + '\n' + '\n'
			rFA_str = tri_pred_str_1 + 'resolveFeatureAngle' + ' ' + str(cMC_start_prs['rFA']) + ';' + '\n' + '\n'
			aFSZF_str = tri_pred_str_1 + 'allowFreeStandingZoneFaces' + ' ' + cMC_start_prs['aFSZF'] + ';' + '\n' + '\n'
			lIM_str = tri_pred_str_1 + 'locationInMesh' + ' ' + '(' + str(cMC_start_prs['lIM'][0]) + ' ' + str(cMC_start_prs['lIM'][1]) + ' ' + str(cMC_start_prs['lIM'][2]) + ')' + ';' + '\n' + '\n'

			cMC_start_prs_str = mGC_str + mLC_str + mRC_str + nCBL_str + rFA_str + aFSZF_str + lIM_str
			castellatedMC_eld_str_itog = cMC_start_prs_str

			if os.path.exists(castellatedMC_2_path):
			
				if f_v == True:
					###features###
					cMC_features_obj_list = castellatedMC_1_obj['features']

					features_pred = tri_pred_str_1 + 'features' + '\n' + tri_pred_str_1 + '('
					features_post = tri_pred_str_1 + ')' + ';' + '\n' + '\n'

					q = 1
					a = 0
					features_middle = ''
					for el_cmcfol in cMC_features_obj_list:
						f_level_single = el_cmcfol['f_level_single']
						f_level_multi = el_cmcfol['f_level_multi']
						if f_level_single == True:
							f_geometry = el_cmcfol['f_geometry']
							file, rash = f_geometry.split('.')
							file_name = file + '.eMesh'
							lvl_single = castellatedMC_2_obj['CM_features_lvl'][a]['lvl_prs']['lvl_single']
							single_str_1 = tri_pred_str_2 + '\n' + tri_pred_str_2 + '{' + '\n' + tri_pred_str_3 + 'file' + ' ' + '"' 
							single_str_2 = file_name + '"' + ';' + '\n' + tri_pred_str_3 + 'level' + ' ' + str(lvl_single) + ';' + '\n' + tri_pred_str_2 + '}' + '\n'
							single_str_itog = single_str_1 + single_str_2

							features_middle = features_middle + single_str_itog

						elif f_level_multi == True:
							f_geometry = el_cmcfol['f_geometry']
							file, rash = f_geometry.split('.')
							file_name = file + '.eMesh'
							f_level_multi_val = el_cmcfol['f_level_multi_val']
							multy_str_1 = '\n' + tri_pred_str_2 + '{' + '\n' + tri_pred_str_3 + 'file' + ' ' + '"' 
							multy_str_2 = file_name + '"' + ';' + '\n' + tri_pred_str_3 + 'levels' + ' ' + '('
							multi_n = len(castellatedMC_2_obj['CM_features_lvl'][a]['multi_prs'])

							u = 1
							t = 0
							multy_lev_vals = ''
							while u <= multi_n:
								lvl_multi_min = castellatedMC_2_obj['CM_features_lvl'][a]['multi_prs'][t]['lvl_multi_' + str(u)][0]
								lvl_multi_max = castellatedMC_2_obj['CM_features_lvl'][a]['multi_prs'][t]['lvl_multi_' + str(u)][1]

								if u != multi_n:
									multy_lev = '(' + str(lvl_multi_min) + ' ' + str(lvl_multi_max) + ')' + ' ' 
								else:
									multy_lev = '(' + str(lvl_multi_min) + ' ' + str(lvl_multi_max) + ')'
								multy_lev_vals = multy_lev_vals + multy_lev 
								u = u + 1
								t = t + 1

							multy_str_itog = multy_str_1 + multy_str_2 + multy_lev_vals + ')' + ';' + '\n' + tri_pred_str_2 + '}' + '\n'

							features_middle = features_middle + multy_str_itog

						q = q + 1 
						a = a + 1

					features_itog = features_pred + features_middle + features_post
					castellatedMC_eld_str_itog = castellatedMC_eld_str_itog + features_itog	

					###surfaceFeatureExtractDict###
					shutil.copyfile(r'./matches/surfaceFeatureExtractDict', prj_path + r'/surfaceFeatureExtractDict')
					sFED = open(prj_path + '/surfaceFeatureExtractDict', 'a')
					cMC_sFED_obj_list = castellatedMC_1_obj['sFED']
					sfed = len(cMC_sFED_obj_list)

					s = 1
					d = 0
					sFED_itog = ''
					while s <= sfed:
						sFED_geometry = cMC_sFED_obj_list[d]['sFED_geometry'] 
						sFED_extractionMethod = cMC_sFED_obj_list[d]['sFED_extractionMethod'] 
						sFED_includedAngle = cMC_sFED_obj_list[d]['sFED_includedAngle'] 
						sFED_writeObj = cMC_sFED_obj_list[d]['sFED_writeObj'] 

						sFED_prs_1 = '\n' + sFED_geometry + '\n' + '{' + '\n'
						sFED_prs_2 = tri_pred_str_1 + 'extractionMethod' + ' ' + sFED_extractionMethod + ';' + '\n'  + '\n'
						sFED_prs_3 = tri_pred_str_1 + 'extractFromSurfaceCoeffs' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'includedAngle' + ' ' + str(sFED_includedAngle) + ';' + '\n' + tri_pred_str_1 + '}' + '\n'  + '\n'
						sFED_prs_4 = tri_pred_str_1 + 'writeObj' + ' ' + sFED_writeObj + ';' + '\n' + '}' + '\n' + '\n'

						sFED_prs = sFED_prs_1 + sFED_prs_2 + sFED_prs_3 + sFED_prs_4
						sFED_itog = sFED_itog + sFED_prs

						s = s + 1
						d = d + 1	

					sFED.write(sFED_itog)
					close_str = '// ************************************************************************* //'
					sFED.write(close_str)
					sFED.close()
				else:
					features_itog = tri_pred_str_1 + 'features' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
					castellatedMC_eld_str_itog = castellatedMC_eld_str_itog + features_itog	

				if rS_v == True:	
					###refinementSurfaces###
					cMC_rS_obj_list = castellatedMC_1_obj['refinementSurfaces']

					refinementSurfaces_pred = tri_pred_str_1 + 'refinementSurfaces' + '\n' + tri_pred_str_1 + '{'

					q = 1
					a = 0
					refinementSurfaces_middle = ''
					for el_rsol in cMC_rS_obj_list:
						rS_surface = el_rsol['rS_surface']
						rS_level_min = el_rsol['rS_level_min']
						rS_level_max = el_rsol['rS_level_max']
						rS_regions = el_rsol['rS_regions']

						if rS_regions == False:
							file, rash = rS_surface.split('.')

							single_str_1 =  '\n' + tri_pred_str_2 + file + '\n' + tri_pred_str_2 + '{' + '\n' + tri_pred_str_3 + 'level' + ' '
							single_str_2 = '(' + str(rS_level_min) + ' ' + str(rS_level_max) + ')' + ';' + '\n' + tri_pred_str_2 + '}' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
							single_str_itog = single_str_1 + single_str_2

							refinementSurfaces_middle = refinementSurfaces_middle + single_str_itog

						elif rS_regions == True:
							rS_regions_val = el_rsol['rS_regions_val']
							file, rash = rS_surface.split('.')
							multy_str_1 = '\n' + tri_pred_str_2 + file + '\n' + tri_pred_str_2 + '{' + '\n' + tri_pred_str_3 + 'level'
							multy_str_2 = ' ' + '(' + str(rS_level_min) + ' ' + str(rS_level_max) + ')' + ';' + '\n' + tri_pred_str_3 + 'regions' + tri_pred_str_2 + '\n' + tri_pred_str_3 + '{' + '\n'

							u = 1
							t = 0
							multy_lev_vals = ''
							while u <= rS_regions_val:
								lvl_multi_reg = castellatedMC_2_obj['CM_refinementSurface_lvl'][a]['rS_regions'][t]
								lvl_multi_lev_min = castellatedMC_2_obj['CM_refinementSurface_lvl'][a]['rS_levels'][t][0]
								lvl_multi_lev_max = castellatedMC_2_obj['CM_refinementSurface_lvl'][a]['rS_levels'][t][1]

								multy_lev_1 = tri_pred_str_4 + lvl_multi_reg + '\n' + tri_pred_str_4 + '{' + '\n' + tri_pred_str_5 + 'level' + ' '
								multy_lev_2 = '(' + str(lvl_multi_lev_min) + ' ' + str(lvl_multi_lev_max) + ')' + ';' + '\n' + tri_pred_str_4 + '}' + '\n'
								multy_lev = multy_lev_1 + multy_lev_2

								multy_lev_vals = multy_lev_vals + multy_lev 
								u = u + 1
								t = t + 1

							multy_str_itog = multy_str_1 + multy_str_2 + multy_lev_vals + tri_pred_str_3 + '}' + '\n' + tri_pred_str_2 + '}' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'

							refinementSurfaces_middle = refinementSurfaces_middle + multy_str_itog

						q = q + 1
						a = a + 1

					refinementSurfaces_itog = refinementSurfaces_pred + refinementSurfaces_middle 
					castellatedMC_eld_str_itog = castellatedMC_eld_str_itog + refinementSurfaces_itog

				else:

					refinementSurfaces_itog = tri_pred_str_1 + 'refinementSurfaces' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
					castellatedMC_eld_str_itog = castellatedMC_eld_str_itog + refinementSurfaces_itog		

				if rR_v == True:	
					###refinementRegions###
					cMC_rR_obj_list = castellatedMC_1_obj['refinementRegions']

					refinementRegions_pred = tri_pred_str_1 + 'refinementRegions' + '\n' + tri_pred_str_1 + '{'
					refinementRegions_post = tri_pred_str_1 + '}' + '\n'

					q = 1
					a = 0
					refinementRegions_middle = ''
					for el_cmcrrol in cMC_rR_obj_list:
						rR_level_single = el_cmcrrol['rR_level_single']
						rR_level_multi = el_cmcrrol['rR_level_multi']
						rR_geometry = el_cmcrrol['rR_surface']
						rR_mode = el_cmcrrol['rR_mode']
						if rR_level_single == True:

							single_level_min = castellatedMC_2_obj['CM_refinementRegions_lvl'][a]['lvl_prs']['lvl_single_min']
							single_level_max = castellatedMC_2_obj['CM_refinementRegions_lvl'][a]['lvl_prs']['lvl_single_min']

							single_str_1 = tri_pred_str_2 + '\n' + tri_pred_str_2 + rR_geometry + '\n' + tri_pred_str_2 + '{' + tri_pred_str_3 + '\n' + tri_pred_str_3 + 'mode' + ' ' + rR_mode + ';'
							single_str_2 = tri_pred_str_3 + '\n' + tri_pred_str_3 + 'levels' + ' ' + '((' + str(single_level_min) + ' ' + str(single_level_max) + '))' + ';' + '\n' + tri_pred_str_2 + '}' + '\n'
							single_str_itog = single_str_1 + single_str_2

							refinementRegions_middle = refinementRegions_middle + single_str_itog							

						elif rR_level_multi == True:
							rR_geometry = el_cmcrrol['rR_surface']
							rR_level_multi_val = el_cmcrrol['rR_level_multi_val']
							multy_str_1 = tri_pred_str_2 + '\n' + tri_pred_str_2 + rR_geometry + '\n' + tri_pred_str_2 + '{' + '\n'
							multy_str_2 = tri_pred_str_3 + 'mode' + ' ' + rR_mode + ';' + '\n' + tri_pred_str_3 + 'levels' + ' ' + '('
							multi_n = len(castellatedMC_2_obj['CM_refinementRegions_lvl'][a]['multi_prs'])

							u = 1
							t = 0
							multy_lev_vals = ''
							while u <= multi_n:
								lvl_multi_min = castellatedMC_2_obj['CM_refinementRegions_lvl'][a]['multi_prs'][t]['lvl_multi_' + str(u)][0]
								lvl_multi_max = castellatedMC_2_obj['CM_refinementRegions_lvl'][a]['multi_prs'][t]['lvl_multi_' + str(u)][1]
								if u != multi_n:
									multy_lev = '(' + str(lvl_multi_min) + ' ' + str(lvl_multi_max) + ')' + ' ' 
								else:
									multy_lev = '(' + str(lvl_multi_min) + ' ' + str(lvl_multi_max) + ')'
								multy_lev_vals = multy_lev_vals + multy_lev 
								u = u + 1
								t = t + 1

							multy_str_itog = multy_str_1 + multy_str_2 + multy_lev_vals + ')' + ';' + '\n' + tri_pred_str_2 + '}' + '\n'

							refinementRegions_middle = refinementRegions_middle + multy_str_itog

						q = q + 1 
						a = a + 1

					refinementRegions_itog = refinementRegions_pred + refinementRegions_middle + refinementRegions_post
					castellatedMC_eld_str_itog = castellatedMC_eld_str_itog + refinementRegions_itog
				else:
					refinementRegions_itog = tri_pred_str_1 + 'refinementRegions' + '\n' + tri_pred_str_1 +'{' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
					castellatedMC_eld_str_itog = castellatedMC_eld_str_itog + refinementRegions_itog

				castellatedMC_post_str = '}' + '\n\n'

				castellatedMC_bl = castellatedMC_pred_str + castellatedMC_eld_str_itog + castellatedMC_post_str
				
		###addLayersControls###
		if os.path.exists(layers_path):	
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '

			layers_pred_str = 'addLayersControls' + '\n' + '{' + '\n' + '\n'
			layers_middle_pred_str = tri_pred_str_1 + 'layers' + '\n' + tri_pred_str_1 + '{' + tri_pred_str_2 + '\n'
			layers_middle_post_str = '\n' + tri_pred_str_1 + '}' + tri_pred_str_2 + '\n' + '\n'
			layers_number = len(layers_obj['layers_base'])
			layers_eld_str_itog = ''
			#layers
			u = 1
			t = 0
			layers_middle_str = ''
			while u <= layers_number:
				layer_str = layers_obj['layers_base'][t]['layer_' + str(u)]
				layer_val = layers_obj['layers_base'][t]['layer_val_' + str(u)]
				layers_middle_str = tri_pred_str_2 + layer_str + '\n' + tri_pred_str_2 + '{' + '\n' + tri_pred_str_3 + 'nSurfaceLayers' + ' ' + str(layer_val) + ';' + '\n' + tri_pred_str_2 + '}'
				u = u + 1
				t = t + 1

			layers_itog = layers_middle_pred_str + layers_middle_str + layers_middle_post_str

			#finalLayerThickness
			fLT_val_str = tri_pred_str_1 + 'finalLayerThickness' + ' ' + str(layers_obj['layers_add']['finalLayerThickness']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + fLT_val_str

			#expansionRatio
			eR_val_str = tri_pred_str_1 + 'expansionRatio' + ' ' + str(layers_obj['layers_add']['expansionRatio']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + eR_val_str

			#minThickness
			mT_val_str = tri_pred_str_1 + 'minThickness' + ' ' + str(layers_obj['layers_add']['minThickness']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + mT_val_str

			#relativeSizes
			rS_val_str = tri_pred_str_1 + 'relativeSizes' + ' ' + layers_obj['layers_add']['relativeSizes'] + ';' + '\n' + '\n'
			layers_itog = layers_itog + rS_val_str

			#featureAngle
			fA_val_str = tri_pred_str_1 + 'featureAngle' + ' ' + str(layers_obj['layers_add']['featureAngle']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + fA_val_str

			#nSmoothSurfaceNormals
			nSSN_val_str = tri_pred_str_1 + 'nSmoothSurfaceNormals' + ' ' + str(layers_obj['layers_add']['nSmoothSurfaceNormals']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + nSSN_val_str

			#nSmoothNormals
			nSN_val_str = tri_pred_str_1 + 'nSmoothNormals' + ' ' + str(layers_obj['layers_add']['nSmoothNormals']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + nSN_val_str

			#nSmoothThickness
			nST_val_str = tri_pred_str_1 + 'nSmoothThickness' + ' ' + str(layers_obj['layers_add']['nSmoothThickness']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + nST_val_str

			#minMedianAxisAngle
			mMAA_val_str = tri_pred_str_1 + 'minMedianAxisAngle' + ' ' + str(layers_obj['layers_add']['minMedianAxisAngle']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + mMAA_val_str

			#maxThicknessToMedialRatio
			mTTMR_val_str = tri_pred_str_1 + 'maxThicknessToMedialRatio' + ' ' + str(layers_obj['layers_add']['maxThicknessToMedialRatio']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + mTTMR_val_str

			#maxFaceThicknessRatio
			mFTR_val_str = tri_pred_str_1 + 'maxFaceThicknessRatio' + ' ' + str(layers_obj['layers_add']['maxFaceThicknessRatio']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + mFTR_val_str

			#nLayerIter
			nLI_val_str = tri_pred_str_1 + 'nLayerIter' + ' ' + str(layers_obj['layers_add']['nLayerIter']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + nLI_val_str

			#nRelaxedIter
			nRI_val_str = tri_pred_str_1 + 'nRelaxedIter' + ' ' + str(layers_obj['layers_add']['nRelaxedIter']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + nRI_val_str

			#nRelaxIter
			nRIter_val_str = tri_pred_str_1 + 'nRelaxIter' + ' ' + str(layers_obj['layers_add']['nRelaxIter']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + nRIter_val_str

			#nGrow
			nG_val_str = tri_pred_str_1 + 'nGrow' + ' ' + str(layers_obj['layers_add']['nGrow']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + nG_val_str

			#nBufferCellsNoExtrude
			nBCNE_val_str = tri_pred_str_1 + 'nBufferCellsNoExtrude' + ' ' + str(layers_obj['layers_add']['nBufferCellsNoExtrude']) + ';' + '\n' + '\n'
			layers_itog = layers_itog + nBCNE_val_str

			layers_post_str = '}' + '\n\n'

			layers_bl = layers_pred_str + layers_itog + layers_post_str
			
		###snapControls###
		if os.path.exists(snapC_path):	
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '

			snapC_pred_str = 'snapControls' + '\n' + '{' + '\n' + '\n'

			snapC_itog = ''

			#nSmoothPatch
			nSP_val_str = tri_pred_str_1 + 'nSmoothPatch' + ' ' + str(snapC_obj['nSmoothPatch']) + ';' + '\n' + '\n'
			snapC_itog = snapC_itog + nSP_val_str

			#tolerance
			t_val_str = tri_pred_str_1 + 'tolerance' + ' ' + str(snapC_obj['tolerance']) + ';' + '\n' + '\n'
			snapC_itog = snapC_itog + t_val_str

			#nSolveIter
			nSI_val_str = tri_pred_str_1 + 'nSolveIter' + ' ' + str(snapC_obj['nSolveIter']) + ';' + '\n' + '\n'
			snapC_itog = snapC_itog + nSI_val_str 

			#nRelaxIter
			nRI_val_str = tri_pred_str_1 + 'nRelaxIter' + ' ' + str(snapC_obj['nRelaxIter']) + ';' + '\n' + '\n'
			snapC_itog = snapC_itog + nRI_val_str

			#nFeatureSnapIter
			if 'nFeatureSnapIter' in snapC_obj:
				nFSI_val_str = tri_pred_str_1 + 'nFeatureSnapIter' + ' ' + str(snapC_obj['nFeatureSnapIter']) + ';' + '\n' + '\n'
				snapC_itog = snapC_itog + nFSI_val_str

			#implicitFeatureSnap
			if 'implicitFeatureSnap' in snapC_obj:
				iFS_val_str = tri_pred_str_1 + 'implicitFeatureSnap' + ' ' + snapC_obj['implicitFeatureSnap'] + ';' + '\n' + '\n'
				snapC_itog = snapC_itog + iFS_val_str

			#explicitFeatureSnap
			if 'explicitFeatureSnap' in snapC_obj:
				eFS_val_str = tri_pred_str_1 + 'explicitFeatureSnap' + ' ' + snapC_obj['explicitFeatureSnap'] + ';' + '\n' + '\n'
				snapC_itog = snapC_itog + eFS_val_str

			#multiRegionFeatureSnap
			if 'multiRegionFeatureSnap' in snapC_obj:
				mRFS_val_str = tri_pred_str_1 + 'multiRegionFeatureSnap' + ' ' + snapC_obj['multiRegionFeatureSnap'] + ';' + '\n'+ '\n'
				snapC_itog = snapC_itog + mRFS_val_str


			snapC_post_str = '}' + '\n\n'

			snapC_bl = snapC_pred_str + snapC_itog + snapC_post_str
			
		#meshQualityControls
		if os.path.exists(meshQC_path):	
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '

			meshQC_pred_str = 'meshQualityControls' + '\n' + '{' + '\n' + '\n'

			meshQC_itog = ''

			#relaxed maxNonOrtho
			rMNO_val_str = tri_pred_str_1 + 'relaxed' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 + 'maxNonOrtho' + ' ' + str(meshQC_obj['meshQC_add']['relaxed_maxNonOrtho']) + ';' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
			meshQC_itog = meshQC_itog + rMNO_val_str

			#nSmoothScale
			nSS_val_str = tri_pred_str_1 + 'nSmoothScale' + ' ' + str(meshQC_obj['meshQC_add']['nSmoothScale']) + ';' + '\n' + '\n'
			meshQC_itog = meshQC_itog + nSS_val_str

			#errorReduction
			eR_val_str = tri_pred_str_1 + 'errorReduction' + ' ' + str(meshQC_obj['meshQC_add']['errorReduction']) + ';' + '\n' + '\n'
			meshQC_itog = meshQC_itog + eR_val_str

			#maxNonOrtho
			if 'maxNonOrtho' in meshQC_obj['meshQC_add']:
				mNO_val_str = tri_pred_str_1 + 'maxNonOrtho' + ' ' + str(meshQC_obj['meshQC_add']['maxNonOrtho']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mNO_val_str

			#maxBoundarySkewness
			if 'maxBoundarySkewness' in meshQC_obj['meshQC_add']:
				mBS_val_str = tri_pred_str_1 + 'maxBoundarySkewness' + ' ' + str(meshQC_obj['meshQC_add']['maxBoundarySkewness']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mBS_val_str

			#maxInternalSkewness
			if 'maxInternalSkewness' in meshQC_obj['meshQC_add']:
				mIS_val_str = tri_pred_str_1 + 'maxInternalSkewness' + ' ' + str(meshQC_obj['meshQC_add']['maxInternalSkewness']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mIS_val_str

			#maxConcave
			if 'maxConcave' in meshQC_obj['meshQC_add']:
				mC_val_str = tri_pred_str_1 + 'maxConcave' + ' ' + str(meshQC_obj['meshQC_add']['maxConcave']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mC_val_str

			#minVol
			if 'minVol' in meshQC_obj['meshQC_add']:
				mV_val_str = tri_pred_str_1 + 'minVol' + ' ' + str(meshQC_obj['meshQC_add']['minVol']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mV_val_str

			#minArea
			if 'minArea' in meshQC_obj['meshQC_add']:
				mA_val_str = tri_pred_str_1 + 'minArea' + ' ' + str(meshQC_obj['meshQC_add']['minArea']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mA_val_str

			#minTetQuality
			if 'minTetQuality' in meshQC_obj['meshQC_add']:
				mTQ_val_str = tri_pred_str_1 + 'minTetQuality' + ' ' + str(meshQC_obj['meshQC_add']['minTetQuality']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mTQ_val_str

			#minTwist
			if 'minTwist' in meshQC_obj['meshQC_add']:
				mT_val_str = tri_pred_str_1 + 'minTwist' + ' ' + str(meshQC_obj['meshQC_add']['minTwist']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mT_val_str

			#minDeterminant
			if 'minDeterminant' in meshQC_obj['meshQC_add']:
				mD_val_str = tri_pred_str_1 + 'minDeterminant' + ' ' + str(meshQC_obj['meshQC_add']['minDeterminant']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mD_val_str

			#minFaceWeight
			if 'minFaceWeight' in meshQC_obj['meshQC_add']:
				mFW_val_str = tri_pred_str_1 + 'minFaceWeight' + ' ' + str(meshQC_obj['meshQC_add']['minFaceWeight']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mFW_val_str

			#minVolRatio
			if 'minVolRatio' in meshQC_obj['meshQC_add']:
				mVR_val_str = tri_pred_str_1 + 'minVolRatio' + ' ' + str(meshQC_obj['meshQC_add']['minVolRatio']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mVR_val_str

			#minTriangleTwist
			if 'minTriangleTwist' in meshQC_obj['meshQC_add']:
				mTT_val_str = tri_pred_str_1 + 'minTriangleTwist' + ' ' + str(meshQC_obj['meshQC_add']['minTriangleTwist']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mTT_val_str
				
			#minVolCollapseRatio
			if 'minVolCollapseRatio' in meshQC_obj['meshQC_add']:
				mVCR_val_str = tri_pred_str_1 + 'minVolCollapseRatio' + ' ' + str(meshQC_obj['meshQC_add']['minVolCollapseRatio']) + ';' + '\n' + '\n'
				meshQC_itog = meshQC_itog + mVCR_val_str

			meshQC_post_str = '}' + '\n\n'

			meshQC_bl = meshQC_pred_str + meshQC_itog + meshQC_post_str
		
		##write flags	
		if initial_obj['sL_flag'] == True or initial_obj['lS_flag'] == True	or initial_obj['lF_flag'] == True:																																	   
			##write flags																																	   
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '

			wf_pred_str = 'writeFlags' + '\n' + '(' + '\n' + '\n'
			wf_itog = ''
			if initial_obj['sL_flag'] == True:		
				wf_sL = tri_pred_str_1 + 'scalarLevels' + '\n' + '\n'
				wf_itog = wf_itog + wf_sL
			if initial_obj['lS_flag'] == True:
				wf_lS = tri_pred_str_1 + 'layerSets' + '\n' + '\n'
				wf_itog = wf_itog + wf_lS
			if initial_obj['lF_flag'] == True:
				wf_lF = tri_pred_str_1 + 'layerFields' + '\n' + '\n'
				wf_itog = wf_itog + wf_lF																																	  

			wf_post_str = ')' + ';' + '\n' + '\n'

			wf_bl = wf_pred_str + wf_itog + wf_post_str
		else:
			wf_bl = ''																																   
																																			   
		#########################################################################
		  			#Сохраняем файл при наличии различных опций#
		#########################################################################
		
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and not None in castellatedMC_1_vkl_arr and not None in castellatedMC_2_vkl_arr \
		and not None in layers_vkl_arr and not None in snapC_vkl_arr and not None in meshQC_vkl_arr:
			shutil.copyfile(r'./matches/snappyHexMeshDict', prj_path + r'/snappyHexMeshDict')
			sHMD = open(prj_path + '/snappyHexMeshDict', 'a')

			sHMD.write(cM_bl + s_bl + aL_bl + mT_bl + geometry_bl + castellatedMC_bl + layers_bl + snapC_bl + meshQC_bl + wf_bl)
			sHMD.close()
			
			snappyHexMeshDict_end(int_lng, prj_path, parn)
			
		elif not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and not None in castellatedMC_1_vkl_arr and None in castellatedMC_2_vkl_arr \
		and not None in layers_vkl_arr and not None in snapC_vkl_arr and not None in meshQC_vkl_arr:
			shutil.copyfile(r'./matches/snappyHexMeshDict', prj_path + r'/snappyHexMeshDict')
			sHMD = open(prj_path + '/snappyHexMeshDict', 'a')

			sHMD.write(cM_bl + s_bl + aL_bl + mT_bl + geometry_bl + castellatedMC_bl + layers_bl + snapC_bl + meshQC_bl + wf_bl)
			sHMD.close()
			
			snappyHexMeshDict_end(int_lng, prj_path, parn)
						
#########################################################################################################################		
#########################################################################################################################		
#########################################################################################################################