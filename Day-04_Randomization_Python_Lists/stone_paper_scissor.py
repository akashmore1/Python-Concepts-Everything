import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

rps_arr = [rock, paper, scissors]

user_input = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
computer_input = random.randint(0, 2)


user_choice = rps_arr[user_input]
comp_choice = rps_arr[computer_input]

print(f'Your choice:\n{user_choice}')
print(f'Comp choice:\n{comp_choice}')

if user_input == computer_input:
    print("It's a tie!")

if user_input == 0 and computer_input == 1:
    print('You Lose')
elif user_input == 0 and computer_input == 2:
    print('You Win')
elif user_input == 1 and computer_input == 0:
    print('You Win')
elif user_input == 1 and computer_input == 2:
    print('You Lose')
elif user_input == 2 and computer_input == 0:
    print('You Lose')
elif user_input == 2 and computer_input == 1:
    print('You Win')
