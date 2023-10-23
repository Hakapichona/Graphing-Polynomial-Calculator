import math
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from os import *

style.use("dark_background")


def muestreo():
    plt.ion()
    plt.grid(lw=0.5)
    plt.xlabel(r"$coordenada x$", c='green')
    plt.ylabel(r"$coordenada y$", c='green')
    plt.show(block=True)


def pointGraf():
    x = 6
    y = 5
    plt.title("Punto")
    plt.plot(x, y, 'rx')


def parGraf():
    x = []
    y = []
    for i in range(-15, 15):
        x.append(3 + i)
        y.append(5 + i ** 2)
    plt.title("Parabola")
    plt.plot(x, y, 'g')


def secMGraf():
    x = []
    y = []
    for i in range(360):
        x.append(10 + i)
        y.append(30 + i)
    plt.title("Segmento")
    plt.plot(x, y, 'g')


def rectGraf():
    x = []
    y = []
    for i in range(360):
        x.append(10 + i)
        y.append(30 + i)
    plt.title("Recta")
    plt.plot(x, y, 'g')


def ciaGraf():
    x = []
    y = []
    h = 10
    k = 30
    ratio = 5
    c = 0.5
    for c in range(0, 720):
        x.append(h + ratio*math.sin(c))
        y.append(k + ratio*math.cos(c))
        c -= 0.5
    plt.title("Circunferencia")
    plt.xlim((h-(ratio*2))-(0.5*ratio), (h+(ratio*2)+(0.5*ratio)))
    plt.ylim(k-(ratio*2), k+(ratio*2))
    plt.plot(x, y, 'go')


print("""A- PUNTO MEDIO DE UN SEGMENTO\nB- DISTANCIA ENTRE DOS PUNTOS
C- DISTANCIA DE UNA PUNTO A UNA RECTA\nD- ECUACIÓN DE RECTA POR UN PUNTO Y LA PENDIENTE
E- ECUACIÓN DE RECTA POR DOS PUNTOS\nF- ECUACIÓN DE RECTA PARALELA A UNA RECTA POR UN PUNTO
G- ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO\nH- ECUACIÓN DE CIRCUNFERENCIA CON CENTRO Y RADIO DADO
I- ECUACIÓN DE CIRCUNFERENCIA POR TRES PUNTOS\nJ- HALLAR FOCO DE UNA PARÁBOLA
K- TANGENTE A UNA PARÁBOLA POR UN PUNTO EXTERNO\nL- INTERSECCIÓN\n
X- Salir del Asistente""")
r = input("Option: ").lower()
if r == "a":
    pointGraf()
    muestreo()
elif r == "h":
    ciaGraf()
    muestreo()
elif r == "i":
    ciaGraf()
    muestreo()
elif r == "k":
    parGraf()
    muestreo()

while r != "x":
    print("""A- PUNTO MEDIO DE UN SEGMENTO\nB- DISTANCIA ENTRE DOS PUNTOS
C- DISTANCIA DE UNA PUNTO A UNA RECTA\nD- ECUACIÓN DE RECTA POR UN PUNTO Y LA PENDIENTE
E- ECUACIÓN DE RECTA POR DOS PUNTOS\nF- ECUACIÓN DE RECTA PARALELA A UNA RECTA POR UN PUNTO
G- ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO\nH- ECUACIÓN DE CIRCUNFERENCIA CON CENTRO Y RADIO DADO
I- ECUACIÓN DE CIRCUNFERENCIA POR TRES PUNTOS\nJ- HALLAR FOCO DE UNA PARÁBOLA
K- TANGENTE A UNA PARÁBOLA POR UN PUNTO EXTERNO\nL- INTERSECCIÓN\n
X- Salir del Asistente""")
    r = input("Option: ").lower()
    if r == "a":
        secMGraf()
        muestreo()
    elif r == "h":
        ciaGraf()
        muestreo()
    elif r == "i":
        ciaGraf()
        muestreo()
    elif r == "k":
        parGraf()
        muestreo()

print("\nGracias por utilizar el programa... ")

