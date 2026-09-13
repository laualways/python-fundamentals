import random
from art import logo, vs
from game_data import data
print(logo)

game_on = True

def forma_data(account, label):
    return f"{label}: {account['name']}, a {account['description']}, from {account['country']}."

random_one = random.choice(data)
random_two = random.choice(data)
points = 0
while game_on:
    print(forma_data(random_one, "Compare A"))
    print(vs)
    print(forma_data(random_two, "Against B"))
    question = input("Who has more followers? Type 'A' or 'B':   ").lower()
    print("\n" * 20)
    print(logo)     
    
    if question == "a":
        if random_one['follower_count'] > random_two['follower_count']:
            random_one = random_two
            new_random = random.choice(data)
            random_two = new_random
            points += 1
            print(f"Your score is: {points}.")
        else:
            print("You lose!")
            game_on = False
    elif question == "b":
        if random_one['follower_count'] < random_two['follower_count']:
            random_one = random_two
            new_random = random.choice(data)
            random_two = new_random
            points += 1
            print(f"Your score is: {points}.")
        else:
            print("You lose!")