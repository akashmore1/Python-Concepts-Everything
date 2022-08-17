class User:
    pass


user_1 = User()
user_1.id = 1234
user_1.name = 'Akash'

# Now if there are a lot of attribute to object and we need to create multiple objects, above method is lengthy

print(user_1)

# Is there a way to make this simpler?
# For this we need to understand what is a constructor.
# A constructor is a part of blue-print(Class), which specify what should happen when our object is being constructed.
# In programming this is also known as initializing an object.
# In python, we create constructor using a special function "def __init__(self):"
# This function is normally used to initialize the attributes.


class Car:
    def __init__(self, seats):
        self.seats = seats


my_car = Car(4)
# This is exactly same as if:
my_car.seats = 4
