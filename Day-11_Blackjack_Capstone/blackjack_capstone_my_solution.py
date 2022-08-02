import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_blackjack():
    want_to_play = True
    want_card = True
    user_sum = 0
    comp_sum = 0
    while want_to_play:
        user_cards = []
        comp_cards = []
        continue_play = input("Do you want to play blackjack? (y/n): ")
        if continue_play == "n":
            return
        elif continue_play == "y":
            for num in range(1, 3):
                user_cards.append(random.choice(cards))

            comp_cards.append(random.choice(cards))
            print(f'Your cards are: {user_cards}')
            print(f'Comp cards are: {comp_cards}')
            while want_card:
                want_new_card = input("Do you want a new card? (y/n)")
                if want_new_card == "y":
                    user_cards.append(random.choice(cards))
                    print(f'Your cards are: {user_cards}')
                    print(f'Comp cards are: {comp_cards}')
                    for card in user_cards:
                        user_sum += card
                    if user_sum > 21:
                        want_card = False
                        print('You lose!')

                elif want_new_card == "n":
                    want_card = False
                    user_sum = 0
                    for card in user_cards:
                        user_sum += card

                    while(comp_sum <= 17):
                        comp_cards.append(random.choice(cards))
                        for card in comp_cards:
                            comp_sum += card

                    print(f'Your cards are: {user_cards}')
                    print(f'Comp cards are: {comp_cards}')

                    print(user_sum, comp_sum)
                    if comp_sum > 21:
                        print("You win")
                    elif(user_sum > comp_sum):
                        print('You win!')
                    elif(user_sum < comp_sum):
                        print('You lose!')
                    else:
                        print('Its a draw')


play_blackjack()
