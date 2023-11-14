from Codigo.Clases.Recta import Recta
from Codigo.Clases.Punto import Punto
from Codigo.Funciones.Recta2 import Recta2


def RectaParalela(Recta: Recta, Punto: Punto):
    pendiente = Recta.Pendiente()

    rectaP = Recta2(Punto, pendiente)
    return rectaP

# Ejemplo
#rectaParalela = RectaParalela(Recta(-2, 3, 0), Punto(4, 6))
# print(rectaParalela)
