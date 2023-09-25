'''
Para obtener las coordenadas de los asientos para hacer los poligonos
'''
import cv2


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Coordenadas del clic: ({x}, {y})')

image = cv2.imread('../asientos.jpg')  # Reemplaza 'tu_imagen.jpg' con la ruta de tu imagen
cv2.imshow('Imagen', image)

cv2.setMouseCallback('Imagen', mouse_callback)

while True:
    key = cv2.waitKey(1)
    if key == 27:  # Presiona la tecla Esc para salir
        break

cv2.destroyAllWindows()