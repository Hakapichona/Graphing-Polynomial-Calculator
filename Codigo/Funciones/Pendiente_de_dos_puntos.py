from Codigo.Clases.Punto import Punto


def Pendiente(puntoA: Punto, puntoB: Punto):
    if puntoA.x - puntoB.x == 0:
        return "Pendiente infinita"

    pendiente = (puntoB.y - puntoA.y) / (puntoB.x - puntoA.x)

    if pendiente % 1 == 0:
        return int(pendiente)

    return round(pendiente, 2)

# Ejemplo
#print(Pendiente( Punto(2,3), Punto(2,4)))