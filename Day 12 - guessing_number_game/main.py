def compare(input_numer, right_number):
  """Compares two numbers and returns the result"""
  if input_number == right_number:
    return f"You got it! The answer was {right_number}."
  elif input_number > right_number:
    return "Too high."
  else:
    return "Too low."

from art import logo
from random import randint
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

right_number = randint(1, 100)
# print(f"Pssst, the correct answer is {right_number}")
game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if game_mode == 'easy':
  tries = 10
elif game_mode == 'hard':
  tries = 5
  
input_number = 0
while tries > 0 and input_number != right_number:
  input_number = int(input("Make a guess: "))
  print(compare(input_number, right_number))
  tries -= 1
  if tries == 0:
    print("You've run out of guesses, you lose.")
  elif input_number != right_number:
    print("Guess again.")
    print(f"You have {tries} attempts remaining to guess the number.")
