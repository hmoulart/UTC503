from objet.Animal import Animal

animal1 = Animal()
animal2 = Animal()

print(type(animal1))
print(type(animal2))

print(animal1.__age)
print(animal2.__age)

animal2.veillir()

print(animal1.__age)
print(animal2.__age)

print(animal1.nom)
animal1.nommer('Milou')
print(animal1.nom)
