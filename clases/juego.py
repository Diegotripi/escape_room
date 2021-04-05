from abc import ABC, abstractmethod

class Juego(ABC):
    def __init__(self,mensaje_requerimiento, requerimiento, nombre, premio, regla, preguntas, ganado):
        self.mensaje_requerimiento = mensaje_requerimiento
        self.requerimiento = requerimiento
        self.nombre = nombre
        self.premio = premio
        self.regla = regla
        self.preguntas = preguntas
        self.ganado = ganado

    def mensaje(self): # Funcion para imprimir el mensaje
        print(self.mensaje_requerimiento)
    
    def requerido(self): # Funcion para imprimir el requerimiento
        print(self.requerimiento)
    
    def nombre_juego(self): # Funcion para imprimir el nombre
        print(self.nombre)
    
    def premio_juego(self): # Funcion para imprimir el premio
        print(self.premio)
    
    def regla_juego(self): # Funcion para imprimir la regla
        print(self.regla)

    @abstractmethod
    def jugar(self, jugador): # Funcion abstracta Jugar
        pass