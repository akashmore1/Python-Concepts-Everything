# from replit import clear
# HINT: You can call clear() to clear the output in the console.


def run_secret_auction():
    bidders_present = True
    bidders_info = {}
    max_amount = 0
    max_amount_bidder = ""

    while bidders_present:
        get_bidders_present = input("Are there any bidders? (yes/no)\n")
        # clear()
        if get_bidders_present.lower() == 'yes':
            bidder_name = input('What is your name?\n')
            bidding_amount = float(input('What is your amount?\n'))
            bidders_info[bidder_name] = bidding_amount
        else:
            bidders_present = False

    for key in bidders_info:
        if bidders_info[key] > max_amount:
            max_amount = bidders_info[key]
            max_amount_bidder = key
    if max_amount == 0:
        print("There is no bidding amount")
    else:
        print(
            f"The maximum amount is given by {max_amount_bidder} with value of ${max_amount}"
        )


run_secret_auction()
