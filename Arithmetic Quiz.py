#Name: Joseph Clarke
#Candidate No: 6040
#Outwood Academy Newbold - 23148
#A453 Programming Task

#importing the required code for the time.sleep(1) function which pauses the code for the time given
import time
#importing the required code to create random intgers
import random

#Variable to count the number of questions asked
question = 1
#Variable to hold the first number in the question
number1 = 1
#Variable to hold the second number in the question
number2 = 1
#Variable to count and hold the users score.
score = 0
#Variable to hold the users name
NAME = ""

#Used to calculate the correct answer for addition questions
def add(x, y):

   return x + y

#Used to calculate the correct answer for subtraction questions
def subtract(x, y):

   return x - y

#Used to calculate the correct answer for multiply questions
def multiply(x, y):

   return x * y

#To see if user has entered name a name
while NAME == "":
   #adds a 1 second delay to the program at this stage
   time.sleep(1)
   #Asks for the users name, if the user doesn't enter a name it will start the loop again
   NAME = input("Hello, \nWhat is your name? ")

#prints a welcome message with ther users name, if the user has entered a name
print("Welcome to this maths quiz", NAME, "Good luck")
#adds a 1 second delay to the program at this stage
time.sleep(1)
#printing a message so that the user know to put only numbers in the answer box
print("Please only type numbers as answers or this will crash the quiz")

#adds a 1 second delay to the program at this stage
time.sleep(1)

while question <= 10:
    number1 = random.randint(0, 12)
    number2 = random.randint(0, 12)
    operator = random.randint(1, 3)
    if operator == 1:
       print(number1,"+",number2)
    elif operator == 2:
      print(number1,"-",number2)
    elif operator == 3:
      print(number1,"*",number2)

    if operator == 1:
       ans = add(number1,number2)
    elif operator == 2:
      ans = subtract(number1,number2)
    elif operator == 3:
      ans = multiply(number1,number2)

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
