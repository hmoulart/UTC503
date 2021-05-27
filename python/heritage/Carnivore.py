from heritage.Mammifere import Mammifere

class Carnivore(Mammifere):
    __quantite_viande = 0.0
    
    def __init__(self, nom, age, nombre_dents, quantite_viande):
        Mammifere.__init__(self, nom, age, nombre_dents)
        self.__quantite_viande = quantite_viande

    def get_quantite_viande(self):
        return self.__quantite_viande


    def set_quantite_viande(self, value):
        self.__quantite_viande = value