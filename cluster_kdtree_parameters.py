# -*- coding: Latin-1 -*-
"""
Created on Sun Mar 25 17:52:37 2018

@author: solis
parámetros del script
"""

"""base de dato con las medidas GPS"""
DB = r"""\\intsrv1008\SGD\00_Proyectos\42141\100_TRABAJO\100_10_DOC_COMUN\
    CHS_SUBSIDENCIA\VEGA_MEDIA_GPS_2015-18.accdb"""
# casa
DB = r"""E:\BBDD\VEGA_MEDIA_GPS_2015-18.accdb"""

"""Cluster seleccionados"""
SELECT_PS = """SELECT ID, FECHA, NOMBRE, Z, X, Y
              FROM MEDIDAS_TODAS
              WHERE FECHA>=#1/31/2018# And FECHA<#2/1/2018#"""

"""Todas las medidas GPS"""
SELECT_D = """SELECT ID, FECHA, NOMBRE, Z, X, Y
              FROM MEDIDAS_TODAS
              ORDER BY FECHA"""

"""distancia máxima entre los puntos que forman el kdtree y los puntos
   con los que se hace el query"""
DISTANCE = 0.5

"""Tamaño del bufer para escribir el fichero de resultados"""
BUFSIZE = 1024000

"""directorio de resultados"""
DIR_OUT = r"""\\intsrv1008\SGD\00_Proyectos\42141\100_TRABAJO\100_10_DOC_COMUN\
    CHS_SUBSIDENCIA"""
# casa
DIR_OUT = r"""E:\WORK\CHS\VM_GPS"""

"""Nombre delfichero de resultados"""
F_OUT = 'GPS_clasiffied.txt'
