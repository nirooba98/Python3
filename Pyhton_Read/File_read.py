"""
You can open a file and perform various actions in python. To open a file you must specify the name or the
url/path(it is necessary to mention the path of the file if the file is not in the same folder) of the file. By default
python reads the file. But you can specify the actions as well, i.e. "read", "write", "append" ect.
"""

var = open("data.txt", "r")
"""
we mention the name of the file and specify the action to be performed. "r" - read. 
we can store the action in a variable and use the read data from the file.
"""

print(var.read())     # the read function reads and prints all the data from the opened file.
var.close()     # it is always a good practice to close the file.
