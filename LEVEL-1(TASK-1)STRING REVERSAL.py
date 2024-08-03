""" 
Task - 1: String Reversal

Create a Python function that takes a string as input and returns the reverse of that string. 
For example, if the input is "hello, " the function should return "olleh." 
"""
# Logic to reverse the string are : 

# LOGIC - 1 : In this ,I am using The concept of "STRING SLICING" which is like <SYNTAX : variable_name[start:end:step] >
def rev_logic_1(string) :
    rev = string[::-1]  # in this i have given step = -1 , so it will automatically starts with the lenght - 1 of string 
                        # and will end at 0
    return rev

# LOGIC - 2 : In this , I am simply using for loop to reverse my string by iterating original string from it's last index
def rev_logic_2(string) :
    rev = "" # declaring a string variable
    for i in range(len(string) - 1 , -1 , -1): # range(start , end , step)
        rev += string[i] 
    return rev

# function to print
def print_(str,rev,a) :
    print("___________________________________________")
    print("LOGIC -",a)
    print("Original string : ",string)
    print("Reverse string : ",rev)
    print("___________________________________________")

# Taking input as string
print("___________________________________________")
string = input("Enter your string => ")
# calling logic 1 function for string reverseal
res_1 = rev_logic_1(string)
print_(string,res_1,1)

# calling logic 2 function for string reverseal
res_2 = rev_logic_2(string)
print_(string,res_2,2)
 

# NOTE -> Logic - 1 is more efficeint , easy and better than logic - --2