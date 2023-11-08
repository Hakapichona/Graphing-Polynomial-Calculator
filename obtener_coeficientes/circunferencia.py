#CORREGIDO

class Circunferencia:

    def __init__(self, a, b, c):

        self.d = a
        self.e = b
        self.f = c

    
def crear_circunferencia():

    ecuacion= input(f"Ingrese la circunferencia en el formato 'x2 + y2 + ax + by + c = 0': ")
    
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

    if 'x2' in coeficientes and 'y2' in coeficientes:

        #Aqui almacenamos en list todos los terminos de la ecuacion por separado
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

        print( "circunferencia: x2 + y2 - %dx - %dy - %d = 0" %( abs(c1.d), abs(c1.e), abs(c1.f) ) )

    elif c1.d < 0 and c1.e < 0:

        print( "circunferencia: x2 + y2 - %dx - %dy + %d = 0" %( abs(c1.d), abs(c1.e), c1.f ) )

    elif c1.d < 0 and c1.f < 0:

        print( "circunferencia: x2 + y2 - %dx + %dy - %d = 0" %( abs(c1.d), c1.e, abs(c1.f) ) )

    elif c1.e < 0 and c1.f < 0:

        print( "circunferencia: x2 + y2 + %dx - %dy - %d = 0" %( c1.d, abs(c1.e), abs(c1.f) ) )

    elif c1.d < 0:

        print( "circunferencia: x2 + y2 - %dx + %dy + %d = 0" %( abs(c1.d), c1.e, c1.f ) )

    elif c1.e < 0:

        print( "circunferencia: x2 + y2 + %dx - %dy + %d = 0" %( c1.d, abs(c1.e), c1.f ) )

    elif c1.f < 0:

        print( "circunferencia: x2 + y2 + %dx + %dy - %d = 0" %(c1.d, c1.e, abs(c1.f) ) )


c1 = crear_circunferencia()

print_circunferencia(c1)
