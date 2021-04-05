import random
import requests
import json
from clases.juego import Juego
from terminaltables import SingleTable
import colored
from colored import stylize

def generar_lista(palabra, palabra_sep):
    palabra_sep =[]
    for i in palabra:
        palabra_sep.append(i)
    return palabra_sep

def generar_lista_vacia(matriz): #
    
    for i in range(0,15):
        matriz[i] = [None] * 15

    return matriz

def vertical( matriz_alfabeto, palabra_sep, matriz_posicion): #Esta funcion permite insertar la palabra en posicion vertical dentro de la matriz. Se guarda la palarabra en matriz alfabeto y un arreglo de 1 en matriz posicion 
    contador = 0

    opcion = random.randint(0, 1)
    if opcion == 0:
        palabra_sep = palabra_sep
    else:
        palabra_sep.reverse()

    m = True
    while m:    #Se valida que las posiciones seleccioadas aleatoriamente no choquen con otra palabra, en caso de que choquen, se retornan las listas sin ningun cambio(Esta misma logica se utiliza en cada funcion de posicion)
        contador += 1
        t = 0
        y = random.randint(0, 14-len(palabra_sep))
        x = random.randint(0, 14)
        for i in range(0,len(matriz_posicion)):
            if matriz_posicion[i][x] == 1:
                t += 1
        if t == 0:
            m = False
        if contador == 10:
            return matriz_alfabeto, matriz_posicion, contador 

    h = 0
    for i in range(y,14):
            matriz_alfabeto[i][x] = palabra_sep[h]
            h += 1
            matriz_posicion[i][x] = 1
            if len(palabra_sep) == h:
                return matriz_alfabeto, matriz_posicion, contador

def horizontal(matriz_alfabeto, palabra_sep, matriz_posicion):

    contador = 0

    opcion = random.randint(0, 1)
    if opcion == 0:
        palabra_sep = palabra_sep
    else:
        palabra_sep.reverse()

    m = True

    while m:

        contador += 1
        t = 0
        y = random.randint(0, 14)
        x = random.randint(0, 14-len(palabra_sep))
        for i in range(0,14):
            if matriz_posicion[y][i] == 1:
                t += 1

        if t == 0:
            m = False

        if contador == 10:
            return matriz_alfabeto, matriz_posicion, contador    

        

    
    h = 0
    for i in range(x,14):
        matriz_alfabeto[y][i] = palabra_sep[h]
        matriz_posicion[y][i] = 1
        h += 1
        if len(palabra_sep) == h:
            return matriz_alfabeto, matriz_posicion, contador
            
def diagonal(matriz_alfabeto, palabra_sep, matriz_posicion): #forma \
    opcion = random.randint(0, 1)
    if opcion == 0:
        palabra_sep = palabra_sep
    else:
        palabra_sep.reverse()

    contador = 0

    m = True
    while m:
        contador += 1
        t = 0
        y = random.randint(0, 14-len(palabra_sep))
        x = random.randint(0, 14-len(palabra_sep))
        x_copy = x
        x_copy2 = x

        for i in range(y,14):
            if matriz_posicion[i][x_copy2] == 1:
                t += 1
                break
            if x_copy > x_copy2:
                t += 1
                break
            else:
                x_copy2 += 1
                if x_copy2 > 14:
                    t += 1
                    break
        if t == 0:
            m = False

        if contador == 10:
            return matriz_alfabeto, matriz_posicion, contador

    
    h = 0 
    for i in range(y,14):
        matriz_alfabeto[i][x] = palabra_sep[h]
        matriz_posicion[i][x] = 1
        x += 1
        h += 1
        if len(palabra_sep) == h:
            return matriz_alfabeto, matriz_posicion, contador

def diagonal1(matriz_alfabeto, palabra_sep, matriz_posicion): #forma diagonal /

    contador = 0
    opcion = random.randint(0, 1)
    if opcion == 0:
        palabra_sep = palabra_sep
    else:
        palabra_sep.reverse()

    m = True
    while m:
        contador += 1
        t = 0
        y = random.randint(0, 14-len(palabra_sep))
        x = random.randint(0, 14-len(palabra_sep))
        x_copy = x
        x_copy2 = x
        
        for i in range(y,14):
            if matriz_posicion[i][x_copy2] == 1:
                t += 1    
                break
            if x_copy < x_copy2:
                t += 1
                break
            else:
                x_copy2 -= 1
                if x_copy2 < 0:
                    t += 1
                    break
        if t == 0:
            m = False

        if contador == 10:
            return matriz_alfabeto, matriz_posicion, contador

    h = 0 
    for i in range(y,14):
        matriz_alfabeto[i][x] = palabra_sep[h]
        matriz_posicion[i][x] = 1
        x -= 1
        h += 1
        if len(palabra_sep) == h:
            return matriz_alfabeto, matriz_posicion, contador

