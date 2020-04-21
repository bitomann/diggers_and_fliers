from animals import Ant, Betta_Fish, Copperhead, Earthworm, Finch, Gerbil, Mouse, Parakeet, Timber_Rattlesnake, Terrapin
from environments import Subterranean, Sky, Water, Surface

andy = Ant("Andy")
bryan = Betta_Fish("Bryan")
catherine = Copperhead("Catherine")
edy = Earthworm("Edy")
phineas = Finch("Phineas")
gilbert = Gerbil("Gilbert")
mickey = Mouse("Mickey")
paul = Parakeet("Paul")
timmy = Timber_Rattlesnake("Timmy")
terror = Terrapin("Terror")

terrarium = Subterranean("terrarium")
cage = Surface("cage")
fish_bowl = Water("fish_bowl")
aviary = Sky("aviary")

terrarium.Animal.addAnimal(timmy)
terrarium.addAnimal(mickey)
terrarium.addAnimal(edy)
terrarium.addAnimal(catherine)

cage.addAnimal(andy)
cage.addAnimal(gilbert)

fish_bowl.addAnimal(bryan)
fish_bowl.addAnimal(terror)

aviary.addAnimal(paul)
aviary.addAnimal(phineas)

print("Animals in a terrarium")
print("")
for animal in terrarium.animals:
    print(animal)

print("")

print("Animals in a cage")
print("")
for animal in cage.animals:
    print(animal)

print("")

print("Animals in a fish bowl")
print("")
for animal in fish_bowl.animals:
    print(animal)

print("")

print("Animals in an Aviary")
print("")
for animal in aviary.animals:
    print(animal)