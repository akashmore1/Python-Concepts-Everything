is_there_bidder = True

bidder_dictionary = {}

while is_there_bidder:
    is_there_bidder = input("Is there a bidder? (y/n)\n")
    if is_there_bidder == 'y':
        name_bidder = input("Name of bidder:\n")
        amount_bidder = int(input("Name of bidder:\n"))
        bidder_dictionary[name_bidder] = amount_bidder
    else:
        is_there_bidder = False

winner_amount = 0
winner = ''

for key in bidder_dictionary:
    if bidder_dictionary[key] > winner_amount:
        winner_amount = bidder_dictionary[key]
        winner = key

print(winner, winner_amount)
