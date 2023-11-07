class Recta:
    def __init__(self, ecuacion):
        # Divide la ecuación en términos separados por '+' o '-'
        terminos = ecuacion.split('+')
        a, b, c = 0, 0, 0
        ec = ecuacion
        for termino in terminos:
            partes = termino.split('-')
            if len(partes) == 1:  # No hay '-' en el término
                coeficiente = partes[0].strip()
                if 'x' in coeficiente:
                    a = eval(coeficiente.replace('x', '*1'))
                elif 'y' in coeficiente:
                    b = eval(coeficiente.replace('y', '*1'))
                elif '=' in coeficiente:
                    c = -eval(coeficiente.replace('=', '*1'))
            else:
                # Término con '-'
                coeficiente = partes[0].strip()
                if 'x' in coeficiente:
                    a = eval(coeficiente.replace('x', '*1'))
                elif 'y' in coeficiente:
                    b = eval(coeficiente.replace('y', '*1'))
                elif '=' in coeficiente:
                    c = -eval(coeficiente.replace('=', '*1'))

        self.a = a
        self.b = b
        self.c = c
        self.ec = ec

    def obtener_coeficientes(self):
        return self.a, self.b, self.c

    def __str__(self):
        return f"{ecuacion_recta.ec}"

# Ejemplo de uso
ecuacion_recta = Recta('2x+3y-1=0')
coeficientes = ecuacion_recta.obtener_coeficientes()
print("Coeficientes de la recta:", coeficientes)
print(ecuacion_recta)

