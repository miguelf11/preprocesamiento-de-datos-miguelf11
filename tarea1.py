#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.getcwd()
os.chdir('/home/ubunto14/Documentos/spyder')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib as mpl
import re
import matplotlib.animation as animation
from sklearn.preprocessing import Imputer
import pylab

data = pd.read_csv('data.csv',encoding='utf-8',names=['col0', 'Periodo', 'Cedula','Fecha','Edad'
,'EstadoCivil','Sexo','Escuela','Ingreso','Modalidad_de_Ingreso','Semestre','X_CambioDireccion','Razon_Cambio_Direccion',
'InscritasAnterior','Aprobadas','Retiradas','Reprobadas','Promedio_Aprobado','Eficiencia','Motivo_Reprob',
'InscritasActual','X_Tesis-Pasantias','Veces_Inscritas_Tesis_Pasantias','Procedencia',
'Tipo_Vivienda_donde_reside_mientras_Universidad','Reside_Con:','TipoResideUniv','Monto_Mensual_Residencia',
'Direccion_Alquilado','X_Matrimonio','X_Beneficio_Adicional','Benef_Adicional_Año_Motivo_Institucion_y_Motivo',
'X_Actividad_Ingreso','Tipo_Actividad_y_Frecuencia','MontoBeca','AporteResp','AporteAmigos','Ingreso_Actividad',
'IngresoTotal','Alimentacion','Transporte','Salud','Odontologicos','GastosPersonales','Residencia','Materiales',
'Recreacion','OtrosGastos','TotalEgreso','ResponsableEconomic','CargaFamiliar','IngresoDelResp',
'OtrosIngresosResp','Total_Ingreso_Responsable','ViviendaR','AlimentoR','TransporteR','SaludR','OdontologR',
'EducativosR','ServiciosR','CondominioR','OtrosGastosR','TotalEgresoR','Opinion','Sugerencias'],header=0)
    

"""---------------------------------------------------------------------------------------"""
"""----------------------------------------FUNCIONES--------------------------------------"""
"""---------------------------------------------------------------------------------------"""
def my_imputer(name,strat,value):
    if value == 0:
        data[name] = data[name].fillna(0)
    imp = Imputer(missing_values=value, strategy=strat, axis=0)
    x = data[name]
    x = x.reshape(-1,1)
    imp.fit(x)
    data[name] = imp.transform(x)

def extraer_num(name,convertir):
    for i in range(0,len(data)):
        if (convertir):
            aux = str(data[name][i])
        else:
            aux=data[name][i]
        aux1=re.findall(r'\d+', aux)
        if len(aux1) == 3:
            aux1[0] = int(aux1[0]) * 1000
            aux1[1] = int(aux1[1])
            aux1[2] = float(aux1[2]) / 100
            aux = aux1[0] + aux1[1]+aux1[2]
            data[name][i] = aux
        if len(aux1) == 2:
            aux1[0] = int(aux1[0])
            aux1[1] = float (aux1[1])/100
            aux = aux1[0] + aux1[1]
            data[name][i] = aux
        if len(aux1) == 1:
            aux1[0] = int(aux1[0])
            aux = aux1[0]
            data[name][i] = aux
        if len(aux1) == 0:
            data[name][i] = float('nan')
                

def xcolumns(name):
    for i in range(0,len(data)):
        aux=data[name][i]
        if aux == 'Si':
            data[name][i]=1
        if aux == 'No':
            data[name][i]=0
            
            

"""---------------------------------------------------------------------------------------"""
"""-------------------------------------FIN FUNCIONES-------------------------------------"""
"""---------------------------------------------------------------------------------------"""








