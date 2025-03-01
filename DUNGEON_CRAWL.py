#This is Dungeon Crawl, a text-based adventure game.
#The player will navigate through a dungeon, fighting monsters and collecting treasure.

#Import the random module
import random

#Needed Functions
def roll_dice(num_sides, quantity):
    rolls = []
    total = 0
    for die in range(quantity):
        rolls.append(random.randint(1, int(num_sides - 1)))
    for roll in rolls:
        total += roll
    print(f"You rolled {quantity} d{num_sides}. Results: {rolls} Total:{total}")

"""
Create Room: random Room Description + Random Monster
  Random Room Description: randomize descriptions, remove from set
  Random Monster: randomize monsters, choose 1, remove from set, populate loot
    ***create dungeon_boss after 5 rooms
  Set number of turns = 0
PC Choice: Sneak or Engage
  If Sneak: Run Stealth
    Stealth: Roll 1d20, Add "Stealth" modifiers, compare against Monster perception (1 d20)
      If pass, bypass room
      If fail, engage monster, go 2nd
  If Engage: Run Engage
    Engage: Go 1st, Choice-attack or dodge, Monster attack or dodge
      Attack - run attack, take damage, check monster.is_alive
        If monster.is_alive = true, next turn
        If monster.is_alive = false, run monster.lootdrop
      Dodge - add +2 to pc.defense
      Monster Choice - random 70/30 attack/dodge (same effects but for monster)
        Attack - run attack, take damage, check pc.is_alive
        If pc.is_alive = True, next turn
        If pc.is_alive = False, run pc.game_over
        
"""      
    
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
basic_sword = Item("basic sword", "attack", 2)
sword_1 = Item("+1 Sword", "attack", 3)
shield = Item("shield", "defend", 1)
shield_2 = Item("+1 shield", "defend", 2)
armor = Item("armor", "defend", 2)
""" magic_cloak = Item("magic cloak", "buff", 2)  """#later functionality?

#Introduction to Game and Player Creation
print("Greetings, and well met! Welcome to DUNGEON CRAWL. Your task? Survive.")

pc_name = input("First, however, we will need to know a bit more about you. What is your name?\n")

PC = Player(pc_name, 20, 5, 10, 0, 2)

print(f"Excellent. Welcome to Eosterra, {pc_name}. It is time to begin your adventure. You start with a basic sword and the clothes on your back. But in the depths of this dungeon, much more awaits you...")



        

