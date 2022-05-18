import time

def print_pause(message):
  print(message)
  time.sleep(2)

# Intro
print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
print_pause("...")

choice = int(input("""Enter 1 to knock on the door of the house.
Enter 2 to peer into the cave.
What would you like to do?
(Please enter 1 or 2)\n"""))

while True:

  if choice == 1:
    print_pause("You approach the door and knock.")
    print_pause("While you wait for someone to come to the door, you hear a loud noise coming from the cave.")
    print_pause("You turn your head quickly in the direction of the cave.")
    print_pause("Then...")
    print_pause("your heart sinks to your stomach of fear when you see a troll with sharp teeth sprinting towards you!")
    print_pause("You look around and see that you kept that stake knife from the dinner you visited earlier.")
    survive = int(input("""Enter 1 to confront the troll with the stake knife.
    Enter 2 to run for your life.
    What would you like to do?
    (Please enter 1 or 2)\n"""))
  if choice == 2:
    print_pause("You walk towards the cave and stop right before you enter.")
    print_pause("Slowly, you pick up your feet and continue your way in quiently.")
    print_pause("17 steps in you see something that caught your eye.")
    print_pause("You stop, stretch out your hand and grab a hold of a long shiny sword")
    print_pause("With the very little light coming into the cave you manage to read the engraved name.")
    print_pause("'Who is Godric Gryffindor?' You wonder.")
    print_pause("You hear something coming from deeper inside the cave.")
    survive2 = int(input("""Enter 1 to continue down the cave.
    Enter 2 to exit the cave.
    What would you like to do?
    (Please enter 1 or 2)\n"""))
  else:
    choice = int(input("(Please enter 1 or 2)\n"))
