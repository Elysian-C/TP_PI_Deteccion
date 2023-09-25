'''
Crea el archivo PKL de las coordenadas de los poligonos
'''
import cv2
import pickle
import numpy as np

img = cv2.imread('asientos.jpg')

coordenadas = [
    [(310, 170), (370, 159), (396, 252), (336, 271)],
    [(477, 220), (400, 225), (400, 320), (490, 302)],
    [(496, 306), (426, 330), (452, 397), (527, 367)],
    [(330, 267), (240, 280), (255, 365), (365, 346)],
    [(365, 351), (285, 371), (299, 436), (381, 419)],
    [(383, 101), (390, 175), (466, 148), (452, 85)],
    [(372, 100), (383, 158), (317, 169), (305, 118)],
    [(424, 33), (478, 16), (494, 70), (443, 91)]
]

espacios = []

for cord in coordenadas:
    espacios.append(cord)
    cv2.polylines(img, [np.array(cord)], isClosed=True, color=(255, 0, 0), thickness=2)

with open('../2. Asientos Deteccion/espacios.pkl', 'wb') as file:
    pickle.dump(espacios, file)
