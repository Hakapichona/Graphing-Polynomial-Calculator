from tkinter import*
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from math import*
ventana = Tk()
ventana.title("GeoAlgebra")
ventana.config(background="black")
ventana.attributes("-fullscreen", True)
fig, ax = plt.subplots(dpi=90, figsize=(7, 5), facecolor='#000000')
ax.set_facecolor('black')
plt.grid(True)
canvas = FigureCanvasTkAgg(fig, master=ventana)  # Crea el área de dibujo en Tkinter, coloca la subplot en el frame


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
    principalMenu.grid(row=1, column=2, sticky=EW)
    optionA.grid(padx=40, pady=8, row=3, column=0, sticky=W)
    optionB.grid(padx=40, pady=8, row=4, column=0, sticky=W)
    optionC.grid(padx=40, pady=8, row=5, column=0, sticky=W)
    optionD.grid(padx=40, pady=8, row=6, column=0, sticky=W)
    optionE.grid(padx=40, pady=8, row=7, column=0, sticky=W)
    optionF.grid(padx=40, pady=8, row=8, column=0, sticky=W)
    optionG.grid(padx=40, pady=8, row=9, column=0, sticky=W)
    optionH.grid(padx=40, pady=8, row=10, column=0, sticky=W)
    optionI.grid(padx=40, pady=8, row=11, column=0, sticky=W)
    optionJ.grid(padx=40, pady=8, row=12, column=0, sticky=W)
    optionK.grid(padx=40, pady=8, row=13, column=0, sticky=W)
    optionL.grid(padx=40, pady=8, row=14, column=0, sticky=W)
    optionX.grid(padx=40, pady=8, row=15, column=0, sticky=W)
    ingresar.grid(row=16, column=1, sticky=W)
    salir.grid(padx=40, row=16, column=0, sticky=W)
    entradaPrincipal.grid(padx=8, row=16, column=2, sticky=W)


def menuClear():
    principalMenu.grid_remove()
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
    salir.grid_remove()
    entradaPrincipal.delete(0, 'end')
    ingresar.grid_remove()
    entradaPrincipal.grid_remove()


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
    if cad1.count(" ") != 0:
        cad1.replace(" ", "")
    if cad2.count(" ") != 0:
        cad2.replace(" ", "")
    x1 = float(cad1[0:cad1.find(",")])
    y1 = float(cad1[cad1.find(",") + 1:len(cad1)])
    x2 = float(cad2[0:cad2.find(",")])
    y2 = float(cad2[cad2.find(",") + 1:len(cad2)])
    x = []
    y = []
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    x.append(x1)
    x.append(mx)
    x.append(x2)
    y.append(y1)
    y.append(my)
    y.append(y2)
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1 / 2
    # d1 = (mx ** 2 + my ** 2) ** 1 / 2
    plt.plot(x, y, 'g')
    plt.plot(x, y, 'rx')
    plt.xlim(mx - d, mx + d)
    plt.ylim(my - d, my + d)
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
    if cad1.count(" ") != 0:
        cad1.replace(" ", "")
    if cad2.count(" ") != 0:
        cad2.replace(" ", "")
    x1 = float(cad1[0:cad1.find(",")])
    y1 = float(cad1[cad1.find(",") + 1:len(cad1)])
    x2 = float(cad2[0:cad2.find(",")])
    y2 = float(cad2[cad2.find(",") + 1:len(cad2)])
    x = []
    y = []
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    m = (y1 - y2) / (x1 - x2)
    for i in range(-720, 720):
        x.append(i)
        y.append((m*i)-(m*x1)+y1)
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1 / 2
    # d1 = (mx ** 2 + my ** 2) ** 1 / 2
    plt.plot(x, y, 'g')
    plt.plot(x1, y1, 'rx')
    plt.plot(x2, y2, 'rx')
    plt.xlim(mx - d, mx + d)
    plt.ylim(my - d, my + d)
    canvas.get_tk_widget().grid(column=4, row=6, padx=5, pady=5)
    guardar.grid(column=4, row=7, padx=5, pady=5)
    limpiar.grid(column=4, row=8, padx=5, pady=5)
    canvas.draw()


def graficarC():
    print("cia")


def graficarD():
    print("cia")


def graficarE():
    print("cia")


def graficarF():
    print("cia")


def graficarG():
    print("cia")


def graficarH():    # hecho
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
    h = int(ec[0:ec.find(",")])
    k = int(ec[ec.find(",") + 1:len(ec)])
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
    print("cia")


def graficarJ():
    print("cia")


def graficarK():
    print("cia")


def graficarL():
    print("cia")


def save():
    fig.savefig("figure.jpg")
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
    mensaje1.configure(text="Ingrese el primer punto: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el segundo punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    graficar.configure(command=graficarA)
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


def menuB():
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
    mensaje1.configure(text="Ingrese la ecuacion de la recta: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def menuD():
    mensaje1.configure(text="Ingrese el punto: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese la pendiente: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def menuE():
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def menuF():
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def menuG():
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def menuH():
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
    mensaje1.configure(text="Ingrese el primer punto: ")
    mensaje1.grid(padx=15, pady=5, row=1, column=0, sticky=W)
    entrada1.grid(padx=15, pady=5, row=1, column=1, sticky=W)
    mensaje2.configure(text="Ingrese el segundo punto: ")
    mensaje2.grid(padx=15, pady=5, row=2, column=0, sticky=W)
    entrada2.grid(padx=15, pady=5, row=2, column=1, sticky=W)
    mensaje3.configure(text="Ingrese el tercer punto: ")
    mensaje3.grid(padx=15, pady=5, row=3, column=0, sticky=W)
    entrada3.grid(padx=15, pady=5, row=3, column=1, sticky=W)
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def menuJ():
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def menuK():
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def menuL():
    volver.grid(padx=15, pady=5, row=14, column=0, sticky=W)


def muestreo():
    if entradaPrincipal.get().lower() == 'a':
        menuClear()
        menuA()
    if entradaPrincipal.get().lower() == 'b':
        menuClear()
        menuB()
    if entradaPrincipal.get().lower() == 'c':
        menuClear()
        menuC()
    if entradaPrincipal.get().lower() == 'd':
        menuClear()
        menuD()
    if entradaPrincipal.get().lower() == 'e':
        menuClear()
        menuE()
    if entradaPrincipal.get().lower() == 'f':
        menuClear()
        menuF()
    if entradaPrincipal.get().lower() == 'g':
        menuClear()
        menuG()
    if entradaPrincipal.get().lower() == 'h':
        menuClear()
        menuH()
    if entradaPrincipal.get().lower() == 'i':
        menuClear()
        menuI()
    if entradaPrincipal.get().lower() == 'j':
        menuClear()
        menuJ()
    if entradaPrincipal.get().lower() == 'k':
        menuClear()
        menuK()
    if entradaPrincipal.get().lower() == 'l':
        menuClear()
        menuL()
    if entradaPrincipal.get().lower() == 'x':
        menuClear()
        ax.clear()
        fig.clear()
        plt.close("all")
        ventana.destroy()


principalMenu = Label(ventana, text="MENU PRINCIPAL", fg="blue", bg="black", font="consolas 20 bold")
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
ingresar = Button(ventana, text="Ingresar opcion ", fg="green", bg="black", font=12, command=muestreo)
entradaPrincipal = Entry(ventana, fg="#000000", font="arial 10")
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
salir = Button(ventana, text="Salir ", fg="green", bg="black", font=12, command=exit)

menuPrincipal()

ventana.mainloop()
