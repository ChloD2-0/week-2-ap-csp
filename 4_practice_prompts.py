
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print(f"I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print(f"Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
num1 = 500
num2 = 55
print(num1 + num2)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it
object1 = "computer"
object2 = "mouse"
object3= "keyboard"
print(f"I see a {object1}, a {object2}, and a {object3}.")
# Familiarize yourself with the syntax of the print() function.
# Print your name.
# Print today's date.
# Print the name of your favorite movie.
names = "Chloe and Arianna"
date = "October 30th"
age1 = 16
age2 = 17
years = 10
future = (age1 + years)
future1 = (age2 + years)
fav_movie1 = "The Accountant"
fav_movie2 = "Mean Girls"
print(f"Hi our names are {names}. The date today is {date}, and our favorite movies are {fav_movie1} and {fav_movie2}!")


# Print your name and age on separate lines using a single print() function.
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
print(f"In 10 years, {names} will be {future} and {future1} years old.")

##############################################################################################################

###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value


#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

blue_beetle_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien " \
"biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, " \
"he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable " \
"powers, forever changing his destiny as he becomes the superhero Blue Beetle."

new = blue_beetle_summary.replace("Blue", "Red")
count = 1
print(blue_beetle_summary)
print(len(blue_beetle_summary))
print(blue_beetle_summary.upper())
print(blue_beetle_summary.lower())
print(new)
print(blue_beetle_summary[334:340])
print(blue_beetle_summary[334:340])
print(blue_beetle_summary[::-1])
# print the length of the summary
# upper case the entire summary
# print the summary
# print the summary in lowercase
# replace the word blue with red
# print the summary
# string index the word beetle and print it out
# print the last word of the summary
# print the summary in reverse


##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.
name = input("What's your name?") 
print("Hi," + name + "! Our names are Chloe and Arianna!")
# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
topic = input("What are you learning?") 
print("Thanks for telling me that you're learning" + topic + "!") 

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
origin = input("Where are you from?") 
print("You're from" + origin + " ? Cool! I'm from Illinois!") 
# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.
first_name = input("What is your first name?") 
print("Your first name is "+ first_name +"." )
surname = input("What is your surname?") 
print("Your surname is "+ surname +"." )
full_name = (first_name + surname)
print("So your full name is" + full_name + ".")

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.

fav_color = input("What is your favorite color?") 
print("Your favorite color is" + fav_color + " and ours are Red and Purple!") 
name = input("What is your name?") 
print("Now I know that your name is" + name + " and your favorite color is" + fav_color + "!")

