"""
J- HALLAR FOCO DE UNA PARÁBOLA
"""
class Parabola:
    def __init__(self, h, k, p):
        self.h = h
        self.k = k
        self.p = p

def calcular_foco(parabola, direccion):
    if direccion == 'x+':
        return parabola.h + parabola.p, parabola.k
    elif direccion == 'x-':
        return parabola.h - parabola.p, parabola.k
    elif direccion == 'y+':
        return parabola.h, parabola.k + parabola.p
    elif direccion == 'y-':
        return parabola.h, parabola.k - parabola.p

h = float(input("Ingrese el valor de h del vértice de la Parábola: "))
k = float(input("Ingrese el valor de k del vértice de la Parábola: "))
p = float(input("Ingrese el valor de p (distancia focal) de la Parábola: "))

direccion = input("Ingrese la dirección de la Parabola (x+, x-, y+, y-): ")

parabola = Parabola(h, k, p)

foco_x, foco_y = calcular_foco(parabola, direccion)

print("\nFoco de la parábola con vértice y distancia focal dados:")
print("--------------------------------------------------------")
print(f"Vértice: ({h}, {k})")
print(f"Distancia focal: {p}")
print(f"Direccion de la Parabola: {direccion}")
print(f"Foco: ({foco_x}, {foco_y})")
