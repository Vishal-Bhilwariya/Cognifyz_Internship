"""
Task -5 : Palindrome Checker

Write a Python Function that checks whether a given string is a palidrome.
A palidrome is a word ,phrase, or sequence that reads the same backward as forward. 
e.g : "madam" or "naman"
"""

# function to return reverse of string
def reverse(str) :
    return str[::-1]

# function to print result
def print_(original_str, rev_str , temp_str) :
    print("___________________________________________")
    print("Original string :",original_str)
    print("Reversed string :",rev_str)
    print("<< String is a ",temp_str.upper(),">>")
    print("___________________________________________")

# taking input string form user
string = input("Enter your string => ")
rev = reverse(string)

#  comparing original string with reversed string
if string == rev:
    print_(string,rev,"palidrome")
else :
    print_(string,rev, "not palidrome")