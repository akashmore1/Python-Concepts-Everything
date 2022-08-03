# 1
from random import randint
number = int(input("Which number do you want to check?"))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# 2
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()


# 3

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num], dice_num)
