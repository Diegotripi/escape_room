import json
import colored
from colored import stylize
from clases.usuario import Usuario

def obtener_usuarios(): # Funcion para obtener los usuarios del json
    with open('archivos/usuarios.json') as f:
        data = json.load(f)
    return data['users']

def guardar_usuario(user_dict): # Guardar nuevo usuario al json
    usuarios = { "users": obtener_usuarios() }
    with open('archivos/usuarios.json', 'w') as f:
        usuarios['users'].append(user_dict)
        json.dump(usuarios, f)
        print(stylize('Usuario creado exitosamente.\n', colored.fg("green")))

def crear_usuario(): # Funcion para crear un nuevo usuario
    username = crear_username()
    password = input('Ingrese la contraseña: \n')
    edad = crear_edad()
    avatar = seleccionar_avatar()
    usuario = Usuario(username, password, edad, avatar, [])
    user_dict = usuario.user_dict()
    guardar_usuario(user_dict)

def crear_username(): # Funcion para ingresar el username y verificar que no exista
    usuarios = obtener_usuarios()
    username = input('Ingrese el username: \n')
    for usuario in usuarios:
        if usuario['username'] == username:
            print(stylize('Username ya existe, intente nuevamente.\n', colored.fg("red")))
            return crear_username()
        else:
            pass
    return username

def crear_edad(): # Funcion para ingresar la edad y verificar que sea valida
    edad = input('Ingrese la edad: \n')
    if not edad.isnumeric():
        print(stylize('Ingrese una edad valida.\n', colored.fg("red")))
        return crear_edad()
    return edad

def seleccionar_avatar(): # Funcion para seleccionar el avatar
    opcion = input('''Seleccione un avatar:
    1. Gandhi
    2. Scharifker
    3. Eugenio Mendoza
    4. Pelusa\n''')

    while (not opcion.isnumeric() or (int(opcion) not in range(1,5))):
            opcion = input('\nIngrese una opcion valida: \n')

    if opcion == '1':
        return "Gandhi"
    elif opcion == '2':
        return "Scharifker"
    elif opcion == '3':
        return "Eugenio Mendoza"
    elif opcion == '4':
        return "Pelusa"

def login(): # Funcion para ingresar al juego con su cuenta
    usuarios = obtener_usuarios()
    user = input('Ingrese su usuario: ')
    password = input('Ingrese la clave: ')
    for usuario in usuarios:
        if usuario['username'] == user:
            if usuario['password'] == password:
                return usuario
    print(stylize("Usted debe crearse una cuenta o verificar sus datos.\n", colored.fg("yellow")))            
    return False