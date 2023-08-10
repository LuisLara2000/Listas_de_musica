# librerias
import cv2 
from datetime import datetime
from datetime import date
from datetime import timedelta

from os import system
from re import I, X
from time import sleep, time
import administracionPLSR_SQLite as bdPlay
from colorama import Cursor
from colorama import Back, Fore, init
#from bs4 import BeautifulSoup
#import requests
import webbrowser # para abrir paginas web
import pyautogui # para tomar ss
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# codigo gestor de la base de datos
import administracionPLSR_SQLite as bdPlay

# variables globales
salir = False
opcionMenu = 0
nivelMenu = 0
nombreCanción = ""
numeroDePlayListActual = 0


def leerPlayListActual():
    archivo = open("numeroPlayListActual.txt", mode="r")
    return archivo.read()
def detectarQueYaPasoUnaSemana():
    # Leo la ultima fecha de la play list 
    fechaUltimaPLSR = open("ultimaPLSR.txt",mode="r")
    textoViernesPLSR = fechaUltimaPLSR.read()
    fechaUltimaPLSR.close()
    # El texto lo convierto en un objeto "date"
    viernesPLSR = datetime.strptime(textoViernesPLSR, '%Y-%m-%d').date()
    # Obtengo la fecha actual
    hoy = date.today()
    
    # Comparo si hoy ya supera la fecha de la play list ultima
    if hoy >= viernesPLSR:
        # Obtengo el numero de play list anterior y sumo 1
        numero = int(leerPlayListActual())
        numero = numero + 1 
        # Guardo ese numero
        archivo = open("numeroPlayListActual.txt", mode="w")
        archivo.write(str(numero))
        archivo.close()
        # A la fecha de la ultima play list le sumo 7 dias para obtner la decha proxima
        viernesPLSR = viernesPLSR + timedelta(days=7)
        # Guardo la fecha
        fechaUltimaPLSR = open("ultimaPLSR.txt", mode="w")
        fechaUltimaPLSR.write(str(viernesPLSR))
        fechaUltimaPLSR.close()
def logo():
    print(""" 
              BUSCADOR DE CANCIONES

    PLAY LIST #"""+str(leerPlayListActual()) + """
    ██████  ██████  ██  ██  ██████  ████
    ██▒▒▒▒  ██▒▒██  ██  ██  ██▒▒██  ██▒▒██
    ██████  ██████  ██  ██  ██████  ██░░██
    ▒▒▒▒██  ▒▒▒▒██  ██  ██  ██▒▒██  ██  ██
    ██████  ░░░░██  ██████  ██░░██  ████▒▒
    ▒▒▒▒▒▒      ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒▒▒░░
    ░░░░░░      ░░  ░░░░░░  ░░  ░░  ░░░░
                               RATONAZTICO
                
               VERSION CONSOLA 1.2
                                           """)
def logo2():
    print("")

    print(""" 
            INGRESANDO CANCIONES DE LA 

    PLAY LIST #"""+str(leerPlayListActual()) + """
    ██████  ██████  ██  ██  ██████  ████
    ██▒▒▒▒  ██▒▒██  ██  ██  ██▒▒██  ██▒▒██
    ██████  ██████  ██  ██  ██████  ██░░██
    ▒▒▒▒██  ▒▒▒▒██  ██  ██  ██▒▒██  ██  ██
    ██████  ░░░░██  ██████  ██░░██  ████▒▒
    ▒▒▒▒▒▒      ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒▒▒░░
    ░░░░░░      ░░  ░░░░░░  ░░  ░░  ░░░░
                               RATONAZTICO
                                           """)
def logoEnPlayList(numero):
    print(""" 
    PLAY LIST #"""+str(numero)+"""
    ██████  ██████  ██  ██  ██████  ████
    ██▒▒▒▒  ██▒▒██  ██  ██  ██▒▒██  ██▒▒██
    ██████  ██████  ██  ██  ██████  ██░░██
    ▒▒▒▒██  ▒▒▒▒██  ██  ██  ██▒▒██  ██  ██
    ██████  ░░░░██  ██████  ██░░██  ████▒▒
    ▒▒▒▒▒▒      ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒▒▒░░
    ░░░░░░      ░░  ░░░░░░  ░░  ░░  ░░░░
                               RATONAZTICO
                               """)
