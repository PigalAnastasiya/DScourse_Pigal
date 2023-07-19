from models import Cat, Dog, Veterenar


cat_first = Cat("Jase", 5, "Mayy", "fish", 12, "WHITE")
cat_second = Cat("Sam", 6, "Mayy", "meat", 9, "Black")


dog_first = Dog("Reks", 2, "Gav", "meat", 13, "Gray")
dog_second = Dog("Shape", 8, "Gav", "dog food", 25, "Ginger")

animal_list = [cat_first, cat_second, dog_first, dog_second]


for animal in animal_list:
    animal.display_info()

print()
for animal in animal_list:
    animal.move()
    print()

children_cat = cat_first.children_animal(cat_second)
children_cat.display_info()
print()

children_dog = dog_first.children_animal(dog_second)
children_dog.display_info()
print()


vet_1 = Veterenar("Golovin Aleksandr")
vet_1.set_target(cat_first)
