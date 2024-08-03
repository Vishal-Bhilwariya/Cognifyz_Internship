"""
Task - 2 : Number Guesser
Create a number guessing game where the program generates a random number between a specified range, and 
the user tries to guess it. Provide feedback to the user if their guess is too high or too low.
"""

print("___________________________________________")
# function to check the number is integer or not
def check_int(num):
    count = 0
    for i in range(len(num)):
        if num[i] in "0123456789":
            count += 1
        if count == len(num) and len(num) > 0:
            return True

# taking starting value of range
while True:
    start = input("Enter starting number of range : ")
    res = check_int(start)
    if res == True:
        start = int(start)
        break
    else :
        print("----------------------------------")
        print("  INVALID NUMBER ENTERED BY YOU")
        print("----------------------------------")  
# taking ending value of range 
while True:
    end = input("Enter ending number of range : ")    
    res = check_int(end)
    if res == True:
        end = int(end)
        break
    else :
        print("----------------------------------")
        print("  INVALID NUMBER ENTERED BY YOU")
        print("----------------------------------") 

# using randint(start,end) function from random module to generate a random number 
import random
n = random.randint(start,end)

# logic of problem
i = 1
while True :
    # taking guessed number input from the user
    while True:
        a = input("Guess a number : ")
        res = check_int(a)
        if res == True:
            a = int(a)
            break
        else :
            print("----------------------------------")
            print("  INVALID NUMBER ENTERED BY YOU")
            print("----------------------------------")        
        
    if n == a :
        print("___________________________________________________")
        print(i,") YOU WON THE GAME BY GUESSING THE NUMBER CORRECTLY")
        print("___________________________________________________")
        
        # want to replay
        rep = input("Enter 'y' to replay the game else enter any key : ").upper()
        if rep != 'Y':
            break
    else :
        if n < a :
            print("---------------------------------")
            print(i,") Your guessed number is TO HIGH ")
            print("---------------------------------")
        else :
            print("---------------------------------")
            print(i,") Your guessed number is TO LOW ")
            print("---------------------------------") 
        i += 1          

print("\n<<<<<<<<< THANK YOU FOR PLAYING THIS GAME >>>>>>>>>>\n")
print("___________________________________________")