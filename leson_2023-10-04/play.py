# from random import randint

# random_number = randint(1, 10)

# guess_number = input()
you = int(input("You: "))
date = int(input("Date: "))

if you in range(3, 10) and date in range(3,10):
    print("Ok")
else:
    print("No")