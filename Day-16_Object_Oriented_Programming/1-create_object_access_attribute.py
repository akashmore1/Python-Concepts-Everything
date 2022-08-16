# import some_module
# print(some_module.another_variable)

# Creating new objects using already existing class Turtle and Screen
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('blue')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
