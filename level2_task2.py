#Number Guesser

import random
a=int(input("Enter the start range:"))
b=int(input("Enter the end range:"))

n=random.randint(a,b)
a=int(input("Enter the guessed number:"))

if a>n:
    print("The number guessed is too high")
elif a<n:
    print("The number guessed is too low")
else:
    print("You have guessed the correct number")
