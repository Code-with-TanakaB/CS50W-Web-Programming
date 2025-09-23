import sys

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    sys.exit(1)

print(f"{x} divided by {y} is {result}")
