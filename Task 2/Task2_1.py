# Take 3 user inputs and find the greatest using conditionals

# Execution Point

x = input("Enter x: ")
y = input("Enter y: ")
z = input("Enter z: ")

if(x>y and x>z):
    print(f"x = {x} is greatest")
elif(y>z and y>x):
    print(f"y = {y} is greatest")
else:
    print(f"z = {z} is greatest")