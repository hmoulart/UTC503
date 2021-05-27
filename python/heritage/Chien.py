from heritage.Carnivore import Carnivore

class Chien(Carnivore):
    def __init__(self, nom, age, nombre_dents, quantite_viande):
        Carnivore.__init__(self, nom, age, nombre_dents, quantite_viande)
    
    def aboyer(self):
        print('Le chien aboie')