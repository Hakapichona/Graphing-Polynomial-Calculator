import math
from Codigo.Clases.Punto import Punto


class Circunferencia:

    def __init__(self, a, b, c):
        self.d = a
        self.e = b
        self.f = c

    def obtener_centro(self):
        h = -self.d / 2
        k = -self.e / 2
        return h, k

    def obtener_radio(self):
        r = math.sqrt(self.d**2 + self.e**2 - 4 * self.f) / 2
        return r

def crear_circunferencia():
    ecuacion = input(f"Ingrese la circunferencia en el formato 'x2 + y2 + ax + by + c = 0': ")

    coef_final = []

    coeficientes = []

    ec = ecuacion.replace(" ", "")

    ec = ec.replace(f"{ecuacion[len(ecuacion) - 1]}", "")

    ec = ec.replace("=", "")

    ec = ec.split('+')

    for termino in ec:

        if '-' in termino:

            termino = termino.split('-')

            coeficientes.append(termino[0])

            for componente in termino[1:]:
                coeficientes.append('-' + componente)

        else:

            coeficientes.append(termino)

    if 'x2' in coeficientes and 'y2' in coeficientes:

        # Aqui almacenamos en list todos los terminos de la ecuacion por separado
        list = []
        for termino in coeficientes:
            if termino != '' and termino != 'x2' and termino != 'y2':
                for coef in termino:
                    list.append(coef)

        for termino in coeficientes:

            if termino != '' and termino != 'x2' and termino != 'y2':

                char = ""

                for coef in termino:

                    if coef != 'x' and coef != 'y':

                        char += coef

                    else:

                        break

                if not char or char == '-' or char == '+':
                    char += '1'

                coef_final.append(int(char))

        if 'x' not in list and 'y' in list:

            return Circunferencia(0, coef_final[0], coef_final[1])

        elif 'y' not in list and 'x' in list:

            return Circunferencia(coef_final[0], 0, coef_final[1])

        elif 'x' not in list and 'y' not in list:

            return Circunferencia(0, 0, coef_final[0])

        else:

            return Circunferencia(coef_final[0], coef_final[1], coef_final[2])

    else:

        print("Error. Ingrese la ecuacion de una circunferencia.")


def print_circunferencia(c1):
    if c1.d < 0 and c1.e < 0 and c1.f < 0:

        print("circunferencia: x2 + y2 - %dx - %dy - %d = 0" % (abs(c1.d), abs(c1.e), abs(c1.f)))

    elif c1.d < 0 and c1.e < 0:

        print("circunferencia: x2 + y2 - %dx - %dy + %d = 0" % (abs(c1.d), abs(c1.e), c1.f))

    elif c1.d < 0 and c1.f < 0:

        print("circunferencia: x2 + y2 - %dx + %dy - %d = 0" % (abs(c1.d), c1.e, abs(c1.f)))

    elif c1.e < 0 and c1.f < 0:

        print("circunferencia: x2 + y2 + %dx - %dy - %d = 0" % (c1.d, abs(c1.e), abs(c1.f)))

    elif c1.d < 0:

        print("circunferencia: x2 + y2 - %dx + %dy + %d = 0" % (abs(c1.d), c1.e, c1.f))

    elif c1.e < 0:

        print("circunferencia: x2 + y2 + %dx - %dy + %d = 0" % (c1.d, abs(c1.e), c1.f))

    elif c1.f < 0:

        print("circunferencia: x2 + y2 + %dx + %dy - %d = 0" % (c1.d, c1.e, abs(c1.f)))


class Recta:

    def __init__(self, xa, yb, c):
        self.a = xa
        self.b = yb
        self.c = c

    def obtener_ordenada(self, x):
        if self.b != 0:
            y = (-self.a * x - self.c) / self.b
            return y
        else:
            return 0

    def Pendiente(self):
        pendiente = -(self.a / self.b)
        if pendiente % 1 == 0:
            return int(pendiente)
        return pendiente

def sacar_coef(ecuacion):
    coef_final = []

    coeficientes = []

    ec = ecuacion.replace(" ", "")

    ec = ec.replace(f"{ecuacion[len(ecuacion) - 1]}", "")

    ec = ec.replace("=", "")

    ec = ec.split('+')

    for termino in ec:

        if '-' in termino:

            termino = termino.split('-')

            coeficientes.append(termino[0])

            for componente in termino[1:]:
                coeficientes.append('-' + componente)

        else:

            coeficientes.append(termino)

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

    return Recta(coef_final[0], coef_final[1], coef_final[2])


def interseccion_recta_circunferencia(a, b, c, centro, radio):
    h, k = centro
    r = radio

    if b != 0:
        # Escribe la ecuación de la recta en términos de y = mx + n
        m = -a / b
        n = -c / b

        # Sustituye y = mx + n en la ecuación de la circunferencia
        A = 1 + m**2
        B = 2 * (m * n - m * k - h)
        C = k**2 - r**2 + h**2 - 2 * n * k + n**2

        # Encuentra las coordenadas x
        discriminante = B**2 - 4 * A * C
        if discriminante < 0:
            return []  # No hay intersecciones

        x1 = (-B + math.sqrt(discriminante)) / (2 * A)
        x2 = (-B - math.sqrt(discriminante)) / (2 * A)

        # Encuentra las coordenadas y correspondientes a x
        y1 = m * x1 + n
        y2 = m * x2 + n

        return [Punto(x1, y1), Punto(x2, y2)]

    else:
        # La recta es vertical, la ecuación es x = -c / a
        x = -c / a

        discriminante = r**2 - (x - h)**2
        if discriminante < 0:
            return []  # No hay intersecciones

        y1 = k + math.sqrt(discriminante)
        y2 = k - math.sqrt(discriminante)

        return [Punto(x, y1), Punto(x, y2)]

def obtener_recta():
    while True:

        recta = input(f"Ingrese la recta en el formato 'ax + by + c = 0': ")

        coef_final = []

        coeficientes = []

        ec = recta.replace(" ", "")

        ec = ec[:-1]

        # ec = ec.replace(f"{recta[len(recta)-1]}","")

        ec = ec.replace("=", "")

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



#Ejemplo de uso
r1 = obtener_recta()

c1 = crear_circunferencia()
centro = c1.obtener_centro()
radio =  c1.obtener_radio()


# Encontrar el punto de intersección
puntos_interseccion = interseccion_recta_circunferencia(r1.a, r1.b, r1.c, centro, radio)

if puntos_interseccion is not None:
    if isinstance(puntos_interseccion, Punto):
        print("Punto de intersección:", puntos_interseccion.x, puntos_interseccion.y)
    else:
        print("Puntos de intersección:")
        for punto in puntos_interseccion:
            print(punto.x, punto.y)
else:
    print("La recta y la circunferencia no se intersecan.")