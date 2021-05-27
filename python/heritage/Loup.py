from heritage.Carnivore import Carnivore

class Loup(Carnivore):
    def __init__(self, nom, age, nombre_dents, quantite_viande):
        Carnivore.__init__(self, nom, age, nombre_dents, quantite_viande)
    
    def hurler(self):
        print('Le loup hurle')