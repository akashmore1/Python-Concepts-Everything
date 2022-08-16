# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

count_t = name1.count("t")
count_t += name2.count("t")
count_r = name1.count("r")
count_r += name2.count("r")
count_u = name1.count("u")
count_u += name2.count("u")
count_e = name1.count("e")
count_e += name2.count("e")

count_true = count_t + count_r + count_u + count_e

count_l = name1.count("l")
count_l += name2.count("l")
count_o = name1.count("o")
count_o += name2.count("o")
count_v = name1.count("v")
count_v += name2.count("v")
count_e = name1.count("e")
count_e += name2.count("e")

count_love = count_l + count_o + count_v + count_e

love_count = int(str(count_true) + str(count_love))

if love_count < 10 or love_count > 90:
    print(f"Your score is {love_count}, you go together like coke and mentos.")
elif love_count >= 40 and love_count <= 50:
    print(f"Your score is {love_count}, you are alright together.")
else:
    print(f"Your score is {love_count}.")
