# This program simulates a simple game where each decision changes the outcome

print('''
*****************************************************
* ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^ *
*/|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\*
*/|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\*
*/|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\*
*****************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
turn = input("You are in the middle of the woods, at a crossroad. Do you go 'left' or 'right'? ").lower()
if turn == "right":
  print("You are attacked by an ogre.\nGame over.")
elif turn == "left":
  second_choice = input("You come across a small river, but it is getting dark. Do you 'swim' across or 'wait' till morning? ").lower()
  if second_choice == "swim":
    print("You get a cramp and drown.\nGame over.")
  elif second_choice == "wait":
    door_choice = input("You see a huge wall with three doors. Which do you pick('blue', 'yellow' or 'red')? ").lower()
    if door_choice == "blue":
      print("You are teleported into a glacier.\nGame over.")
    elif door_choice == "red":
      print("You are burned to a crisp by a dragon waiting on the other side.\nGame over.")
    elif door_choice == "yellow":
      print("You found the secret chamber where the treasure lies.\nYou win!")
      print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    else:
      print("You fell into a trap.\nGame over.")
  else:
    print("You fell into a hole.\nGame over.")
else:
  print("You got lost.\nGame over.")
