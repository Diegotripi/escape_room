import requests
import json
import random
from clases.juego import Juego
from colored import stylize
import colored


def configurador(opciones): #Crea una lista que permite saber cual es la respuesta correcta de las opciones

    leyenda = []

    for i in opciones:

        if i == "correct_answer":
            leyenda.append(True)
        else:
            leyenda.append(False)
        
    return leyenda

def menu(leyenda, jugador, pista, premio):
  
    opcion = input("\nIndica que acción deseas realizar\n1- Responder a la pregunta \n2- Pedir una pista \n3- Salir \n ==> ")
    while not ( opcion.isnumeric()  or ( 1 <= int(opcion) <= 3) ):
        opcion = input("Ingreso invalido, selecciona una opción correcta: ")

    if opcion == "1":
        
        variable = juego(leyenda) #retorna un booleano para saber si ganó el juego

        if variable:
            jugador.agregar_recompensa(premio)
            return True, "\nLo has conseguido. ¡Felicidades!\n", jugador
        else: 
            jugador.perder_vida(0.5)
            return False, "\n¡Oh no!, tu respuesta ha sido incorrecta\n", jugador
        
    elif opcion == "2":  #Evalúa si hay pistas disponibles y la imprime
        if pista != False: 
            if jugador.pistas > 0:
                jugador.usar_pista()
                print(f'La pista es: {pista}')
                pista = False
                return menu(leyenda, jugador, pista, premio)
            else:
                print('Te has quedado sin pistas!')
                return menu(leyenda, jugador, pista, premio)
        else:
            print('Usaste la unica pista del juego!')
            return menu(leyenda, jugador, pista, premio)
    else:
        print('llegue')
        return True, "\nHas salido correctamente del juego\n", jugador

def juego(leyenda):

    opcion = input("\nIntroduce el número de tu respuesta: ")

    while (not opcion.isnumeric() and opcion not in range(0, len(leyenda))):
        opcion = input("¡Vaya! Ingreso inválido. Introduce el número de tu respuesta: ")

    opcion = int(opcion)

    if leyenda[(opcion-1)]:
        return True 
    else:
        return False
        

class cultura_unimetana(Juego):
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
            print("\n¡Bienvenido al quizziz de cultura unimetana!\n")
            print(f"{self.regla}")

            bol = False
            new_question = random.randint(0, len(self.preguntas) - 1)

            informacion = self.preguntas[new_question]

            frase  = informacion['question']
            preguntas = list(informacion.keys())
            respuestas = list(informacion.values())

            opciones = []
            pista = ''
            respuesta = []

            for i in preguntas:
                if i != 'question':
                    if 'clue' not in i:
                        opciones.append(i)
                    elif 'clue' in i:
                        pista = informacion[i]

            for index, i in enumerate(respuestas):
                if index != 0 and index != (len(respuestas)-1):
                    respuesta.append(i)

            print("Debes contestar correctamente la siguiente pregunta: \n")
            print(frase)


            for j,i in enumerate(respuesta): 
                print(f"{j+1}- {i}")

            leyenda = configurador(opciones)

            while not bol:
                bol, expresion, jugador = menu(leyenda, jugador, pista, self.premio)
                if expresion == "\nLo has conseguido. ¡Felicidades!\n":
                    self.ganado = True
                print(expresion)
                print(f'Recibes {self.premio}')

            return jugador
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador