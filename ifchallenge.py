name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if (age > 18) and (age <= 30):
    print(f" Welcome to the holiday {name}!")
else:
    print(f"We are sorry, {name}. You are {age}. You can't enter the party")

