from clases.usuario import Usuario

class Jugador(Usuario):
    def __init__(self, username, password, edad, avatar, records, pistas, vidas, habitacion, recompensas, habitaciones, dificultad):
        super().__init__(username, password, edad, avatar, records)
        self.pistas = pistas
        self.vidas = vidas
        self.habitacion = habitacion
        self.recompensas = recompensas
        self.habitaciones = habitaciones
        self.dificultad = dificultad

    def __str__(self):
        return (f'''
            Pistas: {self.pistas}
            Vidas: {self.vidas}
            Habitacion Actual: {self.habitacion} 
            Recompensas: {self.recompensas}
        ''')

    def user_dict(self):
        return {
            'pistas': self.pistas, 
            'vidas': self.vidas,
            'habitacion_actual': self.habitacion,
            'recompensas': self.recompensas
        }

    def get_habitacion(self): # Funcion para obtener la habitacion actual
        return self.habitacion

    def set_habitacion(self, habitacion): # Funcion para asignar la habitacion actual
        self.habitacion = habitacion

    def perder_vida(self, vida): # Funcion para disminuir la vida
        self.vidas -= vida

    def sumar_vida(self, vida): # Funcion para aumentar la vida
        self.vidas += vida

    def usar_pista(self): # Funcion para descontar una pista
        self.pistas -= 1

    def agregar_recompensa(self, recompensa): # Funcion para agregar una recompensa al jugador
        self.recompensas.append(recompensa)

    def get_habitaciones(self): # Funcion para obtener las habitaciones
        return self.habitaciones
    
    def set_habitacion_plaza(self): # Funcion para aumentar las visitas a la habitacion
        self.habitaciones['rectorado'] = self.habitaciones['rectorado'] + 1

    def set_habitacion_biblioteca(self): # Funcion para aumentar las visitas a la habitacion
        self.habitaciones['biblioteca'] = self.habitaciones['biblioteca'] + 1
    
    def set_habitacion_lab(self): # Funcion para aumentar las visitas a la habitacion
        self.habitaciones['laboratorio'] = self.habitaciones['laboratorio'] + 1

    def set_habitacion_pasillo(self): # Funcion para aumentar las visitas a la habitacion
        self.habitaciones['pasillo'] = self.habitaciones['pasillo'] + 1

    def set_habitacion_servidores(self): # Funcion para aumentar las visitas a la habitacion
        self.habitaciones['servidores'] = self.habitaciones['servidores'] + 1

    def get_dificultad(self): # Funcion para obtener la dificultad
        return self.dificultad