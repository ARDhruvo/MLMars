# Take 3 user inputs of cgpa and
# 1. Find lowest
# 2. Find average

# Execution Point

a = float(input("Enter CGPA of first bondhu: "))
mini = a
b = float(input("Enter CGPA of second bondhu: "))
if b < mini:
    mini = b
c = float(input("Enter CGPA of third bondhu: "))
if c < mini:
    mini = c
    
avg = (a+b+c)/3

print(f"Lowest CGPA =  {mini}\nAverage CGPA = {avg}")