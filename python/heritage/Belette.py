from heritage.Carnivore import Carnivore

class Belette(Carnivore):
    def __init__(self, nom, age, nombre_dents, quantite_viande):
        Carnivore.__init__(self, nom, age, nombre_dents, quantite_viande)