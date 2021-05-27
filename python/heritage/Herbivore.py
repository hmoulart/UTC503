from heritage.Primate import Primate

class Herbivore(Primate):
    __quantite_herbe = 0.0
    
    def __init__(self, nom, age, nombre_dents, nombre_doigt, quantite_herbe):
        Primate.__init__(self, nom, age, nombre_dents, nombre_doigt)
        self.__quantite_herbe = quantite_herbe

    def get_quantite_herbe(self):
        return self.__quantite_herbe


    def set_quantite_herbe(self, value):
        self.__quantite_herbe = value