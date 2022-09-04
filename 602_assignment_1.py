#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
test3 = input('Enter the score for test 3: ')
#cm1 added test 3
# Calculate the average test score.
average = (int(test1) + int(test2) + int(test3)) / 3
#cm2 added int())
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
# cm3 change back to upper case
    print('Congratulations!')
print('That is a great average!')



#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

r1l = input('Enter the length for rectangle 1: ')
r1w = input('Enter the width for rectangle 1: ')
r2l = input('Enter the length for rectangle 2: ')
r2w = input('Enter the width for rectangle 2: ')

area1 = int(r1l) *int(r1w)
area2 = int(r2l) *int(r2w)

print('The area of rectangle 1 and 2 are', area1, 'and', area2)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

firstname = input('What is your first name?')
age = int(input('how old are you?'))

print('Happy birthday,', firstname+'!', 'You are',age,'years old today!')
