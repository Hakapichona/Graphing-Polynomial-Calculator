class Parabola:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.b > 0:
            self.b = f"+{self.b}"
        if self.c > 0:
            self.c = f"+{self.c}"

        return f"{self.a}x²{self.b}y{self.c}=0"


# Ejemplo
#parabola1 = Parabola(-2, 6, -2)
#print(parabola1)
