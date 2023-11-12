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

    def recta_perpendicular(self, punto):

        m = -(self.a/self.b)

        if m == 0:

            return "No se puede calcular la recta perpendicular"
        
        m_perp = -(self.b/self.a)

        if self.b > 0 and self.a < 0:

            c = self.a*punto.y + self.b*punto.x

            mcd = math.gcd(math.gcd(self.a, self.b), self.c)

            if c > 0:

                return f"{self.b/mcd}x + {abs(self.a)/mcd}y + {c/mcd} = 0"
            
            else:

                return f"{self.b/mcd}x + {abs(self.a)/mcd}y - {abs(c)/mcd} = 0"
            
        elif self.b < 0 and self.a > 0:

            c = self.b*punto.x - self.a*punto.y

            mcd = math.gcd(math.gcd(self.a, self.b), self.c)

            if c > 0:

                return f"{abs(self.b)/mcd}x + {self.a/mcd}y + {c/mcd} = 0"
            
            else:

                return f"{abs(self.b)/mcd}x + {self.a/mcd}y - {abs(c)/mcd} = 0"
                
        elif self.b > 0 and self.a > 0:

            c = -self.b*punto.x + self.a*punto.y

            mcd = math.gcd(math.gcd(self.a, self.b), self.c)

            if c > 0:

                return f"{self.b/mcd}x - {abs(self.a)/mcd}y + {c/mcd} = 0"
            
            else:

                return f"{self.b/mcd}x - {abs(self.a)/mcd}y - {abs(c)/mcd} = 0"
                
        elif self.b < 0 and self.a < 0:

            c = self.a*punto.y + self.b*punto.x

            mcd = math.gcd(math.gcd(self.a, self.b), self.c)

            if c > 0:

                return f"{abs(self.b)/mcd}x - {abs(self.a)/mcd}y + {c/mcd} = 0"
            
            else:

                return f"{abs(self.b)/mcd}x - {abs(self.a)/mcd}y - {abs(c)/mcd} = 0"


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

recta1 = obtener_recta()
punto1 = obtener_punto("punto 1")

perpendicular = recta1.recta_perpendicular(punto1)

print("\nRecta perpendicular:")

print(perpendicular)