"""
# ========= Recap on Strings ===========
# A string is a common data type which is used to represent text.
# It is a sequence of characters, such as letters, numerals, symbols, and special characters.
# You have probably already noticed what an important part strings play in programming.
# Many programs you come across will involve the manipulation of strings.
# Therefore, knowing string manipulation techniques or string handling is crucial.
# We have already touched on this subject in the previous strings task, so this will just serve as a brief recap
# and will introduce you to more advanced programs.


# ************ Example 1 ************
# Recap on slicing strings
print("Example 1: ")

string = 'Hello world!'
fizz = string[0:5]
print(fizz)

# Note that slicing a string does not modify the original string.
# You can simply store the substring 'sliced' from the original string in a separate variable.
# By storing the substring in another variable, you keep the original string intact.


# ************ Example 2 ************
print("Example 2: ")

fact1 = "The original name of Windows was Interface Manager."
fact1 = fact1.upper()
print(fact1)
fact1 = fact1.lower()
print(fact1)

# ************ Example 3 ************
print("Example 3: ")

sentence = "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
split_sentence = sentence.split("HELLO")
print(split_sentence)

# Notice how a list is printed out?

# ************ Example 4 ************
print("Example 4: ")

fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
fact2 = fact2.replace("$", "WOW!")
print(fact2)
fact2 = fact2.strip()
print(fact2)
fact2 = fact2.split("WOW!")
print(fact2)

# ************ Example 5 ************
print("Example 5: ")
string_list = ["I", "like", "to", "join", "lists", "to", "make", "strings"]
list_joined = " ".join(string_list)
print(list_joined)

# ========= Escape Character ===========
# Python uses the backslash (\) as an escape character.
# The backslash (\) is used as a marker character to tell the compiler/interpreter that the next character has some special meaning.
# The backslash together with certain other characters are known as escape sequences.

# ************ Example 6 ************
print("Example 6: ")
people = "Person 1 \nPerson 2"
print(people)
# Notice the line break between the two words. The \n character is invisible -- it's a command to insert a new line.


# ************ Example 7 ************
print("Example 7: ")
wage = "Person 1: \t 123.22"
print(wage)
# Notice the tab between the two words. The \t character is invisible -- it's a command to insert a new tab space.

# ************ Example 8 ************
print("Example 8: ")
sentence = "\"The escape character (\\) is a character which invokes an alternative interpretation of subsequent characters in a character sequence.\""
print(sentence)
# Notice that the quotation marks and backslash are printed out as part of the string.


# ****************** END OF EXAMPLE CODE ********************* #

"""
"""
# ============= Creating a List ==================
# To create a list simply put different comma-separated values between square brackets.

# ************ Example 1 ************
# A List of Strings

string_list = ['John', 'Mary', 'Harry']
# Python knows that anything defined in [] is a list.
# There are 3 string items in this list.

# ************ Example 2 ************
# A list containing different datatypes

mixed_list = ['Hello', 3.4, 89, 'World']

# ************ Example 3 ************
# A list containing another list

my_list = ['Monkey', 'Elephant', [3, 4, 6, 10]]

# ============= Indexing Lists ==================
# We are able to access all elements in a list using the index operator [].
# The index starts from 0 for the leftmost item, so a list having 10 elements will have indices from 0 to 9.
# Alternatively the index can begin with -1 for the index of the rightmost item, so a list having
# 10 elements will have indices from -10 to -1.

# ************ Example 4 ************
print("Example 4: ")

pet_list = ['cat', 'dog', 'hamster', 'goldfish', 'parrot']

print(pet_list[0])
# Prints 'cat'.
# The element at position 0 is also known as the first element of a list, or the 'element at index 0'.

print(pet_list[-2])
# Prints 'goldfish'
# The element at position -2 is also known as the 4th element of the list, or the 'element at index -2'. 

# ============= Slicing Lists ==================
# You can slice lists in the same way as you would slice strings.
# We can access a range of items in a list by using the slicing operator (colon).
# In order to slice a list you need to indicate a start and end position of the items you would like to access.
# You place these positions between the square brackets of the index operator [] and separate them with the colon.
# The item in the start position is included in the sliced list, while the item in the end position is not included.

# ************ Example 5 ************
print("\nExample 5: ")

num_list = [1, 4, 2, 7, 5, 9]

print(num_list[1:2])
# Prints from position 1 up to position 2, but does NOT include the element at position 2,
# so it only prints the item in position 1, i.e. 4.

print(num_list[0:])
# Prints everything from the 0th position to the end of the list i.e. the entire list.

print(num_list)
# A faster way to print the entire list. 

# ============= Changing Elements in a Lists ==================
# Elements in a list can be changed.
# You use the assignment operator (=) to change single or multiple elements.

# ************ Example 6 ************
print("\nExample 6:")

name_list = ['James', 'Molly', 'Chris', 'Peter', 'Kim']
name_list[2] = 'Tom'
# We can replace the 3rd element of the list with a new string.
# 'Chris' will be lost and replaced with 'Tom'. 
print(name_list) # To see that the list has changed.

name_list[1:4] = ['Joe', 'Lucy', 'Kelly']
# Here we replace the 2nd, 3rd and 4th elements of the list with a new string.
print(name_list) # To see that the list has changed.

# ============= Adding Elements to a Lists ==================
# You can add an element to the end of a List using the 'append()' method.

# ************ Example 7 ************
print("\nExample 7:")

new_list = [34, 35, 75, 'Coffee', 98.8]
new_list.append('Tea')
# Adds the String 'Tea' to the end of the list
print(new_list)

# ============= Deleting Elements From a list ==================
# You can use the 'del' keyword to delete one or more items from a list.
# You are even able to delete the list entirely.

# ************ Example 8 ************
print("\nExample 8:")

char_list = ['P', 'y', 't', 'h', 'o', 'n']

del char_list[3]
# Deletes the single element 'h'
print(char_list)

del char_list[1:3]
# Deletes multiple elements from the 2nd to 4th element.
print(char_list)

del char_list
# Deletes the entire list

# ============= Getting the Length of a List ==================
# You can get the length of the list (how many elements there are in the list) by using the len() function.
# This is the same function we used to get the length of a string. 

# ************ Example 9 ************
print("\nExample 9:")

oddNum_list = [1, 3, 5, 7, 9]
print(len(oddNum_list))
# Will print the total number of items in the list, currently 5.

# ================== Looping Over Lists ==================
# What if you have a list of items and you want to do something to each item?
# You simply use a for loop to loop over every item in the list.

# ************ Example 10 ************
print("\nExample 10:")

food_list = ['Pizza', 'Burger', 'Fries', 'Pasta', 'Salad'] #Define a list of strings

for food in food_list:
    print(food)
# This loop prints out every item in the list. 
# This is a very powerful tool in Python and shows how you can simply loop through a list.

# ************ Example 11 ************
print("\nExample 11:")
numbers = [1,2,3,4]

for num in numbers:
    print(num)
# Any type of list can be looped over using this construct.
# The above will print out the numbers 1 to 4 - i.e. the entries in list 'numbers'.

# ================== Checking if Something is in a List ==================
# You can simply use an if statement to check if a certain item is in a list.

# ************ Example 12 ************
print("\nExample 12:")
grocery_list = ['Bread', 'Milk', 'Butter', 'Cheese', 'Cereal']

if 'Apples' in grocery_list:
    print('The item Apples was found in the list grocery_list')
else:
    print('The item Apples was not found in the list grocery_list')
        
# This is a much quicker way than looping through all the items, such as if you did:
for item in grocery_list:
    if item == 'Apples':
        print('The item Apples was found in the list grocery_list')

# ================== Using the range Function ==================
# The range function is a special Python function, that will automatically generate a list of integers within a specified range.

# ************ Example 13 ************
print("\nExample 13:")

num_til_10 = list(range(0,10))
print(num_til_10)
# This will create a list of integers =[0,1,2,3,4,5,6,7,9] and store it in the variable 'num_til_10'.

num_til_5 = list(range(0,5)) 
# This will create a list of integers =[0,1,2,3,4] and store it in the variable 'num_til_5'.

num_2_til_5 = list(range(2,5))
# This will create a list of integers =[2,3,4] and store it in the variable 'num_2_til_5'.

# The resulting list can be looped over like any list of integers, e.g., to print the numbers from 1 to 10:
for num in num_til_10:
    print(num)

print("\n")

# Since num_til_10 = list(range(0,10)), the above for loop is exactly the same as:
for num in list(range(0,10)):
    print(num)

# ****************** END OF EXAMPLE CODE ********************* # 
    
"""
# =========== Python list Methods  ===========
# There are many useful built-in list methods available for you to use.
# Some other list methods can be found below:
#   extend()    - Adds all elements of a list to the another list
#   insert()    - Inserts an item at the defined index
#   remove()    - Removes an item from the list
#   pop()       - Removes and returns an element at the given index
#   index()     - Returns the index of the first matched item
#   count()     - Returns the count of number of items passed as an argument
#   sort()      - Sorts items in a list in ascending order
#   reverse()   - Reverses the order of items in the list

