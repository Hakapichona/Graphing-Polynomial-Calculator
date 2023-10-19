class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({puntoa.x},{puntoa.y})"



puntoa = Punto(3, 2)

print(puntoa)

