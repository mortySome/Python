import random
from os import system
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """
    Generates and returns a random card 
    """
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates the scores based on cards dealed to users and computer,
    returns 0 if score is 21 and 11 becomes 1 if score exceeds 21"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(u_score, c_score):
    """Compares the scores between players and returns the winner"""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack.😱"
    elif u_score == 0:
        return "Win, with a blackjack.😎"
    elif u_score > 21:
        return "You went over. You lose.😭"
    elif c_score > 21:
        return "Opponent went over. You win. 😁"
    elif u_score > c_score:
        return "You Win 😃"
    else:
        return "You lose 😤"
    
def play_blackjack():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            deal_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if deal_another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand is: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    system("clear")
    print(logo) 
    play_blackjack()
