class Ordinateur:
    __marque = ''
    __frequence_processeur = 0
    __quantite_memoire = 0
    __taille_disque = 0
    __nombre_usb = 0
        
    # On ne peux avoir qu'un seul constructeur en Python, nous utilisons donc les valeurs par défaut des paramètres
    def __init__(self, m='', processeur=0, memoire=0, disque=0, usb=0):
        self.__marque = m
        self.__frequence_processeur = processeur
        self.__quantite_memoire = memoire
        self.__taille_disque = disque
        self.__nombre_usb = usb

    def get_marque(self):
        return self.__marque


    def get_frequence_processeur(self):
        return self.__frequence_processeur


    def get_quantite_memoire(self):
        return self.__quantite_memoire


    def get_taille_disque(self):
        return self.__taille_disque


    def get_nombre_usb(self):
        return self.__nombre_usb


    def set_marque(self, value):
        self.__marque = value


    def set_frequence_processeur(self, value):
        self.__frequence_processeur = value


    def set_quantite_memoire(self, value):
        self.__quantite_memoire = value


    def set_taille_disque(self, value):
        self.__taille_disque = value


    def set_nombre_usb(self, value):
        self.__nombre_usb = value


    def del_marque(self):
        del self.__marque


    def del_frequence_processeur(self):
        del self.__frequence_processeur


    def del_quantite_memoire(self):
        del self.__quantite_memoire


    def del_taille_disque(self):
        del self.__taille_disque


    def del_nombre_usb(self):
        del self.__nombre_usb