"""
- DISTANCIA ENTRE DOS PUNTOS
"""
class puntos2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        distancia_cuadrada = dx * dx + dy * dy
        return distancia_cuadrada ** 0.5

print("Ingrese las coordenadas del punto 1:")
A = float(input("Ingrese el valor de x: "))
B = float(input("Ingrese el valor de y: "))
print("Ingrese las coordenadas del punto 2:")
C = float(input("Ingrese el valor de x: "))
D = float(input("Ingrese el valor de y: "))
print()
punto1 = puntos2d(A,B)
punto2 = puntos2d(C,D)

distancia= punto1.distancia(punto2)



print("\nCalculo de la distancia entre dos puntos.")
print("------------------------------------------")
print(f"Punto1: ({A} , {B})")
print(f"Punto2: ({C} , {D}) ")
print(f"La Distancia es: {distancia}")
