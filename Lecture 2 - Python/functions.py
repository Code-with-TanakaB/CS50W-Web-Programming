def square(x): #defining a function called square that takes one parameter, x
    return x * x

for i in range(10): #iterating over the numbers from 0 to 9 using a for loop. The range function generates a sequence of numbers, and the loop will execute the block of code inside the loop for each number in that sequence.
    print(f"square of {i} is {square(i)}") #for each number i in the range from 0 to 9, the loop will print a formatted string that includes the value of i and the result of calling the square function with i as an argument. The f-string syntax allows for embedding expressions inside string literals, making it easy to include variable values in the output.
