class Helicoptero:
    def __init__(self, __modelo, __color, __combustible_inicial):
        self.__modelo = __modelo
        self.__color = __color
        self.__combustible_inicial = __combustible_inicial
        self.estado = False 

    @property
    def modelo(self):
        return self.__modelo

    @property
    def color(self):
        return self.__color 

    @property 
    def combustible_inicial(self):
        return self.__combustible_inicial 
    
    def __str__(self):
        return f'Su modelo de helicoptero {self.__modelo} su color es {self.__color} y su combistible marca {self.__combustible_inicial}'

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    def encender_helicoptero(self):
        if self.estado == True: 
            raise ValueError ("El helicoptero esta encendido")
        self.estado = True
    
    def apagar_helicoptero (self) :
        if self.estado == False :
            raise ValueError ("El helicoptero esta apagado")
        self.estado = False
        





    



        
        
        




