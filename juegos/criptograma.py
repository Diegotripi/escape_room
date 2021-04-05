import requests
import json
import random
from clases.juego import Juego
import colored
from colored import stylize
from terminaltables import SingleTable
from juegos.encuentra_logica import *

def desplazar(abecedario, alfabeto_desplazado, m, n): #Esta funcion desplaza el alfabeto
    
    for i in range(m, n):
        alfabeto_desplazado.append(abecedario[i])
    return alfabeto_desplazado

def eliminar_acentos(frase): #realiza un replace de acentos y u con dieresis 

    frase = frase.replace("á","a")
    frase = frase.replace("é","e")
    frase = frase.replace("í","i")
    frase = frase.replace("ó","o")
    frase = frase.replace("ú","u")
    frase = frase.replace("ü","u")
    frase = frase.upper()
    return frase

def generar_frase(frase, alfabeto_desplazado, abecedario): #Separa la frase en caracteres y genera la frase desplazada

    frase_sep = []
    for i in frase:
        frase_sep.append(i)

    guia = []

    for j in frase_sep:
        for l,i in enumerate(abecedario):       #El forloop se encarga de generar una lista con numeros. Cada numero es la posicion de la letra de la frase en el abecedario original. El -6 se usa para representar espacios en blanco
            if j == i:
                guia.append(l)
                break
            elif j == " ":
                guia.append(-6)
                break

    criptograma_lst = []

    for i in guia: #Se va a leer la lista guia que esta llena de numeros. A su vez, sustituye los numeros segun la letra que le corresponde en el alfabeto desplazado
        if i >= 0:
            criptograma_lst.append(alfabeto_desplazado[i])
        else:
             criptograma_lst.append(" ")

    var = ""  #Genera un string con la frase ya dezplazada 
    for i in range(0,len(criptograma_lst)):
        var = var + criptograma_lst[i]
    return var 


class criptograma(Juego):
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
        return 'Mensaje'

    def jugar(self, jugador): 
        if self.ganado == False:
            if self.requerimiento in jugador.recompensas:
                abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                alfabeto_desplazado = []
                rango_desplazamiento = self.preguntas[0]['desplazamiento']
                frase = self.preguntas[0]['question']
                frase = frase.lower()

                alfabeto_desplazado = desplazar(abecedario, alfabeto_desplazado, rango_desplazamiento, 27 )
                alfabeto_desplazado = desplazar(abecedario, alfabeto_desplazado, 0, rango_desplazamiento )
                frase = eliminar_acentos(frase)
                frase_desplazada = generar_frase(frase, alfabeto_desplazado, abecedario)


                print(f'\nBienvenido al juego {self.nombre}')
                print('Debes descifrar la siguiente frase : ' + frase_desplazada)
                print("Reglas:" + self.regla)
                print('\nHas conseguido las siguientes notas que te permitirán resolver el acertijo: \n')

                for i in abecedario:
                    print(i,end=" ")

                print('')

                for i in alfabeto_desplazado:
                    print(i,end=" ")

                while True:

                    opcion = input("\n\nIndica qué acción deseas realizar\n1- Responder al criptograma \n2- Salir\n ==> ")

                    while not ( opcion in('1','2') ):
                        opcion = input("Ingreso invalido, selecciona una opción correcta: ")

                    if opcion == '1':
                        respuesta = input("Introduce tu respuesta: ")

                        if respuesta.lower() == frase.lower(): #Se valida si la frase introducida es igual a la frase que se desea evaluar
                            print('¡Has ganado!')
                            self.ganado = True
                            jugador.agregar_recompensa(criptograma.get_premio(self))
                            print(f"Has conseguido la siguiente recompensa: {self.premio}")
                            return jugador
                        else: 
                            print('Tu respuesta es incorrecta')
                            jugador.perder_vida(1)
                            return jugador
                    if opcion == "2":
                        return jugador
            else:
                print(" ", colored.fg("red"))
                print(f"\n       {self.mensaje_requerimiento}", colored.fg("white"))
                return jugador
        else:
            print(stylize("\n       Este juego ya se completo", colored.fg("yellow")))
            return jugador