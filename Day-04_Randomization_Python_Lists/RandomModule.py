# always refer askpython.com when in doubt.
# First we need to import random module.
# Just like random, we can create our own modules and use them in projects

import random

# This will generate a random number from 100 to 200.
random_integer = random.randint(100, 200)
print(random_integer)

# Following function will generate floating numbers from 0 to 1.
# Range of random.random() id [0,1)
ramdom_float = random.random()
# If we want floating random numbers from 0 to 4, we can write:
random_flot_till_4 = random.random() * 4