# =========== The Copy Module  ===========
# Let's take a closer look at the copy module.
# There are several ways to make a copy of a list.
# The simplest way to make a copy is to use the copy() method.
# Using the copy() method ensures that if you modify the copied list, the original list remains the same.
# However, if your list contains other lists as items, those inner lists in the original list can still be modified
# if the corresponding inner list in the copied list is modified.
# This is called a shallow copy.
# Slicing lists also creates a shallow copy of a list.
# Therefore, when the list contains other lists as items, the inner lists have to be copied as well.
# You could do this manually but Python already contains a method to do it, the deepcopy() method.
# In order to use the deepcopy() and copy() methods you must import the copy module.

# ************ Example 1 ************
print("Example 1:")
import copy

a = [[1, 2, 3], [4, 5, 6]]
b = copy.copy(a)
c = a[:] #also makes a copy of a
d = copy.deepcopy(a)

b[1][0] = 10
c[1][1] = 11
d[1][2] = 12

print("List a:")
print(a)
print("List b:")
print(b)
print("List c:")
print(c)
print("List d:")
print(d) # Notice how the only change to d is element [1][2] because it's a deep copy

# =========== List Comprehension  ===========
# List comprehension can be used to construct lists in an elegant and concise way.
# This is a powerful tool that will apply some operation to every element in a list, and then put the element into a new list.
# List comprehension consists of an expression followed by a for statement inside square brackets.

