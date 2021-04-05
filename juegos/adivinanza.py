import requests
import json
import random
from clases.juego import Juego
import colored
from colored import stylize

class adivinanza(Juego):
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
            if 'contraseña' in jugador.recompensas:
                print(f"\n¡Bienvenido al juego {self.nombre}!")
                print("Regla: "+ self.regla)
                print (f"Debes de conseguir adivinar a qué hace referencia la siguiente frase: \n{self.preguntas[0]['question']}")
                keys = list(self.preguntas[0].keys())
                pistas = []
                for i in keys:
                    if i != 'question' and i != 'answers':
                        pistas.append(self.preguntas[0][i])
                while True: #Se entra en un ciclo while con un menu donde el usuario interactuara con el juego. Aca se manejan las pistas y las respuestas 

                    opcion = input("\nIndica qué acción deseas realizar\n1- Responder a la adivinanza \n2- Pedir una pista \n3- Salir \n ==> ")
                    while not ( opcion in('1','2','3') ):

                        opcion = input("Ingreso invalido, selecciona una opción correcta: ")

                    if opcion == "1": 
                        palabra = input("\nIntroduce la respuesta a la adivinanza: ") #Input de respuesta 
                        if palabra in self.preguntas[0]["answers"]: #Si la respuesta es correcta se agrega la recomensa y se marca el juego como ganado
                            print ("\n¡Vaya! lo has conseguido, felicidades")
                            jugador.agregar_recompensa(self.premio) 
                            self.ganado = True
                            print(f"Has conseguido la siguiente recompensa: {self.premio}")
                            return jugador
                        else: # Si la respuesta es incorrecta se entra en este apartado, se descuenta vida y se hace termina el juego si la vida del jugador es 0
                            print("\n¡Oh no! La respuesta es incorrecta")
                            jugador.perder_vida(0.5)
                            if jugador.vidas <= 0:
                                return jugador

                    elif opcion == "2": #Se manejan las pistas, valida que el jugador disponga de pistas a utilizar
                        if jugador.pistas > 0:
                            if len(pistas) > 0:
                                print(pistas[0])
                                pistas.pop(0)
                                jugador.usar_pista()
                            else:
                                print(f"Ya no quedan pistas a utilizar en este juego {self.nombre}")
                        else:
                            print("Te has quedado sin pistas")

                    else:
                        return jugador
            else: #En caso de no tener los requerimientos necesarios se entra en este apartado
                print(" ", colored.fg("red"))
                print(f"\n       {self.mensaje_requerimiento}", colored.fg("white"))
                return jugador
        else: #Si el juego ya ha sido ganado se entra en este apartado
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador
