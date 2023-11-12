"""
C- DISTANCIA DE UNA PUNTO A UNA RECTA
"""
import math

class Punto:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):

        return f"({self.x}, {self.y})"


class Recta:

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    def __str__(self):

        if self.a != -1:

            a_str = f"{self.a}x"

        else:

            a_str = "-x"
            
        if self.b > 0:

            b_str = f" + {self.b}y"

        else:

            b_str = f" - {abs(self.b)}y"

        if self.c > 0:

            c_str = f" + {self.c}"

        elif self.c < 0:

            c_str = f" - {abs(self.c)}"

        else:

            c_str = ""

        return f"{a_str}{b_str}{c_str} = 0"

    def distancia(self, punto):
        numerador = abs(self.a * punto.x + self.b * punto.y + self.c)
        denominador = math.sqrt(self.a ** 2 + self.b ** 2)
        return numerador / denominador


def obtener_punto(nombre_punto):
    while True:
        punto = input(f"Ingrese las coordenadas del {nombre_punto} en el formato '(x,y)': ")
        punto = punto.replace(" ", "")

        if "(" in punto and ")" in punto:
            punto = punto.replace("(", "")
            punto = punto.replace(")", "")

            coordenadas = []
            for coord in punto.split(","):
                if coord:
                    try:
                        coordenadas.append(float(coord))
                    except ValueError:
                        print("Por favor, asegúrate de ingresar solo números.")
                        break

            if len(coordenadas) == 2:
                return Punto(coordenadas[0], coordenadas[1])
        else:
            print("Por favor, asegúrate de ingresar las coordenadas correctamente en el formato '(x,y)'.")

"""
def signoscorrectos(lista):

    if 'x' in lista and 'y' in lista:

        if (lista[lista.index('x')+1] == '+' or lista[lista.index('x')+1] == '-') and (lista[lista.index('y')+1] == '+' or lista[lista.index('y')+1] == '-'):

            return True
        
        else:
        
            return False

"""

def obtener_recta():

    while True:

        recta= input(f"Ingrese la recta en el formato 'ax + by + c = 0': ")
        
        coef_final = []

        coeficientes = []

        ec = recta.replace(" ", "")

        ec = ec[:-1]

        #ec = ec.replace(f"{recta[len(recta)-1]}","")

        ec = ec.replace("=","")

        ec = ec.split('+')

        for termino in ec:

            if '-' in termino:

                termino = termino.split('-')

                coeficientes.append(termino[0])

                for componente in termino[1:]:

                    coeficientes.append('-' + componente)

            else:

                coeficientes.append(termino)

        list = []

        for termino in coeficientes:

            if termino != '':

                for coef in termino:

                    list.append(coef)

        print(list)

        for letra in list:

            if isinstance(letra, str) and letra.isalpha():

                if letra == 'x' or letra == 'y':

                    error = False
                
                else:

                    error = True

                    break

        if error:

            continue

        for termino in coeficientes:

            if termino != '':

                char = ""

                for coef in termino:

                    if coef != 'x' and coef != 'y':

                        char += coef

                    else:

                        break

                if not char or char == '-' or char == '+':

                    char += '1'

                coef_final.append(int(char))

        if 'x' in list and 'y' not in list and len(coef_final) == 2:

            return Recta(coef_final[0], 0, coef_final[1])
        
        elif 'x' in list and 'y' not in list and len(coef_final) == 1:

            return Recta(coef_final[0], 0, 0)
        
        elif 'x' not in list and 'y' in list and len(coef_final) == 1:

            return Recta(0, coef_final[0], 0)        

        elif 'x' not in list and 'y' in list and len(coef_final) == 2:

            return Recta(0, coef_final[0], coef_final[1])
        
        elif 'x' in list and 'y' in list and len(coef_final) == 2:

            return Recta(coef_final[0], coef_final[1], 0)
        
        elif 'x' in list and 'y' in list and len(coef_final) == 3:

            return Recta(coef_final[0], coef_final[1], coef_final[2])

punto1 = obtener_punto("punto 1")
recta1 = obtener_recta()

distancia = recta1.distancia(punto1)

print("\nCálculo de la distancia entre un punto y una recta:")
print("-----------------------------------------------------")
print(f"Punto: {punto1}")
print(f"Recta: {recta1}")
print(f"Distancia entre el punto y la recta: {distancia}")