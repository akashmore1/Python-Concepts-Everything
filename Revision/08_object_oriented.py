class User:
    def __init__(self, user_name):
        self.user_name = user_name

    def introduce(self):
        print(self.user_name)


akash = User("Akash")
vishwesh = User("Vishwesh")

vishwesh.introduce()
