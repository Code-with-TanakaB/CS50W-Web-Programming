import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError: #catching the ValueError exception that occurs when the user inputs a non-integer value
    print("Error: Please enter valid integers.")
    sys.exit(1)    
    
try:
    result = x / y
except ZeroDivisionError: #catching the ZeroDivisionError exception that occurs when the user tries to divide by zero
    print("Error: Division by zero is not allowed.")
    sys.exit(1) #exiting the program with a status code of 1 to indicate that an error occurred

print(f"{x} divided by {y} is {result}") #printing the result of the division if no exceptions were raised. This line will only be executed if both the ValueError and ZeroDivisionError exceptions were not raised, meaning that the user inputted valid integers and did not attempt to divide by zero.
