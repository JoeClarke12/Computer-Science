import csv

#-- Links the TempByMonth file object and stores it in a variable [f]ile 
f = open('classone.csv')
#-- csv_f will allow us to iterate over the given .csv file i.e. read the data
csv_f = csv.reader(f)

#-- Create an empty list to store the data from the file.
newlist = []


#Iterating through the csv data
for row in csv_f:

    #Convert the string values into integers
    row[1] = int(row[1])
    row[2] = int(row[2])
    row[3] = int(row[3])
    row[4] = int(row[4])

    #Finds the lowest temp for each month
    minimum = min(row[1:4])

    #Adds it to the list
    row.append(minimum)

    #Finds the lowest temp for each month
    maximum = max(row[1:4])

    #Adds it to the list
    row.apendmaximum)

    #Calculate the average of the 4 temperatures and rounds to nearest whole no
    average = round(sum(row[1:4])/4)

    #Adding it to a list
    row.append(average)

    #adding each row to the newlist - [0:6] the range of items on each row
    newlist.append(row[0:8])
    
#test the data in our list
print(newlist)

#--Sorting the data: lowest temp by month--

#Create a new list to store selected items from our previous list (newlist)
#Remember to put the data to be sorted in position [0]
lowTemp = [[x[5], x[0]] for x in newlist]

print('\nAverage Score \n')

#iterate through lowTemp and sort based on [0]
for entry in sorted(lowTemp):
    print(entry)


#--Sorting the data: Highest average temp by month--

#Create a new list to store selected items from our previous list (newlist)
averageTemp = [[x[7], x[0]] for x in newlist]

print('\nHighest Average Score \n')

#iterate through lowTemp and sort based on [0]
for entry in sorted(averageTemp, reverse = True):
    print(entry)




