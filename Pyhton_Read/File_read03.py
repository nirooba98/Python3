var3 = open("data.txt", "r")
print(var3.readlines()[2])  # considers every line in the file as a list. Prints the line at specified index.
var3.close()

"""
The data is aligned as a list [ 'Green', 'Pink', 'Blue', 'Orange', 'Yellow' ]
In this program, 'Blue' is at index 2. Therefore, the program prints 'Blue'
"""
