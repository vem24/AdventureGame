import time
import random

creatures = ['troll', 'wicked fairie', 'gorgon', 'pirate', 'dragon']

enemy = random.choice(creatures)

#weapon = ['sword', '']
# Include a combat simulation in which the player and enemy deal random amounts of damage to one another

def print_pause(message):
  print(message)
  time.sleep(1)

def choice(weapon):
  decision = input("(Please enter 1 or 2)\n")
  if decision == '1':
    house(weapon)
  elif decision == '2':
    cave(weapon)
  else:
    choice(weapon)

def choices(weapon):
  print_pause("Enter 1 to knock on the door of the house.")
  print_pause("Enter 2 to peer into the cave.")
  print_pause("What would you like to do?")
  choice(weapon)


def replay(weapon):
  play_again = input("Would you like to play again? (y/n)")

  if play_again == 'n':
    print_pause("Thanks for playing! See you next time.")
  elif play_again == 'y':
    print_pause("Excellent! Restarting the game ...")
    intro(weapon)
  else:
    replay(weapon)

def intro(weapon):
  print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
  print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
  print_pause("In front of you is a house.")
  print_pause("To your right is a dark cave.")
  print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")

  choices(weapon)

def fight(weapon):
  if weapon == "dagger":
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the {enemy}.")
    print_pause("You have been defeated!")
    replay(weapon)
  elif weapon == "sword":
    print_pause(f"As the {enemy} moves to attack, you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
    print_pause(f"But the {enemy} takes one look at your shiny new toy and runs away!")
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")
    replay(weapon)

def field(weapon):
  print_pause("You run back into the field. Luckily, you don't seem to have been followed.\n")

  choices(weapon)

def house(weapon):
  print_pause("You approach the door of the house.")
  print_pause(f"You are about to knock when the door opens and out steps a {enemy}.")
  print_pause(f"Eep! This is the {enemy}'s house!")
  print_pause(f"The {enemy} attacks you!")

  if weapon == "dagger":
    print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")

  survive = input("Would you like to (1) fight or (2) run away?")
  if survive == '1':
    fight(weapon)
  elif survive == '2':
    field(weapon)
  else:
    replay(weapon)

def cave(weapon):

  print_pause("You peer cautiously into the cave.")
  if weapon == "sword":
    print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.\n")
  else:
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the sword with you.")
  print_pause("You walk back out to the field.\n")

  weapon = "sword"

  choices(weapon)

def play_game():
  weapon = "dagger"
  intro(weapon)

play_game()
