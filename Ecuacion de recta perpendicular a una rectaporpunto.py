"""
G- ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO
"""
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Recta:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def ecuacion_recta(self):
        x1 = self.punto1.x
        y1 = self.punto1.y
        x2 = self.punto2.x
        y2 = self.punto2.y

        if x2 - x1 == 0:
            return "La recta es vertical, no se puede calcular la pendiente."

        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return f"Ecuación de la recta: y = {m} x  +  ({b})"

    def recta_perpendicular(self, punto):
        m = (self.punto2.y - self.punto1.y) / (self.punto2.x - self.punto1.x)
        if m == 0:
            return "La recta es horizontal, no se puede calcular la perpendicular."
        m_perpendicular = -1 / m
        b = punto.y - m_perpendicular * punto.x
        return f"Ecuación de la recta perpendicular: y = {m_perpendicular} x  +  ({b})"

x1 = float(input("Ingrese la coordenada x del primer punto de la recta: "))
y1 = float(input("Ingrese la coordenada y del primer punto de la recta: "))
x2 = float(input("Ingrese la coordenada x del segundo punto de la recta: "))
y2 = float(input("Ingrese la coordenada y del segundo punto de la recta: "))

punto1 = Punto2D(x1, y1)
punto2 = Punto2D(x2, y2)

recta = Recta(punto1, punto2)

x3 = float(input("Ingrese la coordenada x del punto por el que pasa la recta perpendicular: "))
y3 = float(input("Ingrese la coordenada y del punto por el que pasa la recta perpendicular: "))

punto_perpendicular = Punto2D(x3, y3)

ecuacion = recta.ecuacion_recta()
ecuacion_perpendicular = recta.recta_perpendicular(punto_perpendicular)

print("\nEcuación de la recta original:")
print(f"Punto 1: ({x1}, {y1})")
print(f"Punto 2: ({x2}, {y2})")
print(ecuacion)

print("\nEcuación de la recta perpendicular:")
print(f"Punto por el que pasa la recta perpendicular: ({x3}, {y3})")
print(ecuacion_perpendicular)
