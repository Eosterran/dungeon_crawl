#This is Dungeon Crawl, a text-based adventure game.
#The player will navigate through a dungeon, fighting monsters and collecting treasure.

#Import the random module
import random

#Define Classes

#Define the Player class
class Player:
    def __init__ (self, name, hp, attack, defense, gold, potions):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.potions = potions
        self.is_alive = True
        
    def __repr__ (self):
        return "Player Info \n Name: {}\n HP: {}/{}\n Attack: {}\n Defense: {}\n Gold: {}\n Potions: {}\n".format (self.name, self.hp, self.max_hp, self.attack, self.defense, self.gold, self.potions)
    
    def lose_hp(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            self.dead()
        print("{} takes {} damage. {}'s hp is now {}/{}".format(self.name, dmg, self.name, self.hp, self.max_hp))
    
    def knock_out(self):
        if self.is_alive == True:
            self.is_alive = False
        print("{} has met their early end. Good luck next time.".format(self.name))

#Define the Monster class            
class Monster:
    def __init__ (self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

#Define the Item class
class Item:
    def __init__ (self, name, purpose, modifier):
        self.name = name
        self.purpose = purpose
        self.modifier = modifier

#Define the Dungeon class. (Should the dungeon be a class? I'm not sure.)
class Dungeon:
    def __init__ (self, length = 5):
        self.length = length

#Introduction to Game and Player Creation
print("Greetings, and well met! Welcome to DUNGEON CRAWL. Your task? Survive.")

pc_name = input("First, however, we will need to know a bit more about you. What is your name?\n")

print("Excellent. Welcome to Eosterra, {}.".format(pc_name))

while True:
    pc_class = input("Now, what class will you choose? Choose '1' for Fighter or '2' for Sorcerer.\n")
    if pc_class == 1:
        pc_class = "Fighter"
        print("Very well. {} shall be a fighter. Their stats and inventory have been updated to reflect this.")
        break
    elif pc_class == 2:
        print("I'm sorry, but sorcerers haven't been invented yet. Please choose another class.")
        continue
    else:
        print("I'm sorry, I didn't catch that. Try again.")
        continue
    
print("PAUSE HERE.")

#STOPPED HERE at 12:05am on 2/28/25