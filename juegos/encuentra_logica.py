import requests
import json
import random
from clases.juego import Juego
import colored
from colored import stylize

class encuentra_logica(Juego):
    
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
            if (self.requerimiento[0] in jugador.recompensas) and (self.requerimiento[1] in jugador.recompensas):
                arreglo = ("".join(self.preguntas[0].split(" ")))
                print(f"\nBienvenido al {self.nombre}")
                print(f"Debes de resolver el siguiente acertijo para ganar \n{arreglo}")
                respuesta = input("Introduce tu respuesta acá: ")
                if (respuesta == "67" or respuesta == "41"):
                    print("Lo has conseguido")
                    print(f"Ganaste {self.premio}")
                    self.ganado = True
                    jugador.agregar_recompensa(self.premio)
                    return jugador
                else:
                    print("Has perdido")
                    jugador.perder_vida(1)                   #Este juego simplemente valida el input del usuario con la respuesta
                    return jugador
            else:
                print(" ", colored.fg("red"))
                print(f"\n       {self.mensaje_requerimiento}", colored.fg("white"))
                jugador.perder_vida(1)
                return jugador
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador
