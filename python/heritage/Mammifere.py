class Mammifere:
    __nom = ''
    __age = 0
    __nombre_dents = 0
    
    def __init__(self, nom, age, nombre_dents):
        self.__nom = nom
        self.__age = age
        self.__nombre_dents = nombre_dents

    def get_nom(self):
        return self.__nom


    def get_age(self):
        return self.__age


    def get_nombre_dents(self):
        return self.__nombre_dents


    def set_nom(self, value):
        self.__nom = value


    def set_age(self, value):
        self.__age = value


    def set_nombre_dents(self, value):
        self.__nombre_dents = value