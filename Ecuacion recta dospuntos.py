"""
E- ECUACIÓN DE RECTA POR DOS PUNTOS
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


x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

punto1 = Punto2D(x1, y1)
punto2 = Punto2D(x2, y2)

recta = Recta(punto1, punto2)

ecuacion = recta.ecuacion_recta()

print("\nEcuación de la recta por dos puntos:")
print("--------------------------------------")
print(f"Punto 1: ({x1}, {y1})")
print(f"Punto 2: ({x2}, {y2})")
print(ecuacion)