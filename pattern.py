# Output of the arrow head shape star pattern 

# asign maximum number of stars in  a row of the pattern into variable
max_stars_row = 5

# Creating  for loop to iterate  over row and display star pattern 
# Range is decide  1 to 10 according to the maximum length of stars in a row of the pattern

for i in range(1 ,10):

    # Untill i == 5, if statement output the first five rows of the stars pattern
    if i <= max_stars_row:
        print("*" * i)

    # Output last 4 rows of the stars pattern when i > 5   
    else:
        print("*" * (10 - i)) 