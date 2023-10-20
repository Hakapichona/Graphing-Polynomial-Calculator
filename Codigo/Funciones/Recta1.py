from Codigo.Clases.Punto import Punto

def Recta1(puntoA: Punto, puntoB: Punto):
    if puntoA.x == puntoB.x:
        return f"x = {puntoA.x}"
    else:
        m = (puntoB.y - puntoA.y) / (puntoB.x - puntoA.x)
        if m % 1 == 0:
            m = int(m)

    termino_independiente = puntoA.y - m * puntoA.x
    if termino_independiente % 1 == 0:
        termino_independiente = int(termino_independiente)

    if m >= 0:
        return f"{m}x - y + {termino_independiente} = 0"
    else:
        return f"{-1*m}x + y - {termino_independiente} = 0"





ecuacion = Recta1(Punto(1,2),Punto(-3,4/5))
print(ecuacion)