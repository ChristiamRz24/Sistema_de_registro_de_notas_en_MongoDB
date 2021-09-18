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

def abrirVentanaAgregar():
    ventanaAgregar = tkinter.Tk() #Ventana de la aplicación
    ventanaAgregar.title('Agregar registros') #Título de la ventana
    ventanaAgregar.iconbitmap(".\\imagenes\\add.ico")
    ventanaAgregar.resizable(width = 0, height = 0) #Ventana no resizable

    #Centrar la ventana en la pantalla
    def centrarVentana(ventanaAgregar):
        #Dimensiones de la ventana
        w = 415 #Ancho
        h = 265 #Largo
        #Info de la pantalla
        sw = ventanaAgregar.winfo_screenwidth()
        sh = ventanaAgregar.winfo_screenheight()
        #Definir posición en "x" e "y"
        x = (sw - w)/2
        y = (sh - h)/2
        #Posicionar ventana
        ventanaAgregar.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Llamada al método
    centrarVentana(ventanaAgregar)

    #Variables
    nombre = ""
    nota1 = 0
    nota2 = 0

    #Limpiar las cajas de texto
    def limpiar():
        cajaNombre.delete("0","end") #("posición inicial", "posición final")
        cajaNota1.delete("0","end")
        cajaNota2.delete("0","end")

    #Función para grabar datos en la BD (Base de Datos)
    def grabar():
        #Capturar los datos de las cajas de texto
        nombre = cajaNombre.get()
        nota1 = cajaNota1.get()
        nota2 = cajaNota2.get()

        #comprobar que los datos no sean nulos
        if (nombre == "" or nota1 == "" or nota2 == ""):
            alertaLabel["text"] = "Faltan datos!"
        else:
            #Vaciar/borrar la alerta
            alertaLabel["text"] = ""

            #Convertir de str a float
            try: #Capturar el error de conversión
                nota1 = float(nota1)
                nota2 = float(nota2)
            except:
               alertaLabel["text"] = "Solo se permiten números para las notas"

            try: #Capturar error
                #Validar las notas
                if (nota1 <0 or nota1 >10 or nota2 <0 or nota2 >10):
                    alertaLabel["text"] = "Las notas ingresadas son erroneas"
                else:
                    nombreEncontrado = "" #Variable de apoyo
                    #Query para buscar si el estudiante ya esta registrado en la BD
                    for documento in collection.find({
                        "nombre": {
                            "$eq": nombre
                        }
                    }):
                        alertaLabel["text"] = "El estudiante ingresado ya existe en la Base de Datos"
                        #Guardamos el dato en una variable de apoyo
                        nombreEncontrado = nombre
                    
                    #Si en la BD no esta registrado el estudiante grabamos los datos
                    if (nombre != nombreEncontrado):
                        #Query de inserción
                        collection.insert_one({
                            "nombre": nombre, 
                            "nota1": nota1, 
                            "nota2": nota2
                        })
                        alertaLabel["text"] = "Datos ingresados correctamente!" 
            except:
                print("")

    #LabelFrames
    textLblFrame = tkinter.LabelFrame(ventanaAgregar, text = "Datos del estudiante", bg = "#DAE1E7")

    #Labels
    nombreLabel = tkinter.Label(textLblFrame, text = "Nombre:", font = "Georgia 13", bg = "#DAE1E7")
    nota1Label = tkinter.Label(textLblFrame, text = "Nota 1:", font = "Georgia 13", bg = "#DAE1E7")
    nota2Label = tkinter.Label(textLblFrame, text = "Nota 2:", font = "Georgia 13", bg = "#DAE1E7")
    vacioLabel = tkinter.Label(ventanaAgregar, text = "Solo relleno", fg = "#f8f4f4") #Label para rellenar la grid
    alertaLabel = tkinter.Label(ventanaAgregar, text = "") #Label de alerta para el usuario

    #Cajas de texto
    cajaNombre = tkinter.Entry(textLblFrame, font = "Georgia 15")
    cajaNota1 = tkinter.Entry(textLblFrame, font = "Georgia 15")
    cajaNota2 = tkinter.Entry(textLblFrame, font = "Georgia 15")

    #Botones
    btnLimpiar = tkinter.Button(ventanaAgregar, text = "Limpiar", width = 12, height = 2, font = "Georgia 9", bg = "#57CC99", command = limpiar)
    btnGrabar = tkinter.Button(ventanaAgregar, text = "Grabar", width = 12, height = 2, font = "Georgia 9", bg = "#57CC99", command = grabar)

    #Diseño de la app
    alertaLabel.grid(pady = 0.5, column = 0, row = 0, columnspan = 3)
    textLblFrame.grid(padx = 20, pady = (5, 13), column = 0, row = 1, columnspan = 3)
    nombreLabel.grid(padx = (20, 5), pady = (20, 5),column = 0, row = 0)
    cajaNombre.grid(padx = (5, 20), pady = (20, 5),column = 1, row = 0)
    nota1Label.grid(padx = (20, 5), pady = 5,column = 0, row = 1)
    cajaNota1.grid(padx = (5, 20), pady = 5,column = 1, row = 1)
    nota2Label.grid(padx = (20, 5), pady = (5, 20),column = 0, row = 2)
    cajaNota2.grid(padx = (5, 20), pady = (5, 20),column = 1, row = 2)
    vacioLabel.grid(column = 0, row = 2)
    btnLimpiar.grid(column = 1, row = 2)
    btnGrabar.grid(column = 2, row = 2)
