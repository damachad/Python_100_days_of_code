import art
import game_data
import random
from replit import clear

# Check if A has more followers than B
def has_more_followers(person_a, person_b):
  if person_a['follower_count'] > person_b['follower_count']:
    return 1
  else:
    return 0

def game(personality_a):
  personality_b = random.choice(game_data.data)
  if personality_b == personality_a:
    personality_b = random.choice(game_data.data)
  print(f"Compare A: {personality_a['name']}, a {personality_a['description']}, from {personality_a['country']}.")
  print(art.vs)
  print(f"Against B: {personality_b['name']}, a {personality_b['description']}, from {personality_b['country']}.")

# Attribute user choice to either 'A' or 'B'
  guess = input("Who has more followers? Type 'A or 'B': ").lower()
  if guess == 'a':
    user_guess = personality_a
    other_option = personality_b
  elif guess == 'b':
    user_guess = personality_b
    other_option = personality_a

# Evaluate if user wins or looses
  if has_more_followers(user_guess, other_option) == 1:
    global game_score
    game_score += 1
    clear()
    print(art.logo)
    print(f"You are right! Current score: {game_score}")
    personality_a = personality_b
    game(personality_a)
  else:
      clear()
      print(art.logo)
      print(f"Sorry, that's wrong. Final score: {game_score}")

# Launch game
print(art.logo)
game_score = 0
personality_a = random.choice(game_data.data)
game(personality_a)
