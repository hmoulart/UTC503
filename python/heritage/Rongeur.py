from heritage.Mammifere import Mammifere

class Rongeur(Mammifere):
    __couleur_pelage = ''
    
    def __init__(self, nom, age, nombre_dents, couleur_pelage):
        Mammifere.__init__(self, nom, age, nombre_dents)
        self.__couleur_pelage = couleur_pelage

    def get_couleur_pelage(self):
        return self.__couleur_pelage


    def set_couleur_pelage(self, value):
        self.__couleur_pelage = value