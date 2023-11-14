class CircunferenciaCompleta:
    def __init__(self, D: float, E: float, F: float):
        self.D = D
        self.E = E
        self.F = F

    def __str__(self):

        if (self.D * self.D) + (self.E * self.E) - (4 * self.F) <= 0:
            return "Esta ecuacion no representa a una circunferencia"

        if self.D > 0:
            self.D = f"+{self.D}"
        if self.E > 0:
            self.E = f"+{self.E}"
        if self.F > 0:
            self.F = f"+{self.F}"

        return f"x²+y²{self.D}x{self.E}y{self.F}=0"


class CircunferenciaReducida:
    def __init__(self, h: float, k: float, r: float):
        self.h = h
        self.k = k
        self.r = r
        if self.h % 1 == 0 and self.k % 1 == 0:
            self.h = int(h)
            self.k = int(k)

    def __str__(self):
        if self.r < 0:
            return "El radio no puede ser negativo"
        if self.r == 0:
            return "El radio debe ser mayor a 0 para obtener una circunferencia"


        if self.h > 0 and self.k > 0:
            return f"(x{-self.h})²+(y{-self.k})²={self.r}²"
        elif self.h < 0 and self.k < 0:
            return f"(x+{abs(self.h)})²+(y+{abs(self.k)})²={self.r}²"
        elif self.h < 0 and self.k > 0:
            return f"(x+{abs(self.h)})²+(y{-self.k})²={self.r}²"
        elif self.h > 0 and self.k < 0:
            return f"(x{-self.h})²+(y+{abs(self.k)})²={self.r}²"



# Ejemplo
#cia1 = CircunferenciaReducida(4, 9, 5)
#print(cia1)