class sopa_letras(Juego):

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
            alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",]

            palabra_sep =[]
            direccion = [random.randint(0, 3),random.randint(0, 3),random.randint(0, 3)] #Esta lista funciona como un vector que establece la direccion de las palabras
            palabras = []
            pistas = []
            aciertos = []
            
            keys = list(self.preguntas[0].keys())

            for i in keys:         
                if 'clue' not in i:
                    palabras.append(self.preguntas[0][i].lower())
                else:
                    pistas.append(self.preguntas[0][i].lower())

            matriz_alfabeto = [None] * 15  #Se crea una lista con 15 espacios en blanco
            matriz_posicion = [None] * 15

            matriz_alfabeto = generar_lista_vacia(matriz_alfabeto) #Se completa una matriz 15x15
            matriz_posicion = generar_lista_vacia(matriz_posicion)

            for i in range(15):
                for j in range(15):
                    matriz_alfabeto[i][j] = alfabeto[ random.randint(0, 26) ] #Se agrega aleatoriamente un numero entre 0 y 26 en la matriz del juego

            for i in range(15):
                    for j in range(15):
                        matriz_posicion[i][j] = 0 # se agregan ceros en toda la matriz posicion (Esta matriz se utiliza para que despues las palabras no choquen entre sí)

            for j,i in enumerate(direccion): #se utiliza el vector direccion para saber la direccion de la palabra
                if i == 0:
                    palabra = palabras[j]
                    palabra_sep = generar_lista(palabra, palabra_sep) #Se separan las palabras en letras
                    matriz_alfabeto, matriz_posicion, cont = vertical( matriz_alfabeto, palabra_sep, matriz_posicion) 
                    if cont == 10:
                        return self.jugar(jugador) #En caso de que la sopa de letras se tranque, porque no puede insertar la palabra en ninguna posicion, se da un plazo de 10 intentos, si no lo cponsigue se aplica recursividad para empezar desde el principio la creacion del juegos
                elif i == 1:
                    palabra = palabras[j]
                    palabra_sep = generar_lista(palabra, palabra_sep)
                    matriz_alfabeto, matriz_posicion, cont = horizontal( matriz_alfabeto, palabra_sep, matriz_posicion)
                    if cont == 10:
                        return self.jugar(jugador)
                elif i == 2:
                    palabra = palabras[j]
                    palabra_sep = generar_lista(palabra, palabra_sep)
                    matriz_alfabeto, matriz_posicion, cont = diagonal( matriz_alfabeto, palabra_sep, matriz_posicion)
                    if cont == 10:
                        return self.jugar(jugador)
                else:
                    palabra = palabras[j]
                    palabra_sep = generar_lista(palabra, palabra_sep)
                    matriz_alfabeto, matriz_posicion, cont = diagonal1( matriz_alfabeto, palabra_sep, matriz_posicion)
                    if cont == 10:
                        return self.jugar(jugador)

            table_instance = SingleTable(matriz_alfabeto) #Imprime en formato tabla 
            table_instance.outer_border = True
            table_instance.inner_row_border = True

            print(f'\n\nBienvenido al juego {self.nombre}')
            print('Debes buscar en la sopa de letras palabras relacionadas con la UNIMET')
            print(f'{self.regla}')
            print(table_instance.table)

            bol = True

            while bol:

                opcion = input("\nIndica qué acción deseas realizar\n1- Responder una palabra \n2- Pedir una pista \n3- Salir \n ==> ")

                while not ( opcion in('1','2','3') ):

                    opcion = input("Ingreso invalido, selecciona una opción correcta: ")

                if opcion == '1':

                    res = input('Ingresa la palabra: ')
                    res = res.lower()

                    if (res in palabras) and (res not in aciertos):
                        print("Has acertado una palabra")
                        aciertos.append(res)
                    elif res in aciertos:
                        print('Ya has ingresado esa palabra anteriormente')
                    else:
                        print("Vaya, esa palabra no es una respuesta")
                        jugador.perder_vida(0.5)
                        if jugador.vidas <= 0:
                            return jugador

                elif opcion == '2':
                    if jugador.pistas > 0:
                        if len(pistas) > 0:
                            print(pistas[0])
                            pistas.pop(0)
                            jugador.usar_pista()
                        else:
                            print('Ya no quedan más pistas en la sopa de letras')
                    else:
                        print('Te has quedado sin pistas.')

                elif opcion == '3':
                    bol = False
                    return jugador

                if len(aciertos) == 3:
                    print('Superaste el resto')
                    print('Has conseguido una vida extra')
                    self.ganado = True
                    jugador.sumar_vida(1)
                    bol = False
                    return jugador

            return jugador
            
                    

        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador

