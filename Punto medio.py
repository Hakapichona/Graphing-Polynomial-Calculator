"""
Punto medio entre dos puntos
"""
class puntos2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def puntomediox(self, otropunto):
        dx = self.x + otropunto.x
        puntomediox = dx / 2
        return puntomediox

    def puntomedioy(self, otropunto):
        dy = self.y + otropunto.y
        puntomedioy = dy / 2
        return puntomedioy


print("Ingrese las coordenadas del punto 1:")
A = float(input("Ingrese el valor de x: "))
B = float(input("Ingrese el valor de y: "))
print("Ingrese las coordenadas del punto 2:")
C = float(input("Ingrese el valor de x: "))
D = float(input("Ingrese el valor de y: "))

punto1 = puntos2d(A,B)
punto2 = puntos2d(C,D)

puntomediox = punto1.puntomediox(punto2)
puntomedioy = punto1.puntomedioy(punto2)

print("\nCalculo del punto medio entre dos puntos.")
print("------------------------------------------")
print(f"Punto1: ({A} , {B})")
print(f"Punto2: ({C} , {D}) ")
print(f"Punto Medio: ({puntomediox} , {puntomedioy}) ")


