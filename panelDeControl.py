#Librerías
import agregar #Ventana agregar registros
import consultar #Ventana consultar registros
import editar #Ventana editar registros
import eliminar #Ventana eliminar registros
import tkinter #Importamos el módulo

def abrirPanelDeControl():
    panelDeControl = tkinter.Tk() #Ventana de la aplicación
    panelDeControl.title('Panel de control') #Título de la ventana
    panelDeControl.iconbitmap(".\\imagenes\\home.ico")
    panelDeControl.resizable(width = 0, height = 0) #Ventana no resizable

    #Centrar la ventana en la pantalla
    def centrarVentana(panelDeControl):
        #Dimensiones de la ventana
        w = 415 #Ancho
        h = 280 #Largo
        #Info de la pantalla
        sw = panelDeControl.winfo_screenwidth()
        sh = panelDeControl.winfo_screenheight()
        #Definir posición en "x" e "y"
        x = (sw - w)/2
        y = (sh - h)/2
        #Posicionar ventana
        panelDeControl.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Llamada al método
    centrarVentana(panelDeControl)

    #Abrir y leer archivo .txt
    archivo = open(".\\documentos\\usuario.txt") #Ruta del archivo
    usuario = archivo.read() #Lectura del archivo

    #Variables
    opcionRespuesta = 0

    #Obtener una de las cuatro opciones
    def obtenerRespuesta(opcionRespuesta):
        #Abrir las ventanas restantes
        if (opcionRespuesta == 1) :
            agregar.abrirVentanaAgregar()
        else:
            if (opcionRespuesta == 2) :
                editar.abrirVentanaEditar()
            else:
                if (opcionRespuesta == 3) :
                    eliminar.abrirVentanaEliminar()
                else:
                    if (opcionRespuesta == 4) :
                        consultar.abrirVentanaConsultar()
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
    bienvenidaLabel.grid(pady = (18, 25), column = 0, row = 0, columnspan = 2)
    opciones.grid(padx = (20, 0), column = 0, row = 1)
    botonAgregar.grid(padx = (20, 8), pady = (13, 0), column = 0, row = 1)
    botonEditar.grid(padx = 18, pady = (13, 0), column = 1, row = 1)
    botonEliminar.grid(padx = (20, 8), pady = 18, column = 0, row = 2)
    botonConsultar.grid(padx = 18, pady = 18, column = 1, row = 2)
