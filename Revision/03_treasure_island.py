direction = input(
    'We are at cross roads. Where do you want to go left or right?\n'
)

if direction == 'right':
    print("Game over")
elif direction == 'left':
    action = input("Do you want to swim or wait?\n")
    if action == "swim":
        print("Game over")
    elif action == "wait":
        door = input("Choose the door\n")
        if door == "Red":
            print("Game over")
        elif door == "Blue":
            print("Game over")
        elif door == "Yellow":
            print("You won the game")
