"""
Program that reads in a string and makes each alternate character into an upper case character
and each other alternate character a lower case character
"""

# Creating a function that takes a string as input and return updated string alternate between upper and lower case
def alternate_char(string):
     
    # Creating empty variable called "result" to store results
     result = " "

    # Loop through each character in the input string
     for i in range(len(string)):
            
            # if the index is even, change character into upper case
            if i % 2 == 0:
                 result += string[i].upper()
            
             # if the index is not even, change character into lower case
            else:
                  result += string[i].lower()
     
     # returning the result
     return result             



# Creating a function that takes a string as input and return updated string alternate between upper and lower case
def alternate_word(string):
      
    # Creating empty list called "result" to store results
      results = []

    # split the input string into words and store it into string_split as a list
      string_split = string.split()
    
    # Loop through each word in the string
      for j, word in enumerate(string_split):
            
            # If the index is even, change the word to lower case and append it into results     
            if j % 2 == 0:
                  results.append(word.lower())
            
            # If the index is odd, change the word to upper case and append it into results
            else:
                  results.append(word.upper()) 
    
    # Join the modified words back into a string
      results_joined = "  ".join(results)

    # returning the result
      return results_joined

# Getting string form user that user need to change and it store into variable "string"
string = input("Welcome to the alternative!, Please enter a string:").strip().lower()

# output of the new string                 
print(f"Here is the modified string with alternate characters: {alternate_char(string)}")

# output of the new string  
print(f"Here is the modified string with alternate words: {alternate_word(string)}")