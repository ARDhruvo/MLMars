# Define a function that takes NID card informations

# Function Point

def NID(fname, lname, gender, pres_address, perm_address, marital_status, blood_group):
    print(f"Name:\t\t{fname} {lname}\nGender:\t\t{gender}\nBlood Group:\t{blood_group}\nMarital Status:\t{marital_status}\n")
    print(f"Present Address:\t{pres_address}")
    print(f"Permanent Address:\t{perm_address}")
    
    # A random number can be generated here
    # print(f"Your NID Number:\n{nid_no}")

# Execution Point

name1 = input("Enter First Name: ")
name2 = input("Enter Last Name: ")
gender = input("Enter Gender: ")
pres_addr = input("Enter Your Present Address: ")
perm_addr = input("Enter Your Permanent Address: ")
mar = input("Enter Current Marital Status: ")
blood = input("Enter Your Blood Group: ")

# NID("Kuddus", "Ali", "Male", "Dilu Road", "Cumilla", "Unmarried", "B+")
NID(name1, name2, gender, pres_addr, perm_addr, mar, blood)