class Animal:
    def __init__(self):
        self.__age = 0
        self.nom = ''
        print('instanciation de la classe Animal')

    def get_age(self):
        return self.__age

        
    def veillir(self):
        self.__age = self.__age + 1
    
    def nommer(self, nom):
        self.nom = nom
        
        
    