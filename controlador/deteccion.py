import cv2
import numpy as np
import imutils
from PIL import Image, ImageTk
from ultralytics import YOLO
import math
from vista.ui_utils import update_images, clean_labels

# Inicialización del modelo YOLO y configuración de clases
model = YOLO('modelo/best.pt')  # Ruta ajustada para el modelo en su carpeta
clsName = ['Metal', 'Glass', 'Plastic', 'Carton', 'Medical']
cap = None

def Scanning(lblVideo, resources):
    """Función principal de detección, estructurada en capas y paralela"""
    global cap
    if cap is None:
        # Configura la cámara
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(3, 1280)
        cap.set(4, 720)

    # --- Capa de Preprocesamiento ---
    ret, frame = cap.read()
    if ret:
        frame_show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # --- Capa de Inferencia (Detección en Paralelo) ---
        results = model(frame, stream=True, verbose=False)
        detect = False

        # Procesar cada objeto detectado
        for res in results:
            boxes = res.boxes
            for box in boxes:
                detect = True
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                x1, y1, x2, y2 = max(0, x1), max(0, y1), max(0, x2), max(0, y2)

                # Determinar clase y confianza
                cls = int(box.cls[0])
                conf = math.ceil(box.conf[0] * 100)

                # --- Capa de Postprocesamiento ---
                cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 255, 0), 2)
                text = f'{clsName[cls]} {conf}%'
                cv2.putText(frame_show, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

                # Actualizar UI con imágenes según clase detectada
                update_images(cls, resources)

        # Limpiar etiquetas si no se detectan objetos
        if not detect:
            clean_labels(resources)

        # --- Capa de Interfaz de Usuario ---
        # Redimensionar y actualizar visualización en la interfaz
        frame_show = imutils.resize(frame_show, width=640)
        img_display = ImageTk.PhotoImage(image=Image.fromarray(frame_show))
        lblVideo.configure(image=img_display)
        lblVideo.image = img_display
        lblVideo.after(10, lambda: Scanning(lblVideo, resources))
    else:
        cap.release()
