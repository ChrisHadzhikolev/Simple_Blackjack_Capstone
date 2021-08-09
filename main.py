import random as rand
import art

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


def deal_card():
    return rand.choice(list(cards.keys()))


def calculate_score(score, card):
    if card == "A":
        if score + 11 > 21:
            score += 1
            return score
        else:
            score += 11
            return score
    else:
        score += cards[card]
        return score


def check_for_winner(user_score, dealer_score):
    if dealer_score > 21:
        print('You Win!')
    elif dealer_score == user_score:
        print('It\'s a draw')
    elif dealer_score > user_score:
        print('You Lose')


def game():
    print(art.logo)
    print('Welcome to the game of Kinda Blackjack')
    user_score = 0
    dealer_score = 0

    game_ended = False

    # First Phase both dealer and player deal two cards
    for i in range(2):
        dealt_card = deal_card()
        print(f'You dealt: {dealt_card}')
        user_score = calculate_score(user_score, dealt_card)
        dealt_card = deal_card()
        print(f'Dealer dealt: {dealt_card}')
        dealer_score = calculate_score(dealer_score, dealt_card)
    print(f'Your score is: {user_score}')

    # Second Phase player decides to hit or stand
    while not game_ended and input('Enter h for hit and s for stand: ').lower().strip() == 'h':
        dealt_card = deal_card()
        print(f'You dealt: {dealt_card}')
        user_score = calculate_score(user_score, dealt_card)
        print(f'Your score is: {user_score}')
        if user_score > 21:
            print('You Lose!')
            game_ended = True

    # Third phase if user did not lose dealer deals cards, until he wins, loses, or draws
    if not game_ended:
        while dealer_score <= user_score and dealer_score <= 18:
            dealt_card = deal_card()
            print(f'Dealer dealt: {dealt_card}')
            dealer_score = calculate_score(dealer_score, dealt_card)
            print(f'Dealer score is: {dealer_score}')
        check_for_winner(user_score, dealer_score)

    if input('Do you want to play one more(y for yes, anything else for no)? ').lower().strip() == 'y':
        game()


game()
