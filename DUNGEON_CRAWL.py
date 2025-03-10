#This is Dungeon Crawl, a text-based adventure game.
#The player will navigate through a dungeon, fighting monsters and collecting treasure.


#Imports modules
import random
import time
import sys


#Defines functions
def typed(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def roll_dice(num_sides, quantity):
    rolls = []
    total = 0
    for die in range(quantity):
        rolls.append(random.randint(1, int(num_sides - 1)))
    for roll in rolls:
        total += roll
    return total


#Define the Player class
class Player:
    def __init__ (self, name, hp = 20, defense = 10):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attack_modifier = 3
        self.hit_die = 8
        self.damage_dice = 2
        self.defense_value = defense
        self.defense_modifier = 0
        self.gold = 0
        self.potions = 1
        self.items = [basic_sword]
        self.is_alive = True
        
    def __repr__ (self):
        return "Player Info \n Name: {}\n HP: {}/{}\n Attack: {}\n Defense: {}\n Gold: {}\n Potions: {}\n".format (self.name, self.hp, self.max_hp, self.attack, self.defense, self.gold, self.potions)
    
    def attack(self, opponent):
        attack_roll = roll_dice(20, 1) + self.attack_modifier
        if attack_roll >= opponent.defense:
            typed("\nHit!")
            total_dmg = roll_dice(self.hit_die, self.damage_dice) + self.attack_modifier
            typed(f"You inflict {total_dmg} points of damage.\n")
            opponent.take_dmg(total_dmg)   
        else:
            typed("\nMiss!\n")
    
    def receive_loot(self, opponent):
        typed(f"You loot the body.\n")
        self.gold += opponent.gold
        self.potions += opponent.potions
        if self.potions > 2:
            self.potions = 2
            typed("You already have 2 potions. You can't carry any more.\n")
        for item in opponent.items:
            self.items.append(item)
        typed(f"You now have {self.gold} gold, {self.potions} potions, and your pack contains {self.items}\n") 
            
    def dodge(self):
        pass
   
    def equip_item(self):
        if not self.items:
            typed("\nYour pack is empty. You cannot equip any items.\n")
            return
        else:
            pass
        typed("\nYour inventory:\n")    
        for item in self.items:
            print(item.name)
        while True:
            typed("What would you like to equip?\n")
            equip = input()
            if equip.lower() in self.items:
                equip = equip.lower()
                if equip.is_equipped == True:
                    typed("This item is already equipped!\n")
                else:
                    pass
                if equip.purpose == "attack":
                    PC.attack_modifier += equip.modifier
                    equip.is_equipped = True
                    typed(f"{equip.name} has been equipped.")
                    break
                elif equip.purpose == "defend":
                    PC.defense_modifier += equip.modifier
                    equip.is_equipped = True
                    typed(f"{equip.name} has been equipped.")
                    break
                else:
                    typed("This item cannot be equipped.\n")
                    pass
                    break
            else:
                typed("Please enter a valid response.")
        while True:
            typed("\nWould you like to equip anything else?")
            choice = input()
            if choice.lower == "yes":
                PC.equip_item()
            elif choice.lower == "no":
                return
            else:
                typed("Please enter a valid response.\n")
        
    def drink_potion(self):
        while True:
            if self.potions == 0:
                typed("You reach into your pack...and find nothing but empty bottles.\n")
                return
            else:
                typed(f"You have {self.potions} potions. Drink one?\n")
                potion_action = input()
            if potion_action.lower() == "yes":
                healing = roll_dice(8,2)
                self.current_hp += healing
                self.potions -= 1
                if self.current_hp > self.max_hp:
                    self.current_hp = self.max_hp
                typed(f"You regain {healing} health. Your hp is now {self.current_hp}/{self.max_hp}.")
                break
            elif potion_action.lower() == "no":
                return
            else:
                typed("I'm sorry, I didn't catch that.")
    
    def take_dmg(self, dmg):
        self.current_hp -= dmg
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_alive = False
            self.knock_out()
        else:
            typed(f"You take {dmg} damage.\nYou have {self.current_hp}/{self.max_hp} remaining.")
    
    def knock_out(self):
        if self.is_alive == True:
            self.is_alive = False
        typed(f"The world fades from view as you breathe your final breath. {self.name}'s fate is sealed. Good luck in the next life.")

#Defines the "Item" class:
class Item:
    def __init__ (self, name, purpose, modifier):
        self.name = name
        self.purpose = purpose
        self.modifier = modifier
        self.equipped = False
    
    def __repr__(self):
        return self.name
    
#Define the "Monster" class:
class Monster:
    def __init__ (self, name, hp, attack_modifier, hit_die, dmg_dice, defense):
        self.name = name
        self.current_hp = hp
        self.max_hp = hp
        self.attack_modifier = attack_modifier
        self.hit_die = hit_die
        self.dmg_dice = dmg_dice
        self.defense = defense
        self.gold = 0
        self.potions = 0
        self.items = []
        self.is_alive = True
    
    def __repr__(self):
        return (f"This is a {self.name} with {self.hp}/{self.max_hp}. Its attack strength is {self.attack_modifier} and its base defense is {self.defense}.")

    def attack(self, opponent):
        attack_value = roll_dice(20, 1) + self.attack_modifier
        typed(f"The {self.name} swings...\n")
        if attack_value >= opponent.defense_value + opponent.defense_modifier:
            typed(f"The {self.name} lands a hit!\n")
            total_dmg = self.attack_modifier + (self.dmg_dice * self.hit_die)
            opponent.take_dmg(total_dmg)
        else: 
            typed(f"The {self.name} misses!")
    
    def take_dmg(self, dmg):
        self.current_hp -= dmg
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_alive = False
            self.knock_out()
        else:
            pass
    
    """def dodge():
        pass""" #TBD
    
    def knock_out(self):
        typed(f"The {self.name} is dead!\n")
        

#Monster Compendium: Use these to create "Monster" class objects.
goblin = Monster("goblin", 10, 0, 4, 1, 0)
skeleton = Monster("skeleton", 10, 0, 6, 1, 1)
zombie = Monster("zombie", 8, 1, 6, 2, 0)
orc = Monster("orc", 15, 2, 8, 1, 2)
giant_rat = Monster("giant rat", 12, 0, 6, 1, 0)
kobold = Monster("kobold", 8, 1, 2, 2, 3)
gelatinous_cube = Monster("gelatinous cube", 14, 0, 10, 1, 1)
giant_spider = Monster("giant spider", 13, 1, 6, 2, 2)
owlbear = Monster("owlbear", 15, 2, 8, 1, 1)
bugbear = Monster("bugbear", 17, 2, 8, 2, 2)
ghoul = Monster("ghoul", 11, 0, 4, 1, 4)
troll = Monster("troll", 13, 2, 8, 1, 5)
displacer_beast = Monster("displacer_beast", 16, 0, 6, 2, 6)
bulette = Monster("bulette", 10, 0, 8, 1, 6)
carrion_crawler = Monster("carrion crawler", 10, 2, 8, 1, 2)
basilisk = Monster("basilisk", 12, 1, 6, 1, 2)
harpy = Monster("harpy", 11, 2, 6, 1, 2)
gnoll = Monster("gnoll", 11, 2, 6, 1, 3)
stirge = Monster("stirge", 8, 0, 8, 1, 1)

monster_list = [goblin, skeleton, zombie, orc, giant_rat, kobold, gelatinous_cube, giant_spider, owlbear, bugbear, ghoul, troll, displacer_beast, bulette, carrion_crawler, basilisk, harpy, gnoll, stirge]
        
#Item Compendium: Use these to create "Item" class objects.
basic_sword = Item("basic sword", "attack", 2)
sword_1 = Item("+1 Sword", "attack", 3)
shield = Item("shield", "defend", 1)
shield_2 = Item("+1 shield", "defend", 2)
armor = Item("armor", "defend", 2)
""" magic_cloak = Item("magic cloak", "buff", 2)  """#later functionality?

items_list = [sword_1, shield, shield_2, armor]

#Introduction to Game and Player Creation
typed("INTRO TEXT")
"""typed("Greetings, and well met! Welcome to DUNGEON CRAWL. Your task? Survive.")
"""
typed("NAME REQ")
"""typed("First, however, we will need to know a bit more about you. What is your name?")"""
pc_name = input()

PC = Player(pc_name)

typed(f"Excellent. Welcome to Eosterra, {pc_name}.\n")
"""typed("It is time to begin your adventure. You start with a basic sword and the clothes on your back. But in the depths of this dungeon, much more awaits you...")
"""
input("Press 'Enter' to enter the dungeon.\n")

#Initiates Dungeon
room_count = 8
dungeon_monsters = monster_list
dungeon_items = items_list
"""boss_status = False"""

#Determines Boss Status - STILL IN DEV. **No boss_battle function written**
"""while True:
    if room_count == 0:
        boss_battle()
        pass
    elif room_count < 3:
        boss_check = roll_dice(2, 1)
        if boss_check == 1:
            boss_battle()
            pass
        else:
            pass
    else:
        break"""

#Creates & Populates a Room
while True:
    stealth = False
    current_monster = random.choice(monster_list)
    dungeon_monsters.remove(current_monster)
    current_monster.gold += random.randint(0, 5)
    potion_roll = roll_dice(10, 1)
    if potion_roll in range(7, 11):
        current_monster.potions += 1
    item_roll = roll_dice(10, 1)
    if item_roll in range(9, 11):
        item_loot = random.choice(dungeon_items)
        current_monster.items.append(item_loot)
        dungeon_items.remove(item_loot)
    
    if room_count == 8:
        typed("You enter the first room.\n")
    else:
        while True:
            typed("What would you like to do?\n1) Enter the next room.\n2) Equip items.\n3) Drink potions.\n")
            choice = input()
            if choice == "1":
                break
            elif choice == "2":
                PC.equip_item()
            elif choice == "3":
                PC.drink_potion()
            else:
                typed("Please choose a valid option.\n")
        typed("You enter the next room.\n")
    
    #Monster introduced
    typed(f"Before you stands a {current_monster.name}.\n")
    
    #Player Chooses to attack or try to stealth past the monster
    while True:
        if current_monster.is_alive == True:
            action = input("What would you like to do?\n 1: Attack \n 2: Sneak past\n")
            if action == "1":
                while True:
                    typed("You attack!")
                    PC.attack(current_monster)
                    input("Press any key to continue.")
                    if current_monster.is_alive == False:
                        current_monster.knock_out()
                        PC.receive_loot(current_monster)
                        room_count -= 1
                        break
                    else:
                        pass
                    current_monster.attack(PC)
                    input("\nPress any key to continue.\n")
                    typed("You prepare to attack again.\n")
                    if PC.is_alive == False:
                        PC.knock_out()
                        break
                    else:
                        pass
            elif action == "2":
                stealth_check = roll_dice(20, 1)
                perception_check = roll_dice(20, 1)
                if stealth_check >= perception_check: 
                    stealth = True
                    typed(f"\nYou escaped the {current_monster.name}.")
                    room_count -= 1
                    input("Hit any key to continue.\n")
                    break
                else: 
                    typed(f"You were spotted! The {current_monster.name} attacks!")
                    current_monster.attack(PC)       
            else:
                typed("I'm sorry, I didn't catch that.")
        else:
            break    

#GAME OVER
typed("\nGAME OVER.")

            
       
            
        
        
