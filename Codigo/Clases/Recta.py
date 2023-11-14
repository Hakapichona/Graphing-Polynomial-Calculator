class Recta:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.b > 0:
            self.b = f"+{self.b}"
        if self.c > 0:
            self.c = f"+{self.c}"

        return f"{self.a}x{self.b}y{self.c}=0"

    def Pendiente(self):
        pendiente = -(self.a / self.b)
        if pendiente % 1 == 0:
            return int(pendiente)
        return round(pendiente, 2)

# Ejemplo
# recta1 = Recta(4, 1, 8)
# print(recta1)
