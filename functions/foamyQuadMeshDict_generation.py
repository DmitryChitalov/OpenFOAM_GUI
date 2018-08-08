# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------#

from PyQt4 import QtCore, QtGui
import pickle
import os
import shutil

class foamyQuadMeshDict_generation_class:			
	def foamyQuadMeshDict_func(int_lng, parn, tab, gTCT_edit, sCF_edit, s_edit, prj_path, mesh_name_txt, pd_2, fqmd_par): 
		def foamyQuadMeshDict_end(int_lng, prj_path, parn):
			fQMD = open(prj_path + '/foamyQuadMeshDict', 'a')

			close_str = '// ************************************************************************* //'
			fQMD.write(close_str)
			fQMD.close()

			if int_lng == 'Russian':
				msg = "Файл 'foamyQuadMeshDict' сохранен"
			elif int_lng == 'English':
				msg = "The 'foamyQuadMeshDict' file was saved"
			fqmd_par.on_msg_correct(msg)

			parn.cdw.setWidget(parn.outf_scroll)
			parn.outf_scroll.setFixedSize(350, 660)
			parn.cdw_frame.setFixedSize(350, 35)
			
			parn.msh_run.setEnabled(True)

			prj_dir = prj_path + '/foamyQuadMeshDict'

			outf = open(prj_dir)
			data = outf.read()
			if int_lng == 'Russian':
				parn.outf_lbl.setText("Файл " + "<font color='peru'>" + 'foamyQuadMeshDict' + "</font>") 
			elif int_lng == 'English':
				parn.outf_lbl.setText("<font color='peru'>" + 'foamyQuadMeshDict' + "</font>" + " file") 
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
			
			gTCT_v = initial_obj['gTCT']
			sCF_v = initial_obj['sCF']
			s_v = initial_obj['s']
			s_val = initial_obj['s_val']
			
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
			
		#проверяем на заполнение surfaceConformation#	
		surfaceConformation_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceConformation.pkl'
		if gTCT_edit.isChecked() == True:
			
			if os.path.exists(surfaceConformation_path):	
				surfaceConformation_vkl_arr = []

				surfaceConformation_input = open(surfaceConformation_path, 'rb')
				surfaceConformation_obj = pickle.load(surfaceConformation_input)
				surfaceConformation_input.close()

				surfaceConformation_vkl_arr.append('surfaceConformation')
			else:
				surfaceConformation_vkl_arr = []

				if int_lng == 'Russian':
					msg = "Заполните форму 'surfaceConformation'"
				elif int_lng == 'English':
					msg = "Fill out the form 'surfaceConformation'"
				msg_list.append(msg)
				surfaceConformation_vkl_arr.append(None)
				
		#motionControl
		motionControl_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'motionControl.pkl'
		if sCF_edit.isChecked() == True:
			
			if os.path.exists(motionControl_path):	
				motionControl_vkl_arr = []

				motionControl_input = open(motionControl_path, 'rb')
				motionControl_obj = pickle.load(motionControl_input)
				motionControl_input.close()

				motionControl_vkl_arr.append('motionControl')
			else:
				motionControl_vkl_arr = []

				if int_lng == 'Russian':
					msg = "Заполните форму 'motionControl'"
				elif int_lng == 'English':
					msg = "Fill out the form 'motionControl'"
				msg_list.append(msg)
				motionControl_vkl_arr.append(None)
				
		#surfaceFeatureExtractDict
		surfaceFeatureExtractDict_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'surfaceFeatureExtractDict.pkl'
		if s_edit.isChecked() == True:
			
			if os.path.exists(surfaceFeatureExtractDict_path):	
				surfaceFeatureExtractDict_vkl_arr = []

				surfaceFeatureExtractDict_input = open(surfaceFeatureExtractDict_path, 'rb')
				surfaceFeatureExtractDict_obj = pickle.load(surfaceFeatureExtractDict_input)
				surfaceFeatureExtractDict_input.close()

				surfaceFeatureExtractDict_vkl_arr.append('surfaceFeatureExtractDict')
			else:
				surfaceFeatureExtractDict_vkl_arr = []

				if int_lng == 'Russian':
					msg = "Заполните форму 'surfaceFeatureExtractDict'"
				elif int_lng == 'English':
					msg = "Fill out the form 'surfaceFeatureExtractDict'"
				msg_list.append(msg)
				surfaceFeatureExtractDict_vkl_arr.append(None)	
				
		#shortEdgeFilter
		shortEdgeFilter_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'shortEdgeFilter.pkl'
		if os.path.exists(shortEdgeFilter_path):	
			shortEdgeFilter_vkl_arr = []

			shortEdgeFilter_input = open(shortEdgeFilter_path, 'rb')
			shortEdgeFilter_obj = pickle.load(shortEdgeFilter_input)
			shortEdgeFilter_input.close()

			shortEdgeFilter_vkl_arr.append('shortEdgeFilter')
		else:
			shortEdgeFilter_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'shortEdgeFilter'"
			elif int_lng == 'English':
				msg = "Fill out the 'shortEdgeFilter' form"

			msg_list.append(msg)
			shortEdgeFilter_vkl_arr.append(None)	
			
		#extrusion
		extrusion_path = prj_path + '/' + mesh_name_txt + '_' + pd_2 + '/' + 'extrusion.pkl'
		if os.path.exists(extrusion_path):	
			extrusion_vkl_arr = []

			extrusion_input = open(extrusion_path, 'rb')
			extrusion_obj = pickle.load(extrusion_input)
			extrusion_input.close()

			extrusion_vkl_arr.append('extrusion')
		else:
			extrusion_vkl_arr = []

			if int_lng == 'Russian':
				msg = "Заполните форму 'extrusion'"
			elif int_lng == 'English':
				msg = "Fill out the 'extrusion' form"

			msg_list.append(msg)
			extrusion_vkl_arr.append(None)
			
		fqmd_par.on_msg_error(msg_list)	
		
		#########Формируем блоки параметров для файла foamyQuadMeshDict##########
		
		###geometry###
		if os.path.exists(geometry_1_path) and os.path.exists(geometry_2_path):	

			geometry_pred_str = '\n' + '\n' + 'geometry' + '\n' + '{' + '\n'

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
				if el_dict['geometry_' + str(i)] == 'Три-поверхность' or el_dict['geometry_' + str(i)] == 'Tri-surface' \
				or el_dict['geometry_' + str(i)] == 'Закрытая три-поверхность' or el_dict['geometry_' + str(i)] == 'Closed tri-surface' \
				or el_dict['geometry_' + str(i)] == 'Распределенная три-поверхность' or el_dict['geometry_' + str(i)] == 'Distributed tri-surface':

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
		
		###surfaceConformation###
		if os.path.exists(surfaceConformation_path):
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			
			surfaceConformation_pred_str = 'surfaceConformation' + '\n' + '{' + '\n'
			
			lIM_list = surfaceConformation_obj['sC_start_prs']['lIM']
			pPDC = surfaceConformation_obj['sC_start_prs']['pPDC']
			mELC = surfaceConformation_obj['sC_start_prs']['mELC']
			mNLC = surfaceConformation_obj['sC_start_prs']['mNLC']
			mNPDC = surfaceConformation_obj['sC_start_prs']['mNPDC']
			mQA = surfaceConformation_obj['sC_start_prs']['mQA']
			iSNPP = surfaceConformation_obj['sC_start_prs']['iSNPP']
			mP = surfaceConformation_obj['sC_start_prs']['mP']
			iSNePP = surfaceConformation_obj['sC_start_prs']['iSNePP']
			mBCI = surfaceConformation_obj['sC_start_prs']['mBCI']
			rIG = surfaceConformation_obj['sC_start_prs']['rIG']
			rP = surfaceConformation_obj['sC_start_prs']['rP']
			
			sC_itog_1 = tri_pred_str_1 + 'locationInMesh' + tri_pred_str_1 + '(' + lIM_list[0] + ' ' + lIM_list[1] + ' ' + lIM_list[2] + ')' + ';' + '\n' + '\n'
			sC_itog_2 = tri_pred_str_1 + 'pointPairDistanceCoeff' + tri_pred_str_1 + pPDC + ';' + '\n' + '\n'
			sC_itog_3 = tri_pred_str_1 + 'minEdgeLenCoeff' + tri_pred_str_1 + mELC + ';' + '\n' + '\n'
			sC_itog_4 = tri_pred_str_1 + 'maxNotchLenCoeff' + tri_pred_str_1 + str(mNLC) + ';' + '\n' + '\n'
			sC_itog_5 = tri_pred_str_1 + 'minNearPointDistCoeff' + tri_pred_str_1 + str(mNPDC) + ';' + '\n' + '\n'
			sC_itog_6 = tri_pred_str_1 + 'maxQuadAngle' + tri_pred_str_1 + str(mQA) + ';' + '\n' + '\n'
			sC_itog_7 = tri_pred_str_1 + 'insertSurfaceNearestPointPairs' + tri_pred_str_1 + iSNPP + ';' + '\n' + '\n'
			sC_itog_8 = tri_pred_str_1 + 'mirrorPoints' + tri_pred_str_1 + mP + ';' + '\n' + '\n'
			sC_itog_9 = tri_pred_str_1 + 'insertSurfaceNearPointPairs' + tri_pred_str_1 + iSNePP + ';' + '\n' + '\n'
			sC_itog_10 = tri_pred_str_1 + 'maxBoundaryConformingIter' + tri_pred_str_1 + str(mBCI) + ';' + '\n' + '\n'
			
			if gTCT_v == True:
				sC_conf_prs_list = surfaceConformation_obj['sC_conf_prs']
				sC_conf_prs_pred = tri_pred_str_1 + 'geometryToConformTo' + '\n' + tri_pred_str_1 + '{' + '\n'
				sC_conf_prs_post = tri_pred_str_1 + '}' + '\n' + '\n'
				for sC_cp in sC_conf_prs_list:
					g = sC_cp['g']
					fM = sC_cp['fM']
					eFEM = sC_cp['eFEM']
					file, rash = eFEM.split('.')
					file_name = '"' + file + '.extendedFeatureEdgeMesh' + '"'
					sC_conf_prs_itog = tri_pred_str_2 + g + '\n' + tri_pred_str_2 + '{' + '\n' + tri_pred_str_3 + 'featureMethod' + tri_pred_str_1 + fM + ';' + '\n' \
					+ tri_pred_str_3 + 'extendedFeatureEdgeMesh' + ' ' + file_name + ';' + '\n' + tri_pred_str_2 + '}' + '\n'
				sC_itog_11 = sC_conf_prs_pred + sC_conf_prs_itog + sC_conf_prs_post
			else:
				sC_itog_11 = tri_pred_str_1 + 'geometryToConformTo' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
			
			sC_itog_12 = tri_pred_str_1 + 'additionalFeatures' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
			sC_itog_13 = tri_pred_str_1 + 'randomiseInitialGrid' + tri_pred_str_1 + rIG + ';' + '\n' + '\n'
			sC_itog_14 = tri_pred_str_1 + 'randomPerturbation' + tri_pred_str_1 + str(rP) + ';' + '\n'
			
			surfaceConformation_itog = sC_itog_1 + sC_itog_2 + sC_itog_3 + sC_itog_4 + sC_itog_5 + sC_itog_6 + sC_itog_7 + sC_itog_8 + sC_itog_9 + sC_itog_10 + sC_itog_11 + sC_itog_12 + sC_itog_13 + sC_itog_14
			
			surfaceConformation_post_str = '}' + '\n\n'

			surfaceConformation_bl = surfaceConformation_pred_str + surfaceConformation_itog + surfaceConformation_post_str
			
		###motionControl###
		if os.path.exists(motionControl_path):
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			
			motionControl_pred_str = 'motionControl' + '\n' + '{' + '\n'
			mCS = motionControl_obj['mC_start_prs']['mCS']
			dF = motionControl_obj['mC_start_prs']['dF']
			rM = motionControl_obj['mC_start_prs']['rM']
			rS = motionControl_obj['mC_start_prs']['rS']
			rE = motionControl_obj['mC_start_prs']['rE']
			oO = motionControl_obj['mC_start_prs']['oO']
			mSO = motionControl_obj['mC_start_prs']['mSO']
			nWAD = motionControl_obj['mC_start_prs']['nWAD']
			
			sC_itog_1 = tri_pred_str_1 + 'minCellSize' + tri_pred_str_1 + str(mCS) + ';' + '\n' + '\n'
			sC_itog_2 = tri_pred_str_1 + 'defaultPriority' + tri_pred_str_1 + str(dF) + ';' + '\n' + '\n'
			
			if sCF_v == True:
				mC_sCF_prs_list = motionControl_obj['mC_sCF_prs']
				mC_sCF_prs_pred = tri_pred_str_1 + 'shapeControlFunctions' + '\n' + tri_pred_str_1 + '{'
				mC_sCF_prs_post = tri_pred_str_2 + '}' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
				for mC_scfp in mC_sCF_prs_list:
					s = mC_scfp['s']
					t = mC_scfp['t']
					p = mC_scfp['p']
					m = mC_scfp['m']
					cSF = mC_scfp['cSF']
					dCSC = mC_scfp['dCSC']
					
					if mC_scfp['dC_chk'] == True:
						dC = mC_scfp['dC']
					if mC_scfp['tDC_chk'] == True:
						tDC = mC_scfp['tDC']
					if mC_scfp['sOC_chk'] == True:
						sOC = mC_scfp['sOC']
					sCSF = mC_scfp['sCSF']
					sCSC = mC_scfp['sCSC']
					
					mC_sCF_prs_itog = tri_pred_str_2 + s + '\n' + tri_pred_str_2 + '{' \
					+ '\n' + tri_pred_str_3 + 'type' + tri_pred_str_1 + t + ';' + '\n' \
					+ tri_pred_str_3 + 'priority' + tri_pred_str_1 + str(p) + ';' + '\n' \
					+ tri_pred_str_3 + 'mode' + tri_pred_str_1 + m + ';' + '\n' \
					+ tri_pred_str_3 + 'cellSizeFunction' + tri_pred_str_1 + cSF + ';' + '\n' \
					+ tri_pred_str_3 + 'surfaceOffsetLinearDistanceCoeffs' + '\n' + tri_pred_str_3 + '{' + '\n' \
					+ tri_pred_str_4 + 'distanceCellSizeCoeff' + tri_pred_str_1 + str(dCSC) + ';'
					if mC_scfp['dC_chk'] == True:
						mC_sCF_prs_itog_1 = tri_pred_str_4 + 'distanceCoeff' + tri_pred_str_1 + str(dC) + ';'
						mC_sCF_prs_itog = mC_sCF_prs_itog + mC_sCF_prs_itog_1
					if mC_scfp['tDC_chk'] == True:
						mC_sCF_prs_itog_2 = '\n' + tri_pred_str_4 + 'totalDistanceCoeff' + tri_pred_str_1 + str(tDC) + ';'
						mC_sCF_prs_itog = mC_sCF_prs_itog + mC_sCF_prs_itog_2
					if mC_scfp['sOC_chk'] == True:
						mC_sCF_prs_itog_3 = '\n' + tri_pred_str_4 + 'surfaceOffsetCoeff' + tri_pred_str_1 + str(sOC) + ';'
						mC_sCF_prs_itog = '\n' + mC_sCF_prs_itog + mC_sCF_prs_itog_3
					mC_sCF_prs_itog_4 = '\n' + tri_pred_str_3 + '}' + '\n'
					mC_sCF_prs_itog = mC_sCF_prs_itog + mC_sCF_prs_itog_4
					mC_sCF_prs_itog_5 = tri_pred_str_3 + 'surfaceCellSizeFunction' + tri_pred_str_1 + sCSF + ';' + '\n' \
					+ tri_pred_str_3 + 'uniformValueCoeffs' + '\n' + tri_pred_str_3 + '{' + '\n' + tri_pred_str_4 + 'surfaceCellSizeCoeff' \
					+ tri_pred_str_1 + str(sCSC) + ';' + '\n' + tri_pred_str_3 + '}' + '\n'
					mC_sCF_prs_itog = mC_sCF_prs_itog + mC_sCF_prs_itog_5
					
				sC_itog_3 = mC_sCF_prs_pred + mC_sCF_prs_itog + mC_sCF_prs_post
			else:
				sC_itog_3 = tri_pred_str_1 + 'shapeControlFunctions' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
					
			sC_itog_4 = tri_pred_str_1 + 'relaxationModel' + tri_pred_str_1 + rM + ';' + '\n' + '\n'
			sC_itog_5 = tri_pred_str_1 + 'adaptiveLinearCoeffs' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 \
			+ 'relaxationStart' + tri_pred_str_1 + str(rS) + ';' + '\n' + tri_pred_str_2 + 'relaxationEnd' + tri_pred_str_1 + str(rE) + ';' + '\n' \
			+ tri_pred_str_1 + '}' + '\n' + '\n'
			sC_itog_6 = tri_pred_str_1 + 'objOutput' + tri_pred_str_1 + oO + ';' + '\n' + '\n'
			sC_itog_7 = tri_pred_str_1 + 'meshedSurfaceOutput' + tri_pred_str_1 + mSO + ';' + '\n' + '\n'
			sC_itog_8 = tri_pred_str_1 + 'nearWallAlignedDist' + tri_pred_str_1 + str(nWAD) + ';' + '\n'
			
			motionControl_itog = sC_itog_1 + sC_itog_2 + sC_itog_3 + sC_itog_4 + sC_itog_5 + sC_itog_6 + sC_itog_7 + sC_itog_8
			
			motionControl_post_str = '}' + '\n\n'

			motionControl_bl = motionControl_pred_str + motionControl_itog + motionControl_post_str
		
		###shortEdgeFilter###	
		if os.path.exists(shortEdgeFilter_path):
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			
			sEFF = shortEdgeFilter_obj['sEFF']
			eATBF = shortEdgeFilter_obj['eATBF']
			
			shortEdgeFilter_pred_str = 'shortEdgeFilter' + '\n' + '{' + '\n'
			
			sC_itog_1 = tri_pred_str_1 + 'shortEdgeFilterFactor' + tri_pred_str_1 + str(sEFF) + ';' + '\n' \
			+ tri_pred_str_1 + 'edgeAttachedToBoundaryFactor' + tri_pred_str_1 + str(eATBF) + ';' + '\n'
			
			shortEdgeFilter_itog = sC_itog_1
			
			shortEdgeFilter_post_str = '}' + '\n\n'

			shortEdgeFilter_bl = shortEdgeFilter_pred_str + shortEdgeFilter_itog + shortEdgeFilter_post_str
			
		###extrusion###
		if os.path.exists(extrusion_path):
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			
			extrusion_pred_str = 'extrusion' + '\n' + '{' + '\n'
			e = extrusion_obj['e']
			
			extrusion_itog_1 = tri_pred_str_1 + 'extrude' + tri_pred_str_1 + e + ';' + '\n' \
			+ tri_pred_str_1 + '#include    "extrude2DMeshDict";' 
			extrusion_post_str = '\n' + '}' + '\n' + '\n'
			extrusion_bl = extrusion_pred_str + extrusion_itog_1 + extrusion_post_str
			
			shutil.copyfile(r'./matches/extrude2DMeshDict', prj_path + r'/extrude2DMeshDict')
			e2DMD = open(prj_path + '/extrude2DMeshDict', 'a')
			
			eM = extrusion_obj['eM']
			pT = extrusion_obj['pT']
			axisPt_v_list = extrusion_obj['axisPt']
			a_v_list = extrusion_obj['a']
			ang = extrusion_obj['ang']
			
			nL_chck = extrusion_obj['nL_chck']
			if nL_chck == True:
				nL_val = extrusion_obj['nL_val']
				
			eR_chck = extrusion_obj['eR_chck']
			if eR_chck == True:
				eR_val = extrusion_obj['eR_val']
				
			d_chck = extrusion_obj['d_chck']
			if d_chck == True:
				d_val_list = extrusion_obj['d_val']
				
			t_chck = extrusion_obj['t_chck']
			if t_chck == True:
				t_val = extrusion_obj['t_val']

			extrusion_itog_2 = '\n' + '\n' + 'extrudeModel' + tri_pred_str_1 + eM + ';' + '\n' + '\n' \
			+ 'patchType' + tri_pred_str_1 + pT + ';' + '\n' + '\n'
			
			extrusion_itog = extrusion_itog_2
			
			if nL_chck == True:
				extrusion_itog_3 = 'nLayers' + tri_pred_str_1 + str(nL_val) + ';' + '\n' + '\n'
				extrusion_itog = extrusion_itog + extrusion_itog_3
				
			if eR_chck == True:
				extrusion_itog_4 = 'expansionRatio' + tri_pred_str_1 + str(eR_val) + ';' + '\n' + '\n'
				extrusion_itog = extrusion_itog + extrusion_itog_4
			
			extrusion_itog_5 = 'linearDirectionCoeffs' + '\n' + '{' + '\n'
			extrusion_itog = extrusion_itog + extrusion_itog_5
			
			if d_chck == True:
				extrusion_itog_6 = tri_pred_str_1 + 'direction' + tri_pred_str_1 + '(' + str(d_val_list[0]) + ' ' + str(d_val_list[1]) + ' ' + str(d_val_list[2]) + ')' + ';' + '\n'
				extrusion_itog = extrusion_itog + extrusion_itog_6
				
			if t_chck == True:
				extrusion_itog_7 = tri_pred_str_1 + 'thickness' + tri_pred_str_1 + str(t_val) + ';' + '\n'
				extrusion_itog = extrusion_itog + extrusion_itog_7
			
			extrusion_itog_8 = '}' + '\n' + '\n'
			extrusion_itog = extrusion_itog + extrusion_itog_8
			
			extrusion_itog_9 = 'wedgeCoeffs' + '\n' + '{' + '\n' \
			+ tri_pred_str_1 + 'axisPt' + tri_pred_str_1 + '(' + str(axisPt_v_list[0]) + ' ' + str(axisPt_v_list[1]) + ' ' + str(axisPt_v_list[2]) + ')' + ';' + '\n'  \
			+ tri_pred_str_1 + 'axis' + tri_pred_str_1 + '(' + str(a_v_list[0]) + ' ' + str(a_v_list[1]) + ' ' + str(a_v_list[2]) + ')' + ';' + '\n' \
			+ tri_pred_str_1 + 'angle' + tri_pred_str_1 + str(ang) + ';' + '\n' + '}' + '\n' + '\n'
			
			extrusion_itog = extrusion_itog + extrusion_itog_9
			
			extrusion_post_str = '}' + '\n\n'
		
			e2DMD.write(extrusion_itog)
			close_str = '// ************************************************************************* //'
			e2DMD.write(close_str)
			e2DMD.close()

		###surfaceFeatureExtractDict###
		if s_v == True:
			tri_pred_str_1 = '    '
			tri_pred_str_2 = '        '
			tri_pred_str_3 = '            '
			tri_pred_str_4 = '                '
			tri_pred_str_5 = '                    '
			
			shutil.copyfile(r'./matches/surfaceFeatureExtractDict', prj_path + r'/surfaceFeatureExtractDict')
			sFED = open(prj_path + '/surfaceFeatureExtractDict', 'a')
			sfed = s_val
			y = 1
			d = 0
			sFED_itog = ''
			while y <= sfed:
				s = surfaceFeatureExtractDict_obj[d]['s'] 
				eM = surfaceFeatureExtractDict_obj[d]['eM'] 
				iA = surfaceFeatureExtractDict_obj[d]['iA']

				normal_list = surfaceFeatureExtractDict_obj[d]['n']
				basePoint_list = surfaceFeatureExtractDict_obj[d]['bP']

				nME = surfaceFeatureExtractDict_obj[d]['nME'] 
				oE = surfaceFeatureExtractDict_obj[d]['oE'] 
				wO = surfaceFeatureExtractDict_obj[d]['wO'] 
			
				sFED_prs_1 = '\n' + '\n' + s + '\n' + '{' + '\n'
				sFED_prs_2 = tri_pred_str_1 + 'extractionMethod' + tri_pred_str_1 + eM + ';' + '\n'  + '\n'
				sFED_prs_3 = tri_pred_str_1 + 'extractFromSurfaceCoeffs' + '\n' + tri_pred_str_1 + '{' + '\n' \
				+ tri_pred_str_2 + 'includedAngle' + tri_pred_str_1 + str(iA) + ';' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
				sFED_prs_4 = tri_pred_str_1 + 'subsetFeatures' + '\n' + tri_pred_str_1 + '{' + '\n' + tri_pred_str_2 \
				+ 'plane' + tri_pred_str_1 + '(' + str(normal_list[0]) + ' ' + str(normal_list[1]) + ' ' + str(normal_list[2]) + ')' \
				+ '(' + str(basePoint_list[0]) + ' ' + str(basePoint_list[1]) + ' ' + str(basePoint_list[2]) + ')' + ';' + '\n' + '\n' \
 				+ tri_pred_str_2 + 'nonManifoldEdges' + tri_pred_str_1 + nME + ';' + '\n' + '\n' \
				+ tri_pred_str_2 + 'openEdges' + tri_pred_str_1 + oE + ';' + '\n' + tri_pred_str_1 + '}' + '\n' + '\n'
				
				sFED_prs_5 = tri_pred_str_1 + 'writeObj' + tri_pred_str_1 + wO + ';' + '\n' + '}' + '\n' + '\n'

				sFED_prs = sFED_prs_1 + sFED_prs_2 + sFED_prs_3 + sFED_prs_4 + sFED_prs_5
				sFED_itog = sFED_itog + sFED_prs

				y = y + 1
				d = d + 1	

			sFED.write(sFED_itog)
			close_str = '// ************************************************************************* //'
			sFED.write(close_str)
			sFED.close()
																																			   
		#########################################################################
		  			#Сохраняем файл при наличии различных опций#
		#########################################################################
		
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and not None in surfaceConformation_vkl_arr and not None in motionControl_vkl_arr \
		and not None in shortEdgeFilter_vkl_arr and not None in extrusion_vkl_arr \
		and not None in surfaceFeatureExtractDict_vkl_arr:
			shutil.copyfile(r'./matches/foamyQuadMeshDict', prj_path + r'/foamyQuadMeshDict')
			fQMD = open(prj_path + '/foamyQuadMeshDict', 'a')

			fQMD.write(geometry_bl + surfaceConformation_bl + motionControl_bl + shortEdgeFilter_bl + extrusion_bl)
			fQMD.close()
			
			foamyQuadMeshDict_end(int_lng, prj_path, parn)
			
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and gTCT_edit.isChecked() == False and None in surfaceConformation_vkl_arr and not None in motionControl_vkl_arr \
		and not None in shortEdgeFilter_vkl_arr and not None in extrusion_vkl_arr \
		and not None in surfaceFeatureExtractDict_vkl_arr:
			shutil.copyfile(r'./matches/foamyQuadMeshDict', prj_path + r'/foamyQuadMeshDict')
			fQMD = open(prj_path + '/foamyQuadMeshDict', 'a')

			fQMD.write(geometry_bl + surfaceConformation_bl + motionControl_bl + shortEdgeFilter_bl + extrusion_bl)
			fQMD.close()
			
			foamyQuadMeshDict_end(int_lng, prj_path, parn)
			
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and gTCT_edit.isChecked() == False and None in surfaceConformation_vkl_arr \
		and sCF_edit.isChecked() == False and None in motionControl_vkl_arr \
		and not None in shortEdgeFilter_vkl_arr and not None in extrusion_vkl_arr \
		and not None in surfaceFeatureExtractDict_vkl_arr:
			shutil.copyfile(r'./matches/foamyQuadMeshDict', prj_path + r'/foamyQuadMeshDict')
			fQMD = open(prj_path + '/foamyQuadMeshDict', 'a')

			fQMD.write(geometry_bl + surfaceConformation_bl + motionControl_bl + shortEdgeFilter_bl + extrusion_bl)
			fQMD.close()
			
			foamyQuadMeshDict_end(int_lng, prj_path, parn)
			
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and gTCT_edit.isChecked() == False and None in surfaceConformation_vkl_arr \
		and sCF_edit.isChecked() == False and None in motionControl_vkl_arr \
		and s_edit.isChecked() == False and None in shortEdgeFilter_vkl_arr \
		and not None in extrusion_vkl_arr \
		and not None in surfaceFeatureExtractDict_vkl_arr:
			shutil.copyfile(r'./matches/foamyQuadMeshDict', prj_path + r'/foamyQuadMeshDict')
			fQMD = open(prj_path + '/foamyQuadMeshDict', 'a')

			fQMD.write(geometry_bl + surfaceConformation_bl + motionControl_bl + shortEdgeFilter_bl + extrusion_bl)
			fQMD.close()
			
			foamyQuadMeshDict_end(int_lng, prj_path, parn)
			
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and not None in surfaceConformation_vkl_arr \
		and sCF_edit.isChecked() == False and None in motionControl_vkl_arr \
		and not None in shortEdgeFilter_vkl_arr \
		and not None in extrusion_vkl_arr \
		and not None in surfaceFeatureExtractDict_vkl_arr:
			shutil.copyfile(r'./matches/foamyQuadMeshDict', prj_path + r'/foamyQuadMeshDict')
			fQMD = open(prj_path + '/foamyQuadMeshDict', 'a')

			fQMD.write(geometry_bl + surfaceConformation_bl + motionControl_bl + shortEdgeFilter_bl + extrusion_bl)
			fQMD.close()
			
			foamyQuadMeshDict_end(int_lng, prj_path, parn)
			
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and not None in surfaceConformation_vkl_arr \
		and not None in motionControl_vkl_arr \
		and s_edit.isChecked() == False and None in shortEdgeFilter_vkl_arr \
		and not None in extrusion_vkl_arr \
		and not None in surfaceFeatureExtractDict_vkl_arr:
			shutil.copyfile(r'./matches/foamyQuadMeshDict', prj_path + r'/foamyQuadMeshDict')
			fQMD = open(prj_path + '/foamyQuadMeshDict', 'a')

			fQMD.write(geometry_bl + surfaceConformation_bl + motionControl_bl + shortEdgeFilter_bl + extrusion_bl)
			fQMD.close()
			
			foamyQuadMeshDict_end(int_lng, prj_path, parn)
			
		if not None in initial_vkl_arr \
		and not None in geometry_1_vkl_arr and not None in geometry_2_vkl_arr \
		and not None in surfaceConformation_vkl_arr \
		and sCF_edit.isChecked() == False and None in motionControl_vkl_arr \
		and s_edit.isChecked() == False and None in shortEdgeFilter_vkl_arr \
		and not None in extrusion_vkl_arr \
		and not None in surfaceFeatureExtractDict_vkl_arr:
			shutil.copyfile(r'./matches/foamyQuadMeshDict', prj_path + r'/foamyQuadMeshDict')
			fQMD = open(prj_path + '/foamyQuadMeshDict', 'a')

			fQMD.write(geometry_bl + surfaceConformation_bl + motionControl_bl + shortEdgeFilter_bl + extrusion_bl)
			fQMD.close()
			
			foamyQuadMeshDict_end(int_lng, prj_path, parn)
		
#########################################################################################################################		
#########################################################################################################################		
#########################################################################################################################