from Codigo.Clases.Punto import Punto


def Recta2(PuntoA: Punto, Pendinte: float):
    terminoIndependiente = PuntoA.x * Pendinte - PuntoA.y

    if Pendinte == 0:
        if PuntoA.y == 0:
            return f"y=0"
        else:
            return f"y={PuntoA.y}"

    if Pendinte > 0:
        if terminoIndependiente < 0:
            return f"y{-Pendinte}x-{abs(terminoIndependiente)}=0"

        elif terminoIndependiente > 0:
            return f"y{-Pendinte}x+{abs(terminoIndependiente)}=0"
        else:
            return f"y{-Pendinte}x=0"

    if Pendinte < 0:
        if terminoIndependiente < 0:
            return f"{-Pendinte}x+y-{abs(terminoIndependiente)}=0"
        elif terminoIndependiente > 0:
            return f"{-Pendinte}x+y+{abs(terminoIndependiente)}=0"
        else:
            return f"x{-Pendinte}y=0"


# Ejemplo

miRecta = Recta2(Punto(0, -1), 8)

print(miRecta)
