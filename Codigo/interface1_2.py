# Importaciones necesarias

# Librerias
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from math import *
from time import *

# Clases y Funciones locales
from Codigo.Clases.Punto import Punto
from Codigo.Clases.Recta import Recta
from Codigo.Funciones.Punto_Medio import PuntoMedio
from Codigo.Funciones.Distancia_entre_A_y_B import distanciaAB
from Codigo.Funciones.Distancia_Punto_a_Recta import DistanciaPuntoRecta

ventana = Tk()
ventana.title("GeoAlgebra")
ventana.config(background="black")
ventana.attributes("-fullscreen", True)
fig, ax = plt.subplots(dpi=90, figsize=(7, 5), facecolor='#000000')
ax.set_facecolor('black')
plt.grid(True)
canvas = FigureCanvasTkAgg(fig, master=ventana)  # Crea el área de dibujo en Tkinter, coloca la subplot en el frame


def eleccion(event):
    entrada1.delete(0, "end")
    entrada2.delete(0, "end")
    entrada3.delete(0, "end")
    entrada4.delete(0, "end")
    if event.char == 'a':
        menuClear()
        menuA()
    if event.char == 'b':
        menuClear()
        menuB()
    if event.char == 'c':
        menuClear()
        menuC()
    if event.char == 'd':
        menuClear()
        menuD()
    if event.char == 'e':
        menuClear()
        menuE()
    if event.char == 'f':
        menuClear()
        menuF()
    if event.char == 'g':
        menuClear()
        menuG()
    if event.char == 'h':
        menuClear()
        menuH()
    if event.char == 'i':
        menuClear()
        menuI()
    if event.char == 'j':
        menuClear()
        menuJ()
    if event.char == 'k':
        menuClear()
        menuK()
    if event.char == 'l':
        menuClear()
        menuL()
    if event.char == 'x':
        menuClear()
        ax.clear()
        fig.clear()
        plt.close("all")
        ventana.destroy()


