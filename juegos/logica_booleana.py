import random
import requests
import json
from clases.juego import Juego
import colored
from colored import stylize

class logica_booleana(Juego):
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
            if self.requerimiento in jugador.recompensas:
                pregunta = self.preguntas[0]['question']
                respuesta = self.preguntas[0]['answer']
                respuesta = respuesta.lower()

                print(f"\nBienvenido al juego {self.nombre}")
                print(self.regla)
                print(pregunta)
                res = input("Introduce tu respuesta acá: ")

                res = res.lower()

                while res != respuesta:  #Compara la respuesta del usuario con la respuesta de a Api
                    jugador.perder_vida(0.5)
                    if jugador.vidas <= 0:
                        break
                    print("Respuesta incorrecta!")
                    opcion = input('Selecciona una acción a realizar: \n1.Ingresar otra respuesta \n2. Salir')   

                    while not opcion in ('1','2'):
                        opcion = input('Selecciona una acción a realizar:' )
                    if opcion == '1':

                        res = input("Respuesta incorrecta. Introduce tu respuesta acá: ")
                        res = res.lower()

                    else:
                        return jugador

                res = res.lower()
                if res == respuesta:
                    print("Felicidades, superaste el reto")
                    jugador.agregar_recompensa(self.premio)
                    self.ganado = True
                    print(f"Has conseguido {self.premio}")
                    return jugador
                else:
                    print("Vuelve a intentarlo en la próxima")

            else:
                print(" ", colored.fg("red"))
                print(f"\n       {self.mensaje_requerimiento}. Necesitas un {self.requerimiento}", colored.fg("white"))
                return jugador
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador