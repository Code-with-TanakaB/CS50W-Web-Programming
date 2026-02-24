def announce(f): #defining a decorator function called announce that takes a function f as an argument
    def wrapper(): #defining a wrapper function that will be returned by the decorator. This function will call the original function f and print messages before and after it is called.
        print("About to run the function...")
        f() #calling the original function f
        print("Done with the function.")
    return wrapper

@announce #using the @ syntax to apply the announce decorator to the hello function. This is equivalent to writing hello = announce(hello)
def hello():
    print("Hello, world!")
hello()