"""-----------------------------------------------------------------------------------------"""
"""-----------------------------------------PERIODO-----------------------------------------"""
"""-----------------------------------------------------------------------------------------"""
for i in range(0,len(data)):
    aux=data['Periodo'][i]
    
    patron= ("[PRI]+\s*\w*\s*/*-*\s*2*0*1*\w*4+-*\s*") 
    if (re.match(patron,aux, re.IGNORECASE)):       
        data['Periodo'][i] ='2014-I'
        aux = '2014-I'

    patron= ("\s*\w*\s*\w*[20]*[14]+\w*\s*\w*II+")
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'
    patron=("(II+\s*-*\s*[20]*[14]+\s*) ")
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'
    patron = ("[SE]+[G]*[C]*\s*\w*\s*\w*-*\s*[20]*14+-*\s*")
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'
    patron=("2014+-*2015+")
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'
    patron=("[20]*14+-*\s*0*2+")
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'
    if aux=='2014':       
        data['Periodo'][i] ='2014-II'
        aux = '2014-II'
    patron=("2014+_*\s*2015+")
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'

    patron=("I+\s*-*\s*[20]*[15]\s*")
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2015-I'
        data['Periodo'][i] ='2015-I'
    patron= ("[PRI|1]+\s*-*\s*\w*\s*/*-*\s*2*0*1*\w*5+-*\s*") 
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2015-I'
        data['Periodo'][i] ='2015-I'
    patron=("[20]*15+-*\s*s*0*1+s*") 
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2015-I'
        data['Periodo'][i] ='2015-I'
    if aux=='2015':
        aux = '2015-I'
        data['Periodo'][i] ='2015-I'
        
    patron = ("[SE]+[G]*[C]*\s*\w*\s*\w*-*\s*[20]*15+-*\s*")
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2015-II'
        data['Periodo'][i] ='2015-II'
    patron = ('[20]*15+-*\ws*20*16+')
    if (re.match(patron,aux, re.IGNORECASE)):       
        data['Periodo'][i] ='2015-II'
        aux = '2015-II'
    patron= ("\w*\s*-+\w*-+\s*2+-+\w*\s*2*0*-*")
    if (re.match(patron,aux, re.IGNORECASE)):
       data['Periodo'][i] ='2014-II'
       aux = '2014-II'
    patron = ("segundo+\s*\w*\s*\w*")
    if (re.match(patron,aux, re.IGNORECASE)): 
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'
    patron= ("\w*[-]+2+[-][20]*[14]+")
    if (re.match(patron,aux, re.IGNORECASE)): 
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'
    patron= ("2+\s*\w*[do|semestre]+") 
    if (re.match(patron,aux, re.IGNORECASE)):
        aux = '2014-II'
        data['Periodo'][i] ='2014-II'
    if (aux != '2014-II' and aux != '2014-I' and aux != '2015-II' and aux != '2015-I'):
        data['Periodo'][i] ='eliminar'

    if aux == '2014-I':
        data['Periodo'][i] = 1
    if aux == '2014-II':
        data['Periodo'][i] = 2
    if aux == '2015-I':
        data['Periodo'][i] = 3
    if aux == '2015-II':
        data['Periodo'][i] = 4
     
        

data = data[data.Periodo != 'eliminar']
data = data.reset_index(drop=True)
        


"""-----------------------------------------------------------------------------------------"""
"""-------------------------------------FIN PERIODO-----------------------------------------"""
"""-----------------------------------------------------------------------------------------"""



"""---------------------------------------------------------------------------------------"""
"""-----------------------------------FECHA DE NACIMIENTO---------------------------------"""
"""---------------------------------------------------------------------------------------"""
for i in range(0,len(data.Fecha)):
    aux=data.Fecha[i]
    if(len(aux) >10):
        aux=aux[:10]
    if(len(aux) ==9):
        aux=aux[:3]+'0'+aux[-6:]
    if (len(aux) == 10 and aux[2] != '-'):
        aux =aux[:2]+'-'+aux[3:5]+'-'+aux[-4:]
    if(len(aux) == 8):
        if (aux[2] == '/' or aux[2] ==' '):
            if int(aux[-2:]) > 15:
                aux=aux[:2]+'-'+aux[3:5]+'-'+'19'+aux[-2:]
            else:
                aux=aux[:2]+'-'+aux[3:5]+'-'+'20'+aux[-2:]
        else:
            if(aux[2] != '-'):
                aux=aux[:2]+'-'+aux[2:4]+'-'+aux[-4:]
            else:
                if int(aux[-2:]) >15:
                    aux=aux[:6]+'20'+aux[-2:]
                else:
                    aux=aux[:6]+'19'+aux[-2:]
    if(len(aux) == 7):
        aux=aux[:2]+'-0'+aux[2]+'-'+aux[-4:]  
    data['Fecha'][i]=aux
    
