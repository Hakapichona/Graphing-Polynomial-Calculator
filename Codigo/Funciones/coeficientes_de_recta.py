class Recta:

    def __init__(self, xa, yb, c):

        self.a = xa
        self.b = yb
        self.c = c

    
def sacar_coef():

    while True:

        recta= input(f"Ingrese la recta en el formato 'ax + by + c = 0': ")
        
        coef_final = []

        coeficientes = []

        ec = recta.replace(" ", "")

        ec = ec[:-1]

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
            
sacar_coef()

