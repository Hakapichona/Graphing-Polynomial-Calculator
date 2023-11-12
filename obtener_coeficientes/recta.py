class Recta:

    def __init__(self, xa, yb, c):

        self.a = xa
        self.b = yb
        self.c = c

    
def sacar_coef(ecuacion):
        
    coef_final = []

    coeficientes = []

    ec = ecuacion.replace(" ", "")

    ec = ec.replace(f"{ecuacion[len(ecuacion)-1]}","")

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

