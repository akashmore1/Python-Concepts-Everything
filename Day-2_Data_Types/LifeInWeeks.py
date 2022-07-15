# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leftYears = 90 - int(age)

daysLeft = leftYears * 365
weeksLeft = round(leftYears * 52)
monthsLeft = round(leftYears * 12)

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")



