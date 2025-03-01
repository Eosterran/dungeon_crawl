#This is Dungeon Crawl, a text-based adventure game.
#The player will navigate through a dungeon, fighting monsters and collecting treasure.

#Import the random module
import random

#Random Needed Functions??
def roll_dice(num_sides, quantity):
    rolls = []
    total = 0
    for die in range(quantity):
        rolls.append(random.randint(1, int(num_sides - 1)))
    for roll in rolls:
        total += roll
    print(f"You rolled {quantity} d{num_sides}. Results: {rolls};{total}")
        
    
#Define Classes
#Define the Player class
class Player:
    def __init__ (self, name, hp, attack, defense, gold, potions):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.attack_value = attack
        self.defense_value = defense
        self.gold = gold
        self.potions = potions
        self.is_alive = True
        
    def __repr__ (self):
        return "Player Info \n Name: {}\n HP: {}/{}\n Attack: {}\n Defense: {}\n Gold: {}\n Potions: {}\n".format (self.name, self.hp, self.max_hp, self.attack, self.defense, self.gold, self.potions)
    
    def attack(self, opponent):
        dmg = self.attack
        opponent.lose_hp(dmg)
        if opponent.hp == 0:
            opponent.drop_loot #add this method to the monster class
    
    def lose_hp(self, dmg):
        dmg = dmg - self.defense_value
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            self.knock_out()
        print("{} takes {} damage. {}'s hp is now {}/{}".format(self.name, dmg, self.name, self.hp, self.max_hp))
    
    def knock_out(self):
        if self.is_alive == True:
            self.is_alive = False
        print(f"{self.name} has met their early end. Good luck next time.")

#Define the Monster class
class Monster:
    def __init__ (self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.gold = 0
        self.loot = []
    
    def __repr__(self):
        return (f"This is a {self.name} with {self.hp}/{self.max_hp}. Its attack strength is {self.attack} and its base defense is {self.defense}.")

#Define the Item class
class Item:
    def __init__ (self, name, purpose, modifier):
        self.name = name
        self.purpose = purpose
        self.modifier = modifier
        
#Item Compendium
sword = Item("sword", "attack", 2)
shield = Item("shield", "defend", 1)
armor = Item("armor", "defend", 2)
magic_cloak = Item("magic cloak", "buff", 2) #later functionality?

#Introduction to Game and Player Creation
print("Greetings, and well met! Welcome to DUNGEON CRAWL. Your task? Survive.")

pc_name = input("First, however, we will need to know a bit more about you. What is your name?\n")

print(f"Excellent. Welcome to Eosterra, {pc_name}.")

while True:
    pc_class = input("Now, what class will you choose? Choose '1' for Fighter or '2' for Sorcerer.\n")
    if pc_class == "1":
        pc_class = "Fighter"
        print(f"Very well. {pc_name} shall be a fighter. Their stats and inventory have been updated to reflect this.")
        break
    elif pc_class == "2":
        print("I'm sorry, but sorcerers haven't been invented yet. Please choose another class.")
    else:
        print("I'm sorry, I didn't catch that. Try again.")
        

