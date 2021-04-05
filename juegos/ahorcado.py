import requests
import json
import random
from clases.juego import Juego
import colored
from colored import stylize

def lista_espacios(palabra): #Esta funcion se cuenta el numero de letras que tiene la palabra para crear una lista con "_" para mostrar en la consola
    espacios = []
    letras = []
    for i in palabra:
        letras.append(i)
        espacios.append("_")

    return letras, espacios

def configuracion(letras, espacios, letra, aciertos): #Esta funcion sustituye "_" por letras en caso de queel usuario haya acertado
    k = 0
    for i,j in enumerate(letras):
        if j == letra:
            espacios[i] = letra
            aciertos.append(j)
            k += 1

    return espacios, k, aciertos

def menu(frase, imagen, espacios, seleccion, errores, letras, aciertos, pistas, jugador): #Se maneja el menu principal, así como los inputs
    
    while (len(aciertos) < len(espacios)) and ( errores < 4) : #Valida que si la persona se ha equivocado 4 veces cerrar el juego porque se "ahorcó"
        
        print(f"\n{frase}")
        print(imagen) #Variable imagen hace referencia al diagrama del dibujo donde se dibuja el muñeco

        for i in espacios:
            print(i,end=" ")

        opcion = input("\n\nIndica que acción deseas realizar\n1- Introducir una letra \n2- Pedir una pista \n3- Salir \n ==> ")

        while not ((opcion in ('1','2','3') )) :
            opcion = input("Ingreso invalido, selecciona una opción correcta: ")

        if opcion == "1":

           seleccion , errores, imagen, aciertos, jugador =  juego(espacios, seleccion, errores, letras, imagen, aciertos, jugador)#Se llama la función juego
           if jugador.vidas <= 0:
                return False, jugador

        elif opcion == "2": # Se manejan las pistas del juego para saber si el usuario tiene pistas disponibles
            if jugador.pistas > 0:
                if len(pistas) > 0:
                    print('Pista: '+ pistas[0])
                    pistas.pop(0)
                    jugador.usar_pista()
                else:
                    print(f"Ya no quedan pistas a utilizar en este juego")
            else:
                print("Te has quedado sin pistas")
            
        else:
            return "exit", jugador

    if errores < 4:
        return True, jugador                # Se retorna un bool que permite conocer si el usuario gano o perdio
    else:
        return False, jugador

def nada_ahorcado():
    return( '''
                -------|
                |      |
                       |
                       |
                       |
            -------------''')

def cara_ahorcado():
    return( '''
                -------|
                |      |
                O      |
                       |
                       |
            -------------''')

def cuerpo_ahorcado():
    return( '''
                -------|
                |      |
                O      |
                |      |
                       |
            -------------''')

def brazos_ahorcado():
    return( '''
                -------|
                |      |
                O      |
               \|/     |
                       |
            -------------''')

def piernas_ahorcado():
    return( '''
                -------|
                |      |
                O      |
               \|/     |
               / \     |
            -------------''')

def juego(espacios, seleccion, errores, letras, imagen, aciertos, jugador):

    
    letra = input("Introduce una letra: ")
    letra = letra.lower()
    while (letra in seleccion) or (len(letra) > 1): #Validar que se introdujo un caracter que no se haya introducido antes. 
        if letra in seleccion:
            letra = input("Ya has introducido esta letra anteriormente, escoge otra: ")
        else:
            letra = input("¡Vaya! Estás yendo muy rápido, introduce una letra a la vez: ")
    seleccion.append(letra)
    espacios, k, aciertos = configuracion(letras, espacios, letra, aciertos) # se llama configuraciones para validar si acertó en el caracter
    if k == 0: #Si se equivoca entra a este if donde se evalua cuantos fallos lleva. Aca se asigna la imagen que se debe de imprimit
        errores += 1
        if errores == 1:
            print("\n¡Ouch! te quedan 3 oportunidades más")
            jugador.perder_vida(0.25)
            imagen = cara_ahorcado()
        elif errores == 2:
            print("\n¡Ouch! te quedan 2 oportunidades más")
            jugador.perder_vida(0.25)
            imagen = cuerpo_ahorcado()
        else:
            imagen = brazos_ahorcado()
            jugador.perder_vida(0.25)
            print("\n¡Ouch! te queda 1 oportunidad más")
        

    return seleccion, errores, imagen, aciertos, jugador
        

class ahorcado(Juego):
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
            frase = self.preguntas[0]['question']
            palabra = self.preguntas[0]['answer']
            palabra = palabra.lower()
            letras, espacios = lista_espacios(palabra)
            seleccion = []
            aciertos = []
            errores = 0 
            palabra = palabra.lower()
            imagen = nada_ahorcado()
            keys = list(self.preguntas[0].keys())
            pistas = []
            for i in keys:
                if i != 'question' and i != 'answer':
                    pistas.append(self.preguntas[0][i])
            print(f"\nBienvenido al juego {self.nombre}\n")
            print(f"La palabra que debes de adivinar está relacionada con la siguiente frase: \n-{frase} \nTienes solo 4 oportunidades antes de ahorcarte\n{self.regla} \n¡¡EMPECEMOS!!")
            bol, jugador = menu(frase, imagen, espacios, seleccion, errores, letras, aciertos, pistas, jugador)
            if bol == True: #Se agrega la recompensa al validar si gano el juego
                print("Felicidades, has ganado")
                self.ganado = True
                jugador.agregar_recompensa(self.premio)
                print(f"Has conseguido la siguiente recompensa: {self.premio}")
                return jugador
            elif bol == "exit": # permite al jugador salir del juego
                return jugador
            else:
                print(piernas_ahorcado())
                jugador.perder_vida(0.25)
                print("Vaya, no has conseguido superar el reto")
                return jugador
        
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador
    