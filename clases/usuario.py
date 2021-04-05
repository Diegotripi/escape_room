class Usuario():
    def __init__(self, username, password, edad, avatar, records):
        self.username = username
        self.password = password
        self.edad = edad
        self.avatar = avatar
        self.records = records

    def __str__(self):
        print(f'''
            Usuario: {self.username}
            La edad del usuario es {self.edad}
            Avatar: {self.avatar}
        ''')

    def user_dict(self): # Funcion para retornar un diccionario con los datos del usuario
        return {
            'username': self.username, 
            'password': self.password, 
            'edad': self.edad, 
            'avatar': self.avatar, 
            'records': self.records
        }