# Python dictionaries are just like js objects.
# They have key value pair.

student = {
    "name": "Akash",
    "age": 23,
}

# To access name:
print(student["name"])

# To add new key value pair:
student["subject"] = "Programming"

# To modify current key
student["age"] = 24

# to wipe out all content of dictionary, reassign
student = {}

# looping a dictionary  => Just like for in loop of js
for key in student:
    print(key)
    print(student[key])
