class User:
    def __init__(self, uid, name):
        self.user_id = uid
        self.user_name = name
        self.follower = 0


user_1 = User('123', 'Akash')
user_2 = User('121', 'Angela')
# This will create object using a constructor function
# If we don't pass any value while creating object, it will give error.
# In above example we are setting follower count = 0 by default because by default initial follower count is going to be 0.
# In python, we can provide a default value to object attribite in Class.
# To increase follower we will learn about object methods.
