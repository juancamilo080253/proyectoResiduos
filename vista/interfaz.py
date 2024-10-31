from tkinter import *
from PIL import Image, ImageTk
from controlador.deteccion import Scanning
from vista.ui_utils import load_images

def ventana_principal():
    global lblVideo, pantalla

    # Crear la ventana principal
    pantalla = Tk()
    pantalla.title("RECICLAJE INTELIGENTE")
    pantalla.geometry("1280x720")

    # Cargar y establecer la imagen de fondo
    fondo_img = Image.open("vista/setUp/Canva.png")
    fondo_img = ImageTk.PhotoImage(fondo_img)
    background = Label(pantalla, image=fondo_img)
    background.image = fondo_img  # Mantener referencia
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Cargar imágenes y configuraciones de la interfaz
    resources = load_images()

    # Configura las etiquetas en la ventana principal
    resources['lblimg'] = Label(pantalla)
    resources['lblimgtxt'] = Label(pantalla)
    resources['lblimg'].place(x=44, y=282)
    resources['lblimgtxt'].place(x=999, y=274)

    # Configurar display de video en la UI
    lblVideo = Label(pantalla)
    lblVideo.place(x=320, y=180)

    # Iniciar detección y actualizar UI
    Scanning(lblVideo, resources)
    pantalla.mainloop()
