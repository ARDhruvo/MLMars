# Create a class with length and breadth and find its area using the class

# Class Point

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        a = self.length * self.breadth
        print(f"Area = {a} sq. units")
        
        
# Execution Point

l = float(input("Enter Length of rectangle: "))
b = float(input("Enter Breadth of rectangle: "))

rectangle = Rectangle(l, b)
rectangle.area()