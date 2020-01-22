name = input("Please enter your name: ")
age = int(input("How old are you, {}".format(name)))
print(f"{name} ,you are  {age} years old")
print(type(age))

if age >= 18:
    print("You are old enough to vote")
else:
    print("You are a baby. No voting yet.")
    print("Please come back in {0} years".format(18 - age))


print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, YOU GUESSED IT")
    else:
        print("You suck big time")
else:
    print("You got it  the first time!!!! You RULEE!")



