"""---------------------------------------------------------------------------------------"""
"""--------------------------------FIN FECHA DE NACIMIENTO--------------------------------"""
"""---------------------------------------------------------------------------------------"""

"""---------------------------------------------------------------------------------------"""
"""---------------------------------------EDAD-SEMESTRE-----------------------------------"""
"""---------------------------------------------------------------------------------------"""
extraer_num('Edad',0)
extraer_num('Semestre',0)

for i in range(0,len(data)):
    aux = data['Sexo'][i]
    if aux == 'Femenino':
        data['Sexo'][i] = 1
    if aux == 'Masculino':
        data['Sexo'][i] = 0
"""---------------------------------------------------------------------------------------"""
"""-----------------------------------FIN EDAD-SEMESTRE-----------------------------------"""
"""---------------------------------------------------------------------------------------"""

"""-----------------------------------------------------------------------------------------"""
"""-------------------------------------ESTADO CIVIL----------------------------------------"""
"""-----------------------------------------------------------------------------------------"""

for i in range(0,len(data)):    
    aux=data['EstadoCivil'][i]
    patron= ("Soltero+\s*\w*\s*\w*")  
    if (re.match(patron,aux, re.IGNORECASE)):            
        data['EstadoCivil'][i] = 1
    patron= ("Casado+\s*\w*\s*\w*")  
    if (re.match(patron,aux, re.IGNORECASE)):
        data['EstadoCivil'][i] = 2
    patron= ("Viudo+\s*\w*\s*\w*")  
    if (re.match(patron,aux, re.IGNORECASE)):
        data['EstadoCivil'][i] = 3
    patron= ("Divorciado+\s*\w*\s*\w*")  
    if (re.match(patron,aux, re.IGNORECASE)):
        data['EstadoCivil'][i] = 4
        
        
    aux = data['EstadoCivil'][i]
    if (aux != 4 and aux != 1 and aux != 2 and aux !=3):
        data['EstadoCivil'][i] = 1
        
        
"""-----------------------------------------------------------------------aux------------------"""
"""----------------------------------FIN ESTADO CIVIL---------------------------------------"""
"""-----------------------------------------------------------------------------------------"""


"""-----------------------------------------------------------------------------------------"""
"""--------------------------------------ESCUELA--------------------------------------------"""
"""-----------------------------------------------------------------------------------------"""
for i in range(0,len(data)):
    aux=data['Escuela'][i]
    patron= ("Bio+\s*-*\s*\w*\s*") 
    if (re.match(patron,aux, re.IGNORECASE)):             
        data['Escuela'][i] = 1
    patron= ("En+\s*-*\s*\w*\s*") 
    if (re.match(patron,aux, re.IGNORECASE)): 
        data['Escuela'][i] = 0
        

"""-----------------------------------------------------------------------------------------"""
"""------------------------------------FIN ESCUELA------------------------------------------"""
"""-----------------------------------------------------------------------------------------""" 
    



"""-----------------------------------------------------------------------------------------"""
"""-------------------------------------MODALIDAD-------------------------------------------"""
"""-----------------------------------------------------------------------------------------"""
for i in range(0,len(data)):
    aux = data['Modalidad_de_Ingreso'][i]
    patron = ("[asignado]+\s*\w*\s*[OPSU]+")
    if (re.match(patron,aux, re.IGNORECASE)):       
        data['Modalidad_de_Ingreso'][i] = 1
    patron = ("prueba+\s*\w*[interna]+[y/o]*\s*\w*[prope]+")
    if (re.match(patron,aux, re.IGNORECASE)):       
        data['Modalidad_de_Ingreso'][i] = 2
    patron = ("convenios+\s*interno+\w*\s*[(]*\w*\s*[)]*")
    if (re.match(patron,aux, re.IGNORECASE)):       
        data['Modalidad_de_Ingreso'][i] = 3
    patron = ("convenios+\s*\w*Interinstitucionales+\s*[(]*\w*\s*\w*\s*\w*\s*[)]*")
    if (re.match(patron,aux, re.IGNORECASE)):       
        data['Modalidad_de_Ingreso'][i] = 4
        
