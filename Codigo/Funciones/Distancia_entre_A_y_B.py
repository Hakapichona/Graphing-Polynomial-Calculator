from Codigo.Clases.Punto import Punto


def distanciaAB(PuntoA: Punto, PuntoB: Punto):
    try:
        distancia = ((PuntoA.x - PuntoB.x) ** 2 + (PuntoA.y - PuntoB.y) ** 2) ** (1 / 2)
        return round(distancia, 2)
    except ValueError:
        return "Formato incorrecto de puntos "

# Ejemplo
# disA = distanciaAB(Punto(2,4), Punto(5,6))
# print(disA)
