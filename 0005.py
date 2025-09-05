class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Dog(Animal):
    def __init__(self, name, age, breed, sound):
        super().__init__(name, age, "Dog")
        self.breed = breed
        self.sound = sound

class Cat(Animal):
    def __init__(self, name, age , color,sound):
        super().__init__(name, age, "Cat")
        self.color = color
        self.sound = sound
dog_1 = Dog("Shalaby", 3, "Golden", "Woof")
print(dog_1.name, dog_1.age, dog_1.species, dog_1.breed , dog_1.sound)

cat_1 = Cat("Tom", 2 , "black and white" , "Meow")
print(cat_1.name, cat_1.age, cat_1.species, cat_1.color, cat_1.sound)

