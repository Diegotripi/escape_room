import time # Libraria de Tiempo
import threading # Libreria para Funciones en Paralelo
import os,signal
from art import * # Libreria para imprimir Texto con Estilos
import colored # Libreria para agregar color al Texto
from colored import stylize # Libreria para agregar color al Texto
from clases.timer import Timer
from clases.usuario import Usuario
from clases.jugador import Jugador
from funciones.config_funciones import *
from funciones.usuario_funciones import *
from funciones.habitacion_funciones import *
from funciones.estadisticas_funciones import *
from funciones.instrucciones_funciones import *
from multiprocessing import Process # Libreria para Funciones en Paralelo

t1 = ''
timer = '' # variable global para mantener el programa al tanto del tiempo restantte
mapa = [] # variable global para saber en que habitacion esta el jugador
jugador = {} # variable global del jugador

def menu_principal(): # Funcion para mostrar al jugador las opciones
    global t1
    tprint('***MENU***')
    opcion = input('''
    1. Comenzar Juego.
    2. Crear Usuario.
    3. Ver Estadisticas.
    4. Intrucciones.
    5. Salir
    ==> ''')

    while (not opcion.isnumeric() or (int(opcion) not in range(1,6))):
            opcion = input('\nIngrese una opcion valida: \n')
    
    opcion = int(opcion)

    if opcion == 1:
        config_game()
    elif opcion == 2:
        crear_usuario()
    elif opcion == 3:
        menu_estadisticas()
    elif opcion == 4:
        imprimir_instrucciones()
    elif opcion == 5:
        os._exit(0)
    menu_principal()

def menu_estadisticas(): # Funcion para indicarle al jugador que estadistica desea visualizar
    tprint('***Estadisticas***')
    opcion = input('''
    1. Learderboard.
    2. ¿Cuáles son los cuartos más visitados por cada jugador?.
    3. ¿Quienes son los usuarios que más juegan?.
    4. Volver
    ==> ''')

    while (not opcion.isnumeric() or (int(opcion) not in range(1,5))):
            opcion = input('\nIngrese una opcion valida: \n')
    
    opcion = int(opcion)

    if opcion == 1:
        top_leaders()
    elif opcion == 2:
        top_cuartos_visitados()
    elif opcion == 3:
        top_cantidad_de_juegos()
    elif opcion == 4:
        pass

def timer(t): # Funcion que declara la clase Timer y comienza a contar los segundos para concluir el tiempo 
    global timer
    global t1
    timer = Timer(0, 0)
    cont = 0
    while t:
        mins, secs = divmod(t, 60)
        countdown = '{:02d}:{:02d}'.format(mins, secs)
        timer.set_time(countdown)
        timer.set_time_seg(cont)
        time.sleep(1)
        t -= 1
        cont += 1
    
    print('')
    tprint('Perdedor')
    os._exit(0)

