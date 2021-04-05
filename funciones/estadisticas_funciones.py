import json
from art import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import colored
from colored import stylize
from clases.usuario import Usuario

def obtener_records(): # Funcion para obtener todos los records hasta el momento
    with open('archivos/records.json') as f:
        data = json.load(f)
    return data['records']

def guardar_record(record_dict): # Funcion para guardar un nuevo record
    records = { "records": obtener_records() }
    with open('archivos/records.json', 'w') as f:
        records['records'].append(record_dict)
        json.dump(records, f)
        print(stylize('Rercord guardado exitosamente.\n', colored.fg("green")))

def sort_key(d):
    return d['c']

def imprimir_lista(dificultad, lista): # Funcion para Imprimir la Grafica con los Top Leaders
    tprint("\n" + dificultad)
    for index, i in enumerate(lista):
        print(f'{index+1}. Usuario: ' + i['username'] + ' -- Tiempo: ' +  str(int(i['tiempo']/60)) + ' minutos')

    # Lista de Usuarios
    people = (lista[0]['username'], lista[1]['username'], lista[2]['username'], lista[3]['username'], lista[4]['username'])
    y_pos = np.arange(len(people))
    # Lista con los tiempos de los usuarios
    performance = [lista[0]['tiempo']/60, lista[1]['tiempo']/60, lista[2]['tiempo']/60, lista[3]['tiempo']/60, lista[4]['tiempo']/60]
    error = np.random.rand(len(people))

    fig, ax = plt.subplots()

    hbars = ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()
    ax.set_xlabel('Tiempos') # Leyenda
    ax.set_title(f'Top 5 en dificultad {dificultad}') # Titulo de la Grafica

    
    ax.bar_label(hbars, fmt='%.2f')
    ax.set_xlim(right=lista[4]['tiempo']/60 + 3)

    plt.show() # Imprimir Grafica

def top_leaders(): # Funcion para Imprimir los Top de Jugadores por Dificultad
    facil = []
    intermedio = []
    dificil = []
    records = obtener_records()
    new_record = sorted(records, key=lambda record: record['tiempo'], reverse=False)
    for i in new_record:
        if i['dificultad'] == "Facil":
            if len(facil) < 5:
                facil.append(i)
        elif i['dificultad'] == "Intermedio":
            if len(intermedio) < 5:
                intermedio.append(i)
        elif i['dificultad'] == "Dificil":
            if len(dificil) < 5:
                dificil.append(i)
    tprint('**Top 5**')
    imprimir_lista('Facil', facil)
    imprimir_lista('Intermedio', intermedio)
    imprimir_lista('Dificil', dificil)


def top_cuartos_visitados(records=None): # Funcion Top de Cuartos visitados por usuarios
    usuarios = []
    usuarios = obtener_usuario_habitacion(usuarios)
    tprint('Habitaciones + Visitadas')
    for user in usuarios:
        cont = 0
        print(user['username'].upper())
        user['hab'] = user['habitaciones'].copy()
        while cont < 5:
            habitaciones = user['habitaciones']
            max_key = max(habitaciones, key=habitaciones.get)
            print(str(cont + 1) + '. ' + max_key.title() + ' ' + str(user['habitaciones'][max_key]))
            del user['habitaciones'][max_key]
            cont += 1
        # Labels de la grafica
        labels = 'Rectorado', 'Biblioteca', 'Pasillo', 'Laboratorio', 'Servidores' 
        # Catidad de visitas a habitaciones
        sizes = [user['hab']['rectorado'], user['hab']['biblioteca'], user['hab']['pasillo'], user['hab']['laboratorio'], user['hab']['servidores']]
        explode = (0, 0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal') 
        ax1.set_title('Porcentaje de Habitaciones Visitadas por ' + user['username']) # Titulo de la grafica

        plt.show() # Imprimir grafica



def obtener_usuario_habitacion(usuarios, records=None): # Funcion para obtener las habitaciones mas visitadas por usuario
    records = obtener_records() if records == None else records
    for i in range(0, len(records) - 1):
        for j in range(i + 1, len(records)):
            if records[i]['username'] == records[j]['username']:
                records[i]['habitaciones']['rectorado'] += records[j]['habitaciones']['rectorado']
                records[i]['habitaciones']['biblioteca'] += records[j]['habitaciones']['biblioteca']
                records[i]['habitaciones']['pasillo'] += records[j]['habitaciones']['pasillo']
                records[i]['habitaciones']['laboratorio'] += records[j]['habitaciones']['laboratorio']
                records[i]['habitaciones']['servidores'] += records[j]['habitaciones']['servidores']
                records.pop(j)
                return obtener_usuario_habitacion(usuarios, records)
    return records


def top_cantidad_de_juegos(records=None): # Funcion para devolver la cantidad de partidas por jugador
    usuarios = []
    
    usuarios = obtener_usuario_juegos(usuarios)
    tprint('Top 5 Jugadores con + juegos')
    usuarios = sorted(usuarios, key=lambda user: user['juegos'], reverse=True)
    for i in range(0,5):
        print(str(i + 1) + '. Usuario: ' + usuarios[i]['username'].title() + ' ha jugado ' + str(usuarios[i]['juegos']) + ' veces.')

    # Variable con los usuarios
    people = (usuarios[0]['username'].title(), usuarios[1]['username'].title(), usuarios[2]['username'].title(), usuarios[3]['username'].title(), usuarios[4]['username'].title())
    y_pos = np.arange(len(people))
    # Variable con la cantidad de juegos
    performance = [usuarios[0]['juegos'], usuarios[1]['juegos'], usuarios[2]['juegos'], usuarios[3]['juegos'], usuarios[4]['juegos']]
    error = np.random.rand(len(people))

    fig, ax = plt.subplots()

    hbars = ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()
    ax.set_xlabel('Tiempos') # Leyenda
    ax.set_title(f'Top 5 Jugadores con + Juegos') # Titulo de la Grafica

    
    ax.bar_label(hbars, fmt='%.2f')
    ax.set_xlim(right=usuarios[0]['juegos'] + 2)

    plt.show() # Imprimir la estadistica


def obtener_usuario_juegos(usuarios, records=None): # Funcion para obtener los juegos por usuario
    records = obtener_records() if records == None else records
    for i in range(0, len(records) - 1):
        for j in range(i + 1, len(records)):
            if records[i]['username'] == records[j]['username']:
                if "juegos" in records[i]:
                    records[i]['juegos'] += 1
                else:
                    records[i]['juegos'] = 0
                records.pop(j)
                return obtener_usuario_juegos(usuarios, records)
    return records
                



    
