"""
TASK - 4 : Calculator Program
Create a Python program that acts as a basic calculator . It should prompt the user to enter two number and an 
operator(+,-,*,/,%), and then display the result of the operation.
"""
print("___________________________________________")
# function to check that the number is valid or not
def check_number_valid_or_not(num):
    count = 0
    for i in range(len(num)):
        if num[i] in "01234566789.":
            count += 1
    if count == len(num) and count != 0:
        return True
    else:
        return False

# function to print invalid if number is not valid
def print_num() :
        print("-----------------------------------------")
        print("Warning :INVALID NUMBER ")
        print("Please enter a valid number")
        print("-----------------------------------------")

def print_line():
    print("___________________________________________")
        
# function to print your input data
def print_input(a,b,operation) :
    print("YOUR INPUT : a =",a,",b =", b,", opertaion =",operation)

# taking first number input from user
while True:
    a = input("Enter first number => ")
    boolean = check_number_valid_or_not(a) # calling function to check the number is valid or not
    if boolean == True:
        a = eval(a)
        break
    else:
        print_num()

# taking second number input from user
while True:
    b = input("Enter second number => ")
    boolean = check_number_valid_or_not(b) # calling function to check the number is valid or not
    if boolean == True:
        b = eval(b)
        break
    else:
        print_num()

# taking operation input from user
while True:
    operation = input("Enter operation you want to perform between two numbers => ")
    if operation != "" and len(operation) == 1 and operation in "+-*%/":
        break
    else:
        print("-----------------------------------------")
        print("Warning :INVALID OPERATION ")
        print("Please enter a valid operation")
        print("-----------------------------------------")
    
# logic of problem -> here we will use the concept of the function " match "

if operation == "+" :
    print_line()
    print_input(a,b,operation)
    print("RESULT : ",a,operation,b,"=",a+b)
elif operation == "-" :
    print_line()
    print_input(a,b,operation)
    print("RESULT : ",a,operation,b,"=",a-b)
elif operation == "*" :
    print_line()    
    print_input(a,b,operation)
    print("RESULT : ",a,operation,b,"=",a*b)
elif operation == "/" :
    print_line()
    print_input(a,b,operation)
    print("RESULT : ",a,operation,b,"=",a/b)
else :
    print_line()
    print_input(a,b,operation)
    print("RESULT : ",a,operation,b,"=",a%b)

print_line()