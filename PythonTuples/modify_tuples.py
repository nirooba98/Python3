tuple1 = (12, "name", True, "python", 24)
print(tuple1)

new_list = list(tuple1)
print(new_list)     # a tuple can be converted into a list to perform any modifications

new_list.append("Learn")
tuple1 = tuple(new_list)    # add a new element to the list and convert it back to a tuple
print(tuple1)

tuple2 = (True,)            # python does not consider a variable as tuple without a comma (,)
tuple1 += tuple2            # we can add two tuples together in python
print(tuple1)

tuple1 = 2 * tuple1         # we can also multiply a tuple by any number
print(tuple1)

new_list = list(tuple1)
new_list.remove(24)         # removes the first occurrence of the specified value
print(new_list)

tuple1 = tuple(new_list)
print(tuple1)







