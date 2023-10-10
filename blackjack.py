from art import logo
import random

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
number_cards = len(cards)
index_cards = number_cards-1
player_cards_collection = []
computer_cards_collection = []

def player_cards():
    for _ in range(10):
        player_cards_collection.append(cards[random.randint(0,index_cards)])
    return player_cards_collection

computer_final_cards = []

def computer_cards():
    for _ in range(10):
        computer_cards_collection.append(cards[random.randint(0,index_cards)])
    return computer_cards_collection

def computer_score_calculator():
    j=0
    computer_score = 0
    while computer_score <17:
        computer_final_cards.append(computer_cards_collection[j])
        computer_score += computer_cards_collection[j]
        j+=1
    return computer_score


player_final_cards = []
def black_jack():
    player_cards()
    computer_cards()
    computer_score = computer_score_calculator()
    i=0
    for _ in range(2):
        player_final_cards.append(player_cards_collection[i])
        i+=1
    player_score = 0
    for _ in player_final_cards:
        player_score += _

    print(f"\n Your cards: {player_final_cards} Your score: {player_score} \n Computer's first card is {computer_final_cards[0]}")
    
    pick_another_card = input("\n Tyep 'y' to get another card, type 'n' to pass: ").lower()
    while pick_another_card == 'y':
        player_final_cards.append(player_cards_collection[i])
        player_score += player_cards_collection[i]
        i+=1
        if player_score >21:
            print("you lose")
            break
        print(f"\nYour cards: {player_final_cards} and score: {player_score} \n \n Computer's first card: {computer_final_cards[0]}")
        pick_another_card = input("\n Type 'y' to get another card, type 'n' to pass: ")

    print(f"\n Your cards: {player_final_cards} Your score: {player_score} \n Computer score = {computer_score} and Cards = {computer_final_cards}" )

    if computer_score > 21:
        print("\n You Win! Computer Bust")
    elif player_score >21:
        print("\n You Lose! You bust")
    else:
        if player_score > computer_score:
            print(f"\n You win with a score of {player_score} beating computer's socre of {computer_score}")
        elif computer_score > player_score:
            print("\n You Lose!")
        else:
            print('\n Draw')

    

continue_true = True
while continue_true:
    x = input('y to play, n to stop ').lower()
    if x == 'y':
        print(logo)
        player_cards_collection = []
        computer_cards_collection = []
        player_final_cards = []
        computer_final_cards = []
        player_score = 0
        computer_score = 0
        black_jack()
    else:
        continue_true = False
        break

