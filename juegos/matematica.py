import sympy 
import random
import requests
import json
import random
from clases.juego import Juego
import colored
from colored import stylize

def funcion(frase):

    funcion = frase[frase.find("=")+1:]
    funcion = funcion.replace('sen', 'sin')  #Extrae la funcion que se debe evaluar y hace replace de la funcion seno para que se pueda usar con la libreria sympy
    funcion = sympy.parse_expr(funcion)
    return funcion

def variable(frase):

    var = frase[frase.find("pi"): frase.find(" ", frase.find("pi"))]

    return var

class matematica(Juego):
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
                x,y = sympy.symbols("x y")

                frase = self.preguntas[0]['question']
                print(f"Bienvenido al juego {self.nombre}")
                print(frase)
                y = funcion(frase)
                var = variable(frase) #Derivar con la libreria
                f =  y.diff(x)
                res = ''

                if var == "pi":
                    resultado = f.subs(x , sympy.pi)  #Valida cual numero se debe usar a la hora de evaluar la derivada
                elif var == "pi/2":
                    resultado = f.subs(x , (sympy.pi)/2)
                else:
                    resultado = f.subs(x , (sympy.pi)/3)

                resultado = str(resultado)

                while res != resultado:
                    opcion = input("\nIndica qué acción deseas realizar\n1- Responder \n2- Pedir una pista \n3- Salir \n ==> ")
                    while not ( opcion in('1','2','3') ):
                        opcion = input("Ingreso invalido, selecciona una opción correcta: ")

                    if opcion == '1': 
                        res = input('Ingrese su respuesta: ')#Valida que la respuesta es correcta
                        if res == resultado:
                            jugador.sumar_vida(1)
                            print('Los has conseguido.')
                            self.ganado = True
                            return jugador
                        else:
                            jugador.perder_vida(0.25)
                            print('Has perdido.')
                            if jugador.vidas <= 0:
                                return jugador
                    elif opcion == '2':
                        print('No hay pistas aquí jajajajaja')
                    else:
                        return jugador
            else:
                print(" ", colored.fg("red"))
                print(f"\n       No puedes ingresar. {self.mensaje_requerimiento}", colored.fg("white"))
                return jugador
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador