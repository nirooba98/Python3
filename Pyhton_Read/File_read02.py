var2 = open("data.txt", "r")
print(var2.readline())  # prints only the first line of data in the file.
print(var2.readline())  # prints the second line of data in the file.
var2.close()

"""
the readline() method prints only one line of data at a time. for example, if we call the readline() method four times
in a print statement, the first four lines are printed consecutively. 

this program prints:
Green

Pink
"""
