class Pet:
    def __init__(self, name , species , tricks, health = 0, energy = 0):
        self.name = name
        self.species = species
        self.tricks = tricks
        self.health = health
        self.energy = energy

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
# play() - increases the pet's health by 5
    def play(self, tricks):
        self.health += 5
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print("Meeeeeeeoooooooooow")
