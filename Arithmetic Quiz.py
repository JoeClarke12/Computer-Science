import time
import random

question = 1
numberTwo = 1
numberTwo = 1
operator = 1
score = 0
name = ""

def add(x, y):

   return x + y

def subtract(x, y):

   return x - y

def multiply(x, y):

   return x * y

while name == "":
   time.sleep(1)
   name = input("Hello, \nWhat is your name? ")
   
print("Welcome to this maths quiz", name, "Good luck")
time.sleep(1)
print("Please only type numbers as answers or this will crash the quiz")

time.sleep(1)

while question <= 10:
    numberOne = random.randint(0, 12)
    numberTwo = random.randint(0, 12)
    operator = random.randint(1, 3)
    if operator == 1:
       print(numberOne,"+",numberTwo)
    elif operator == 2:
      print(numberOne,"-",numberTwo)
    elif operator == 3:
      print(numberOne,"*",numberTwo)

    if operator == 1:
       ans = add(numberOne,numberTwo)
    elif operator == 2:
      ans = subtract(numberOne,numberTwo)
    elif operator == 3:
      ans = multiply(numberOne,numberTwo)

    answer = int(input())
    
    if answer == ans:
        print("Correct")
        score = score + 1
    else:
        print("False, the answer was actually", ans)
        

    question = question + 1


if score < 5:
   print("Unfortunatly your score was", score)

else:
   print("Amazing, your score was", score)
