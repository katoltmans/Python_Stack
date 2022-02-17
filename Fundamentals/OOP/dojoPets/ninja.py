import random

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self, ):
        self.pet.play(self)
        print(f"Taking {self.pet.name} for a walk. Nytrix performs {random.choice(self.pet.tricks)}")
        if self.pet.energy < 20 or self.pet.health < 20:
            print("Oh no!! You need more pet food!")
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"Feeding {self.pet.name} {random.choice(self.treats)}!")
        self.pet.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()