"""
asignado por OPSU = 1
prueba interna o propedeutico = 2
convenio interno = 3
convenios interinstitucionales = 4
"""

"""-----------------------------------------------------------------------------------------"""
"""-----------------------------------FIN MODALIDAD-----------------------------------------"""
"""-----------------------------------------------------------------------------------------"""


    
    
  
"""---------------------------------------------------------------------------------------"""
"""---------------------------------PROMEDIO-EFICIENCIA------.----------------------------"""
"""---------------------------------------------------------------------------------------"""

for i in range(0,len(data)):
    aux = data['Promedio_Aprobado'][i]
    if aux >10000:
        aux=aux/1000
    if aux > 100 and aux < 1000:
        aux = aux / 10
    if aux < 10:
        data['Promedio_Aprobado'][i] = -1
    i,aux
    data['Promedio_Aprobado'][i]=aux
    
data = data[data.Promedio_Aprobado != -1]
data = data.reset_index(drop=True)
        
for i in range(0,len(data)):
    aux=data.Eficiencia[i]
    if (aux>1000 and aux <= 10000):
        aux=float(aux/10000)
    if (aux >10000 and aux <= 100000):
        aux=float(aux/1000000)
    if (aux>100 and aux <= 1000):
        aux=float(aux/1000)
    if (aux>10 and aux <= 100):
        aux=float(aux/100) 
    if (aux == 1):
        data['Motivo_Reprob'][i] = float('NaN')
    data['Eficiencia'][i] = aux

"""---------------------------------------------------------------------------------------"""
"""-------------------------------FIN-PROMEDIO-EFICIENCIA---------------------------------"""
"""---------------------------------------------------------------------------------------"""

  
"""-----------------------------------------------------------------------------------------"""
"""----------------------------------#TESIS/PASANTIAS---------------------------------------"""
"""-----------------------------------------------------------------------------------------"""
data['Veces_Inscritas_Tesis_Pasantias'] = data['Veces_Inscritas_Tesis_Pasantias'].fillna(0)
for i in range(0,len(data)):
    aux = data['Veces_Inscritas_Tesis_Pasantias'][i]
    if (aux != 0 and aux != 1 and aux != 2 and aux != 3):
        patron = ("primera+\s*\w*\s*vez*")
        if (re.match(patron,aux, re.IGNORECASE)):       
            data['Veces_Inscritas_Tesis_Pasantias'][i] = 1
        patron = ("segunda+\s*\w*\s*vez*")
        if (re.match(patron,aux, re.IGNORECASE)):       
            data['Veces_Inscritas_Tesis_Pasantias'][i] = 2
        patron = ("M\xe1s+\s*\w*\s*de*\s*\w*dos*")
        if (re.match(patron,aux, re.IGNORECASE)):       
            data['Veces_Inscritas_Tesis_Pasantias'][i] = 3
"""-----------------------------------------------------------------------------------------"""
"""-------------------------------FIN #TESIS/PASANTIAS--------------------------------------"""
"""-----------------------------------------------------------------------------------------"""

"""---------------------------------------------------------------------------------------"""
"""------------------------------MATERIAS INSCRITAS/APROBADAS-----------------------------"""
"""---------------------------------------------------------------------------------------"""
extraer_num('Aprobadas',0)
for i in range(0,len(data)):
    if (data['InscritasAnterior'][i] != data['Aprobadas'][i] + data['Retiradas'][i] + data['Reprobadas'][i]):
        data['Aprobadas'][i] = -1
        data['Reprobadas'][i] = -1
        data['Retiradas'][i] = -1
             