def menuPrincipal():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    canvas.draw()
    canvas.get_tk_widget().grid_remove()
    volver.grid_remove()
    graficar.grid_remove()
    limpiar.grid_remove()
    guardar.grid_remove()
    mensaje1.grid_remove()
    mensaje2.grid_remove()
    mensaje3.grid_remove()
    mensaje4.grid_remove()
    entrada1.delete(0, "end")
    entrada2.delete(0, "end")
    entrada3.delete(0, "end")
    entrada4.delete(0, "end")
    entrada1.grid_remove()
    entrada2.grid_remove()
    entrada3.grid_remove()
    entrada4.grid_remove()
    principalMenu.grid(row=1, column=3, sticky=E)
    principalMenu1.grid(row=1, column=4, sticky=E)
    optionA.grid(padx=60, pady=8, row=3, column=0, sticky=W)
    optionB.grid(padx=60, pady=8, row=4, column=0, sticky=W)
    optionC.grid(padx=60, pady=8, row=5, column=0, sticky=W)
    optionD.grid(padx=60, pady=8, row=6, column=0, sticky=W)
    optionE.grid(padx=60, pady=8, row=7, column=0, sticky=W)
    optionF.grid(padx=60, pady=8, row=8, column=0, sticky=W)
    optionG.grid(padx=60, pady=8, row=9, column=0, sticky=W)
    optionH.grid(padx=60, pady=8, row=10, column=0, sticky=W)
    optionI.grid(padx=60, pady=8, row=11, column=0, sticky=W)
    optionJ.grid(padx=60, pady=8, row=12, column=0, sticky=W)
    optionK.grid(padx=60, pady=8, row=13, column=0, sticky=W)
    optionL.grid(padx=60, pady=8, row=14, column=0, sticky=W)
    optionX.grid(padx=60, pady=8, row=15, column=0, sticky=W)
    optionA.bind("<Enter>", lambda event: optionA.configure(background="white", fg="black"))
    optionB.bind("<Enter>", lambda event: optionB.configure(background="white", fg="black"))
    optionC.bind("<Enter>", lambda event: optionC.configure(background="white", fg="black"))
    optionD.bind("<Enter>", lambda event: optionD.configure(background="white", fg="black"))
    optionE.bind("<Enter>", lambda event: optionE.configure(background="white", fg="black"))
    optionF.bind("<Enter>", lambda event: optionF.configure(background="white", fg="black"))
    optionG.bind("<Enter>", lambda event: optionG.configure(background="white", fg="black"))
    optionH.bind("<Enter>", lambda event: optionH.configure(background="white", fg="black"))
    optionI.bind("<Enter>", lambda event: optionI.configure(background="white", fg="black"))
    optionJ.bind("<Enter>", lambda event: optionJ.configure(background="white", fg="black"))
    optionK.bind("<Enter>", lambda event: optionK.configure(background="white", fg="black"))
    optionL.bind("<Enter>", lambda event: optionL.configure(background="white", fg="black"))
    optionX.bind("<Enter>", lambda event: optionX.configure(background="white", fg="black"))
    optionA.bind("<Leave>", lambda event: optionA.configure(background="black", fg="green"))
    optionB.bind("<Leave>", lambda event: optionB.configure(background="black", fg="green"))
    optionC.bind("<Leave>", lambda event: optionC.configure(background="black", fg="green"))
    optionD.bind("<Leave>", lambda event: optionD.configure(background="black", fg="green"))
    optionE.bind("<Leave>", lambda event: optionE.configure(background="black", fg="green"))
    optionF.bind("<Leave>", lambda event: optionF.configure(background="black", fg="green"))
    optionG.bind("<Leave>", lambda event: optionG.configure(background="black", fg="green"))
    optionH.bind("<Leave>", lambda event: optionH.configure(background="black", fg="green"))
    optionI.bind("<Leave>", lambda event: optionI.configure(background="black", fg="green"))
    optionJ.bind("<Leave>", lambda event: optionJ.configure(background="black", fg="green"))
    optionK.bind("<Leave>", lambda event: optionK.configure(background="black", fg="green"))
    optionL.bind("<Leave>", lambda event: optionL.configure(background="black", fg="green"))
    optionX.bind("<Leave>", lambda event: optionX.configure(background="black", fg="green"))
    optionA.bind("<Button-1>", lambda event: menuA())
    optionB.bind("<Button-1>", lambda event: menuB())
    optionC.bind("<Button-1>", lambda event: menuC())
    optionD.bind("<Button-1>", lambda event: menuD())
    optionE.bind("<Button-1>", lambda event: menuE())
    optionF.bind("<Button-1>", lambda event: menuF())
    optionG.bind("<Button-1>", lambda event: menuG())
    optionH.bind("<Button-1>", lambda event: menuH())
    optionI.bind("<Button-1>", lambda event: menuI())
    optionJ.bind("<Button-1>", lambda event: menuJ())
    optionK.bind("<Button-1>", lambda event: menuK())
    optionL.bind("<Button-1>", lambda event: menuL())
    optionX.bind("<Button-1>", lambda event: exit())
    ventana.bind("<Key>", eleccion)


def menuClear():
    principalMenu.grid_remove()
    principalMenu1.grid_remove()
    optionA.grid_remove()
    optionB.grid_remove()
    optionC.grid_remove()
    optionD.grid_remove()
    optionE.grid_remove()
    optionF.grid_remove()
    optionG.grid_remove()
    optionH.grid_remove()
    optionI.grid_remove()
    optionJ.grid_remove()
    optionK.grid_remove()
    optionL.grid_remove()
    optionX.grid_remove()
    ventana.unbind("<Key>")


