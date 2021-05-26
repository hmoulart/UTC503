class Animal:
    def __init__(self):
        self.__age = 0
        self.nom = ''
        
    def veillir(self):
        self.__age = self.__age + 1
    
    def nommer(self, nom):
        self.nom = nom