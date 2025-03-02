import random

def roll_dice(num_sides, quantity):
    rolls = []
    total = 0
    for die in range(quantity):
        rolls.append(random.randint(1, int(num_sides - 1)))
    for roll in rolls:
        total += roll
    return rolls, total
    
print(roll_dice (20, 2))

#This is for choosing a class, which isn't functional yet
""" while True:
    pc_class = input("Now, what class will you choose? Choose '1' for Fighter or '2' for Sorcerer.\n")
    if pc_class == "1":
        pc_class = "Fighter"
        print(f"Very well. {pc_name} shall be a fighter. Their stats and inventory have been updated to reflect this.")
        break
    elif pc_class == "2":
        print("I'm sorry, but sorcerers haven't been invented yet. Please choose another class.")
    else:
        print("I'm sorry, I didn't catch that. Try again.") """