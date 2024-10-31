from tkinter import Label
from PIL import Image, ImageTk

def load_images():
    """Carga y retorna todas las imágenes de la UI"""
    images = {
        'metal': Image.open("vista/setUp/metal.png"),
        'metaltxt': Image.open("vista/setUp/metaltxt.png"),
        'glass': Image.open("vista/setUp/vidrio.png"),
        'glasstxt': Image.open("vista/setUp/vidriotxt.png"),
        'plastic': Image.open("vista/setUp/plastico.png"),
        'plasticotxt': Image.open("vista/setUp/plasticotxt.png"),
        'carton': Image.open("vista/setUp/carton.png"),
        'cartontxt': Image.open("vista/setUp/cartontxt.png"),
        'medical': Image.open("vista/setUp/medical.png"),
        'medicaltxt': Image.open("vista/setUp/medicaltxt.png"),
        'lblimg': Label(),  # Agrega la etiqueta lblimg a resources
        'lblimgtxt': Label()  # Agrega la etiqueta lblimgtxt a resources
    }
    return images

def clean_labels(resources):
    """Limpia todas las etiquetas de la interfaz"""
    resources['lblimg'].config(image='')
    resources['lblimgtxt'].config(image='')

def update_images(cls, resources):
    """Muestra la imagen correspondiente en la UI según la clase detectada"""
    if cls == 0:
        img = ImageTk.PhotoImage(resources['metal'])
        img_txt = ImageTk.PhotoImage(resources['metaltxt'])
    elif cls == 1:
        img = ImageTk.PhotoImage(resources['glass'])
        img_txt = ImageTk.PhotoImage(resources['glasstxt'])
    elif cls == 2:
        img = ImageTk.PhotoImage(resources['plastic'])
        img_txt = ImageTk.PhotoImage(resources['plasticotxt'])
    elif cls == 3:
        img = ImageTk.PhotoImage(resources['carton'])
        img_txt = ImageTk.PhotoImage(resources['cartontxt'])
    elif cls == 4:
        img = ImageTk.PhotoImage(resources['medical'])
        img_txt = ImageTk.PhotoImage(resources['medicaltxt'])

    # Configurar imágenes en la UI
    resources['lblimg'].configure(image=img)
    resources['lblimg'].image = img  # Referencia para evitar que la imagen se recolecte
    resources['lblimgtxt'].configure(image=img_txt)
    resources['lblimgtxt'].image = img_txt
