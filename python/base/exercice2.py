"""Une boucle while : entrez un prix HT (entrez 0 pour terminer) et affichez sa valeur TTC."""

prixHT = float(input("Prix HT (0 pour terminer) ?"))
while prixHT > 0:
    print("Prix TTC : ", prixHT*1.2)
    prixHT = float(input("Prix HT (0 pour terminer) ?"))

print("Au revoir !")