# python function work just like js. with one exception:

def add_numbers(num1, num2):
    print(num1 + num2)


add_numbers(4, 6)

# now the exception:
# In js we cannot change order of arguments, whatever the order of parameters, that should be order of arguments.
# But in python, we can change order by specifying like this:
add_numbers(num1=7, num2=3)
