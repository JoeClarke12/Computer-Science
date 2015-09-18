import time
import random

question = 1
number1 = 1
number2 = 1

NAME = input("Hello, \nWhat is your name? ")
print("Welcome to this maths quiz", NAME, "Good luck")

time.sleep(1)

while question <= 10:
    number1 = random.randint(0, 101)
    number2 = random.randint(0, 101)
    print(number1, "+", number2)
    answer = int(input())
    if answer == number1 + number2:
        print("correct")
    else:
        print("false")

    question = question + 1
