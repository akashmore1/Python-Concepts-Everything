print('Welcome to tip calculator')

total_bill = float(input("What is the total bill?\n"))
tip_percentage = int(input("What percentage tip you would like to give?\n"))
no_of_people = int(input("How many people to split the bill?\n"))

bill_and_tip = total_bill + total_bill * tip_percentage / 100
individual_bill = round(bill_and_tip / no_of_people, 2)

print(f"Each person should pay {individual_bill}")
