from Codigo.Clases.Punto import Punto
from Codigo.Clases.Recta import Recta

def DistanciaPuntoRecta(recta: Recta, punto: Punto):
    try:
        distancia = float((abs(punto.x * recta.a + punto.y * recta.b + recta.c)) / ((recta.a ** 2 + recta.b ** 2) ** (1 / 2)))
        return round(distancia, 2)
    except ValueError:
        return "Datos ingresados en formato invalido"