def graficarA():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()
    cad2 = entrada2.get()

    # Elimina cualquier espacio
    if cad1.count(" ") != 0:
        cad1.replace(" ", "")
    if cad2.count(" ") != 0:
        cad2.replace(" ", "")

    # Creacion del primer punto
    Punto1 = Punto(float(cad1[0:cad1.find(",")]), float(cad1[cad1.find(",") + 1:len(cad1)]))

    # Creacion del segundo punto
    Punto2 = Punto(float(cad2[0:cad2.find(",")]), float(cad2[cad2.find(",") + 1:len(cad2)]))

    # Punto medio mediante la funcion Punto-medio
    punto_medio = PuntoMedio(Punto1, Punto2)

    x = []
    y = []

    x.extend([Punto1.x, punto_medio.x, Punto2.x])
    y.extend([Punto1.y, punto_medio.y, Punto2.y])

    d = distanciaAB(Punto1, Punto2)
    # d1 = (mx ** 2 + my ** 2) ** (1 / 2)
    plt.plot(x, y, 'g')
    plt.plot(x, y, 'rx')
    plt.xlim(punto_medio.x - d, punto_medio.x + d)
    plt.ylim(punto_medio.y - d, punto_medio.y + d)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarB():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()
    cad2 = entrada2.get()

    # Elimina cualquier espacio
    if cad1.count(" ") != 0:
        cad1.replace(" ", "")
    if cad2.count(" ") != 0:
        cad2.replace(" ", "")

    # Creacion del primer punto
    Punto1 = Punto(float(cad1[0:cad1.find(",")]), float(cad1[cad1.find(",") + 1:len(cad1)]))

    # Creacion del segundo punto
    Punto2 = Punto(float(cad2[0:cad2.find(",")]), float(cad2[cad2.find(",") + 1:len(cad2)]))

    # Punto medio mediante la funcion Punto-medio
    punto_medio = PuntoMedio(Punto1, Punto2)

    x = []
    y = []

    x.extend([Punto1.x, punto_medio.x, Punto2.x])
    y.extend([Punto1.y, punto_medio.y, Punto2.y])

    d = distanciaAB(Punto1, Punto2)

    plt.plot(x, y, 'g:')
    plt.plot(Punto1.x, Punto1.y, 'rx')
    plt.plot(Punto2.x, Punto2.y, 'rx')
    plt.xlim(punto_medio.x - d, punto_medio.x + d)
    plt.ylim(punto_medio.y - d, punto_medio.y + d)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarC():  # Problemas pendientes
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()  # recta
    cad2 = entrada2.get()  # punto

    # Elimina signos y espacios
    if cad1.count("+") != 0:
        cad1 = cad1.replace("+", "")
    if cad1.count(" ") != 0:
        cad1 = cad1.replace(" ", "")

    recta = Recta(
        float(cad1[0:cad1.find("x")]),
        float(cad1[cad1.find("x") + 1:cad1.find("y")]),
        float(cad1[cad1.find("y") + 1:cad1.find("=")])
    )

    x = []
    y = []

    for i in range(-720, 720):
        x.append(i)
        y.append(-(recta.a * i + recta.c) / recta.b)

    plt.plot(x, y, 'g')  # recta

    if cad2.count(" ") != 0:
        cad2.replace(" ", "")

    punto = Punto(float(cad2[0:cad2.find(",")]), float(cad2[cad2.find(",") + 1:len(cad2)]))

    x = []
    y = []

    angulo = float(atan(recta.b / recta.a))
    distancia = float(
        (abs(punto.x * recta.a + punto.y * recta.b + recta.c)) / ((recta.a ** 2 + recta.b ** 2) ** (1 / 2))
    )

    px = float(punto.x + (cos(angulo) * distancia))
    py = float(punto.y + (sin(angulo) * distancia))

    x.extend([punto.x, px])
    y.extend([punto.y, py])

    plt.plot(punto.x, punto.y, 'rx')
    plt.xlim((punto.x - (distancia * 6)) - (0.9 * distancia), (punto.x + (distancia * 6) + (0.5 * distancia)))
    plt.ylim(punto.y - (distancia * 6), punto.y + (distancia * 6))  # mejor
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarD():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()
    cad2 = entrada2.get()

    #Elimina espacios en blanco
    if cad1.count(" ") != 0:
        cad1.replace(" ", "")
    if cad2.count(" ") != 0:
        cad2.replace(" ", "")

    punto = Punto(float(cad1[0:cad1.find(",")]), float(cad1[cad1.find(",") + 1:len(cad1)]))

    x = []
    y = []
    m = float(cad2)

    for i in range(-720, 720):
        x.append(i)
        y.append((m * i) - (m * punto.x) + punto.y)

    d1 = ((punto.x ** 2 + punto.y ** 2) ** 1 / 2) + 10
    plt.plot(x, y, 'g')
    plt.plot(punto.x, punto.y, 'rx')
    plt.xlim(punto.x - d1, punto.x + d1)
    plt.ylim(punto.y - d1, punto.y + d1)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarE():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()
    cad2 = entrada2.get()

    #Elimina los espacios en blanco
    if cad1.count(" ") != 0:
        cad1.replace(" ", "")
    if cad2.count(" ") != 0:
        cad2.replace(" ", "")

    punto1 = Punto(float(cad1[0:cad1.find(",")]), float(cad1[cad1.find(",") + 1:len(cad1)]))
    punto2 = Punto(float(cad2[0:cad2.find(",")]), float(cad2[cad2.find(",") + 1:len(cad2)]))

    x = []
    y = []

    puntoMedio = PuntoMedio(punto1, punto2)
    m = (punto1.y - punto2.y) / (punto1.x - punto2.x)
    for i in range(-720, 720):
        x.append(i)
        y.append((m * i) - (m * punto1.x) + punto1.y)
    d = distanciaAB(punto1, punto2)
    plt.plot(x, y, 'g')
    plt.plot(punto1.x, punto1.y, 'rx')
    plt.plot(punto2.x, punto2.y, 'rx')
    plt.xlim(puntoMedio.x - d, puntoMedio.x + d)
    plt.ylim(puntoMedio.y - d, puntoMedio.y + d)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarF():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()  # recta
    cad2 = entrada2.get()  # punto

    #Elimina espacios y signos
    if cad1.count("+") != 0:
        cad1 = cad1.replace("+", "")
    if cad1.count(" ") != 0:
        cad1 = cad1.replace(" ", "")

    recta = Recta(
        float(cad1[0:cad1.find("x")]),
        float(cad1[cad1.find("x") + 1:cad1.find("y")]),
        float(cad1[cad1.find("y") + 1:cad1.find("=")])
    )

    x = []
    y = []
    for i in range(-720, 720):
        x.append(i)
        y.append(-(recta.a * i + recta.c) / recta.b)
    plt.plot(x, y, 'g')  # recta

    if cad2.count(" ") != 0:
        cad2.replace(" ", "")

    punto = Punto(float(cad2[0:cad2.find(",")]), float(cad2[cad2.find(",") + 1:len(cad2)]))

    distancia = float((abs(punto.x * recta.a + punto.y * recta.b + recta.c)) / ((recta.a ** 2 + recta.b ** 2) ** (1 / 2)))
    plt.plot(punto.x, punto.y, 'rx')

    x = []
    y = []
    for i in range(-720, 720):
        x.append(i)
        y.append((recta.Pendiente() * i) - (recta.Pendiente() * punto.x) + punto.y)
    plt.plot(x, y, 'g')  # recta

    plt.xlim(punto.x - (distancia * 8), punto.x + (distancia * 8))
    plt.ylim(punto.y - (distancia * 8), punto.y + (distancia * 8))
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarG():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()  # recta
    cad2 = entrada2.get()  # punto

    #Elimina espacios y signos
    if cad1.count("+") != 0:
        cad1 = cad1.replace("+", "")
    if cad1.count(" ") != 0:
        cad1 = cad1.replace(" ", "")

    recta = Recta(
        float(cad1[0:cad1.find("x")]),
        float(cad1[cad1.find("x") + 1:cad1.find("y")]),
        float(cad1[cad1.find("y") + 1:cad1.find("=")])
    )

    x = []
    y = []

    for i in range(-720, 720):
        x.append(i)
        y.append(-(recta.a * i + recta.c) / recta.b)
    plt.plot(x, y, 'g')  # recta

    if cad2.count(" ") != 0:
        cad2.replace(" ", "")

    punto = Punto(float(cad2[0:cad2.find(",")]), float(cad2[cad2.find(",") + 1:len(cad2)]))

    distancia = DistanciaPuntoRecta(recta, punto)
    plt.plot(punto.x, punto.y, 'rx')

    x = []
    y = []
    m = (recta.b/recta.a)
    for i in range(-720, 720):
        x.append(i)
        y.append((m * i) - (m * punto.x) + punto.y)
    plt.plot(x, y, 'g')  # recta

    # 3x+4y+5=0
    plt.xlim((punto.x - (distancia * 6)) - (0.9 * distancia), (punto.x + (distancia * 6) + (0.5 * distancia)))
    plt.ylim(punto.y - (distancia * 6), punto.y + (distancia * 6))  # mejor
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarH():  # hecho
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad = entrada1.get()
    ec = cad
    cad2 = entrada2.get()
    h = float(ec[0:ec.find(",")])
    k = float(ec[ec.find(",") + 1:len(ec)])
    ratio = int(cad2)
    x = []
    y = []
    for c in range(0, 720):
        count = c * 0.5
        x.append(h + ratio * sin(count))
        y.append(k + ratio * cos(count))
    plt.xlim((h - (ratio * 2)) - (0.9 * ratio), (h + (ratio * 2) + (0.5 * ratio)))
    plt.ylim(k - (ratio * 2), k + (ratio * 2))
    plt.plot(x, y, 'go')
    plt.plot(h, k, 'rx')
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarI():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()
    cad2 = entrada2.get()
    cad3 = entrada3.get()
    if cad1.count(" ") != 0:
        cad1.replace(" ", "")
    if cad2.count(" ") != 0:
        cad2.replace(" ", "")
    if cad3.count(" ") != 0:
        cad3.replace(" ", "")
    x1 = float(cad1[0:cad1.find(",")])
    y1 = float(cad1[cad1.find(",") + 1:len(cad1)])
    x2 = float(cad2[0:cad2.find(",")])
    y2 = float(cad2[cad2.find(",") + 1:len(cad2)])
    x3 = float(cad3[0:cad3.find(",")])
    y3 = float(cad3[cad3.find(",") + 1:len(cad3)])
    mx = float((x1 + x2) / 2)
    my = float((y1 + y2) / 2)
    pendiente1 = float(-1 / ((y1 - y2) / (x1 - x2)))
    mx2 = float((x1 + x3) / 2)
    my2 = float((y1 + y3) / 2)
    pendiente2 = float(-1 / ((y1 - y3) / (x1 - x3)))
    a = float(-pendiente1)
    b = 1
    c = float(pendiente1 * mx - my)
    x = []
    y = []
    for i in range(-720, 720):
        x.append(i)
        y.append(pendiente1 * (i - mx) + my)
    # plt.plot(x, y, 'g')
    x = []
    y = []
    i = -720
    distMin = float((abs(i * a + ((pendiente2 * (i - mx2) + my2) * b) + c)) / ((a ** 2 + b ** 2) ** (1 / 2)))
    h = i
    k = float(pendiente2 * (i - mx2) + my2)
    for i in range(-720, 720):
        x.append(i)
        y.append(pendiente2 * (i - mx2) + my2)
        distancia = float((abs(i * a + ((pendiente2 * (i - mx2) + my2) * b) + c)) / ((a ** 2 + b ** 2) ** (1 / 2)))
        if distancia < distMin:
            distMin = distancia
            h = float(i)
            k = float(pendiente2 * (i - mx2) + my2)
    ratio = ((h - x2) ** 2 + (k - y2) ** 2) ** (1 / 2)
    plt.plot(h, k, 'rx')
    # plt.plot(x, y, 'g')
    x = []
    y = []
    for c in range(0, 720):
        count = c * 0.5
        x.append(h + ratio * sin(count))
        y.append(k + ratio * cos(count))
    plt.xlim((h - (ratio * 2)) - (0.9 * ratio), (h + (ratio * 2) + (0.5 * ratio)))
    plt.ylim(k - (ratio * 2), k + (ratio * 2))
    plt.plot(x, y, 'g:')
    plt.plot(x1, y1, 'rx')
    plt.plot(x2, y2, 'rx')
    plt.plot(x3, y3, 'rx')
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarJ():  # semihecho
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()  # parabola
    if cad1.count("+") != 0:
        cad1 = cad1.replace("+", "")
    if cad1.count(" ") != 0:
        cad1 = cad1.replace(" ", "")
    a = float(cad1[0:cad1.find("x2")])
    ec = cad1[cad1.find("x2") + 2:len(cad1)]
    b = float(ec[0:ec.find("y")])
    c = float(ec[ec.find("y") + 1:ec.find("=")])
    x = []
    y = []
    for i in range(-720, 720):
        aux = i / 10
        x.append(aux)
        y.append(-(a * (aux ** 2) + c) / b)
    plt.plot(x, y, 'g')  # parabola
    plt.plot(0, (c / -b), 'rx')
    plt.plot(0, (c / -b) + (-b / (4 * a)), 'rx')
    # 3x2 + 5y + 1 = 0
    focoOrd = float((c / -b) + (-b / (4 * a)))
    parametro = float(-b / a)
    plt.xlim(parametro, -parametro)
    plt.ylim(focoOrd + parametro, focoOrd - parametro)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarK():  # semihecho
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()  # parabola
    cad2 = entrada2.get()  # punto
    if cad1.count("+") != 0:
        cad1 = cad1.replace("+", "")
    if cad1.count(" ") != 0:
        cad1 = cad1.replace(" ", "")
    a = float(cad1[0:cad1.find("x2")])
    ec = cad1[cad1.find("x2") + 2:len(cad1)]
    b = float(ec[0:ec.find("y")])
    c = float(ec[ec.find("y") + 1:ec.find("=")])
    x = []
    y = []
    for i in range(-720, 720):
        aux = i / 10
        x.append(aux)
        y.append(-(a * (aux ** 2) + c) / b)
    plt.plot(x, y, 'g')  # parabola

    if cad2.count(" ") != 0:
        cad2.replace(" ", "")
    x2 = float(cad2[0:cad2.find(",")])
    y2 = float(cad2[cad2.find(",") + 1:len(cad2)])
    plt.plot(x2, y2, 'rx')
    """
    x = []
    y = []
    m = float(-a / b)
    for i in range(-720, 720):
        x.append(i)
        y.append((m * i) - (m * x2) + y2)
    plt.plot(x, y, 'g')  # recta"""

    #   plt.plot(0, (c/b), 'rx')
    # 3x2 + 5y + 1 = 0
    focoOrd = (c / b) + (b / (4 * a))
    d = ((0 - x2) ** 2 + (focoOrd - y2) ** 2) ** 1 / 2
    plt.xlim(-(d * 2), (d * 2))
    plt.ylim(focoOrd - d * 2, focoOrd + (d * 2))
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarL():  # semihecho
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    cad1 = entrada1.get()
    cad2 = entrada2.get()
    if cad1.count(" ") != 0:
        cad1 = cad1.replace(" ", "")
    if cad1.count("+") != 0:
        cad1 = cad1.replace("+", "")
    if cad2.count(" ") != 0:
        cad2 = cad2.replace(" ", "")
    if cad2.count("+") != 0:
        cad2 = cad2.replace("+", "")
    if cad1.count(",") != 0:
        x1 = float(cad1[0:cad1.find(",")])
        y1 = float(cad1[cad1.find(",") + 1:len(cad1)])
        plt.plot(x1, y1, 'rx')
    elif cad1.count("x2") != 0 and cad1.count("y2") != 0:
        cad1 = cad1[cad1.find("y2") + 2:len(cad1)]
        a = float(cad1[0:cad1.find("x")])
        b = float(cad1[cad1.find("x") + 1:cad1.find("y")])
        c = float(cad1[cad1.find("y") + 1:cad1.find("=")])
        h = float(-a / 2)
        k = float(-b / 2)
        ratio = float(((a ** 2 + b ** 2 - 4 * c) ** (1 / 2)) / 2)
        x = []
        y = []
        for c in range(0, 720):
            count = c * 0.5
            x.append(h + ratio * sin(count))
            y.append(k + ratio * cos(count))
        plt.xlim((h - (ratio * 2)) - (0.9 * ratio), (h + (ratio * 2) + (0.5 * ratio)))
        plt.ylim(k - (ratio * 2), k + (ratio * 2))
        plt.plot(x, y, 'go')
        plt.plot(h, k, 'rx')
        # x2 + y2 - 6x - 6y + 12 = 0
    elif cad1.count("x2") != 0:
        a = float(cad1[0:cad1.find("x2")])
        ec = cad1[cad1.find("x2") + 2:len(cad1)]
        b = float(ec[0:ec.find("y")])
        c = float(ec[ec.find("y") + 1:ec.find("=")])
        x = []
        y = []
        for i in range(-720, 720):
            aux = i / 10
            x.append(aux)
            y.append(-(a * (aux ** 2) + c) / b)
        plt.plot(x, y, 'g')  # parabola
        # plt.plot(0, (c / -b), 'rx')
        # plt.plot(0, (c / -b) + (-b / (4 * a)), 'rx')
        # 3x2 + 5y + 1 = 0
        focoOrd = float((c / -b) + (-b / (4 * a)))
        parametro = float(-b / a)
        plt.xlim(parametro, -parametro)
        plt.ylim(focoOrd + parametro, focoOrd - parametro)
    elif cad1.count("x") != 0:
        a = float(cad1[0:cad1.find("x")])
        b = float(cad1[cad1.find("x") + 1:cad1.find("y")])
        c = float(cad1[cad1.find("y") + 1:cad1.find("=")])
        x = []
        y = []
        for i in range(-720, 720):
            x.append(i)
            y.append(-(a * i + c) / b)
        plt.plot(x, y, 'g')
    if cad2.count(",") != 0:
        x2 = float(cad2[0:cad2.find(",")])
        y2 = float(cad2[cad2.find(",") + 1:len(cad2)])
        plt.plot(x2, y2, 'rx')
    elif cad2.count("x2") != 0 and cad2.count("y2") != 0:
        cad2 = cad2[cad2.find("y2") + 2:len(cad2)]
        a = float(cad2[0:cad2.find("x")])
        b = float(cad2[cad2.find("x") + 1:cad2.find("y")])
        c = float(cad2[cad2.find("y") + 1:cad2.find("=")])
        h = float(-a / 2)
        k = float(-b / 2)
        ratio = float(((a ** 2 + b ** 2 - 4 * c) ** (1 / 2)) / 2)
        x = []
        y = []
        for c in range(0, 720):
            count = c * 0.5
            x.append(h + ratio * sin(count))
            y.append(k + ratio * cos(count))
        plt.xlim((h - (ratio * 2)) - (0.9 * ratio), (h + (ratio * 2) + (0.5 * ratio)))
        plt.ylim(k - (ratio * 2), k + (ratio * 2))
        plt.plot(x, y, 'go')
        plt.plot(h, k, 'rx')
        # x2 + y2 - 6x - 6y + 12 = 0
    elif cad2.count("x2") != 0:
        a = float(cad2[0:cad2.find("x2")])
        ec = cad2[cad2.find("x2") + 2:len(cad2)]
        b = float(ec[0:ec.find("y")])
        c = float(ec[ec.find("y") + 1:ec.find("=")])
        x = []
        y = []
        for i in range(-720, 720):
            aux = i / 10
            x.append(aux)
            y.append(-(a * (aux ** 2) + c) / b)
        plt.plot(x, y, 'g')  # parabola
        plt.plot(0, (c / -b), 'rx')
        plt.plot(0, (c / -b) + (-b / (4 * a)), 'rx')
        # 3x2 + 5y + 1 = 0
        focoOrd = float((c / -b) + (-b / (4 * a)))
        parametro = float(-b / a)
        plt.xlim(parametro, -parametro)
        plt.ylim(focoOrd + parametro, focoOrd - parametro)
    elif cad2.count("x") != 0:
        a = float(cad2[0:cad2.find("x")])
        b = float(cad2[cad2.find("x") + 1:cad2.find("y")])
        c = float(cad2[cad2.find("y") + 1:cad2.find("=")])
        x = []
        y = []
        for i in range(-720, 720):
            x.append(i)
            y.append(-(a * i + c) / b)
        plt.plot(x, y, 'g')
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def save():
    image = str(str(int(time() / 60 / 60 / 24 / 365) + 1970) + "-" + strftime("%m-%d", gmtime()) + "-" + \
                str(int(time() / 60 / 60 % 24) - 3) + "+" + str(int(time() / 60 % 60)) + "+" + str(int(time() % 60)))
    fig.savefig("figure" + image + ".jpg")
    guardar.grid_remove()


