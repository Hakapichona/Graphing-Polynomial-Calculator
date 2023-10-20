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

        return f"{self.a}X{self.b}Y{self.c}"


recta1 = Recta(2, 5, 7)

print(recta1)
