from Codigo.Clases.Recta import Recta
from Codigo.Clases.Punto import Punto


def RectaParalela(Recta: Recta, Punto: Punto):
    pendiente = Recta.Pendiente()

    if pendiente > 0:

        terminoIndependiente = (Recta.b * Punto.y) + (Recta.a * Punto.x)

        if terminoIndependiente < 0:
            if Recta.a > 0 and Recta.b > 0:
                return f"{Recta.a}x+{Recta.b}y-{abs(terminoIndependiente)}=0"
            elif Recta.a < 0 and Recta.b > 0:
                return f"{abs(Recta.a)}x-{Recta.b}y+{abs(terminoIndependiente)}=0"
            elif Recta.a > 0 and Recta.b < 0:
                return f"{Recta.a}x-{abs(Recta.b)}y-{abs(terminoIndependiente)}=0"
            else:
                return f"{abs(Recta.a)}x+{abs(Recta.b)}y+{abs(terminoIndependiente)}=0"
        elif terminoIndependiente > 0:
            if Recta.a > 0 and Recta.b > 0:
                return f"{Recta.a}x+{Recta.b}y+{abs(terminoIndependiente)}=0"
            elif Recta.a < 0 and Recta.b > 0:
                return f"{abs(Recta.a)}x-{Recta.b}y-{abs(terminoIndependiente)}=0"
            elif Recta.a > 0 and Recta.b < 0:
                return f"{Recta.a}x-{abs(Recta.b)}y+{abs(terminoIndependiente)}=0"
            else:
                return f"{abs(Recta.a)}x+{abs(Recta.b)}y-{abs(terminoIndependiente)}=0"
        else:
            return f"y{-pendiente}x=0"

    if pendiente < 0:

        terminoIndependiente = (Recta.b * Punto.y) - (Recta.a * Punto.x)

        if terminoIndependiente < 0:
            if Recta.a > 0 and Recta.b > 0:
                return f"{Recta.a}x+{Recta.b}y-{abs(terminoIndependiente)}=0"
            elif Recta.a < 0 and Recta.b > 0:
                return f"{abs(Recta.a)}x-{Recta.b}y+{abs(terminoIndependiente)}=0"
            elif Recta.a > 0 and Recta.b < 0:
                return f"{Recta.a}x-{abs(Recta.b)}y-{abs(terminoIndependiente)}=0"
            else:
                return f"{abs(Recta.a)}x+{abs(Recta.b)}y+{abs(terminoIndependiente)}=0"
        elif terminoIndependiente > 0:
            if Recta.a > 0 and Recta.b > 0:
                return f"{Recta.a}x+{Recta.b}y+{abs(terminoIndependiente)}=0"
            elif Recta.a < 0 and Recta.b > 0:
                return f"{abs(Recta.a)}x-{Recta.b}y-{abs(terminoIndependiente)}=0"
            elif Recta.a > 0 and Recta.b < 0:
                return f"{Recta.a}x-{abs(Recta.b)}y+{abs(terminoIndependiente)}=0"
            else:
                return f"{abs(Recta.a)}x+{abs(Recta.b)}y-{abs(terminoIndependiente)}=0"
        else:
            return f"{Recta.a}x+{Recta.b}y=0"

    return f"La recta paralela a {Recta} es: {rectaParalela}"


# Ejemplo
rectaParalela = RectaParalela(Recta(-2, -3, 5), Punto(4, 6))

print(rectaParalela)