def validarOpciones():
    global nivelMenu
    global salir
    if(opcionMenu == 5):
        salir = True
    elif(opcionMenu == 1):
        nivelMenu = 1
    elif(opcionMenu == 2):   
        nivelMenu = 2
    elif(opcionMenu == 3):
        nivelMenu = 3
    elif(opcionMenu == 4):
        nivelMenu = 4
    elif(opcionMenu == 0):
        nivelMenu = 0
def imprimirMenuPrincipal():
    system("cls")
    logo()
    print("")
    print("                 [1] BUSCAR       [1]")
    print("                 [2] PLAY LISTs   [2]")
    print("                 [3] ESTADISTICAS [3]")
    print("                 [4] INGRESAR     [4]")
    print("                 [5] SALIR        [5]")
    print("")
    print("")
def imprimirBusqueda(nombreCanción):
    system("cls")
    lista = []
    lista = bdPlay.buscarCancionConsola(nombreCanción)
    
    if(len(lista) == 0):
        print("NO SE ENCONTRO NINGUNA CANCION")
        print("")
        print("")
        print("")
        input("")
    else:
        # SE IMPRIME LA CABECERA DE LA TABLA #
        print(Back.RED + " ID".center(5, ' '), end=" ")
        print(Back.RESET+" ", end=" ")
        print(Back.RED + "NOMBRE".center(100, ' '), end=" ")
        print(Back.RESET+" ", end=" ")
        print(Back.RED + " USUARIO".center(8, ' '), end=" ")
        print(Back.RESET+" ", end=" ")
        print(Back.RED + " PLAY LIST".center(10, ' '), end=" ")
        print(Back.RESET+" ", end=" ")
        print(Back.RED + "FECHA".center(14, ' '))
        print(Back.RESET+"")
        # SE IMPRIME LOS ELEMENTOS DE LA TABLA #
        # 0 = ID
        # 1 = ID_USUARIO
        # 2 = ID_PLAYLIST
        # 3 = NOMBRE_CANCION
        # 4 = FECHA 
        bandera = 1;     
        for cancion in lista:
            if(bandera == 0): 
                print(Back.BLACK + Fore.WHITE + str(cancion[0]).center(5, ' '), end=" ")
                print(Back.RESET+" ", end=" ")
                print(Back.BLACK + str(cancion[3]).center(100, ' '), end=" ")
                print(Back.RESET+" ", end=" ")
                print(Back.BLACK + str(cancion[1]).center(8, ' '), end=" ")
                print(Back.RESET+" ", end=" ")
                print(Back.BLACK + str(cancion[2]).center(10, ' '), end=" ")
                print(Back.RESET+" ", end=" ")
                print(Back.BLACK + str(cancion[4]).center(14, ' '), end=" ")
                print(Back.RESET+Fore.RESET+"")
                bandera = 1
            elif(bandera == 1):
                
                print(Back.BLUE + str(cancion[0]).center(5,' '), end=" ")
                print(Back.RESET+" ", end=" ")
                print(Back.BLUE + str(cancion[3]).center(100, ' '), end=" ")
                print(Back.RESET+" ", end=" ")
                print(Back.BLUE + str(cancion[1]).center(8, ' '), end=" ")
                print(Back.RESET+" ", end=" ")
                print(Back.BLUE + str(cancion[2]).center(10, ' '), end=" ")
                print(Back.RESET+" ", end=" ")
                print(Back.BLUE + str(cancion[4]).center(14, ' '), end=" ")
                print(Back.RESET+Fore.RESET+"")
                bandera = 0
               
        print(Back.RESET+" ")
        print("")
        print(Back.RED+"RESULTADOS DE LA BUSQUEDA".center(150, ' '))
        print(Back.RED+" ".center(150, ' '))
        print(Back.RESET+Fore.RESET+"")
        print(str("BUSCASTE: " + nombreCanción).center(75, ' '),end=" ")
        print(str("SIMILITUDES: " + str(len(lista))).center(75, ' '), end=" ")
        input("")   
