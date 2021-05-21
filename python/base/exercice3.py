"""Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls. 
Comptez combien il y avait de données et combien étaient supérieures à 100.

Entrer un nombre inférieur ou égal à 0 indique la fin de la suite."""

somme = 0
nombreTotal = 0
nombreGrands = 0

x = int(input("x un nombre entier positif (0 pour terminer) ? "))

while x > 0:
    somme += x # somme = somme + x
    nombreTotal += 1
    if x > 100:
        nombreGrands += 1
    x = int(input("x un nombre entier positif (0 pour terminer) ? "))

print("Somme : ", somme)
print(nombreTotal, "valeur(s) en tout, dont ", nombreGrands, " supérieure(s) à 100")