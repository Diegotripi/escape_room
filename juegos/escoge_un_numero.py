import random
import requests
import json
from clases.juego import Juego
import colored
from colored import stylize
from juegos.encuentra_logica import *


class escoge_un_numero(Juego):
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

    def get_premio(self):
        self.premio = self.premio.replace("í","i")
        self.premio = self.premio.title()
        return self.premio

    def jugar(self, jugador): 
        if self.ganado == False:
            info = self.preguntas[0]
            print(f"Bienvenido al juego {self.nombre}")
            frase = info['question']
            print(frase)
            a = frase[frase.find("entre")+6:]
            a = a.split('-') #Selecciona el intervalo donde se agarrá un número random
            q = random.randint(int(a[0]),int(a[1]))
            res2 = 0
            fallas = 0
            while True:

                opcion = input("Introduce que acción deseas realizar: \n1. Seleccionar un número \n2. Pista \n3.Salir \n==>")
                while not opcion in ('1','2','3'):
                    opcion = input("Introduce que acción deseas realizar: ")

                if opcion == "1":
                    res  = input("Introduce tu respuesta: ")
                    while not res.isnumeric():
                        res  = input("Introduce tu respuesta: ")

                    if int(res) == q:
                        print('Felicidades, superaste el reto')
                        print(f"Has conseguido {self.premio}")
                        self.ganado = True
                        jugador.agregar_recompensa(escoge_un_numero.get_premio(self))
                        return jugador
                    else:
                        print('Vuelve a intentarlo')
                        fallas += 1
                        if fallas == 3:
                            jugador.perder_vida(0.25)
                            fallas = 0
                            if jugador.vidas <= 0:
                                return jugador
                        res2 = res

                elif opcion == "2": # Las pistas validan que numero introdujiste anteriormente y te indica que tan cerca estas 

                    if res2 == 0:

                        print("Debes ingresar una respuesta anteriormente para obtener una pista")

                    else:
                        if jugador.pistas > 0:
                            jugador.usar_pista()
                            if (int(res)-4) > q:
                                print("Estás muy arriba")
                            elif int(res)+4 < q:  #arbitrariamente escogí el cuatro como limite entre que esta cerca y esta lejos el numero
                                print("Estás muy abajo")
                            elif int(res) < q:
                                print("Estás un poco abajo")
                            elif int(res) > q:
                                print("Estás un poco arriba")
                        else:
                            print('Te has quedado sin pistas.')
                
                else: 
                    return jugador
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador