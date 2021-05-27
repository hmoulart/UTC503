class Livre:
    __titre = ''
    __auteur = ''
    __prix = 0.0
    __annee = 0
    
    def __init__(self, titre = '', auteur = '', prix = 0.0, annee = 0):
        self.__titre = titre
        self.__auteur = auteur
        self.__prix = prix
        self.__annee = annee
        
    def correspond(self, titre):
        return self.__titre.__eq__(titre)
    
    def get_titre(self):
        return self.__titre
        
mon_premier_livre = Livre()
mon_deuxieme_livre = Livre('Des fleurs pour Algernon', 'Daniel Keyes')
mon_troisieme_livre = Livre('Le Tour du monde en 80 jours', 'Jules Verne', 8.99, 1872)
print(mon_deuxieme_livre.correspond(mon_troisieme_livre.get_titre())) # False
print(mon_deuxieme_livre.correspond('Des fleurs pour Algernon')) # True
