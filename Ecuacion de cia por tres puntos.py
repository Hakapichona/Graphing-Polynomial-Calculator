"""
I- ECUACIÓN DE CIRCUNFERENCIA POR TRES PUNTOS
"""
import math
from fractions import Fraction

class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def punto_medio(p1, p2):
    return Punto2D((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

def pendiente(p1, p2):
    return (p2.y - p1.y) / (p2.x - p1.x)

def interseccion(puntoMedio, pendiente):
    return puntoMedio.y - pendiente * puntoMedio.x

x1 = float(input("Ingrese el valor de x del Punto 1: "))
y1 = float(input("Ingrese el valor de y del Punto 1: "))
punto1 = Punto2D(x1, y1)

x2 = float(input("Ingrese el valor de x del Punto 2: "))
y2 = float(input("Ingrese el valor de y del Punto 2: "))
punto2 = Punto2D(x2, y2)

x3 = float(input("Ingrese el valor de x del Punto 3: "))
y3 = float(input("Ingrese el valor de y del Punto 3: "))
punto3 = Punto2D(x3, y3)

puntoMedio12 = punto_medio(punto1, punto2)
puntoMedio23 = punto_medio(punto2, punto3)

pendiente12 = -1 / pendiente(punto1, punto2)
pendiente23 = -1 / pendiente(punto2, punto3)

b12 = interseccion(puntoMedio12, pendiente12)
b23 = interseccion(puntoMedio23, pendiente23)

if pendiente12 != pendiente23:
    h = (b23 - b12) / (pendiente12 - pendiente23)
    k = pendiente12 * h + b12
else:
    print("Los puntos ingresados no forman una circunferencia válida.")
    exit()

radio = math.sqrt((x1 - h)**2 + (y1 - k)**2)

h_fraction = Fraction(h).limit_denominator()
k_fraction = Fraction(k).limit_denominator()
radio_fraction = Fraction(radio**2).limit_denominator()

print("\nEcuación de la circunferencia por tres puntos:")
print("------------------------------------------------")
print(f"Punto 1: ({x1}, {y1})")
print(f"Punto 2: ({x2}, {y2})")
print(f"Punto 3: ({x3}, {y3})")
print(f"Ecuación Canónica de la Circunferencia: (x - ({h_fraction}) )^2 + (y - ({k_fraction}) )^2 = {radio_fraction}")
print(f"Ecuación General de la Circunferencia: x^2 + y^2 + ({-2*h_fraction})x + ({-2*k_fraction})y + ({h_fraction**2 + k_fraction**2 - radio_fraction}) = 0")

