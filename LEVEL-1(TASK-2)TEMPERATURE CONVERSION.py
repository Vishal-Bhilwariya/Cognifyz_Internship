"""
Task - 2: Temperature Conversion

Create a Python program that converts temperatures between Celsius and Fahrenheit. Prompt the user to enter a temperature 
value and the unit of measurement, and then display the converted temperature.
"""
# Taking value input
print("___________________________________________")
while True:
    value = input("Enter a temperature value => ")
    count = 0 ; temp = 0
    for i in range(len(value)):
        temp = 1
        if value[i] in "0123456789":
            count += 1
    if count == len(value) and temp == 1:
        value = int(value)
        break        
    else:
        print("-----------------------------------------")
        print("Warning :INVALID NUMBER ")
        print("Please enter a valid number")
        print("-----------------------------------------")
        
# Taking unit input of temperature
while True :
    unit = input("Enter temperature unit ( Enter 'c' for celsius and 'f' for fahrenheit )=> ").lower()
    if unit in "cf":
        break
    else:
        print("-----------------------------------------")
        print("Warning :INVALID UNIT ")
        print("Please enter a valid unit ( c or f )")
        print("-----------------------------------------")

# LOGIC 

if unit == 'c':
    F = (9/5)*value + 32
    print("___________________________________________")
    print("YOUR INPUT -> ",value,"celsius")
    print("Result -> ",F,"fahrenheit")
    print("___________________________________________")
else:
    print("___________________________________________")
    C = ( value - 32 ) * (5/9)
    print("YOUR INPUT -> ",value,"fahrenheit")
    print("Result -> ",C,"celsius")
    print("___________________________________________")