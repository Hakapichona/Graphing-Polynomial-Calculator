from Codigo.Clases.Punto import Punto


def Recta1(puntoA: Punto, puntoB: Punto):
    if puntoA.x == puntoB.x:
        if puntoA.x == 0:
            return f"x=0"
        elif puntoA.x > 0:
            return f"x+{puntoA.x}=0"
        elif puntoA.x < 0:
            return f"x{puntoA.x}=0"
    else:
        m = round((puntoB.y - puntoA.y) / (puntoB.x - puntoA.x), 2)
        if m % 1 == 0:
            m = int(m)
            print(m)
        else:
            m = round(m, 2)

    termino_independiente = - puntoA.y + m * puntoA.x
    if termino_independiente % 1 == 0:
        termino_independiente = int(termino_independiente)
    else:
        termino_independiente = round(termino_independiente, 2)

    if m == 1:
        if termino_independiente > 0:
            return f"-x+y+{termino_independiente}=0"
        elif termino_independiente < 0:
            return f"-x+y{termino_independiente}=0"
        else:
            return f"-x+y=0"
    elif m == -1:
        if termino_independiente > 0:
            return f"x+y+{termino_independiente}=0"
        elif termino_independiente < 0:
            return f"x+y{termino_independiente}=0"
        else:
            return f"x+y=0"
    elif m == 0:
        if termino_independiente > 0:
            return f"y+{termino_independiente}=0"
        elif termino_independiente < 0:
            return f"y{termino_independiente}=0"
        else:
            return f"y=0"
    elif m > 0:
        if termino_independiente > 0:
            return f"-{m}x+y+{termino_independiente}=0"
        if termino_independiente < 0:
            return f"-{m}x+y{termino_independiente}=0"
        else:
            return f"-{m}x+y=0"
    elif m < 0:
        if termino_independiente > 0:
            return f"{-m}x+y+{termino_independiente}=0"
        elif termino_independiente < 0:
            return f"{-m}x+y{termino_independiente}=0"
        else:
            return f"{-m}x+y=0"

# ecuacion = Recta1(Punto(0,0),Punto(0,1))
# print(ecuacion)
