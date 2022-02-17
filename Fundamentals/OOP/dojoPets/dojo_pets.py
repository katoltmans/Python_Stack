import random
import ninja
from pets import * # import * will import all classes from the file - call individual class names if any classes need to be excluded


Nytrix = Pet("Nytrix", "Bengal Cat", ["hunt", "stalk", "super zoom"])
NinjaKat = ninja.Ninja("Kat", "Oltmans", ["meat stick", "turkey", "fish"], "cat food", Nytrix)

NinjaKat.walk().feed().feed().bathe()

print()
Jesha = Bengal("Jesha", ["flopping fish", "toy mouse", "feather"])

Jesha.get_toy()
