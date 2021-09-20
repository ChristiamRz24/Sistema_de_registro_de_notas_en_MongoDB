#Librerías
import tkinter #Importamos el módulo
from tkinter import ttk
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
        w = 493 #Ancho
        h = 300 #Largo
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

    #Creación de la tabla
    tabla = ttk.Treeview(ventanaConsultar, columns = ("#1","#2"))
    tabla.tag_configure('fuente', font=("Georgia", 11)) #Cambiar la fuente de los registros

    #Query de búsqueda
    for documento in collection.find({}):
        tabla.insert('', 0, tag = 'fuente', text = documento['nombre'], values = (documento['nota1'], documento['nota2']))

    #Label
    titulo = tkinter.Label(ventanaConsultar, text = "Datos de los estudiantes", font = "Georgia 15")

    #ScrollBar
    verscrlbar = ttk.Scrollbar(ventanaConsultar, orient = "vertical", command = tabla.yview)
    tabla.configure(yscrollcommand = verscrlbar.set)

    #Diseño de la ventana
    titulo.grid(pady = 10, row = 0, column = 0, columnspan = 4)
    tabla.grid(padx = (20, 0), row = 1, column = 0, columnspan = 3)
    tabla.heading("#0", text = "Nombre") #Indice de la tabla
    tabla.heading("#1", text = "Nota 1")
    tabla.heading("#2", text = "Nota 2")

    tabla.column("#0", width = 250)
    tabla.column("#1", width = 100, anchor = "center")
    tabla.column("#2", width = 100, anchor = "center")

    verscrlbar.grid(row = 1, column = 4, ipady = 88)