data = data[data.Aprobadas != -1]
data = data.reset_index(drop=True)
"""---------------------------------------------------------------------------------------"""
"""----------------------------FIN MATERIAS INSCRITAS/APROBADAS-----------------------------"""
"""---------------------------------------------------------------------------------------"""






"""---------------------------------------------------------------------------------------"""
"""------------------------------------COLUMNAS SI/NO-------------------------------------"""
"""---------------------------------------------------------------------------------------"""
xcolumns('X_Actividad_Ingreso')
xcolumns('X_CambioDireccion') 
xcolumns('X_Tesis-Pasantias')




"""---------------------------------------------------------------------------------------"""
"""--------------------------------FIN COLUMNAS SI/NO-------------------------------------"""
"""---------------------------------------------------------------------------------------"""




"""---------------------------------------------------------------------------------------"""
"""--------------------------------INGRESOS ESTUDIANTES-----------------------------------"""
"""---------------------------------------------------------------------------------------"""
my_imputer('AporteAmigos','mean','NaN')
my_imputer('AporteResp','mean','NaN')

for i in range(0,len(data)):
    if (data['X_Actividad_Ingreso'][i] == 0):
        data['Ingreso_Actividad'][i] =0

for i in range(0,len(data)):
    act=data['Ingreso_Actividad'][i]
    beca=data['MontoBeca'][i]
    resp=data['AporteResp'][i]
    amigos = data['AporteAmigos'][i]
    total = data['IngresoTotal'][i]
    aux = act+beca+resp+amigos
    if aux != total:
        total = aux
        data['IngresoTotal'][i] = total
        
"""---------------------------------------------------------------------------------------"""
"""-----------------------------FIN INGRESOS ESTUDIANTES----------------------------------"""
"""---------------------------------------------------------------------------------------"""  


    


"""---------------------------------------------------------------------------------------"""
"""--------------------------------EGRESOS ESTUDIANTES------------------------------------"""
"""---------------------------------------------------------------------------------------"""



my_imputer('Alimentacion','median','NaN')
my_imputer('Transporte','mean','NaN')
my_imputer('Odontologicos','median','NaN')
my_imputer('GastosPersonales','mean','NaN')
my_imputer('Salud','mean','NaN')
my_imputer('Materiales','median','NaN')
my_imputer('Recreacion','median','NaN')
my_imputer('OtrosGastos','mean','NaN')



data['Monto_Mensual_Residencia'] = data['Monto_Mensual_Residencia'].fillna('0')
data['Residencia'] = data['Residencia'].fillna(0)
extraer_num('Monto_Mensual_Residencia',1)
"""comparo los 2 valores de gasto en residencia/alquiler y tomo el mayor de los 2"""

for i in range(0,len(data)):
    aux = data['Monto_Mensual_Residencia'][i]
    aux2 = data['Residencia'][i]
    if aux > aux2:
        data['Residencia'][i] = aux
    if aux2 > aux:
        data['Monto_Mensual_Residencia'][i] = aux2


for i in range(0,len(data)):
    alim = data['Alimentacion'][i]
    trans = data['Transporte'][i]
    salud = data['Salud'][i]
    odont = data['Odontologicos'][i]
    personal = data['GastosPersonales'][i]
    resid = data['Residencia'][i]
    mater = data['Materiales'][i] 
    recreacion = data['Recreacion'][i]
    otrosg =  data['OtrosGastos'][i]
    aux = alim + trans + salud + odont + personal + resid + mater + recreacion + otrosg
    total = data['TotalEgreso'][i]
    if aux < total:
        otrosg = otrosg + (total-aux)
        data['OtrosGastos'][i] = otrosg 
        aux = alim + trans + salud + odont + personal + resid + mater + recreacion + otrosg
    if aux > total:
        total = aux
        data['TotalEgreso'][i] = total
        
