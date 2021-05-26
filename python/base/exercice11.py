"""Proportion d'une séquence dans une chaîne ADN"""

# Definition des fonctions
def valide(seq):
    """Retoune vrai si la séquence est valide, faux sinon"""
    resultat = any(seq)
    for c in seq:
        resultat = resultat and c in "atgc"
    return resultat

def proportion(a, s):
    """Retourne la proportion de la séquence s dans la chaîne a """
    return 100*a.count(s)/len(a)

def saisie(ch):
    s = input("{:s}".format(ch))
    while not valide(s):
        print("'{:s}' ne peut contenir que les chaînons suivant a, t, g, c et ne doit pas être vide".format(s))
        s = input("{:s}".format(ch))
    return s

# Programme principale
adn = saisie("chaîne")
seq = saisie("séquence")

print("Il y a {:.2f} % de {:s} dans votre chaîne.".format(proportion(adn, seq), seq))