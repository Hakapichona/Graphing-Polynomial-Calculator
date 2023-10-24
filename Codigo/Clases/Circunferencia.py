class Circunferencia:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):

        if (self.a * self.a) + (self.b * self.b) - (4 * self.c) <= 0:
            return "Esta ecuacion no representa a una circunferencia"

        if self.a > 0:
            self.a = f"+{self.a}"
        if self.b > 0:
            self.b = f"+{self.b}"
        if self.c > 0:
            self.c = f"+{self.c}"

        return f"x²+y²{self.a}x{self.b}y{self.c}=0"


#Ejemplo
cia1 = Circunferencia(4, 9, -1)

print(cia1)
