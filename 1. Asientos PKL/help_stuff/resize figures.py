'''
Ajusta los tamaños de los poligonos
'''
import numpy as np

poligonos_originales = [
    [(329, 202), (370, 192), (385, 241), (344, 253)],
    [(467, 252), (424, 261), (432, 303), (475, 293)],
    [(489, 323), (445, 338), (461, 380), (508, 361)],
    [(326, 285), (279, 302), (288, 340), (340, 328)],
    [(353, 368), (303, 380), (312, 421), (363, 410)],
    [(400, 110), (416, 147), (452, 139), (443, 100)],
    [(362, 114), (369, 150), (328, 157), (320, 125)],
    [(438, 41), (472, 30), (482, 64), (450, 77)]
]

factor_ajuste = 1.6

poligonos_ajustados = []

for poligono in poligonos_originales:
    centro = np.mean(poligono, axis=0)

    poligono_ajustado = [(int((p[0] - centro[0]) * factor_ajuste + centro[0]),
                          int((p[1] - centro[1]) * factor_ajuste + centro[1]))
                         for p in poligono]

    poligonos_ajustados.append(poligono_ajustado)

for poligono in poligonos_ajustados:
    print(poligono)