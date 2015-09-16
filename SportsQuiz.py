#Quiz
#Joe Clarke - 14th september 2015
import time
Score = 0
Q1 = "Null"
Q2 = "Null"
Q3 = "Null"
Q4 = "Null"
Q5 = "Null"
Q6 = "Null"
Q7 = "Null"
Q8 = "Null"
Q9 = "Null"
Q10 = "Null"

NAME = input("What is your name? ")


print("Welcome to this quiz", NAME, "Good luck!")
time.sleep(2)
print("Question 1")
Q1 = input("Who won the world cup in 1966? ")
if Q1 == "england":
    print("Correct!")
    Score = Score + 1
elif Q1 == "England":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually England")

time.sleep(2)
print("Question 2")
Q2 = input("Which is the national sport of Canada? ")
if Q2 == "ice hockey":
    print("Correct!")
    Score = Score + 1
elif Q2 == "Ice Hockey":
    print("Correct!")
    Score = Score + 1
elif Q2 == "lacrosse":
    print("Correct!")
    Score = Score + 1
elif Q2 == "Lacrosse":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Ice Hockey")
    
time.sleep(2)
print("Question 3")
Q3 = input("Who has won cricket world cup for the maxium number of times? ")
if Q3 == "australia":
    print("Correct!")
    Score = Score + 1
elif Q3 == "Australia":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Australia")

time.sleep(2)
print("Question 4")
Q4 = input("Who has won the world cup the most times? ")
if Q4 == "brazil":
    print("Correct!")
    Score = Score + 1
elif Q4 == "Brazil":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Brazil")
    
time.sleep(2)
print("Question 5")
Q5 = input("Which country has hosted Commonwealth Games for the maximum number of times? ")
if Q5 == "canada":
    print("Correct!")
    Score = Score + 1
elif Q5 == "Canada":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Canada")

time.sleep(2)
print("Question 6")
Q6 = input("Where was the first olympic games held? ")
if Q6 == "canada":
    print("Correct!")
    Score = Score + 1
elif Q6 == "Canada":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Canada")
    
time.sleep(2)
print("Question 7")
Q7 = input("Which country started the Football World? ")
if Q7 == "uruguay":
    print("Correct!")
    Score = Score + 1
elif Q7 == "Uruguay":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Uruguay")
    
time.sleep(2)
print("Question 8")
Q8 = input("Bandy is national sport of which country? ")
if Q8 == "russia":
    print("Correct!")
    Score = Score + 1
elif Q8 == "Russia":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Russia")

    time.sleep(2)
print("Question 9")
Q9 = input("Which Formula One driver was nicknamed The Professor? ")
if Q9 == "alain prost":
    print("Correct!")
    Score = Score + 1
elif Q9 == "Alain Prost":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Alain Prost")

time.sleep(2)
print("Question 10")
Q10 = input("Which famous European football club is known as The Old Lady? ")
if Q10 == "juventus":
    print("Correct!")
    Score = Score + 1
elif Q10 == "Juventus":
    print("Correct!")
    Score = Score + 1
else:
    print("False")
    time.sleep(1)
    print("It was actually Juventus")


time.sleep(2)
if Score <= 5:
    
    print("Unfortunatly", NAME, "Your score is\n", Score, "/10")
else:
    print("Congratulations", NAME, "Your score is\n", Score, "/10")
