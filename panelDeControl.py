#Librerías
import agregar
import tkinter #Importamos el módulo
from PIL import ImageTk, Image

def abrirPanelDeControl():
    panelDeControl = tkinter.Tk() #Ventana de la aplicación
    panelDeControl.title('Panel de control') #Título de la ventana
    panelDeControl.iconbitmap(".\\imagenes\\home.ico")
    panelDeControl.geometry("415x280") #Tamaño de la ventana

    #Abrir y leer archivo .txt
    archivo = open("username.txt") #Ruta del archivo
    usuario = archivo.read() #Lectura del archivo

    #Variables
    opcionRespuesta = 0

    #Obtener una de las cuatro opciones
    def obtenerRespuesta(opcionRespuesta):
        #Abrir las ventanas restantes
        if (opcionRespuesta == 1) :
            print("Ventana agregar")
            agregar.abrirVentanaAgregar()
        else:
            if (opcionRespuesta == 2) :
                print("Ventana editar")
                #agregar.abrirVentanaAgregar()
            else:
                if (opcionRespuesta == 3) :
                    print("Ventana eliminar")
                    #agregar.abrirVentanaAgregar()
                else:
                    if (opcionRespuesta == 4) :
                        print("Ventana consultar")
                        #agregar.abrirVentanaAgregar()
                    else:
                        opcionRespuesta = 0

    #LabelFrames
    opciones = tkinter.LabelFrame(panelDeControl, text = "Administrar estudiantes", bg = "#DAE1E7")

    #Botones opciones
    botonAgregar = tkinter.Button(opciones, text = "Agregar",pady = 15 , width = 18, font = "Georgia 9 bold", bg = "#1C4B82", fg = "white", command = lambda: obtenerRespuesta(1))
    botonEditar = tkinter.Button(opciones, text = "Editar",pady = 15 , width = 18, font = "Georgia 9 bold", bg = "#1C4B82", fg = "white", command = lambda: obtenerRespuesta(2))
    botonEliminar = tkinter.Button(opciones, text = "Eliminar",pady = 15 , width = 18, font = "Georgia 9 bold", bg = "#DD6B4D", fg = "white", command = lambda: obtenerRespuesta(3))
    botonConsultar = tkinter.Button(opciones, text = "Consultar",pady = 15 , width = 18, font = "Georgia 9 bold", bg = "#1C4B82", fg = "white", command = lambda: obtenerRespuesta(4))

    #Labels
    bienvenidaLabel = tkinter.Label(panelDeControl, text = "Bienvenido " + usuario , font = "Georgia 20")

    #Diseño de la app
    bienvenidaLabel.grid(pady = 25, column = 0, row = 0, columnspan = 2)
    opciones.grid(padx = (20, 0), column = 0, row = 1)
    botonAgregar.grid(padx = (20, 8), pady = (13, 0), column = 0, row = 1)
    botonEditar.grid(padx = 18, pady = (13, 0), column = 1, row = 1)
    botonEliminar.grid(padx = (20, 8), pady = 18, column = 0, row = 2)
    botonConsultar.grid(padx = 18, pady = 18, column = 1, row = 2)
