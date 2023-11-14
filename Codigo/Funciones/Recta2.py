from Codigo.Clases.Punto import Punto


def Recta2(PuntoA: Punto, Pendinte: float):
    terminoIndependiente = PuntoA.x * Pendinte - PuntoA.y

    if terminoIndependiente % 1 == 0:
        terminoIndependiente = int(terminoIndependiente)
    else:
        terminoIndependiente = round(terminoIndependiente, 2)

    if Pendinte == 0:
        if PuntoA.y == 0:
            return f"y=0"
        else:
            return f"y={PuntoA.y}"

    if Pendinte > 0:
        if Pendinte == 1:
            if terminoIndependiente < 0:
                return f"x-y+{abs(terminoIndependiente)}=0"

            elif terminoIndependiente > 0:
                return f"x-y-{abs(terminoIndependiente)}=0"
            else:
                return f"x+y=0"

        if terminoIndependiente < 0:
            return f"{-1 * -Pendinte}x-y+{abs(terminoIndependiente)}=0"

        elif terminoIndependiente > 0:
            return f"{-1 * -Pendinte}x-y-{abs(terminoIndependiente)}=0"
        else:
            return f"{-Pendinte}x+y=0"

    if Pendinte < 0:
        if terminoIndependiente < 0:
            return f"{-Pendinte}x+y-{abs(terminoIndependiente)}=0"
        elif terminoIndependiente > 0:
            return f"{-Pendinte}x+y+{abs(terminoIndependiente)}=0"
        else:
            return f"{-Pendinte}x+y=0"

# Ejemplo

# miRecta = Recta2(Punto(-3, 9), 1)

# print(miRecta)
