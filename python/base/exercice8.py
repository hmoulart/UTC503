"""Hauteur parcourue par le gardien de phare"""

def hauteurParcourue(nb_marche, hauteur_marche):
    calcul_hauteur = nb_marche * hauteur_marche * 2 * 5 * 7 / 100.0
    print("Pour {:d} marches de {:d} cm, il parcourt {:.2f} m par semaine.".format(nb_marche, hauteur_marche, calcul_hauteur))
    
nbMarches = int(input("Combien de marches ? "))
hauteurMarche = int(input("Hauteur d'une marche (cm) ?"))

hauteurParcourue(nbMarches, hauteurMarche)