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
        pass
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"Feeding {self.pet.name} {random.choice(self.treats)}!")
        self.pet.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        pass

class Pet:
    def __init__(self, name , species , tricks, health = 0, energy = 0):
        self.name = name
        self.species = species
        self.tricks = tricks
        self.health = health
        self.energy = energy

    # sleep() - increases the pets energy by 25
    def sleep(self):
        pass
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
# play() - increases the pet's health by 5
    def play(self, tricks):
        pass
        # if self.energy < 20 or self.health < 20:
        #     print("Oh no!! You need more pet food!")
        # else:
        #     print(f"{name} is well fed!")
# noise() - prints out the pet's sound
    def noise(self):
        pass

Nytrix = Pet("Nytrix", "Bengale Cat", "hunt")
NinjaKat = Ninja("Kat", "Oltmans", ["meat stick", "turkey", "fish"], "cat food", Nytrix)

NinjaKat.feed()
