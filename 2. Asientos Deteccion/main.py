'''
Realiza la deteccion de espacios en blanco
'''
import cv2
import pickle
import numpy as np

asientos = []

with open('espacios.pkl', 'rb') as file:
    asientos = pickle.load(file)

video = cv2.VideoCapture('asientos.mp4')

while True:
    check, img = video.read()
    imgBlur = cv2.GaussianBlur(img, (5, 5), 0)
    imgBN = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTH = cv2.adaptiveThreshold(imgBN, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgTH, 5)
    kernel = np.ones((5,5), np.int8)
    imgDil = cv2.dilate(imgMedian, kernel)
    kernel_open = np.ones((5, 5), np.uint8)
    imgOpen = cv2.morphologyEx(imgDil, cv2.MORPH_OPEN, kernel_open)

    for puntos in asientos:
        puntos = np.array(puntos, np.int32)
        mascara = np.zeros_like(imgBN)
        cv2.fillPoly(mascara, [puntos], 255)
        espacio = cv2.bitwise_and(imgOpen, imgOpen, mask=mascara)
        count = cv2.countNonZero(espacio)
        cv2.putText(img, str(count), (puntos[0][0], puntos[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)
        cv2.polylines(img, [puntos], isClosed=True, color=(255, 0, 0), thickness=2)
        if count < 2000:
            cv2.polylines(img, [puntos], isClosed=True, color=(0, 255, 0), thickness=2)
    cv2.imshow('video', img)
    cv2.waitKey(1)