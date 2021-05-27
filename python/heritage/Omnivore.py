from heritage.Carnivore import Carnivore
from heritage.Herbivore import Herbivore

class Omnivore(Carnivore, Herbivore):
    def __init__(self, nom, age, nombre_dents, quantite_viande, nombre_doigt, quantite_herbe):
        Carnivore.__init__(self, nom, age, nombre_dents, quantite_viande)
        Herbivore.__init__(self, nom, age, nombre_dents, nombre_doigt, quantite_herbe)
    
    def manger(self):
        print('Je mange de tout !')