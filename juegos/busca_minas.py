import random
import requests
import json
import random
from clases.juego import Juego
import colored
from colored import stylize

def generar_mapa_minas(n, k, m, h):

    selecciones = []

    arr = [[0 for i in range(n)] for j in range(n)] #se crea una matriz cuadrada nxn

    for num in range(k):  #ciclo for donde se colocan las minas 
        x = random.randint(1,n-1) #Genera aleatoramiente una posicion donde colocar una mina
        y = random.randint(1,n-1)
        
        while [int(x),int(y)] in selecciones or ((int(m))==x and (int(h))==y): #Se entra en este ciclo en cado de que la posicion escogida ya haya sido ocupada por una mina o sea el primer movimiento del jugador
            x = random.randint(1,n-1)
            y = random.randint(1,n-1)

        sel = [int(x),int(y)]
        selecciones.append(sel)

        arr[y][x] = 'X'
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # Se evalua donde esta la mina y se suma 1 unidad en la casilla de la derecha de la mina
        if (x >=2 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # se suma 1 unidad en la casilla izquierda de la mina
        if (x >= 2 and x <= n-1) and (y >= 2 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # se suma 1 unidad en la casilla de la esquina superior izquierda
 
        if (x >= 0 and x <= n-2) and (y >= 2 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # se suma 1 unidad en la casilla de la esquina superior derecha
        if (x >= 0 and x <= n-1) and (y >= 2 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # se suma 1 unidad en la casilla de la esquina de arriba
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # esquina inferior derecha
        if (x >= 2 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # esquina inferior izquierda
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # abajo de la mina



    letra = ['+','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    num = ['1', '2', '3', '4', '5', '6', '7', '8']

    arr[0] = letra



    for c,i in enumerate(arr):
        for p,j in enumerate(i):
            if p == 0 and p >=1:
                arr[c][0] = num[0]
                num.pop(0)

    mostrar(arr)
 
    return arr

def generar_mapa_jugador(n):

    arr = [['-' for i in range(n)] for j in range(n)]

    letra = ['-','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    num = ['1', '2', '3', '4', '5', '6', '7', '8']

    arr[0] = letra
    for c,i in enumerate(arr):
        for p,j in enumerate(i):
            if p == 0 and c>=1:
                arr[c][0] = num[0]
                num.pop(0)
    return arr
    
def mostrar(map): #Muestra el arreglo mas ordenadp
    for i in map:
        print(" ".join(str(k) for k in i))
        print("")

def victoria(map, n): #valida si el jugador gano
    ktt= 0
    for i in map:
        for k in i:
            if k == '-':
                ktt += 1
    if ktt > n:
        return False
    return True

def validar_ingreso(a):
    while not a in ('1','2','3','4','5','6','7','8'):
        a = input("Ingreso inválido. Selecciona una opción correcta: ")
    
    return a

def validar_ingreso_letra(a):
    a = a.title()

    letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    while not a in letras:
        a = input("Ingreso inválido. Selecciona una opción correcta: ")
        a = a.title()

    for j,k in enumerate(letras):
        if k == a:
            a = j+1

    return a 

def juego(): #Funcion donde se maneja todo el juego

    n = 9 #Define la matriz cuadrad de n filas y n columnas (en este caso 9x9)
    k = 8 #Define el numero de bombas

    mapa_usuario = generar_mapa_jugador(n) #Se crea el mapa que ve el jugador, tablero de juego. Este se va rellenando a medida que el jugador introducece las celdas que desea abrir
    mostrar(mapa_usuario)

    print("Introduce la celda que deseas seleccionar: ")
    x = input("Ingresa una letra: ")
    x = validar_ingreso_letra(x)
    y = input("Ingresa un número: ")
    y = validar_ingreso(y)
    bol = False #Este bool permite saber si el jugador gana o pierde


    mapa_minas = generar_mapa_minas(n, k, x, y) #Una vez que el jugador introduce su primer movimiento se crea el mapa con las minas, de esta forma nunca podrá perder en su primer movimiento
    
    while True: #Ciclo while donde se mueve todo el juego

        if victoria(mapa_usuario, n) == False: #permite validar si el jugador ya gano

            if bol:
                print("Introduce la celda que deseas seleccionar: ")
                x = input("Ingresa una letra: ")
                x = validar_ingreso_letra(x)
                y = input("Ingresa un número: ")
                y = validar_ingreso(y)

            bol = True
            x = int(x) 
            y = int(y)  
            if (mapa_minas[y][x] == 'X'): #Se valida si exploto una mina
                print("Has perdido!")
                return False
            else:
                mapa_usuario[y][x] = mapa_minas[y][x]
                mostrar(mapa_usuario)

        else:
            mostrar(mapa_usuario)
            print("Has ganado!")
            return True



class busca_minas(Juego):
    def __init__(self, mensaje_requerimiento, requerimiento, nombre, premio, regla, preguntas, ganado):
        super().__init__(mensaje_requerimiento, requerimiento, nombre, premio, regla, preguntas, ganado)

    def mensaje(self):
        print(self.mensaje_requerimiento)
    
    def requerido(self):
        print(self.requerimiento)
    
    def nombre_juego(self):
        print(self.nombre)
    
    def premio_juego(self):
        print(self.premio)
    
    def regla_juego(self):
        print(self.regla)

    def jugar(self, jugador): 

        if self.ganado == False:
            if self.requerimiento[0] in jugador.recompensas and self.requerimiento[1] in jugador.recompensas:

                print(f'\n\nBienvenido al {self.nombre}\n\n')
                bol = juego()
                if bol: #Retorna la recompensa si gana
                    self.ganado = True
                    jugador.agregar_recompensa(self.premio)
                    return jugador
                else:
                    jugador.perder_vida(1)
                    return jugador  
            else:
                print(" ", colored.fg("red"))
                print(f"\n       {self.mensaje_requerimiento}", colored.fg("white"))
                return jugador
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador