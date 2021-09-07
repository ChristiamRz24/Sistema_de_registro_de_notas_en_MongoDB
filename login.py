#Librerías
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
ventana.iconbitmap("C:\\Users\\User\\Desktop\\Python\\imagenes\\log-in.ico")
ventana.geometry("395x445") #Tamaño de la ventana (Ancho x Largo)
#ventana.configure(bg = bgColorVentana)

#Funciones
#Capturar texto de las cajas
def entradaDeTexto():
    usuario = cajaUsuario.get()
    contraseña = cajaContraseña.get()
    #Query para comparar si las credenciales son correctas
    for documento in collection.find({
        "usuario": {
            "$eq": usuario
            },
            "contraseña": {
                "$eq": contraseña
            }
        }):
            alertaLabel["text"] = "Ingresando..." #Alerta

#Botón Login
botonLogin = tkinter.Button(ventana, text = "Ingresar",pady = 15 , width = 30, bg = "#57CC99", font = "Georgia 10", command = entradaDeTexto) #Config del botón

#Labels
bienvenidaLabel = tkinter.Label(ventana, text = "BIENVENIDO", font = "Georgia 25")
usuarioLabel = tkinter.Label(ventana, text = "Usuario", font = "Georgia 13")
contraseñaLabel = tkinter.Label(ventana, text = "Contraseña", font = "Georgia 13")
alertaLabel = tkinter.Label(ventana, text = "") 

#Cajas de texto
cajaUsuario = tkinter.Entry(ventana, font = "Georgia 15")
cajaContraseña = tkinter.Entry(ventana, font = "Georgia 15")

#Imágenes
userImage = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Desktop\\Python\\imagenes\\user.png"))
userImageLabel = tkinter.Label(ventana, image = userImage)

#Diseño de la app
bienvenidaLabel.pack(pady = 25)
userImageLabel.pack()
usuarioLabel.pack(pady = 10)
cajaUsuario.pack()
contraseñaLabel.pack(pady = 9)
cajaContraseña.pack()
botonLogin.pack(pady = 9)
alertaLabel.pack(side = tkinter.BOTTOM)

ventana.mainloop() #Bucle principal, matiene la ventana abierta
