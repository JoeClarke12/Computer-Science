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

#To see if user has entered a name into the input
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

#start of the while loop so it will ask 10 random questions
while question <= 10:
   #generating first random number
    number1 = random.randint(0, 12)
    #generating second random number
    number2 = random.randint(0, 12)
    #generating random number for selecting random operator
    operator = random.randint(1, 3)
    #when the operator number is one runs the indented code
    if operator == 1:
       #prints the correct question depending on the operator selected
       print(number1,"+",number2)
       #when the operator number is two runs the indented code
    elif operator == 2:
       #prints the correct question depending on the operator selecte
      print(number1,"-",number2)
      #when the operator number is three runs the indented code
    elif operator == 3:
       #prints the correct question depending on the operator selecte
      print(number1,"*",number2)


      #when the operator number is one runs the indented code
    if operator == 1:
       #works out the correct answer for adding
       ans = add(number1,number2)
       #when the operator number is one runs the indented code
    elif operator == 2:
       #works out the correct answer for subtracting
      ans = subtract(number1,number2)
      #when the operator number is one runs the indented code
    elif operator == 3:
       #works out the correct answer for multiply
      ans = multiply(number1,number2)

   #taking the users input for there answer
    answer = int(input())

    #check if the users answer matches the answer worked out by the program
    if answer == ans:
       #printing correct if the answer they put matched the answer worked out by the computer
        print("Correct")
        #adding 1 to there total score if they got the answer correct
        score = score + 1
    else:
       #telling the user there answer was false and telling them the correct answer
        print("False, the answer was actually", ans)

      #adding 1 to the questions asked so that the program only asks the right amount of questions
    question = question + 1


if score < 5:
   #printing a message of unfortunate with there score if there score is less than 5
   print("Unfortunatly your score was", score)

else:
   #printing a message of congradulations with there score if there score isn't less than 5
   print("Amazing, your score was", score)