"""------------------------------------------------------------------------------------------"""
"""-------------------------------FIN EGRESOS ESTUDIANTES------------------------------------"""
"""------------------------------------------------------------------------------------------"""
            




"""---------------------------------------------------------------------------------------"""
"""--------------------------------INGRESOS RESPONSABLE-----------------------------------"""
"""---------------------------------------------------------------------------------------"""
extraer_num('Total_Ingreso_Responsable',1)
extraer_num('IngresoDelResp',1)
data['OtrosIngresosResp'] = data['OtrosIngresosResp'].fillna(u'0')
extraer_num('OtrosIngresosResp',0)  

for i in range(0,len(data)):
    otros = data['OtrosIngresosResp'][i]
    ingreso = data['IngresoDelResp'][i]
    total = data['Total_Ingreso_Responsable'][i]
    aux = otros + ingreso
    if aux < total:
        otros += total-aux
        data['OtrosIngresosResp'][i] = otros
    elif aux > total:
        data['Total_Ingreso_Responsable'][i] = aux
        

"""---------------------------------------------------------------------------------------"""
"""------------------------------FIN INGRESOS RESPONSABLE---------------------------------"""
"""---------------------------------------------------------------------------------------"""



"""---------------------------------------------------------------------------------------"""
"""------------------------------EGRESOS RESPONSABLE--------------------------------------"""
"""---------------------------------------------------------------------------------------"""
extraer_num('AlimentoR',1)
extraer_num('ViviendaR',1)
extraer_num('TransporteR',1)
extraer_num('SaludR',1)
extraer_num('OdontologR',1)
extraer_num('EducativosR',1)
extraer_num('ServiciosR',1) 
extraer_num('CondominioR',1)
extraer_num('OtrosGastosR',1)
extraer_num('TotalEgresoR',1)


my_imputer('AlimentoR','median',0)
my_imputer('ViviendaR','mean','NaN')
my_imputer('TransporteR','median','NaN')
my_imputer('SaludR','median','NaN')
my_imputer('OdontologR','mean','NaN')
my_imputer('EducativosR','mean','NaN')
my_imputer('ServiciosR','mean','NaN')
my_imputer('CondominioR','mean','NaN')
my_imputer('OtrosGastosR','median','NaN')


for i in range(0,len(data)):
    alim = data['AlimentoR'][i]
    vivienda = data['ViviendaR'][i]
    trans = data['TransporteR'][i]
    salud = data['SaludR'][i]
    odont = data['OdontologR'][i]
    educ = data['EducativosR'][i]
    serv = data['ServiciosR'][i]
    condom = data['CondominioR'][i]
    otros =  data['OtrosGastosR'][i]
    aux = alim + vivienda + trans + salud + odont + educ + serv + condom + otros
    total = data['TotalEgresoR'][i]
    if aux < total:
        otros = otros + (total-aux)
        data['OtrosGastosR'][i] = otros
        aux = alim + vivienda + trans + salud + odont + educ + serv + condom + otros
    else:
        total = aux


            
"""---------------------------------------------------------------------------------------"""
"""----------------------------FIN EGRESOS RESPONSABLE------------------------------------"""
"""---------------------------------------------------------------------------------------"""
    
    
    
    
"""--------------------------------------------------------------------------------------"""
"""-----------------------------------ELIMINAR COLUMNAS----------------------------------"""
"""--------------------------------------------------------------------------------------""" 
del data['OtrosIngresosResp']
del data['IngresoDelResp']

del data['TotalEgreso']
del data['IngresoTotal']
del data['Razon_Cambio_Direccion']
del data['TotalEgresoR'] ##totales egreso responsable
del data['Tipo_Actividad_y_Frecuencia']
del data['col0']
del data['X_Matrimonio']

del data['Monto_Mensual_Residencia']


"""--------------------------------------------------------------------------------------"""
"""-------------------------------FIN ELIMINAR COLUMNAS----------------------------------"""
"""--------------------------------------------------------------------------------------"""     
    
data.to_csv('minable.csv',encoding='utf-8',index=0)

 












