from art import logo, vs
from replit import clear
import random
from game_data import data


# retreive info function
def format_info(account):
  """
  Receive account data and return in a printable format."""
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  info = f"{account_name}, a {account_description}, from {account_country}"
  return info

# Check if guess is correct
def check_answer(user_guess, a_followers, b_followers):
  """Use if statement if user is correct"""
  if a_followers > b_followers:
    return user_guess == "a"
  else:
    return user_guess == "b"


def hi_or_low():
  # Display art
  print(logo)
  
  # variables
  score = 0 # keeps count of score
  game_should_continue = True # keeps track of game status
  account_b = random.choice(data)
  
  # make the game repeatable - Some while loop
  while game_should_continue:
    # get 2 random accounts in game_data list
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
      account_b = random.choice(data)
    
    # Get follower count of each account
    followers_a =  account_a["follower_count"]
    followers_b = account_b["follower_count"]
    # Give user feedback on their guess
    
    # Make account on position B become the next account on position A
    
    # list comparison A
    print(f"Compare A: {format_info(account_a)}")
    # Display Vs.
    print(vs)
    # list comparison B
    print(f"Against B: {format_info(account_b)}")
    
    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B'").lower()
  
    clear()
    print(logo)
    
    # if guess is correct, add 1 to score
    if check_answer(guess, followers_a, followers_b):
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      game_should_continue = False
      print(f"You're wrong! Final score: {score}")

hi_or_low()
# make game repeatable
while input("Do you want to play again? Type 'y' or 'n'.").lower() == "y":
  clear()
  hi_or_low()