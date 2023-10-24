"""
H- ECUACIÓN DE CIRCUNFERENCIA CON CENTRO Y RADIO DADO
"""
import math
from fractions import Fraction

class Punto2D:
    def __init__(self, h, k, radio):
        self.h = h
        self.k = k
        self.radio = radio

x = float(input("Ingrese el valor de x del Centro de la Circunferencia: "))
y = float(input("Ingrese el valor de y del Centro de la Circunferencia: "))

radio = float(input("Ingrese el valor del radio de la Circunferencia: "))

punto = Punto2D(x, y, radio)

x_fraction = Fraction(x).limit_denominator()
y_fraction = Fraction(y).limit_denominator()
denominator = Fraction(radio ** 2).limit_denominator()
radio_fraction = denominator

print("\nEcuación de la circunferencia con centro y radio dado:")
print("--------------------------------------------------------")
print(f"Punto del centro: ({x}, {y})")
print(f"Radio: {radio}")
print(f"Ecuación Canónica de la Circunferencia: (x - ({x_fraction}) )^2 + (y - ({y_fraction}) )^2 = {radio_fraction}")
print(f"Ecuación General de la Circunferencia: x^2 + y^2 + ({-2*x_fraction})x + ({-2*y_fraction})y + ({x_fraction**2 + y_fraction**2 - radio_fraction}) = 0")
