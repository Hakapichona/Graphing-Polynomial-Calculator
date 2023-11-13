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

    def punto_interseccion(self, otra_recta):
        a, b, c = otra_recta.a, otra_recta.b, otra_recta.c
        determinante = self.a * b - a * self.b

        if determinante == 0:  # Verificar si las rectas son paralelas
            return None  # No hay punto de intersección

        x = -1*((self.c * b - c * self.b) / determinante)
        y = -1*((self.a * c - a * self.c) / determinante)
        return Punto(x, y)


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



# Ejemplo de uso
recta1 = obtener_recta()
recta2 = obtener_recta()

if recta1 and recta2:  # Verificar si las rectas son válidas
    interseccion = recta1.punto_interseccion(recta2)
    if interseccion:
        print("Punto de intersección:", interseccion)
    else:
        print("Las rectas son paralelas, no hay punto de intersección.")
else:
    print("Las ecuaciones de las rectas no son válidas.")