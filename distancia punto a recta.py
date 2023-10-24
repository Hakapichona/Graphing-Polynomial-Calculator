"""
C- DISTANCIA DE UNA PUNTO A UNA RECTA
"""
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Recta:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def distanciapuntorecta(self, punto):
        numerador = abs(self.A * punto.x + self.B * punto.y + self.C)
        denominador = (self.A**2 + self.B**2)**0.5
        return numerador / denominador

x_punto = float(input("Ingrese el valor de x del punto: "))
y_punto = float(input("Ingrese el valor de y del punto: "))

A_recta = float(input("Ingrese el coeficiente A de la recta: "))
B_recta = float(input("Ingrese el coeficiente B de la recta: "))
C_recta = float(input("Ingrese el coeficiente C de la recta: "))

punto = Punto2D(x_punto, y_punto)
recta = Recta(A_recta, B_recta, C_recta)

distancia = recta.distanciapuntorecta(punto)

print("\nCálculo de la distancia entre un punto y una recta:")
print("-----------------------------------------------------")
print(f"Punto: ({x_punto}, {y_punto})")
print(f"Recta: {A_recta} x  +  ({B_recta}) y  +  ({C_recta}) = 0")
print(f"Distancia entre el punto y la recta: {distancia}")

