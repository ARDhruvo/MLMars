a = 7
b = 4
# Perform a^b and explain it

# Execution Point

c = a^b
print(c)

# ^ is XOR operation
# a = 7 = 1 1 1
# b = 4 = 1 0 0 
# --------------
# a ^ b = 0 1 1 = 3

# Explanation:
# 0 XOR 0 = 0
# 0 XOR 1 = 1
# 1 XOR 0 = 1
# 1 XOR 1 = 0
# LSB and 2nd bit has 1 XOR 0 = 1
# MSB has 1 XOR 1 = 1 
