"""
Task - 4 : Fibonacci Sequence
Write a Python function that generates the Fibonacci sequence up to a given number of terms.
The function should take an integer input from the user and display the Fibonacci sequence up to that number of terms.
"""
print("______________________________________________")
def Fibonacci(n):
    a = 0
    b = 1
    print(a,b,end=" ")
    for i in range(n-2):
        sum = a + b
        a = b
        b = sum
        print(b,end=" ")

# taking number input from the user
while True:
    count = 0
    a = input("Enter a number : ")
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
    
print("------------------------------------")
print("<<<<<<<< FIBONACCI SERIES >>>>>>>>>>")
Fibonacci(a)
print("\n------------------------------------")
print("______________________________________________")