def room_options():
    global mapa
    global jugador
    global timer
    
    habitacion_actual = mapa[jugador.habitacion] # Variable para tener la informacion de la habitacion actual
    objetos = len(habitacion_actual.objetos_dentro) # Variable para conocer la cantidad de objetos de la habitacion
    opciones = len(habitacion_actual.objetos_dentro) # Variable para conocer la cantidad de objetos de la habitacion
    tprint(f'       {habitacion_actual.nombre}')
    print(f'        JUGADOR -> {jugador.avatar} VIDA: {jugador.vidas} ❤️ PISTAS RESTANTE: {jugador.pistas} 🔎')
    print(f'        RECOMPENSAS:')
    print(f'        {jugador.recompensas}')
    print(f'        TE RESTAN ' + timer.get_time(), end="\r")
    habitacion_actual.plano_habitacion()

    if (habitacion_actual.habitacion_izquierda == ''):
        print(f'        {objetos + 1}. Ir a {habitacion_actual.habitacion_derecha}')
        opciones += 2
    elif (habitacion_actual.habitacion_derecha == ''):
        opciones += 2
        print(f'        {objetos + 1}. Ir a {habitacion_actual.habitacion_izquierda}')
    else:
        print(f'        {objetos + 1}. Ir a {habitacion_actual.habitacion_izquierda}')
        print(f'        {objetos + 2}. Ir a {habitacion_actual.habitacion_derecha}')
        opciones += 3

    select = input('        Selecciona una opcion:')
    while (not select.isnumeric() or (int(select) not in range(1,opciones))):
        select = input('\n        Ingrese una opcion valida: ')
    select = int(select)


    if select <= objetos:
        juego = habitacion_actual.objetos_dentro[select-1]['game']
        jugador = juego.jugar(jugador)
        if jugador.vidas <= 0:
            tprint('Perdedor')
            os._exit(0)
        if 'Trofeo' in jugador.recompensas:
            record = {"username": jugador.username, "tiempo": timer.get_time_seg(), "dificultad": jugador.get_dificultad(), "habitaciones": jugador.get_habitaciones() }
            guardar_record(record)
            tprint('Ganador')
            os._exit(0)
    else:
        puerta = False # Variable para verificar que la puerta en el pasillo esta rota
        if (select == objetos + 1):
            if (habitacion_actual.habitacion_izquierda == ''):
                jugador.set_habitacion(jugador.habitacion + 1)
            else:
                puerta = True
                jugador.set_habitacion(jugador.habitacion - 1)
        else:
            hab = mapa[jugador.habitacion + 1]
            if hab.nombre.lower() == 'laboratorio sl001':
                hab = mapa[jugador.habitacion]
                if hab.objetos_dentro[0]['game'].ganado == True:
                    puerta = True
                    jugador.set_habitacion(jugador.habitacion + 1)
            else:
                jugador.set_habitacion(jugador.habitacion + 1)
                    
        habitacion_actual = mapa[jugador.habitacion]

        if habitacion_actual.nombre.lower() == 'biblioteca':
            jugador.set_habitacion_biblioteca() # Aumenta la cantidad de visitas en la habitacion
        elif habitacion_actual.nombre.lower() == 'laboratorio sl001':
            jugador.set_habitacion_lab() # Aumenta la cantidad de visitas en la habitacion
        elif habitacion_actual.nombre.lower() == 'plaza rectorado':
            jugador.set_habitacion_plaza() # Aumenta la cantidad de visitas en la habitacion
        elif habitacion_actual.nombre.lower() == 'pasillo laboratorios ':
            if puerta == True:
                jugador.set_habitacion_pasillo() # Aumenta la cantidad de visitas en la habitacion
            else:
                print(stylize('No puedes pasar hasta romper la puerta', colored.fg("yellow")))
        elif habitacion_actual.nombre.lower() == 'cuarto de servidores ':
            jugador.set_habitacion_servidores() # Aumenta la cantidad de visitas en la habitacion
        

    room_options()

def start_game(t):
    global t1
    global jugador
    t1 = threading.Thread(target=timer, args=(t, )) # Declara el timer con una funcion paralela
    t1.start() # Comienza el timer
    time.sleep(0.5) # Se para el programa or 0.5 seg antes de correr el juego 
    
    print(stylize(f'\nHoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {timer.time} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?', colored.fg("sky_blue_2")))

    opcion = input('(si/no)==> ')
    opcion = opcion.lower()
    while not opcion in ('si', 'no'):
        opcion = input('Ingresa una opcion valida(si/no)==> ')

    if opcion == 'si':
        print(stylize(f"\n\nBienvenido {jugador.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.", colored.fg("sky_blue_2")))
        room_options() # Comienza el juego
    else:
        tprint('Cobarde')
        os._exit(0) # Sale del programa y mata al timer
        
def crear_mapa(usuario): # Funcion para crear la lista con las habitaciones y sus objetos
    global mapa
    global jugador
    mapa = obtener_info_api() # Obtener info API
    configs = obtener_configuraciones() # Obtener las configuraciones del juego
    tprint('Dificultad')
    for index, config in enumerate(configs):
        print(str(index+1)+'. ' + config['dificultad'])

    opcion = input('Ingrese la dificultad: ')

    while (not opcion.isnumeric() or (int(opcion) not in range(1,len(configs)+1))):
        opcion = input('\nIngrese una opcion valida: \n')
    
    opcion = int(opcion)
    selecion = configs[opcion-1]
    jugador = Jugador(usuario['username'], usuario['password'], usuario['edad'], usuario['avatar'], usuario['records'], selecion['pistas'], selecion['vidas'], 1, [], {"rectorado": 0, "biblioteca": 1, "pasillo": 0, "laboratorio": 0, "servidores": 0} ,configs[opcion-1]['dificultad'])
    t = selecion['time']
    start_game(t)
    
def config_game():
    res = login()
    if res != False:
        crear_mapa(res)

def main():
    menu_principal()

main()