def imprimirMenuBusqueda():
    system("cls")
    print("[ INGRESE EL NOMBRE O PARTE DEL NOMBRE DE LA CANCION A BUSCAR ]")
    print("[ SI DESEA VOLVER AL MENU PRINCIPAL INGRESE EL NUMERO 0 ]")
    print("")
    nombreCanción = input("SU CANCION: ")
    if(nombreCanción == "0"):
        global nivelMenu
        nivelMenu = 0
    else:
        imprimirBusqueda(nombreCanción)
def verPlayList(numeroDePlayListActual):
    listaCanciones = bdPlay.obtenerElNombreDeLasCanciones(numeroDePlayListActual)
    x = 0
    for i in listaCanciones:
        if(i!=""):
            print(str(x)+" "+str(i))
            x+=1
"""
def posicionRaton():
    xd = True
    while xd == True:
        if str(input())=="p":
            print(pyautogui.position())
posicionRaton()
"""
def principal(): 
    detectarQueYaPasoUnaSemana()
    while(salir==False):
        if(nivelMenu == 0):
            imprimirMenuPrincipal()
            global opcionMenu
            opcionMenu = int(input(""))
            validarOpciones()
        elif(nivelMenu == 1):
            imprimirMenuBusqueda()
            input()
            opcionMenu = 0
            validarOpciones()
        elif(nivelMenu == 2):
            global numeroDePlayListActual
            system("cls")
            logoEnPlayList(numeroDePlayListActual)
            print(" ")
            verPlayList(numeroDePlayListActual) 
            print(" ")
            print("OPCIONES ")
            print("ESCUCHAR   [#]")
            print("AVANZAR    [a] ")
            print("RETROCEDER [d]")
            print("SALIR      [s]")
            print(" ")
            opcion = str(input())

            if(opcion == "a"):
                numeroDePlayListActual -= 1
                if(numeroDePlayListActual < -1):
                    numeroDePlayListActual = int(leerPlayListActual())
            elif(opcion == "d"):
                numeroDePlayListActual += 1
                if(numeroDePlayListActual > int(leerPlayListActual())):
                    numeroDePlayListActual = -1
            elif(opcion == "s"):
                opcionMenu = 0
                validarOpciones()
            else:
                listaCanciones = bdPlay.obtenerElNombreDeLasCanciones(numeroDePlayListActual)
                url = bdPlay.obtenerElURL(listaCanciones[int(opcion)])
                webbrowser.open_new(url)
        elif(nivelMenu == 3):
            system("cls")
            lista = bdPlay.cada10Canciones()
            print(Back.RED + " ID".center(5, ' '), end=" ")
            print(Back.RESET+" ", end=" ")
            print(Back.RED + "NOMBRE".center(100, ' '), end=" ")
            print(Back.RESET+" ", end=" ")
            print(Back.RED + " USUARIO".center(8, ' '), end=" ")
            print(Back.RESET+" ", end=" ")
            print(Back.RED + "FECHA".center(14, ' '))
            print(Back.RESET+"")

            bandera = 0
            for cancion in lista:
                nombre = ""
                if(cancion[1] == 1):
                    nombre = "LUJA"
                elif(cancion[1] == 2):
                    nombre = "JAZIEL"
                else:
                    nombre = "ROBERTO"

                if bandera == 1:
                    print(Back.BLACK + Fore.WHITE + str(cancion[0]).center(5, ' '), end=" ")
                    print(Back.RESET+" ", end=" ")
                    print(Back.BLACK + str(cancion[2]).center(100, ' '), end=" ")
                    print(Back.RESET+" ", end=" ")
                    print(Back.BLACK + str(nombre).center(9, ' '), end=" ")
                    print(Back.RESET+" ", end=" ")
                    print(Back.BLACK + str(cancion[3]).center(14, ' '), end=" ")
                    print(Back.RESET+" ", end=" ")
                    print(Back.RESET+Fore.RESET+"")
                    bandera = 0
                elif bandera == 0:
                    print(Back.BLUE + str(cancion[0]).center(5, ' '), end=" ")
                    print(Back.RESET+" ", end=" ")
                    print(Back.BLUE + str(cancion[2]).center(100, ' '), end=" ")
                    print(Back.RESET+" ", end=" ")
                    print(Back.BLUE + str(nombre).center(9, ' '), end=" ")
                    print(Back.RESET+" ", end=" ")
                    print(Back.BLUE + str(cancion[3]).center(14, ' '), end=" ")
                    print(Back.RESET+" ", end=" ")
                    print(Back.RESET+Fore.RESET+"")
                    bandera = 1
                    
            print("\n\n")
            ultima = int(leerPlayListActual())
            for i in range(-1, ultima+1):
                print("PLSR# "+str(i)+" -> "+str(bdPlay.contarCancionesPorPlayList(i)))
            print("\n\n")
            lista = [0,0,0]
            for x in range(1,4):
                lista[x-1] = bdPlay.contarCancionesPorUsuario(x)
                
            print("LUJA -> "+str(lista[0]))
            print("JAZIEL -> "+str(lista[1]))
            print("ROBERTO -> "+str(lista[2]))
            input()
            opcionMenu = 0
            validarOpciones()
        elif(nivelMenu == 4):
            system("cls")
            #logo2()
            print("INGRESE LA CANTIDAD DE CANCIONES: ",end="")
            cantidadCanciones = int(input())
            listaEnlaces = []
            listaNombres = []

            for x in range(cantidadCanciones):
                listaEnlaces.append("")
                listaNombres.append("")
                
            for i in range(cantidadCanciones):
                system("cls")
                #logo2()
                print("DATOS CANCION #"+str(i))
                print("INGRESE EL NOMBRE DEL INTEGRANTE: ", end="")
                listaNombres[i] = str(input())
                print("INGRESE EL ENLACE DE LA CANCION: ", end="")
                listaEnlaces[i] = str(input())
                sleep(1)

            system("cls")
            #logo2()
            print("RESULTADOS")

            for w in range(cantidadCanciones):
                # la pagina debe estar al 90% de zoom
                # la barra de tareas debe estar abajo, NO A LOS LADOS
                # Se abre la pagina 
                webbrowser.open(listaEnlaces[w], new=2, autoraise=True)
                # Espero a que se carge
                sleep(7)
                # Muevo el raton a donde se reproduce el video
                pyautogui.moveTo(320,360,1)
                pyautogui.click()
                sleep(1)
                # Primero tomo captura del nombre, por facilidad ya que al presionar "t" se mueve la pagina
                nombre = pyautogui.screenshot(region=(60, 610, 840, 42))
                nombre.save("nombre.png")
                sleep(1)
                # presiono "t" para hacer el modo teatro en el video, es mas facil obtener la duracion del video asi
                pyautogui.press("t")
                sleep(1)
                # Tomo  la duracion
                duracion = pyautogui.screenshot(region=(172, 590, 40, 30))
                # Guardo la captura
                duracion.save("duracion.png")
                sleep(1)
                # Solo filtro el nombre, algunos videos tienen hastags que no deseo leer
                imagenNombre = cv2.imread("nombre.png")
                filtroNombre = cv2.inRange(imagenNombre, (100, 100, 100), (255, 255, 255))
                cv2.imwrite("nombreFiltrado.png", filtroNombre)
                sleep(2)
                # Las capturas las proceso para que solo aparescan el texto que necesito (omitimos esto)
                #imagenNombre = cv2.imread("nombre.png")
                #imagenDuracion = cv2.imread("duracion.png")
                
                # Filtro para ambas imagenes (omitimos el filtro)
                #filtroNombre = cv2.inRange(imagenNombre, (100, 100, 100), (255, 255, 255))
                #filtroDuracion = cv2.inRange(imagenDuracion, (100, 100, 100), (255, 255, 255))
                
                # Guardo las nuevas imagenes (omitimos guardar las imagenes con el filtro)
                #cv2.imwrite("duracionFiltrado.png", filtroDuracion)
                #cv2.imwrite("nombreFiltrado.png", filtroNombre)
                # Las imagenes filtradas las comvierto en texto

                nom = pytesseract.image_to_string(Image.open('nombreFiltrado.png'))
                dur = pytesseract.image_to_string(Image.open('duracion.png'))
                sleep(1)
                # Dejo la pagina como estaba incialmente
                pyautogui.press("t")

                # Limpio el texto
                nombreLimpio = ""
                tiempo = ""
                
                # Limpio el texto "nombre"
                for i in range(len(nom)-2):
                    nombreLimpio += nom[i]
                
                # valido que el tiempo tenga un formato
                if dur.count(":") == 1: # formato correcto
                    tiempo = str(dur[0])+str(dur[1])+str(dur[2])+str(dur[3])
                    if (ord(dur[0]) >= 48 and ord(dur[0]) <= 57) and (ord(dur[2]) >= 48 and ord(dur[2]) <= 57) and (ord(dur[3]) >= 48 and ord(dur[3]) <= 57):
                        tiempo = tiempo
                    else:
                        tiempo = str("0:01")
                else:
                    tiempo = str(dur[0])+str(":")+str(dur[1])+str(dur[2])
                    if (ord(dur[0]) >= 48 and ord(dur[0]) <= 57) and (ord(dur[1]) >= 48 and ord(dur[1]) <= 57) and (ord(dur[2]) >= 48 and ord(dur[2]) <= 57):
                        tiempo = tiempo
                    else:
                        tiempo = str("0:01")

                # 0 - Nombre usuario
                # 1 - PlayList
                # 2 - NombreCancion
                # 3 - Enlace
                # 4(6) - Duracion
                # 5 - Coincidencia
                # traducimos el nombre del usuario
                if(listaNombres[w]=="l"):
                    bdPlay.datosParaIngresarCancion[1] = "1"
                    listaNombres[w] = "LUJA"
                elif(listaNombres[w] == "j"):
                    bdPlay.datosParaIngresarCancion[1] = "2"
                    listaNombres[w] = "JAZIEL"
                else:
                    bdPlay.datosParaIngresarCancion[1] = "3"
                    listaNombres[w] = "ROBERTO"

                bdPlay.datosParaIngresarCancion[2] = str(leerPlayListActual())
                bdPlay.datosParaIngresarCancion[3] = str(nombreLimpio)
                bdPlay.datosParaIngresarCancion[4] = str(listaEnlaces[w])
                bdPlay.datosParaIngresarCancion[6] = str(tiempo)
                bdPlay.datosParaIngresarCancion[7] = str("Ninguna")

                print("")
                print("CANCION #"+str(w))
                print("INTEGRANTE: "+str(listaNombres[w]))
                print("NOMBRE: "+str(nombreLimpio))
                print("DURACION: "+str(tiempo))
                print("")
                # Ingreso la cancion 
                bdPlay.ingresarCancion()
            print("FINALIZADO")
            input()
            opcionMenu = 0
            validarOpciones()

