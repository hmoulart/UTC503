from math import pi

rayon = float(input("Rayon du cône (cm) : "))
hauteur = float(input("Hauteur du cône (cm) : "))

volume = (pi*rayon*rayon*hauteur)/3.0
print("Volume du cône :", round(volume, 2), "cm3")