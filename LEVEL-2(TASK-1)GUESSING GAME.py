"""
Task - 1 : Guessing Game
Write a Python program that generates a random number between 1 and 100. The user should then try to guess the number.
The program should provide hints such as "too high" or "too low" until the correct number is guessed.
"""

print("___________________________________________")
# using randint(start,end) function from random module to generate a random number 
import random
n = random.randint(1,100)

j = 1
while True :
    # taking guessed number input from the user
    while True:
        count = 0
        a = input("Guess a number : ")
        for i in range(len(a)):
            if a[i] in "0123456789":
                count += 1
        if count == len(a) and len(a) > 0:
            a = int(a)
            break
        else :
            print("----------------------------------")
            print("  INVALID NUMBER ENTERED BY YOU")
            print("----------------------------------")

    if n == a :
        print("___________________________________________________")
        print(j,") YOU WON THE GAME BY GUESSING THE NUMBER CORRECTLY")
        print("___________________________________________________")
        
        # want to replay
        rep = input("Enter 'y' to replay the game else enter any key : ").upper()
        if rep != 'Y':
            break
    else :
        if n < a :
            print("---------------------------------")
            print(j,") Your guessed number is TO HIGH ")
            print("---------------------------------")
        else :
            print("---------------------------------")
            print(j,") Your guessed number is TO LOW ")
            print("---------------------------------")  
        j += 1         

print("\n<<<<<<<<< THANK YOU FOR PLAYING THIS GAME >>>>>>>>>>\n")
print("___________________________________________")