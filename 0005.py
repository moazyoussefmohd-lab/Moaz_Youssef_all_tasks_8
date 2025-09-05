class Animal:
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species

class Dog(Animal):
    def breed(self,breed):
        self.breed = breed

class Cat(Animal):
    def color(self,color):
        self.color = color
                
dog_1=Dog("Shalaby", 3, "Dog")
dog_1.breed("Golden")
print(dog_1.name, dog_1.age, dog_1.species, dog_1.breed)


cat_1=Cat("Tom", 2, "Cat")
cat_1.color("balck and white")
print(cat_1.name, cat_1.age, cat_1.species, cat_1.color)

