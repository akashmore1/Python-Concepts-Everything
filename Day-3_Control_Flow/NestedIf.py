height = int(input("What is your height? "))
age = int(input("What is your age? "))

if height > 120:
    if age >= 18:
        print("You can ride with 12$ bill")
    else:
        print("You can ride with 7$ bill")
else:
    print("You cannot ride!")
