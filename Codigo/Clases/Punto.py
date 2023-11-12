class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


# Ejemplo
# punto1 = Punto(-2, 4)
# print(punto1)
