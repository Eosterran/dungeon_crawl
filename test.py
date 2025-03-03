import time
import sys

def typed(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

typed("Hello, Shawn. My name is Jerry.")


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