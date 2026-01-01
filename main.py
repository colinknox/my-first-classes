#!/usr/bin/python3

# Project 1: Dragon Class
class Dragon:
    fire_breath = 100
    wing_span = 50
    scales = 500

smaug = Dragon()
drogon = Dragon()

print(smaug.fire_breath)
print(drogon.fire_breath)



# Project 2: Wizard Class
class Wizard:
    mana = 150
    spell_power = 75
    level = 1

harry = Wizard()
hermione = Wizard()
ron = Wizard()

print(harry.level)
print(hermione.level)
print(ron.level)
print(hermione.spell_power)



# Project 3: Book Class
class Book:
    pages = 271
    author_name = "William Gibson"
    year = 1984
    genre = "Sci-fi"

neuromancer = Book()
lord_of_the_rings = Book()

print(neuromancer.author_name)
print(lord_of_the_rings.genre)