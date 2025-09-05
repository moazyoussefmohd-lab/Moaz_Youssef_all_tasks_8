class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Dog(Animal):
    def __init__(self, name, age, species, breed):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, age, species, color):
        self.name = name
        self.age = age
        self.species = species
        self.color = color

dog_1 = Dog("Shalaby", 3, "Dog", "Golden")
print(dog_1.name, dog_1.age, dog_1.species, dog_1.breed)

cat_1 = Cat("Tom", 2, "Cat", "black and white")
print(cat_1.name, cat_1.age, cat_1.species, cat_1.color)


