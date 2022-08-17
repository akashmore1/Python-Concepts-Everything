# We can have define new mthod in class along side __init__(self).
# Every method in class must have a "self" parameter

class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.follower += 1


user_1 = User('001', 'Akash')
user_2 = User('002', 'Angela')

user_2.follow(user_1)

print(user_1.follower)
print(user_2.follower)
print(user_1.following)
print(user_2.following)
