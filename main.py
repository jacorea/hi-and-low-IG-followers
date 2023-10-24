from art import logo, vs
import random
from game_data import data


# retreive info function
def format_info(account):
  """
  Format account data into printable format."""
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  info = f"{account_name}, a {account_description}, from {account_country}"
  return info

# Check if guess is correct
def check_answer(user_guess, a_followers, b_followers):
  """Use if statement if user is correct"""
  if user_guess == "a" and a_followers > b_followers:
    return True
  elif user_guess == "b" and b_followers > a_followers:
    return True
  else:
    return False


# Display art
print(logo)

# get 2 randint contained in game_data list
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)




# Get follower count of each account
followers_a =  account_a["follower_count"]
followers_b = account_b["follower_count"]
print({followers_a, followers_b})
# Use if statement to see if guess is correct
# Give user feedback on their guess


# keep score
score = 0 
# make the game repeatable - Some while loop
# Make account on position B become the next account on position A

# list comparison A
print(f"Compare A: {format_info(account_a)}")
# Display Vs.
print(vs)
# list comparison B
print(f"Against B: {format_info(account_b)}")

#Ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B'").lower()
