# Detector-de-Uso-de-Mascarilla
Este proyecto consiste en la implementación de un detector de uso de mascarillas en tiempo real utilizando la combinación de OpenCV, MediaPipe y MobileNetV2. El modelo detecta si una persona está utilizando correctamente una mascarilla y puede desplegar un aviso en pantalla. A continuación se describe la arquitectura del sistema y el proceso de entrenamiento.

Descripción del Proyecto
El objetivo del detector es identificar si una persona lleva o no una mascarilla en tiempo real a través de la cámara web. El flujo del proyecto incluye las siguientes etapas:

Detección de rostros: Se utiliza MediaPipe para localizar las caras.
Clasificación del uso de mascarilla: Un modelo entrenado con MobileNetV2 determina si la persona lleva o no mascarilla.
Visualización en tiempo real: Se usa OpenCV para capturar el video de la cámara y mostrar los resultados en pantalla.

# Mask-Use-Detector
This project consists of the implementation of a real-time mask-use detector using the combination of OpenCV, MediaPipe and MobileNetV2. The model detects whether a person is wearing a mask correctly and can display an on-screen warning. The system architecture and training process is described below.

Project Description
The goal of the detector is to identify whether or not a person is wearing a mask in real time via webcam. The project flow includes the following stages:

Face detection: MediaPipe is used to locate faces.
Mask wear classification: A model trained with MobileNetV2 determines whether the person is wearing a mask or not.
Real-time visualization: OpenCV is used to capture the video from the camera and display the results on screen.
