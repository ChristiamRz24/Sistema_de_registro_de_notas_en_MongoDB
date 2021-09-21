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

def abrirVentanaEliminar():
    ventanaEliminar = tkinter.Tk() #Ventana de la aplicación
    ventanaEliminar.title('Eliminar registros') #Título de la ventana
    ventanaEliminar.iconbitmap(".\\imagenes\\delete.ico")

    #Centrar la ventana en la pantalla
    def centrarVentana(ventanaEliminar):
        #Dimensiones de la ventana
        w = 415 #Ancho
        h = 280 #Largo
        #Info de la pantalla
        sw = ventanaEliminar.winfo_screenwidth()
        sh = ventanaEliminar.winfo_screenheight()
        #Definir posición en "x" e "y"
        x = (sw - w)/2
        y = (sh - h)/2
        #Posicionar ventana
        ventanaEliminar.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #Llamada al método
    centrarVentana(ventanaEliminar)

    #Creación de la tabla
    tabla = ttk.Treeview(ventanaEliminar, height = 2, columns = ("#1","#2"))
    tabla.tag_configure('fuente', font=("Georgia", 11)) #Cambiar la fuente de los registros

    #Variables
    datoBuscar = ""

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

            #Limpiar toda la tabla
            limpiarTabla()

            #Inserar los datos en la tabla
            tabla.insert('', 0, tag = 'fuente', text = documento['nombre'], values = (documento['nota1'], documento['nota2']))
            

        #Verificamos que la caja de texto no este vacía
        if (datoBuscar == ""):
            alertaLabel["text"] = "Por favor, ingrese un nombre a buscar en la caja de texto!"
        else: 
            #Comparamos si el registro existe en la Base de datos
            if(datoBuscar != datoBuscarAux):
                alertaLabel["text"] = "El registro \"" + datoBuscar + "\" no existe en la Base de datos!"
    
    #Limpia todos los datos de la tabla
    def limpiarTabla():
        for i in tabla.get_children():
            tabla.delete(i)

    #Limpiar la caja de texto
    def limpiar():
        cajaBuscar.delete("0","end") #("posición inicial", "posición final")
    
    #Eliminar registro de la basde de datos
    def eliminar():
        datoBuscar = cajaBuscar.get()
        limpiar()
        #Comprobamos si el estdudiante esta registrado en la Basde de Datos
        for documento in collection.find({
            "nombre": {
                "$eq": datoBuscar
            }
        }):
            #Query de eliminación
            collection.delete_one({
                "nombre": datoBuscar
            })
            limpiarTabla()
            alertaLabel["text"] = "Datos eliminados correctamente!"
    
    #LabelFrames
    datoBuscarLblFrame = tkinter.LabelFrame(ventanaEliminar, text = "Datos a buscar", bg = "#DAE1E7")

    #Labels
    nombreBuscar = tkinter.Label(datoBuscarLblFrame, text = "Nombre:", font = "Georgia 13", bg = "#DAE1E7") #Nombre a buscar en la BD
    alertaLabel = tkinter.Label(ventanaEliminar, text = "") #Label de alerta para el usuario
    infoLabel = tkinter.Label(ventanaEliminar, text = "Datos del estudiante:  ", font = "Georgia 12")

    #Cajas de texto
    cajaBuscar = tkinter.Entry(datoBuscarLblFrame, font = "Georgia 12", width = 16)

    #Botones
    btnBuscar = tkinter.Button(datoBuscarLblFrame, text = "Buscar", width = 8, height = 1, font = "Georgia 9 bold", bg = "#1C4B82", fg = "white", command = buscar)
    btnEliminar = tkinter.Button(ventanaEliminar, text = "Eliminar", width = 12, height = 2, font = "Georgia 9 bold", bg = "#DD6B4D", fg = "white", command = eliminar)

    #Diseño de la app
    alertaLabel.grid(pady = 0.5, column = 0, row = 0, columnspan = 3)
    #------------------------------------------------------------------------
    datoBuscarLblFrame.grid(padx = 20, pady = (3, 17), column = 0, row = 1, columnspan = 3)
    nombreBuscar.grid(padx = (20, 5), pady = (5, 9), column = 0, row = 0)
    cajaBuscar.grid(padx = (5, 0), pady = (5, 9) , column = 1, row = 0)
    btnBuscar.grid(padx = (5, 20), pady = (5, 9) , column = 2, row = 0)
    #------------------------------------------------------------------------
    infoLabel.grid(pady = 5, column = 0, row = 2)
    #------------------------------------------------------------------------
    tabla.grid(padx = 20 , row = 3, column = 0, columnspan = 3)
    tabla.heading("#0", text = "Nombre") #Indice de la tabla
    tabla.heading("#1", text = "Nota 1")
    tabla.heading("#2", text = "Nota 2")

    tabla.column("#0", width = 210)
    tabla.column("#1", width = 80, anchor = "center")
    tabla.column("#2", width = 80, anchor = "center")
    #------------------------------------------------------------------------
    btnEliminar.grid(pady = (10, 0), column = 2, row = 4)
    
