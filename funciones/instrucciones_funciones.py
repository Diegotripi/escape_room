import colored
from art import *
from colored import stylize

def imprimir_instrucciones(): # Funcion para leer el txt de instrucciones e imprimirlas en consola
    tprint('Instrucciones')
    f = open("archivos/instrucciones.txt", "r")
    for x in f:
        print(x)
    res = input(stylize('\nPresiones enter para volver al menu.\n', colored.fg("blue")))
    pass