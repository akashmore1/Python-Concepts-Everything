import random
from game_data import data


def higher_lower():
    game_on = True
    score = 0
    first_number = random.randint(0, len(data) - 1)
    second_number = first_number
    while second_number == first_number:
        second_number = random.randint(0, len(data) - 1)

    while game_on:
        print(
            f'option A is {data[first_number]["name"]}, {data[first_number]["description"]} from {data[first_number]["country"]}'
        )
        print(
            f'option B is {data[second_number]["name"]}, {data[second_number]["description"]} from {data[second_number]["country"]}'
        )
        user_input = input("Which option is more famous?(A/B) \n").lower()

        if user_input == 'a':
            if data[first_number]["follower_count"] < data[second_number][
                    "follower_count"]:
                print(
                    f'\nIncorrect {data[first_number]["name"]} has {data[first_number]["follower_count"]} followers while {data[second_number]["name"]} has {data[second_number]["follower_count"]}'
                )
                print(f"Your score is {score}")
                game_on = False
                return False

        if user_input == 'b':
            if data[first_number]["follower_count"] > data[second_number][
                    "follower_count"]:
                print(
                    f'\nIncorrect {data[first_number]["name"]} has {data[first_number]["follower_count"]} followers while {data[second_number]["name"]} has {data[second_number]["follower_count"]}'
                )
                print(f"Your score is {score}")
                game_on = False
                return False

        score += 1
        first_number = second_number
        second_number = first_number
        while second_number == first_number:
            second_number = random.randint(0, len(data) - 1)


higher_lower()
