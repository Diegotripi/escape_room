import random
import requests
import json
from clases.juego import Juego
import colored
from colored import stylize

def config(palabra):
    k = 0
    n = len(palabra)
    while not k == 20:
        k += 1
        m = random.randint(0, n-1)
        f = random.randint(0,n-1)
        while m == f:
            f = random.randint(0,n-1)
        a = palabra[m]
        b = palabra[f]
        palabra[m] = b 
        palabra[f] = a 
    
    resultado = "".join(palabra)   #Utiliza random para mezclar las palabras. Se realizan 20 movimientos en el ciclo while

    return resultado

def mezclador(palabras):

    mezcla = []

    for i in palabras:

        palabra = []

        for j in i:
            palabra.append(j.lower())

        resultado = config(palabra)

        while resultado == i:
            resultado = config(palabra) #inserta en una lista la palabra mezclada
        
        mezcla.append(resultado)

    return mezcla
    

class palabra_mezclada(Juego):

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
            informacion = self.preguntas
            nquestion = random.randint(0,(len(informacion))-1)
            palabras = []

            for i in informacion[nquestion]['words']:
                palabras.append(i)

            print(f"\nBienvenido al juego {self.nombre}")
            print(f"{informacion[nquestion]['question']}")
            print("Reglas: "+ self.regla)
            print(f"Categoria: {informacion[nquestion]['category']}\nCOMENCEMOS\n")

            mezcla = mezclador(palabras)

            for i,j in enumerate(mezcla):

                print(f"\n{i+1}- {j}")
                respuesta = input("Introduce la palabra ordenada: ")
                respuesta = respuesta.lower() #valida que la palabra es correcta y pasa a a la siguiente

                print(respuesta)

                while not respuesta == palabras[i]:
                    jugador.perder_vida(0.5)
                    respuesta = input("\nRespuesta incorrecta. Introduce la palabra ordenada: ")

            print("Felicidades")
            self.ganado = True
            jugador.agregar_recompensa(self.premio)
            print(f"Has conseguido {self.premio} ")
            return jugador
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador
