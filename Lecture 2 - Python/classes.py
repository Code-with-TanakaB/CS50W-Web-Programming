class Point(): #defining a class called Point
    def __init__(self, input1, input2): #defining the __init__ method, which is a special method that is called when an instance of the class is created. It takes two parameters, input1 and input2, which are used to initialize the attributes of the class.
        self.x = input1 #setting the x attribute of the class to the value of input1
        self.y = input2 #setting the y attribute of the class to the value of input2

p = Point(2, 8)
print(p.x)
print(p.y)        