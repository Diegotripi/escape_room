class Timer():
    def __init__(self, time, time_seg):
        self.time = time
        self.time_seg = time_seg
    
    def set_time(self, time): # Funcion para asignar el tiempo en formato min y seg 
        self.time = time

    def set_time_seg(self, time_seg): # Funcion para obtener el tiempo en formato min y seg 
        self.time_seg = time_seg
    
    def get_time(self): # Funcion para asignar el tiempo en seg 
        return self.time

    def get_time_seg(self): # Funcion para obtener el tiempo en seg 
        return self.time_seg