def pruebaColor():
    while True:
        pyautogui.press("t")
        duracion = pyautogui.screenshot(region=(172, 590, 40, 30))
        duracion.save("duracion.png")
        dur = pytesseract.image_to_string(Image.open('duracion.png'))
        print(dur)
        pyautogui.press("t")
        input()
    """
    input()
    print(pyautogui.position())
    input()
    print(pyautogui.position())
    input()
    """


principal()

""" 
            INGRESANDO CANCIONES DE LA 

    PLAY LIST #"""+str(leerPlayListActual()) + """
    ██████  ██████  ██  ██  ██████  ████
    ██▒▒▒▒  ██▒▒██  ██  ██  ██▒▒██  ██▒▒██
    ██████  ██████  ██  ██  ██████  ██░░██
    ▒▒▒▒██  ▒▒▒▒██  ██  ██  ██▒▒██  ██  ██
    ██████  ░░░░██  ██████  ██░░██  ████▒▒
    ▒▒▒▒▒▒      ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒▒▒░░
    ░░░░░░      ░░  ░░░░░░  ░░  ░░  ░░░░
                               RATONAZTICO
"""
#                              
#       _|_|_ ─┐ ┌─
#  PLAY _|_|_ ─┤ └─┐
#  LIST  | |  ─┘  ─┘
#  /██████  /██████  /██ /██  /██████  /████
# | ██___/ | ██ /██ | ██| ██ | ██  ██ | ██_/██
# | ██████ | ██████ | ██| ██ | ██████ | ██| ██
# |/____██ |/___/██ | ██| ██ | ██_/██ | ██| ██
#  /██████     | ██ | ██████ | ██| ██ | ████_/  
# |/_____/     |/_/ |/_____/ |/_/|/_/ |/___/
#                        R A T O N A Z T I C O 
#
#
#┐┤┘┌└ ╣ ╠ ═
# ─┐ ┌─
# ─┤ └─┐
# ─┘  ─┘
#   _|_|_
#   _|_|_
#    | |
#
#
