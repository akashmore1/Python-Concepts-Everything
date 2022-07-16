print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

final_bill = 0

if size == "S" or size == "s":
    final_bill += 15
    if add_pepperoni == "Y" or add_pepperoni == "y":
        final_bill += 2
elif size == "M" or size == "m":
    final_bill += 20
    if add_pepperoni == "Y" or add_pepperoni == "y":
        final_bill += 3
elif size == "L" or size == "l":
    final_bill += 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        final_bill += 3

if extra_cheese == "Y" or extra_cheese == "y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")
