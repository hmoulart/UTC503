from objet.Animal import Animal

class Reptile(Animal):
    def __init__(self):
        super().__init__()
        self.nombre_ecailles = 1000
        print('instanciation de la classe Reptile')

    
    def nommer(self, nom):
        '''surcharge de la méthode nommer'''
        print("on nomme depuis la classe Reptile")
        self.nom = nom
    
reptile = Reptile();

print('Classe de reptile')
print(type(reptile))
print('Age de reptile')
print(reptile.get_age())

print('On renomme reptile')
reptile.nommer('kaa')
print(reptile.nom)
