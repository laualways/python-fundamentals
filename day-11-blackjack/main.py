import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


game_started = True

while game_started:
    start_option = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_option == 'y':
        print("\n" * 20)
        print(logo)

        player_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 2)

        is_game_over = False

        while not is_game_over:
            player_score = calculate_score(player_cards)
            computer_score = calculate_score(computer_cards)
            player_sum = player_score

            print(f"Your cards: {player_cards}, current score: {player_sum}")
            print(f"Computer's first card: {computer_cards[0]}")

            if player_score == 0 or computer_score == 0 or player_score > 21:
                is_game_over = True
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if another_card == 'y':
                    player_cards.append(random.choice(cards))
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17 and player_score <= 21:
            computer_cards.append(random.choice(cards))
            computer_score = calculate_score(computer_cards)

        print(f"\nYour final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(player_score, computer_score))
        print("\n")
    else:
        game_started = False