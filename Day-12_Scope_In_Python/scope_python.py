# In python there is only functional scope.
# There is no block scope unlike JS.

# e.g.
if 3 > 2:
    name = 'Akash'

print(name)

# Above is a valid syntax.

# whereas


def dummy_call():
    f_name = 'Akash'


dummy_call()
# print(f_name)  # =>This is not a valid syntax

# Modifying vs reading global scope variables.

number = 4


def read_number():
    number = 6
    print(f"Number inside function is {number}")  # prints 6


read_number()

print(f"Number outside function is {number}")  # prints 4

# The above thing is happening because, number inside function is considered as a new variable.
# python highly recommend not to modify global variables inside a function. Thas's why this is happening.
# so If we write number += number inside function after removing line 28, it will give us an error.

# So if we have to modify a global variable inside function we use global keyword
# e.g.
global_var = 24


def change_global_var():
    global global_var
    global_var += 4


change_global_var()
# ^ In this way we can use global keyword to modify global variables inside function =>(Never do this though)

# Instead what we can do is return value in function and again assign it to global variable
# e.g.

var_global = 44


def correct_modify_global_var():
    return var_global + 4


var_global = correct_modify_global_var()
# In this way we should modify global variable


# While declaring global variables, use variable name in all capital
URL = 'www.google.com'
