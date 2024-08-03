"""
Task - 3 : Email Validator

Develop a Python function that validates whether a given string is a valid email address. Implement checks for the format, 
including the presence of an "@" symbol and a domain name
"""

# function to validates that email is valid or not
def check(email):
    count = 0 ; index = -1
    for i in range(len(email)):
        if "@" == email[i]:
            count = 1
            index = i
            break
    starting_part = email[:index]
    ending_part = email[index+1:]

    if ending_part == "gmail.com":
        count += 1
    if len(starting_part) > 7 :
        count += 1
    return count

# taking input email as string
print("___________________________________________")
email = input("Enter your email i'd => ")
count = check(email)
if count == 3:
    print(email,"is a valid email")
else:
    print(email,"is a invalid email")
print("___________________________________________")
