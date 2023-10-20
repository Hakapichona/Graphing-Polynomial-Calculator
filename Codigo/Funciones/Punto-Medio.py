from Codigo.Clases.Punto import Punto


def PuntoMedio(puntoA: Punto, puntoB: Punto):

    X_del_punto_medio = (puntoA.x + puntoB.x) / 2
    Y_del_punto_medio = (puntoA.y + puntoB.y) / 2

    if X_del_punto_medio % 1 == 0:
        X_del_punto_medio = int(X_del_punto_medio)

    if Y_del_punto_medio % 1 == 0:
        Y_del_punto_medio = int(Y_del_punto_medio)

    return f"({X_del_punto_medio}, {Y_del_punto_medio})"


print(PuntoMedio(Punto(3, 8), Punto(2, 2)))
