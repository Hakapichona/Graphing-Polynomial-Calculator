"""
D-ECUACIÓN DE RECTA POR UN PUNTO Y LA PENDIENTE

"""
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Recta:
    def __init__(self, punto, pendiente):
        self.punto = punto
        self.pendiente = pendiente

    def ecuacion_recta(self):
        x1 = self.punto.x
        y1 = self.punto.y
        m = self.pendiente
        b = y1 - m * x1
        return f"Ecuación de la recta: y = {m} x  +  ({b})"

x_punto = float(input("Ingrese el valor de x del punto: "))
y_punto = float(input("Ingrese el valor de y del punto: "))

pendiente = float(input("Ingrese la pendiente de la recta: "))

punto = Punto2D(x_punto, y_punto)
recta = Recta(punto, pendiente)

ecuacion = recta.ecuacion_recta()

print("\nEcuación de la recta por un punto y la pendiente:")
print("--------------------------------------------------")
print(f"Punto: ({x_punto}, {y_punto})")
print(f"Pendiente: {pendiente}")
print(ecuacion)

