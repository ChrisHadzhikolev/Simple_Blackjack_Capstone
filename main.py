import art
import random as rand

print(art.logo)
print('Welcome to the game of kinda Blackjack')
cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


def deal_card():
    return rand.choice(list(cards.keys()))


# def deal_and_check(score):
#     dealt_card = deal_card()
#     print(f'Your card is: {dealt_card}')
#     if score + cards[dealt_card] > 21:
#         return 0
#     elif score + cards[dealt_card] == 21:
#         return 1
#     else:
#         return 2


user_cards = []
dealer_cards = []
user_cards.append(deal_card())
print(f'Your first card is: {user_cards[0]}')
dealer_cards.append(deal_card())
print(f'Dealer first card is: {dealer_cards[0]}')
user_cards.append(deal_card())
print(f'Your second card is: {user_cards[1]}')
dealer_cards.append(deal_card())
print(f'Dealer second card is: {dealer_cards[1]}')
user_score = cards[user_cards[0]] + cards[user_cards[1]]
dealer_score = cards[dealer_cards[0]] + cards[dealer_cards[1]]
print(f'Your score: {user_score}')
print(f'Dealer score: {dealer_score}')
should_continue = True
game_ended = False

while should_continue and not game_ended:
    if input('Enter h for Hit or s for Stand: ').lower().strip() == 'h':
        dealt_card = deal_card()
        user_cards.append(dealt_card)
        print(f'Your card is: {dealt_card}')
        if dealt_card == "A":
            if user_score > 11:
                user_score += 1
            else:
                user_score += 11
        else:
            user_score += cards[dealt_card]
        print(f'Your score is: {user_score}')
        if user_score > 21:
            game_ended = True
            print('You Lose!')
    else:
        should_continue = False

if not game_ended:
    while not game_ended:
        dealt_card = deal_card()
        dealer_cards.append(dealt_card)
        print(f'Dealer card is: {dealt_card}')
        if dealt_card == "A":
            if dealer_score > 11:
                dealer_score += 1
            else:
                dealer_score += 11
        else:
            dealer_score += cards[dealt_card]
        print(f'Dealer score is: {dealer_score}')
        if dealer_score > 21:
            print('You Win!')
            game_ended = True
        elif dealer_score == 21 == user_score:
            print('It\'s a draw!')
            game_ended = True
        elif dealer_score > user_score:
            print('You Lose!')
            game_ended = True
