from heritage.Mammifere import Mammifere

class Primate(Mammifere):
    __nombre_doigt = 0
    
    def __init__(self, nom, age, nombre_dents, nombre_doigt):
        Mammifere.__init__(self, nom, age, nombre_dents)
        self.__nombre_doigt = nombre_doigt

    def get_nombre_doigt(self):
        return self.__nombre_doigt


    def set_nombre_doigt(self, value):
        self.__nombre_doigt = value