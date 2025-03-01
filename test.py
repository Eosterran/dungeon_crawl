import random

def roll_dice(num_sides, quantity):
    rolls = []
    total = 0
    for die in range(quantity):
        rolls.append(random.randint(1, int(num_sides - 1)))
    for roll in rolls:
        total += roll
    print(f"You rolled {quantity} d{num_sides}. Results: {rolls} Total:{total}")
    
roll_dice (20, 2)