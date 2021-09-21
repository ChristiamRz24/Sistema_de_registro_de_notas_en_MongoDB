#Librerías
import tkinter #Importamos el módulo
from bson import json_util, ObjectId
import json
from pymongo import MongoClient, collation

###Conección a la base de datos###
MONGO_URI = 'mongodb://localhost' #Url local
client = MongoClient(MONGO_URI)
db = client ['registro_estudiantes'] #Nombre de la base de datos
collection = db['datos'] #Colección de la base de datos
##################################

def abrirVentanaEditar():
    ventanaEditar = tkinter.Tk() #Ventana de la aplicación
    ventanaEditar.title('Editar registros') #Título de la ventana
    ventanaEditar.iconbitmap(".\\imagenes\\edit.ico")
    ventanaEditar.resizable(width = 0, height = 0) #Ventana no resizable

    #Centrar la ventana en la pantalla
    def centrarVentana(ventanaEditar):
        #Dimensiones de la ventana
        w = 415 #Ancho
        h = 339 #Largo
        #Info de la pantalla
        sw = ventanaEditar.winfo_screenwidth()
        sh = ventanaEditar.winfo_screenheight()
        #Definir posición en "x" e "y"
        x = (sw - w)/2
        y = (sh - h)/2
        #Posicionar ventana
        ventanaEditar.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Llamada al método
    centrarVentana(ventanaEditar)

    #Variables
    datoBuscar = ""
    nombre = ""
    nota1 = 0
    nota2 = 0

    def buscar():
        datoBuscar = cajaBuscar.get()
        datoBuscarAux = ""
        #Query para buscar si el estudiante ya esta registrado en la BD
        for documento in collection.find({
            "nombre": {
                "$eq": datoBuscar
            }
        }):
            alertaLabel["text"] = "Datos encontrados!"
            datoBuscarAux = datoBuscar

            #----------------Escritura y lectura de archvos JSON-------------------
            #Corregir el error: "Object of type ObjectId is not JSON serializable"
            newDocumento = json.loads(json_util.dumps(documento))
 
            #Guardar los datos del estudiante en un json
            with open(".\\documentos\\dataDB.json", "w") as archivoDataDB:
                json.dump(newDocumento, archivoDataDB)

            #Leer json
            with open(".\\documentos\\dataDB.json") as archivoDataDB:
                datos = json.load(archivoDataDB)
            #Leer solo los datos que pedimos del archivo json
            for datoJson in datos['_id']:
                jsonNota1 = (datos["nota1"])
                jsonNota2 = (datos["nota2"])
            #-----------------------------------------------------------------------

            #Insertar texto a las cajas
            if(cajaNombre == ""): #Comprobamos que la caja este vacía para insertar el dato
                cajaNombre.insert(0, datoBuscar)
                cajaNota1.insert(0, jsonNota1)
                cajaNota2.insert(0, jsonNota2)
            else: #Si no esta vacía, primero limpia y luego inserta el dato en la caja
                limpiar()
                cajaNombre.insert(0, datoBuscar)
                cajaNota1.insert(0, jsonNota1)
                cajaNota2.insert(0, jsonNota2)                

        #Verificamos que la caja de texto no este vacía
        if (datoBuscar == ""):
            alertaLabel["text"] = "Por favor, ingrese un nombre a buscar en la caja de texto!"
        else: 
            #Comparamos si el registro existe en la Base de datos
            if(datoBuscar != datoBuscarAux):
                alertaLabel["text"] = "El registro \"" + datoBuscar + "\" no existe en la Base de datos!"

    #Limpiar las cajas de texto
    def limpiar():
        cajaNombre.delete("0","end") #("posición inicial", "posición final")
        cajaNota1.delete("0","end")
        cajaNota2.delete("0","end")

    #Función para grabar datos en la BD (Base de Datos)
    def grabar():
        #Capturar los datos de las cajas de texto
        datoBuscar = cajaBuscar.get()
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
                    #Query de inserción de datos a MongoDB
                    collection.update_one({
                        "nombre": datoBuscar }, {
                        "$set": {
                            "nombre": nombre,
                            "nota1": nota1,
                            "nota2": nota2
                        }
                    })
                    alertaLabel["text"] = "Datos editados correctamente!"
            except:
                print("")

    #LabelFrames
    datoBuscarLblFrame = tkinter.LabelFrame(ventanaEditar, text = "Datos a buscar", bg = "#DAE1E7")
    textLblFrame = tkinter.LabelFrame(ventanaEditar, text = "Datos del estudiante", bg = "#DAE1E7")

    #Labels
    nombreBuscar = tkinter.Label(datoBuscarLblFrame, text = "Nombre:", font = "Georgia 13", bg = "#DAE1E7") #Nombre a buscar en la BD
    nombreLabel = tkinter.Label(textLblFrame, text = "Nombre:", font = "Georgia 13", bg = "#DAE1E7")
    nota1Label = tkinter.Label(textLblFrame, text = "Nota 1:", font = "Georgia 13", bg = "#DAE1E7")
    nota2Label = tkinter.Label(textLblFrame, text = "Nota 2:", font = "Georgia 13", bg = "#DAE1E7")
    vacioLabel = tkinter.Label(ventanaEditar, text = "Solo relleno", fg = "#f8f4f4") #Label para rellenar la grid
    alertaLabel = tkinter.Label(ventanaEditar, text = "") #Label de alerta para el usuario

    #Cajas de texto
    cajaBuscar = tkinter.Entry(datoBuscarLblFrame, font = "Georgia 12", width = 15)
    cajaNombre = tkinter.Entry(textLblFrame, font = "Georgia 15")
    cajaNota1 = tkinter.Entry(textLblFrame, font = "Georgia 15")
    cajaNota2 = tkinter.Entry(textLblFrame, font = "Georgia 15")

    #Botones
    btnBuscar = tkinter.Button(datoBuscarLblFrame, text = "Buscar", width = 8, height = 1, font = "Georgia 9 bold", bg = "#1C4B82", fg = "white", command = buscar)
    btnLimpiar = tkinter.Button(ventanaEditar, text = "Limpiar", width = 12, height = 2, font = "Georgia 9", bg = "#57CC99", command = limpiar)
    btnGrabar = tkinter.Button(ventanaEditar, text = "Grabar", width = 12, height = 2, font = "Georgia 9", bg = "#57CC99", command = grabar)

    #Diseño de la app
    alertaLabel.grid(pady = 0.5, column = 0, row = 0, columnspan = 3)
    #------------------------------------------------------------------------
    datoBuscarLblFrame.grid(padx = 20, pady = (3, 17), column = 0, row = 1, columnspan = 3)
    nombreBuscar.grid(padx = (20, 5), pady = (5, 9), column = 0, row = 0)
    cajaBuscar.grid(padx = (5, 0), pady = (5, 9) ,column = 1, row = 0)
    btnBuscar.grid(padx = (5, 20), pady = (5, 9) ,column = 2, row = 0)
    #------------------------------------------------------------------------
    textLblFrame.grid(padx = 20, pady = (0, 13), column = 0, row = 2, columnspan = 3)
    nombreLabel.grid(padx = (20, 5), pady = (20, 5),column = 0, row = 0)
    cajaNombre.grid(padx = (5, 20), pady = (20, 5),column = 1, row = 0)
    nota1Label.grid(padx = (20, 5), pady = 5,column = 0, row = 1)
    cajaNota1.grid(padx = (5, 20), pady = 5,column = 1, row = 1)
    nota2Label.grid(padx = (20, 5), pady = (5, 20),column = 0, row = 2)
    cajaNota2.grid(padx = (5, 20), pady = (5, 20),column = 1, row = 2)
    vacioLabel.grid(column = 0, row = 3)
    #------------------------------------------------------------------------
    btnLimpiar.grid(column = 1, row = 3)
    btnGrabar.grid(column = 2, row = 3)
