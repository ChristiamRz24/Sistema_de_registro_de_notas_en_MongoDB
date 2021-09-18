#Librerías
import tkinter #Importamos el módulo
from PIL import ImageTk, Image
from pymongo import MongoClient, collation

###Conección a la base de datos###
MONGO_URI = 'mongodb://localhost' #Url local
client = MongoClient(MONGO_URI)
db = client ['registro_estudiantes'] #Nombre de la base de datos
collection = db['datos'] #Colección de la base de datos
##################################

def abrirVentanaConsultar():
    ventanaConsultar = tkinter.Tk() #Ventana de la aplicación
    ventanaConsultar.title('Consultar registros') #Título de la ventana
    ventanaConsultar.iconbitmap(".\\imagenes\\search.ico")

    #Centrar la ventana en la pantalla
    def centrarVentana(ventanaConsultar):
        #Dimensiones de la ventana
        w = 415 #Ancho
        h = 265 #Largo
        #Info de la pantalla
        sw = ventanaConsultar.winfo_screenwidth()
        sh = ventanaConsultar.winfo_screenheight()
        #Definir posición en "x" e "y"
        x = (sw - w)/2
        y = (sh - h)/2
        #Posicionar ventana
        ventanaConsultar.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #Llamada al método
    centrarVentana(ventanaConsultar)