def clean():
    canvas.get_tk_widget().grid_remove()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    canvas.draw()
    limpiar.grid_remove()
    guardar.grid_remove()


def menuA():
    menuClear()
    mensaje1.configure(text="Ingrese el primer punto: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el segundo punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarA)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuB():
    menuClear()
    mensaje1.configure(text="Ingrese el primer punto: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el segundo punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarB)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuC():
    menuClear()
    mensaje1.configure(text="Ingrese la ecuacion de la recta: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarC)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuD():
    menuClear()
    mensaje1.configure(text="Ingrese el punto: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese la pendiente: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarD)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuE():
    menuClear()
    mensaje1.configure(text="Ingrese el primer punto: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el segundo punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarE)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuF():
    menuClear()
    mensaje1.configure(text="Ingrese la ecuacion de la recta: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarF)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuG():
    menuClear()
    mensaje1.configure(text="Ingrese la ecuacion de la recta: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarG)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuH():
    menuClear()
    mensaje1.configure(text="Ingrese el centro de la circunferencia: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el radio de la circunferencia: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarH)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuI():
    menuClear()
    mensaje1.configure(text="Ingrese el primer punto: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el segundo punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    mensaje3.configure(text="Ingrese el tercer punto: ")
    mensaje3.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    entrada3.grid(padx=15, pady=5, row=3, column=1, sticky=W)
    graficar.configure(command=graficarI)
    entrada1.focus()
    graficar.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=5, column=0, sticky=W)
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuJ():
    menuClear()
    mensaje1.configure(text="Ingrese la ecuacion de la parabola: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    graficar.configure(command=graficarJ)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuK():
    menuClear()
    mensaje1.configure(text="Ingrese la ecuacion de la parabola: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el segundo punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarK)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


def menuL():
    menuClear()
    mensaje1.configure(text="Ingrese la primera ecuacion: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese la segunda ecuacion: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarL)
    graficar.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    volver.grid(padx=15, pady=5, row=4, column=0, sticky=W)
    entrada1.focus()
    ax.clear()
    ax.axhline(linewidth=1, color='white')
    ax.axvline(linewidth=1, color='white')
    ax.set_xlabel("Eje  Horizontal", color='white')
    ax.set_ylabel("Eje  Vertical", color='white')
    ax.tick_params(direction='out', length=6, width=2, colors='white', grid_color='white', grid_alpha=0.2)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)


principalMenu = Label(ventana, text="MENU", fg="blue", bg="black", font="consolas 30 bold")
principalMenu1 = Label(ventana, text=" PRINCIPAL", fg="yellow", bg="black", font="consolas 30 bold")
optionA = Label(ventana, text="A- PUNTO MEDIO DE UN SEGMENTO", fg="green", bg="black")
optionB = Label(ventana, text="B- DISTANCIA ENTRE DOS PUNTOS", fg="green", bg="black")
optionC = Label(ventana, text="C- DISTANCIA DE UNA PUNTO A UNA RECTA", fg="green", bg="black")
optionD = Label(ventana, text="D- ECUACIÓN DE RECTA POR UN PUNTO Y LA PENDIENTE", fg="green", bg="black")
optionE = Label(ventana, text="E- ECUACIÓN DE RECTA POR DOS PUNTOS", fg="green", bg="black")
optionF = Label(ventana, text="F- ECUACIÓN DE RECTA PARALELA A UNA RECTA POR UN PUNTO", fg="green", bg="black")
optionG = Label(ventana, text="G- ECUACIÓN DE RECTA PERPENDICULAR A UNA RECTA POR UN PUNTO", fg="green", bg="black")
optionH = Label(ventana, text="H- ECUACIÓN DE CIRCUNFERENCIA CON CENTRO Y RADIO DADO", fg="green", bg="black")
optionI = Label(ventana, text="I- ECUACIÓN DE CIRCUNFERENCIA POR TRES PUNTOS", fg="green", bg="black")
optionJ = Label(ventana, text="J- HALLAR FOCO DE UNA PARÁBOLA", fg="green", bg="black")
optionK = Label(ventana, text="K- TANGENTE A UNA PARÁBOLA POR UN PUNTO EXTERNO", fg="green", bg="black")
optionL = Label(ventana, text="L- INTERSECCIÓN", fg="green", bg="black")
optionX = Label(ventana, text="X- SALIR DEL ASISTENTE", fg="green", bg="black")
volver = Button(ventana, text="volver ", fg="green", bg="black", font=12, command=menuPrincipal)
graficar = Button(ventana, text="Graficar ", fg="green", bg="black", font=12, command=NONE)
entrada1 = Entry(ventana, fg="#000000", font="arial 10")
mensaje1 = Label(ventana, fg="green", bg="black", font=12)
entrada2 = Entry(ventana, fg="#000000", font="arial 10")
mensaje2 = Label(ventana, fg="green", bg="black", font=12)
entrada3 = Entry(ventana, fg="#000000", font="arial 10")
mensaje3 = Label(ventana, fg="green", bg="black", font=12)
entrada4 = Entry(ventana, fg="#000000", font="arial 10")
mensaje4 = Label(ventana, fg="green", bg="black", font=12)
guardar = Button(ventana, text="Guardar ", fg="green", bg="black", font=12, command=save)
limpiar = Button(ventana, text="Limpiar ", fg="green", bg="black", font=12, command=clean)
aumento = Button(ventana, text=" + ", fg="green", bg="black", font=12, command=clean)
decremento = Button(ventana, text=" - ", fg="green", bg="black", font=12, command=clean)

menuPrincipal()

ventana.mainloop()

"""
A   hecho
B   hecho
C   semihecho
D   hecho
E   hecho
F   hecho
G   hecho
H   hecho
I   hecho
J   semihecho
K   semihecho
L   semihecho
"""
