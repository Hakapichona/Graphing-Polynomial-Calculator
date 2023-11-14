from sympy import symbols, solve, N


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

    while len(coef_final) < 3:
        coef_final.append(0)

    return Parabola(coef_final[0], coef_final[1], coef_final[2])


def interseccion(p1, p2):
    x, y = symbols('x y')

    eq1 = p1.a * x ** 2 + p1.b * y + p1.c
    eq2 = p2.a * x ** 2 + p2.b * y + p2.c

    sol = solve((eq1, eq2), (x, y))

    sol_decimal = [(N(sol[i][0]), N(sol[i][1])) for i in range(len(sol))]
    return sol_decimal


Parabola1 = sacar_coef('2x2+3y-1=0')
Parabola2 = sacar_coef('-x2+4y+2=0')

print(interseccion(Parabola1, Parabola2))