import os
import sqlite3
from datetime import datetime
from colorama import Cursor
import time

"""
datosParaIngresarCancion[0] = idCancion
datosParaIngresarCancion[1] = idUsuario
datosParaIngresarCancion[2] = IdPlayList
datosParaIngresarCancion[3] = NombreCancion
datosParaIngresarCancion[4] = Enlace
datosParaIngresarCancion[5] = Fecha
datosParaIngresarCancion[6] = Duracion
datosParaIngresarCancion[7] = Coincidencia
"""
datosParaIngresarCancion = [0, 0, 0, "", "", "", "", ""]
canciones = ["", "", "", "", "", "", "", "", "", ""]
busquedaDeCanciones = ["", "", "", "", ""]
playListVer = 0
minutosConvertidos = 0
archivosCreados = False

def obtenerFechaActual():
    return str(datetime.today().strftime('%d/%m/%Y'))
def obtenerLaUltimaCancionIndex():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT IdCancion FROM canciones order by IdCancion desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return int(resultado[0][0])+1

def obtenerLaCantidadDeMinutos():
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = ("SELECT SUM(Duracion) FROM canciones")
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    # Obtengo la conversion a minutos y segundos
    minutosTotales = int(int(resultado[0][0])/60)
    segundosTotales = int(resultado[0][0]) - minutosTotales*60
    return str(str(minutosTotales)+":"+str(segundosTotales))       
def obtenerLaCantidadDePlayList():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT IdPlayList FROM canciones order by IdPlayList desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return int(resultado[0][0])+2
def obtenerCantidadDeCancionesCero():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 1 and Duracion <= 59"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesUno():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 60 and Duracion <= 119"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesDos():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 120 and Duracion <= 179"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesTres():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 180 and Duracion <= 239"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesCuatro():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 240 and Duracion <= 299"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesCinco():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 300 and Duracion <= 359"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesSeis():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 360 and Duracion <= 419"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesSiete():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 420 and Duracion <= 479"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesOcho():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 480 and Duracion <= 539"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def obtenerCantidadDeCancionesNueve():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT count(*) FROM canciones WHERE Duracion >= 540 and Duracion <= 599"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]
def ingresarCancion():
    datosParaIngresarCancion[0] = obtenerLaUltimaCancionIndex()
    datosParaIngresarCancion[5] = obtenerFechaActual()
    segundos = convertirMinutosSegundo(datosParaIngresarCancion[6])
    datosParaIngresarCancion[6] = segundos
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "INSERT INTO canciones(IdCancion,IdUsuario,IdPlayList,NombreCancion,Enlace,Fecha,Duracion,Coincidencia) VALUES (?,?,?,?,?,?,?,?)"
    valores = (datosParaIngresarCancion[0], datosParaIngresarCancion[1],
               datosParaIngresarCancion[2], datosParaIngresarCancion[3], datosParaIngresarCancion[4], datosParaIngresarCancion[5], datosParaIngresarCancion[6], datosParaIngresarCancion[7])
    cursor.execute(sentencia, valores)
    bd.commit()
def obtenerLasCantidadDeCanciones():
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor=bd.cursor()
    sentencia = "SELECT IdCancion FROM canciones order by IdCancion desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return int(resultado[0][0])+1
def convertirMinutosSegundo(minutos):
    return int(int(minutos[0])*60 + int(str(minutos[2])+str(minutos[3])))
def buscarCancion(nombre):
    global busquedaDeCanciones
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor=bd.cursor()
    sentencia = "select NombreCancion from canciones where NombreCancion like '%"+str(nombre)+"%'"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    busquedaDeCanciones[0] = ""
    busquedaDeCanciones[1] = ""
    busquedaDeCanciones[2] = ""
    busquedaDeCanciones[3] = ""
    busquedaDeCanciones[4] = ""
    if len(resultado) <= 5:
        for i in range(len(resultado)):
            busquedaDeCanciones[i] = resultado[i][0]
    else:
        for i in range(5):
            busquedaDeCanciones[i] = resultado[i][0]
def crearRespaldo():
    try:
        archivo = open("C:/PLSR_Datos/respaldoCanciones.txt", "w")
        archivo.close()
    except:
        archivosCreados = True

    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "SELECT * FROM canciones"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    # Creamos un archivo de texto con l ainformacion de las tablas
    archivo = open('C:/PLSR_Datos/respaldoCanciones.txt', 'w', encoding="utf-8")
    for i in range(len(resultado)-1):
        archivo.write(str(resultado[i]))
        archivo.write('\n')
    archivo.close()
def crearTablas():
    os.mkdir('C:/PLSR_Datos')
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS canciones(IdCancion INT(255) ,IdUsuario TINYINT(255),IdPlayList TINYINT(255),NombreCancion CHAR(255),Enlace TEXT,Fecha CHAR(25),Duracion INT(255),Coincidencia CHAR(10),PRIMARY KEY (IdCancion))")
def ingresarTodosLasCanciones():
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    archivo = open("respaldoCanciones.txt", "r", encoding="utf-8")
    for i in range(40):
        sentencia = "INSERT INTO canciones(IdCancion,IdUsuario,IdPlayList,NombreCancion,Enlace,Fecha,Duracion,Coincidencia) VALUES "+str(archivo.readline()+";")  
        cursor.execute(sentencia)  
        bd.commit()
    archivo.close()  

def buscarCancionConsola(nombre):
    global busquedaDeCanciones
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor=bd.cursor()
    sentencia = "select IdCancion,IdUsuario,IdPlayList,NombreCancion,Fecha from canciones where NombreCancion like '%"+str(nombre)+"%'"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado
def obtenerElNombreDeLasCanciones(numeroDePlayList):
    global canciones
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = str(
        "SELECT NombreCancion FROM canciones WHERE IdPlayList = '"+str(numeroDePlayList)+"'")
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    canciones = ["", "", "", "", "", "", "", "", "", ""]
    for i in range(len(resultado)):
        canciones[i] = resultado[i][0]
    return canciones



def obtenerElURL(nombreCancion):
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = str("SELECT Enlace FROM canciones WHERE NombreCancion = '"+str(nombreCancion)+"'")
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]

"""
def cada10Canciones():
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "select IdCancion, IdUsuario, NombreCancion, Fecha from canciones where IdCancion IN(0, 10, 20, 30, 40, 50, 60, 70, 80, 90,100,110,120)"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado
"""


def cada10Canciones():
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    sentencia = "select IdCancion, IdUsuario, NombreCancion, Fecha from canciones where IdCancion IN(0, 9, 19, 29, 39, 49, 59, 69, 79, 89,99,109,119,129,139,149,159,169,179,189)"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado

def contarCancionesPorPlayList(numeroplayList):
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    # SELECT COUNT(ProductID) AS NumberOfProducts FROM Products;
    sentencia = "select count(IdPlayList) from canciones where IdPlayList = "+str(numeroplayList)
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]


def contarCancionesPorUsuario(numeroUsuario):
    # CONECTAR LA BASE DE DATOS
    bd = sqlite3.connect("C:/PLSR_Datos/bdPlayList")
    cursor = bd.cursor()
    # SELECT COUNT(ProductID) AS NumberOfProducts FROM Products;
    sentencia = "select count(IdUsuario) from canciones where IdUsuario = " + \
        str(numeroUsuario)
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado[0][0]


crearRespaldo()
