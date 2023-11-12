from Codigo.Clases.Punto import Punto

def Recta1(puntoA: Punto, puntoB: Punto):
    if puntoA.x == puntoB.x:
        if puntoA.x == 0:
            return f"x=0"
        else:
            return f"x-{puntoA.x}=0"
    else:
        m = (puntoB.y - puntoA.y) / (puntoB.x - puntoA.x)
        if m % 1 == 0:
            m = int(m)

    termino_independiente = puntoA.y - m * puntoA.x
    if termino_independiente % 1 == 0:
        termino_independiente = int(termino_independiente)


    if m > 0:
        if m == 1:
            if termino_independiente == 0:
                return f"x-y=0"
            else:
                return f"x-y+{termino_independiente}=0"
        else:
            if termino_independiente == 0:
                return f"{m}x-y=0"
            else:
                if termino_independiente > 0:
                    return f"{m}x-y+{termino_independiente}=0"
                else:
                    return f"{m}x-y-{-1*termino_independiente}=0"
    elif m < 0:
        if m == -1:
            if termino_independiente == 0:
                return f"-x+y=0"
            else:
                return f"-x+y-{termino_independiente}=0"
        else:
            if termino_independiente == 0:
                return f"{-1*m}x+y=0"
            else:
                if termino_independiente > 0:
                    return f"{-1*m}x+y-{termino_independiente}=0"
                else:
                    return f"{-1 * m}x+y+{-1*termino_independiente}=0"
    elif m == 0:
        if termino_independiente == 0:
            return f"y=0"
        else:
            return f"y-{termino_independiente}=0"

#ecuacion = Recta1(Punto(0,0),Punto(0,1))
#print(ecuacion)