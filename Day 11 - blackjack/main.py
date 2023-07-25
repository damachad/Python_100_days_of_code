from art import logo
import random
from replit import clear

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(card_list):
  """Take a list and return the sum of its elements as a score"""
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0
  else:
    if 11 in card_list and sum(card_list) > 21:
      card_list.remove(11)
      card_list.append(1)
    return sum(card_list)

def compare(user_score, computer_score):
  """Compares two scores and prints the result"""
  if computer_score == user_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
    
def play_game():
  print(logo)
  game_over = False
  
  user_cards = [deal_card(), deal_card()]
  computer_cards = [deal_card(), deal_card()]
  
  while game_over == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
      if (input("Type 'y' to get another card, type 'n' to pass: ") == 'y'):
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while computer_score < 17 and computer_score > 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(user_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y'):
  clear()
  play_game()
