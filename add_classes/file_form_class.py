# -*- coding: utf-8 -*-
#---------------------------Импорт модулей и внешних форм-------------------------
#---------------------------
from PyQt4 import QtCore, QtGui
from forms.rCF_forms.fvSolution_form import fvSolution_form
from forms.rCF_forms.fvSchemes_form import fvSchemes_form
from forms.rCF_forms.controlDict_form import controlDict_form
#from forms.rCF_forms.refineMeshDict_form import refineMeshDict_form
#from forms.rCF_forms.boundary_form import boundary_form
from forms.rCF_forms.turbulenceProperties_form import turbulenceProperties_form
from forms.rCF_forms.thermophysicalProperties_form import thermophysicalProperties_form
#from forms.mesh_form import mesh_form
from forms.rCF_forms.p_form import p_form
from forms.rCF_forms.T_form import T_form
from forms.rCF_forms.U_form import U_form

#---------------------------Возврат ссылки на форму сетки-------------------------

class mesh_form_class:
    def mesh_form_class_func(self):
        global mesh_form_gl
        mesh_form_gl = mesh_form(self)
        
    def out_mesh_form_func(): return mesh_form_gl
    
#-------------------------Возврат ссылок на формы параметров----------------------
    
class file_form_class:
    def inp_file_form_func(self, file_name):
        global file_form
        global file_name_gl
        
        file_name_gl = file_name

        if  file_name_gl == "transportProperties":
            file_form = transportProperties_form(self)
           
        elif  file_name_gl == "fvSolution":
            file_form = fvSolution_form(self)

        elif  file_name_gl == "fvSchemes":
            file_form = fvSchemes_form(self)

        elif  file_name_gl == "controlDict":
            file_form = controlDict_form(self)

        #elif  file_name_gl == "refineMeshDict":
            #file_form = refineMeshDict_form(self)

        #elif  file_name_gl == "boundary":
            #file_form = boundary_form(self)

        elif  file_name_gl == "turbulenceProperties":
            file_form = turbulenceProperties_form(self)

        elif  file_name_gl == "thermophysicalProperties":
            file_form = thermophysicalProperties_form(self)

        elif  file_name_gl == "p":
            file_form = p_form(self)

        elif  file_name_gl == "T":
            file_form = T_form(self)

        elif  file_name_gl == "U":
            file_form = U_form(self)

        else:
            file_name_gl = None
            file_form = None
          
    def out_file_name_func(): return file_name_gl
    def out_file_form_func(): return file_form


