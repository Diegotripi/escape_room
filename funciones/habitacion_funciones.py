import json
import requests
import random as rd
from clases.habitacion import *
from juegos.encuentra_logica import encuentra_logica
from juegos.ahorcado import ahorcado
from juegos.adivinanza import adivinanza
from juegos.criptograma import criptograma
from juegos.matematica import matematica
from juegos.cultura_unimetana import cultura_unimetana
from juegos.memoria import memoria
from juegos.palabras_mezcladas import palabra_mezclada
from juegos.sopa_de_letra import sopa_letras
from juegos.escoge_un_numero import escoge_un_numero
from juegos.logica_booleana import logica_booleana
from juegos.pregunta_sobre_python import pregunta_python
from juegos.busca_minas import busca_minas

def obtener_info_api(): # Funcion para obtener la info de la API 
    mapa = []
    res = requests.get('https://api-escapamet.vercel.app/')
    rooms = json.loads(res.text)
    for index, room in enumerate(rooms):
        for objeto in room['objects']:
            questions = len(objeto['game']['questions'])
            ## Verificacion de Cantidad Preguntas
            if objeto['game']['name'] == 'Quizizz Cultura Unimetana':
                pass
            elif questions > 1:
                new_question = rd.randint(0, questions - 1)
                objeto['game']['questions'] = [objeto['game']['questions'][new_question]]

            ## Inicializacion de los juegos
            if objeto['game']['name'] == 'Quizizz Cultura Unimetana':
                juego = cultura_unimetana('', objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'Encuentra la lógica y resuelve':
                juego = encuentra_logica(objeto['game']['message_requirement'], objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'ahorcado':
                juego = ahorcado('', objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'Adivinanzas':
                juego = adivinanza(objeto['game']['message_requirement'], objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'Criptograma':
                juego = criptograma(objeto['game']['message_requirement'], objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'Preguntas matemáticas':
                juego = matematica(objeto['game']['message_requirement'], objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'memoria con emojis':
                juego = memoria('', objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'Palabra mezclada':
                juego = palabra_mezclada('', objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'sopa_letras':
                juego = sopa_letras('', objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'escoge un número entre':
                juego = escoge_un_numero('', objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'Lógica Booleana':
                juego = logica_booleana(objeto['game']['message_requirement'], objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'Preguntas sobre python':
                juego = pregunta_python(objeto['game']['message_requirement'], objeto['game']['requirement'], objeto['game']['name'], objeto['game']['award'], objeto['game']['rules'], objeto['game']['questions'], False)
                objeto['game'] = juego
            elif objeto['game']['name'] == 'Juego Libre':
                juego = busca_minas(objeto['game']['message_requirement'], objeto['game']['requirement'], 'Buscaminas', 'Trofeo', objeto['game']['rules'], [], False)
                objeto['game'] = juego
                

        if index == 0:
            habitacion = Habitacion(room['name'], rooms[3]['name'], rooms[4]['name'], room['objects'], laboratorio())
        elif index == 1:
            habitacion = Habitacion(room['name'], rooms[2]['name'], rooms[3]['name'], room['objects'], biblioteca())
        elif index == 2:
            habitacion = Habitacion(room['name'], '', rooms[1]['name'], room['objects'], plaza())
        elif index == 3:
            habitacion = Habitacion(room['name'], rooms[1]['name'], rooms[0]['name'], room['objects'], pasillo())
        elif index == 4:
            habitacion = Habitacion(room['name'], rooms[0]['name'], '', room['objects'], servidores())

        mapa.append(habitacion)

    mapa_final = [mapa[2], mapa[1], mapa[3], mapa[0], mapa[4]]

    """ for maps in mapa:
        for objeto in maps.objetos_dentro:
            print(objeto) """
    return mapa_final