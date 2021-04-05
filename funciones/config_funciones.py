import json

def obtener_configuraciones(): # Funcion para leer el archivo de configuracion 
    with open('archivos/config.json') as f:
        data = json.load(f)
    return data['configs']