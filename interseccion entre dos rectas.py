"""
L- INTERSECCIÓN entre dos rectas

"""
from fractions import Fraction

class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Recta:
    def __init__(self, m, b):
        self.m = Fraction(m)
        self.b = Fraction(b)

    def interseccion(self, otra_recta):
        x = (otra_recta.b - self.b) / (self.m - otra_recta.m)
        y = self.m * x + self.b
        return Punto2D(x, y)

m1 = input("Ingrese la pendiente de la primera recta: ")
b1 = input("Ingrese la intersección con el eje y de la primera recta: ")

recta1 = Recta(m1, b1)

m2 = input("Ingrese la pendiente de la segunda recta: ")
b2 = input("Ingrese la intersección con el eje y de la segunda recta: ")

recta2 = Recta(m2, b2)

interseccion = recta1.interseccion(recta2)
print(f"El punto de intersección es ({float(interseccion.x)}, {float(interseccion.y)})")
