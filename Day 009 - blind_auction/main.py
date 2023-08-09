from replit import clear
from art import logo

print(logo)

bidders = {}
switch = True
while switch == True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bidders[name] = bid
  continue_auction = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if continue_auction == "no":
    switch = False
  elif continue_auction == "yes":
    clear()

#Check highest bidder
highest_bid = 0
winner = ""
for key in bidders:
  if bidders[key] > highest_bid:
    highest_bid = bidders[key]
    winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}")
