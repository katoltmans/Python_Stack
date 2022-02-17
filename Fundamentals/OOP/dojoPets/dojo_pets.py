import random
import ninja
import pets


Nytrix = pets.Pet("Nytrix", "Bengal Cat", ["hunt", "stalk", "super zoom"])
NinjaKat = ninja.Ninja("Kat", "Oltmans", ["meat stick", "turkey", "fish"], "cat food", Nytrix)

NinjaKat.walk().feed().feed().bathe()
