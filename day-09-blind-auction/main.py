from art import logo

print(logo)

game_data = {}
another_user = True

while another_user:
    user = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_user = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    game_data[user] = bid
    print("\n" * 20)

    if add_user == "yes":
        another_user = True
    elif add_user == "no":
        another_user = False
    else:
        print("You wrote a wrong answer")

highest_bid = 0
winner = ""

for person in game_data:
    current_bid = game_data[person]
    if current_bid > highest_bid:
        highest_bid = current_bid
        winner = person

print(f"The winner is {winner} with a bid of ${highest_bid}")