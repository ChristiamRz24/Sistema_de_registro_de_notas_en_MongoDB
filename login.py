#Librerías
import panelDeControl
import tkinter #Importamos el módulo
from PIL import ImageTk, Image
from pymongo import MongoClient, collation

###Conección a la base de datos##
MONGO_URI = 'mongodb://localhost' #Url local
client = MongoClient(MONGO_URI)
db = client ['pruebas'] #Nombre de la base de datos
collection = db['usuarios'] #Colección de la base de datos
#################################

#Variables
usuario = ""
contraseña = ""
#bgColorVentana = "#7EB5A6"

#Diseño de la ventana Login
ventana = tkinter.Tk() #Ventana de la aplicación
ventana.title("Ingresar") #Título de la ventana
ventana.iconbitmap(".\\imagenes\\log-in.ico")
#ventana.configure(bg = bgColorVentana)

#Funciones
#Centrar la ventana en la pantalla
def centrarVentana(ventana):
    #Dimensiones de la ventana
    w = 390 #Ancho
    h = 449 #Largo
    #Info de la pantalla
    sw = ventana.winfo_screenwidth()
    sh = ventana.winfo_screenheight()
    #Definir posición en "x" e "y"
    x = (sw - w)/2
    y = (sh - h)/2
    #Posicionar ventana
    ventana.geometry('%dx%d+%d+%d' % (w, h, x, y))

#Llamada al método
centrarVentana(ventana)

#Capturar texto de las cajas
def entradaDeTexto():
    usuario = cajaUsuario.get()
    contraseña = cajaContraseña.get()

    #Obtener estado del check
    obtenerEstado(usuario, contraseña)

    #Query para comparar si las credenciales son correctas
    for documento in collection.find({
        "usuario": {
            "$eq": usuario
            },
            "contraseña": {
                "$eq": contraseña
            }
        }):
            #Cierra/destruye la ventana
            ventana.destroy()
            #Abrir ventana 2 (panel de control)
            panelDeControl.abrirPanelDeControl()

#guardar nombre de usuario en un archivo .txt
def guardarDato(ruta, contenido):
    archivo = open(ruta,"w") #Creación del archivo
    archivo.write(contenido)
    archivo.close() #Cerrar el archivo

estadoCheck = tkinter.IntVar()

#Obtener estado del check
def obtenerEstado(datoUsuario, datoContraseña):
    #Rutas de los archivos
    ruta1 = ".\\documentos\\usuario.txt"
    ruta2 = ".\\documentos\\contraseña.txt"
    ruta3 = ".\\documentos\\estado.txt"

    #Validad que las cajas de texto no esten vacías o el check desmarcado
    if(datoUsuario == "" or datoContraseña == "" or estadoCheck.get() == 0):
        estadoCheck.set(0) #Desmarca la casilla

        #Estado del check es inactivo
        guardarDato(ruta3, "0")
        #Vaciar los archivos
        guardarDato(ruta1, "")
        guardarDato(ruta2, "")

    else: #Guardar los datos del usuario
        #Estado del check es activo
        guardarDato(ruta3, "1") 
        guardarDato(ruta1, datoUsuario) #Guarda el dqto "Usuario"
        guardarDato(ruta2, datoContraseña) #Guarda el dqto "Contraseña"


#Botón Login
botonLogin = tkinter.Button(ventana, text = "Ingresar", pady = 15 , width = 30, bg = "#57CC99", font = "Georgia 10", command = entradaDeTexto) #Config del botón

#Checkbutton
recordarDatos = tkinter.Checkbutton(ventana, text = "Recordar usuario y contraseña", variable = estadoCheck, onvalue = 1, offvalue = 0)

#Labels
bienvenidaLabel = tkinter.Label(ventana, text = "BIENVENIDO", font = "Georgia 25")
usuarioLabel = tkinter.Label(ventana, text = "Usuario", font = "Georgia 13")
contraseñaLabel = tkinter.Label(ventana, text = "Contraseña", font = "Georgia 13")
alertaLabel = tkinter.Label(ventana, text = "") 

#Cajas de texto
cajaUsuario = tkinter.Entry(ventana, font = "Georgia 15")
cajaContraseña = tkinter.Entry(ventana, font = "Georgia 15")

###############################################################
#Se ejecuta a iniciar
archivoEstado = open(".\\documentos\\estado.txt")
estado = archivoEstado.read() #Lectura del archivo
if(estado == "1"):
    #Definir estado del check
    estadoCheck.set(1)
    #Leer dato "Usuario"
    archivoUsuario = open(".\\documentos\\usuario.txt")
    usuario = archivoUsuario.read() #Lectura del archivo
    #Leer dato "Contraseña"
    archivoContraseña = open(".\\documentos\\contraseña.txt")
    contraseña = archivoContraseña.read() #Lectura del archivo

    #Insertar texto a las cajas
    cajaUsuario.insert(0, usuario)
    cajaContraseña.insert(0, contraseña)
###############################################################

#Imágenes
userImage = ImageTk.PhotoImage(Image.open(".\\imagenes\\user.png"))
userImageLabel = tkinter.Label(ventana, image = userImage)

#Diseño de la app
bienvenidaLabel.pack(pady = 25)
userImageLabel.pack()
usuarioLabel.pack(pady = 10)
cajaUsuario.pack()
contraseñaLabel.pack(pady = 9)
cajaContraseña.pack()
recordarDatos.pack(pady = 12)
botonLogin.pack(pady = 3)
alertaLabel.pack(side = tkinter.BOTTOM)

ventana.mainloop() #Bucle principal, matiene la ventana abierta
