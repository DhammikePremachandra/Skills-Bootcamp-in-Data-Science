"""
Program that reads in a string and makes each alternate character into an upper case character
and each other alternate character a lower case character
"""

# Getting string form user that user need to change and it store into variable "string"
string = input("Welcome to the alternative!, Please enter a string:")


# Creating a function that takes a string as input and return updated string
def alternate_case(string):
     
    # Creating empty variable called "result" to store results
     result = " "

    # Loop through each character in the input string
     for i, char in enumerate(string):
            
            # if the index is even, change character into upper case
            if i % 2 == 0:
                 result += char.upper()
            
             # if the index is not even, change character into lower case
            else:
                  result += char.lower()
     
     # returning the result
     return result             

# output of the new string                 
print(f"Here is modified string: {alternate_case(string)}")