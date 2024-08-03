"""
Task - 3 : Password Strength Checker
Create a Python function that evaluates the strength of a password entered by the user. 
Implement checks for factors such as length, presence of uppercase and lowercase letters, digits, and special characters.
"""
print("________________________________________________________________")

def check_strenght(password):
    res = [0,0,0,0] # -> [upper,lower,digit,special_char]
    for i in range(len(password)):
        if password[i].isupper():
            res[0] = 1
            break
    for i in range(len(password)):
        if password[i].islower():
            res[1] = 1
            break
    for i in range(len(password)):
        if password[i].isdigit():
            res[2] = 1
            break
    for i in range(len(password)):
        if password[i] in "!@#$%^&*()_":
            res[3] = 1
            break
    count = 0
    for i in range(len(res)):
        if res[i] == 1 :
            count += 1
        else:
            break
    return count

password = input("Enter your password : ")
count = check_strenght(password)
if len(password) > 8 and count == 4:
    print("--------------------------------")
    print("      A STRONG PASSWORD ")
    print("--------------------------------")
else :
    print("--------------------------------")
    print("      A WEAK PASSWORD ")
    print("--------------------------------")

print("________________________________________________________________")