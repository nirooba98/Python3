
"""
Syntax:
for variable in sequence:           'for' and 'in' are keywords
    print("instructions")
"""

for char in "shiva":        # looping through a string. Prints each letter of the string in a new line
    print(char)


colours = ["orange", "Yellow", "olive", "black"]
for colour in colours:      # Prints all the values in an array.
    print(colour)


for i in range(6, 15):      # prints the numbers (0 - 14)
    print(i)


for shade in colours:
    if shade == "olive":    # if statement breaks the loop to execute a specified condition.
        print("olive - Colour of the month!")
    else:
        print(shade)        # if condition untrue, prints the values in the array.

clothes = ["Shirt", "Gown", "Jacket"]
for dress in clothes:
    for color in colours:
        print(color, dress)
