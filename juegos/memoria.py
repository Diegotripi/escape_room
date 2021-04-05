import requests
import json
import random
from clases.juego import Juego
import colored
from colored import stylize
from terminaltables import SingleTable

def generar_lista_vacia(matriz):  #Inserta mas listas en la matriz para crear el tablero de juego
    
    for i in range(0,5):
        matriz[i] = ["|X|"] * 5

    matriz[0] = ["-","A",'B','C','D'] #Inserta esta lista para poder identificar columnas
    j = 1
    for h,i in enumerate(matriz):  #Convierte el primer elemento (indice 0) de cada lista (a partir de la lista de indice 1), en un numero para identificar filas
        if h > 0:
            i[0] = str(j)
            j +=1 
        

    return matriz

def extraer(matriz_emojis_api): #Permite extraer de la api los emojis

    matriz_nueva = (''.join(matriz_emojis_api.splitlines()))
    matriz_nueva = eval(matriz_nueva)

    return matriz_nueva

def mezclador(matriz_emoji):
    k = 0
    while not k == 50:
        x = random.randint(0,3)
        y = random.randint(0,3)  # genera numero random para establecer  2 cordenadas que van a intercambiar sus caracteres. Es un ciclo que se repite 50 veces 

        m = random.randint(0,3)
        n = random.randint(0,3)

        a = matriz_emoji[y][x]
        b = matriz_emoji[m][n]

        matriz_emoji[y][x] = b
        matriz_emoji[m][n] = a

        k +=1

    return matriz_emoji

def seleccionar():  #Permite al usuario seleccionar la celda que desea voltear

    letras = ['A','B','C','D']
    vertical = input("\nIntroduce la columna que deseas seleccionar(Letras): ")
    vertical = vertical.capitalize()
    while vertical not in letras:
        vertical = input("\nIngreso inválido. Introduce una columna existente: ")
    vertical = vertical.capitalize()
    horizontal = input("\nIntroduce la fila que deseas seleccionar(Números): ")
    while horizontal not in ('1','2','3','4'):
        horizontal = input("\nIngreso inválido. Introduce una fila existente: ")

    for i , j in enumerate(letras):
        if j == vertical:
            vertical = i+1

    vertical = int(vertical)
    horizontal = int(horizontal)
    posicion = [horizontal, vertical]
    return posicion

def voltear(posicion, matriz_emoji, matriz_vacia): #Voltea las coordenadas que ingresa el usuario

    a = matriz_emoji[posicion[0]-1][posicion[1]-1]
    matriz_vacia[posicion[0]][posicion[1]] = f" {a}"

    return matriz_emoji, matriz_vacia, a

def mostrar(matriz):  #Utiliza la libreria para imprimir en formato de tabla
    print("\n")
    table_instance = SingleTable(matriz)
    table_instance.outer_border = True
    table_instance.inner_row_border = True
    print(table_instance.table)
    

def menu(a,b): #Seleccionar una opcion del menu

    opcion = input(f"\nSelecciona una de las siguientes opciones: \n1- {a} \n2- {b} \n==> ")
    while not (opcion in ('1','2')):
        opcion = input("Ingreso inválido. Selecciona un opción correcta")

    return opcion

def juego(matriz_emoji, matriz_vacia, jugador):

    selecciones = [] #Se utiliza esta lista para saber si ya selecciono la celda anteriormente
    aciertos = 0

    mostrar(matriz_vacia)


    while True:

        opcion = menu("Voltear una tarjeta","Salir")

        if opcion == "1":

            mostrar(matriz_vacia)

            posicion = seleccionar()
            while posicion in selecciones:
                print('\nYa has seleccionado esta celda anteriormente')
                posicion = seleccionar()

            selecciones.append(posicion)
            matriz_emoji, matriz_vacia, a = voltear(posicion, matriz_emoji, matriz_vacia)

            mostrar(matriz_vacia)

            variable = menu("Voltear otra tarjeta","Utilizar una pista")

            if variable == "1":

                segunda_posicion = seleccionar()

                while segunda_posicion in selecciones: 
                    print('Ya has seleccionado esta celda anteriormente')
                    segunda_posicion = seleccionar()
                
                

                selecciones.append(segunda_posicion)
                matriz_emoji, matriz_vacia, b = voltear(segunda_posicion, matriz_emoji, matriz_vacia)

                mostrar(matriz_vacia)

                if a == b:
                    print("\n¡Has conseguido una pareja!") #Valida si has conseguido una pareja
                    aciertos += 1
                else:
                    jugador.perder_vida(0.25)
                    print("\n¡Vaya, no has acertado!")
                    matriz_vacia[posicion[0]][posicion[1]] = "|X|"
                    matriz_vacia[segunda_posicion[0]][segunda_posicion[1]] = "|X|"
                    selecciones.pop(-1)
                    selecciones.pop(-1)
                    if jugador.vidas <= 0:
                        return jugador, False
            else:
                if jugador.pistas > 0:
                    jugador.usar_pista()
                    for i,j in enumerate(matriz_emoji):
                        for l,m in enumerate(j):
                            if m == a:
                                segunda_posicion = [i+1,l+1]
                                if segunda_posicion != posicion: #Busca la pareja de la celda seleccionada anteriormente y la voltea (pistas)
                                    voltear(segunda_posicion, matriz_emoji, matriz_vacia)
                                    selecciones.append(segunda_posicion)
                                    aciertos += 1

                    mostrar(matriz_vacia)
                else:
                    print('Te has quedado sin pistas.')
        else:
            return jugador, False

        if aciertos == 8:
            print("\n¡Has ganado!")
            return jugador, True


class memoria(Juego):
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
            print("\nBienvenido al juego de memoria")
            print("En este juego deberás especificar la celda, con su columna(letra) y fila(numero)  ")
            print(f'Regla: perderás {self.regla}')
            matriz_emojis_api = self.preguntas[0]['question']
            matriz_emoji = extraer(matriz_emojis_api)
            matriz_vacia = ["|X|"] * 5 #Genera una lista con 5 |X|
            matriz_vacia = generar_lista_vacia(matriz_vacia)
            matriz_emoji = mezclador(matriz_emoji) #Permite mezclar el orden de los emojis 
            jugador, self.ganado = juego(matriz_emoji, matriz_vacia, jugador)
            if self.ganado == True:
                jugador.agregar_recompensa(self.premio)
                print(f"Conseguiste {self.premio}")

            return jugador

        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador
        