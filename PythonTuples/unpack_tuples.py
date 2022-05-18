new_tuple = (12, "name", True, "python", 24)        # creating a tuple is called packing a tuple
(var1, var2, var3, var4, var5) = new_tuple     # unpacking is extracting the values from a tuple into variables
print(var1, var3)       # prints '12' and 'True'

(x, y, *z) = new_tuple     # use an asterisk character in front of a variable name to extract the values as a list
print(x, y, z)

(*s,) = new_tuple       # Similarly, we can also convert a tuples into a list by this technique
print(s)
print(type(s))          # returns " <class 'list'> "