# ************ Example 2 ************
print("\nExample 2:")

num_list = ['1', '5', '8', '14', '25', '31']
print(num_list)

new_num_list_ints = [int(element) for element in num_list]
# We are looping over num_list, which is a list of strings 
# For each element, we are casting it to an Integer and putting it into a new list, new_num_list_ints.

print(new_num_list_ints)  # Do you see the difference?

# We can now sum this list, since new_num_list_ints is a list of integers and not strings.
print(sum(new_num_list_ints))
# We can compute the sum of the Integers using the built-in function sum()
# This function gives you 1+5+8+14+25+31=84.

# ************ Example 3 ************
# You can do many operations with list comprehensions. 
print("\nExample 3:")

double_list = [2 * element for element in new_num_list_ints]
# A new list, with each element double its value in the previous list.
print(double_list)

half_list = [0.5 * element for element in new_num_list_ints]
# A new list, with each element half its value from the previous list.
print(half_list)

# =========== Dictionaries ===========

# =========== Creating a Dictionary ===========
# To create a dictionary simply place the items inside curly braces and separate them by commas.
# An item has a key and a value, which is expressed as a pair (key: value)
# Items in a dictionary can have a value of any datatype, however the key must be either a String or number and must be unique.

# ************ Example 4 ************

# An empty dictionary 
empty_dict = {}

# A dictionary with integer keys
int_key_dict = {1: 'apple',
                2: 'banana',
                3: 'orange'
               }

# A dictionary with string keys
string_key_dict = {'name': 'John',
                   'surname': 'Doe',
                   'gender': 'male'
                  }

# A dictionary with mixed keys 
mix_key_dict = {'word': 'Python',
                2: [1, 3, 4, 5]
               }
               
# =========== Accessing Elements from a Dictionary ===========
# While you might use indexing to access elements in a list, dictionaries use keys.
# Keys can be used to access values either by placing them inside square brackets [], such as with indices in lists, or with the get() method.
# Note, if you use the get() method, it will return 'None' instead of 'KeyError', if the key is not found.

# ************ Example 5 ************
print("\nExample 5:")

profile_dict = {'name': 'Chris',
                'surname': 'Smith',
                'age': 28,
                'cell': '083 233 3242'
               }

# Using square brackets []
print(profile_dict['surname'])
# prints out 'Smith'

# Using the get() method
print(profile_dict.get('cell'))
# prints out '083 233 3242'

# =========== Changing Elements in a Dictionary ===========
# We can add new items or change items using the assignment operator (=)
# If there is already a key present, the value gets updated, else if there is no key, a new key: value pair is added.

# ************ Example 6 ************
print("\nExample 6:")

profile_dict = {'name': 'Chris',
                'surname': 'Smith',
                'age': 28,
                'cell': '083 233 3242'
               }

# Changing a value
profile_dict['age'] = 29
print(profile_dict)

# Adding a value
profile_dict['gender'] = 'male'
print(profile_dict)

# =========== Dictionary Membership Test ===========
# You can test if a key is in a dictionary by using the keyword 'in'.
# You simply enter the key you want to test for membership, followed by the 'in' keyword and lastly the name of the dictionary.
# This will return either True or False, depending on whether the dictionary contains the key or not.
# The membership test is for keys only, not for values.

# ************ Example 7 ************
print("Example 7:")

doubles = { 1: 2,
            2: 4,
            3: 6,
            4: 8,
            5: 10
          }

print(1 in doubles)
# prints out True because 1 is a key

print(8 in doubles)
# prints out False because 8 is not a key but a value

# ****************** END OF EXAMPLE CODE ********************* # 