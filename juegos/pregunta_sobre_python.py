import random
import requests
import json
from clases.juego import Juego
import colored
from colored import stylize

#Respuestas
## int(float(frase.split(' ')[4].replace(',','.')))
#  " ".join([frase.split(' ')[0][::-1],frase.split(' ')[1][::-1],frase.split(' ')[2][::-1],frase.split(' ')[3][::-1],frase.split(' ')[4][::-1],frase.split(' ')[5][::-1],frase.split(' ')[6][::-1]])
#  ' '.join([i[::-1] for i in frase.split()])

class pregunta_python(Juego):
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
                oracion = self.preguntas[0]['question']
                keys = list(self.preguntas[0].keys())

                pistas = []
                respuesta = []

                for i in keys: #
                    if i != 'answer' and i != 'question':
                        pistas.append(self.preguntas[0][i])
                    elif i == 'answer':
                        respuesta.append(self.preguntas[0][i])

                frase = oracion[oracion.find("\"")+1: oracion.find(".", oracion.find("\""))] #Extrae la frase del enunciado
                print(f'Bienvenido al juego {self.nombre}')
                print(oracion)
                while True:
                    opcion = input("\nIndica qué acción deseas realizar\n1- Responder a la pregunta \n2- Pistas\n3- Salir\n==> ")
                    while not ( opcion in('1','2', '3') ):
                        opcion = input("Ingreso invalido, selecciona una opción correcta: ")

                    if opcion == "1":

                        res = input(f"Introduce tu respuesta acá, la oración {frase} se encuentra guardada en la variable frase: ")

                        if "Validar en python que de el siguiente resultado: 50.00 en formato entero" in respuesta:

                            try:
                                if 50 == eval(res):
                                    print('Has superado el reto')
                                    print(f'Has conseguido {self.premio}')
                                    self.ganado = True
                                    jugador.agregar_recompensa(self.premio)
                                    break
                                else:
                                    print('Tu respuesta es incorrecta')
                                    jugador.perder_vida(0.5)
                            except:
                                print('Tu respuesta es incorrecta')
                                jugador.perder_vida(0.5)
                        else:
                            try:

                                tt = eval(res)

                                if "estudio en la metro ingenieria de sistemas" == eval(res): #Evalua el string de la respuesta con eval() para saber si las frases coinciden
                                    print('Lo has conseguido')
                                    self.ganado = True
                                    jugador.agregar_recompensa(self.premio)
                                    break
                                else:
                                    print(tt)
                                    print('Tu respuesta es incorrecta')
                                    jugador.perder_vida(0.5)
                            except:
                                print('Tu respuesta es incorrecta')
                                jugador.perder_vida(0.5)

                    elif opcion == '2':

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

                return jugador
            else:
                print(" ", colored.fg("red"))
                print(f"\n       {self.mensaje_requerimiento}\n       Te hace falta {self.requerimiento} para jugar este juego.", colored.fg("white"))
                return jugador

        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador