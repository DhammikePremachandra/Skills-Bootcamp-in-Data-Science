"""
# =========== Reading From Files in Python ===========

# ************ Example 1 ************
# Before you can read a file you need to open it.
# You open a file using Python's built in open() function which creates a file object.
# The line below creates a new file 'object' named f that is linked to the example.txt file in this folder.

f = open('example.txt', 'r+')


# This means f is open for reading.
# The first argument (example.txt) is the filename and the second argument is the mode.
# The mode determines the mode in which the file has to be opened.

# Here we intend to read and write from/to example.txt, which is already in the same folder as this file, example.py.
# Python will look in this directory for 'example.txt', and try read its context.

# The most common way to read from a file is simply to loop over the lines of the file:
# We can directly loop over the variable f, which is stored in Python as a list of lines.
# Each line is 1 line of the file.

# ************ Example 2 ************
print("\nExample 2: ")
for line in f:
        print("The first character of this line is: " + line[0] + "\n")
        print("The entire line is: " + line)

f.close()
# Always close files when done with them, using the close() function.
# This is in order to free up the resources that the file was using.
# Notice this is a function that takes in 0 input.


# ************ Example 3 ************
# We could build up all lines of the text file into a large string called contents as follows:

print("\nExample 3: ")
contents = ""
with open('example.txt', 'r+') as f: # Open the file again, this time using the 'with' syntax
        for line in f:
                contents = contents + line

# You don't need to close the file here because it has reached the end of block; this is a benefit of the 
# 'with' syntax

# We now have the contents of an external resource (a text file), stored inside our program in a variable called contents.
# That's pretty powerful! But for now, let's just print the contents to a screen:

print(contents)

# =========== Read Method ===========
# You can also use the read method in order to read from a file.
# The syntax for this method is as follows:
# file.read(n)   -   reads n number of characters from the file, or if n is blank reads the entire file


# ************ Example 4 ************
print("\nExample 4: ")

f = open('example.txt','r+', encoding='utf-8') # Open the file again!
# Notice in the code above how we pass an extra optional arugment through to the open function.
# This arguments specifies the encoding of the file.
newContents = f.read()
print(newContents)

f.close() # Always close files when done with them.


# ****************** END OF EXAMPLE CODE ********************* #

# =========== Encoding Files =========== #




# When you run the unencoded example you will notice that the output displays strange characters.
# This can be fixed by specifying the encoding scheme, UTF-8 or UTF-8-SIG, as an additional arugment to the open() function. 
# utf-8-sig is a variation of the utf-8 encoding that includes a Byte Order Mark (BOM) at the beginning of the file.
# The BOM is a special marker that indicates the file is UTF-8 encoded.
# By using utf-8-sig, you can avoid the appearance of strange characters at the beginning of the text, as the BOM is properly handled.
# When you run the encoded example, using utf-8-sig, you will notice that the data is transformed so that it is compatible for reading.


# Unencoded example
print("\n--Unencoded Example--\n")

with open('example.txt', 'r') as file:
    lines = file.readlines() 
print(lines)


# Encoded example using utf-8
print("\n--Encoded Example using utf-8--\n")

with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines() 
print(lines) # do you see the BOM at the beginning of the file?


# Encoded example using utf-8-sig
print("\n--Encoded Example using utf-8-sig--\n")

with open('example.txt', 'r', encoding='utf-8-sig') as file:
    lines = file.readlines() 
print(lines)

"""

# =========== Write Method ===========
# You can use the write() method in order to write to a file.
# The syntax for this method is as follows:
#   file.write("string")   - writes "string" to the file

# ************ Example 1 ************
# Before you can write to a file you need to open it.
# You open a file using Python's built-in open() function which creates a file
# called output.txt (it doesn't exist yet) in write mode.
# Python will automatically create this file in the same directory/folder 
# that our program is in.

ofile = open('output.txt', 'w')

# We ask the user for their name. When they enter it, it is stored as a string 
# in the variable 'name'.
name = input("Enter your name: ")

# We use the write method to write the contents of the 'name' variable to the output file.
ofile.write(name + "\n")


# You must run this Python file for the file 'output.txt' to be created with the
# output from this program in it.
ofile.write("My name is on the line above in this text file.")
# When we write to the file again, the current contents of the file will not be 
# overwritten. The new string will be written on the second line of the text file.

ofile.close() # Don't forget to close the file!



# ****************** END OF EXAMPLE CODE ********************* #