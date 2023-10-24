"""
L- INTERSECCIÓN entre dos circunferencias

"""
from fractions import Fraction
import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

def interseccion(c1, c2):
    dx = Fraction(c2.centro[0] - c1.centro[0])
    dy = Fraction(c2.centro[1] - c1.centro[1])
    d = math.sqrt(dx * dx + dy * dy)

    if d > c1.radio + c2.radio:
        print("Los círculos no se intersectan.")
        return None
    elif d < abs(c1.radio - c2.radio):
        print("Un círculo está dentro del otro.")
        return None
    elif d == 0 and c1.radio == c2.radio:
        print("Los círculos son coincidentes.")
        return None

    a = (c1.radio * c1.radio - c2.radio * c2.radio + d * d) / (2.0 * d)
    h = math.sqrt(c1.radio * c1.radio - a * a)
    x2 = c1.centro[0] + (dx * a / d)
    y2 = c1.centro[1] + (dy * a / d)
    rx = -dy * (h / d)
    ry = dx * (h / d)

    xi = x2 + rx
    xi_prime = x2 - rx
    yi = y2 + ry
    yi_prime = y2 - ry

    return (float(xi), float(yi), float(xi_prime), float(yi_prime))

x1 = Fraction(input("Ingrese la coordenada x del centro del primer círculo: "))
y1 = Fraction(input("Ingrese la coordenada y del centro del primer círculo: "))
r1 = Fraction(input("Ingrese el radio del primer círculo: "))
c1 = Circulo((x1, y1), r1)

x2 = Fraction(input("Ingrese la coordenada x del centro del segundo círculo: "))
y2 = Fraction(input("Ingrese la coordenada y del centro del segundo círculo: "))
r2 = Fraction(input("Ingrese el radio del segundo círculo: "))
c2 = Circulo((x2, y2), r2)

interseccion_points = interseccion(c1, c2)
if interseccion_points is not None:
    print(f"Los puntos de intersección son ({interseccion_points[0]}, {interseccion_points[1]}) y ({interseccion_points[2]}, {interseccion_points[3]})")
