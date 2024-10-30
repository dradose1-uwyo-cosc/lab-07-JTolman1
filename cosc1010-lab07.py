# Jared Tolman
# UWYO COSC 1010
# Oct 30th, 2024
# Lab 07
# Lab Section: 15
# Sources, people worked with, help given to: Some Google searches were made on function and syntax information.
#

# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

integer=input(f"Please input a value for a factorial: ")
if integer.isdigit()==False or int(integer) <= 0:
    print("Please enter a positive whole number")
    integer=input(f"Please input a value for a factorial: ")

integer=int(integer)

factorial = 1

while integer > 1:
    factorial*=integer
    integer-=1

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

sumvalues=[0]
state=True
while state == True:
    integer2=input(f"Please input an integer value to sum. When finished, type 'exit': ")
    if integer2.lower() == "exit":
        state=False
    elif integer2.replace("-","").isdigit() != True:
        print(f"Unsupported value")
        integer2=input(f"Please input an integer value to sum: ")
    else:
        integer2=int(integer2)
        sumvalues.append(integer2)


num_sum = sum(sumvalues)

print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

state2=True
while state2==True:
    calc=input(f"Please type a simple math expression. When finished, type 'exit': ")
    calc=calc.replace(" ","")
    if calc.lower() == "exit":
        state2=False
    elif "+" in calc:
        clist=calc.split("+")
        ans=int(clist[0])+int(clist[1])
    elif "-" in calc:
        clist=calc.split("-")
        ans=int(clist[0])-int(clist[1])
    elif "*" in calc:
        clist=calc.split("*")
        ans=int(clist[0])*int(clist[1])
    elif "/" in calc:
        clist=calc.split("/")
        ans=int(clist[0])/int(clist[1])
    print(f"Answer = {ans}")
