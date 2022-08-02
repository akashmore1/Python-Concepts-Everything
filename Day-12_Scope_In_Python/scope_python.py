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
print(f_name)  # =>This is not a valid syntax
