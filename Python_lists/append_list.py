fruit = ["Apple", "Pineapple", "Orange", "Strawberry"]
fruit.append("Banana")          # you can add a new element to the end of the list by using append function
print(fruit)

fruit.pop()                     # removes the last element out of the list
print(fruit)

fruit.insert(2, "Peach")    # You can add a new value to list at a specific index using insert function.
print(fruit)   # The insert function takes two parameters. The index value and the element you want to add to the list.

fruit.pop(2)       # you can also remove a particular element from the list by specifying the index value
print(fruit)

fruit.insert(3, "Apple")
print(fruit)
print(fruit.count("Apple"))     # counts the number of times an element has been repeated in a list.

fruit.remove("Strawberry")   # you can also remove an element out of the list by using the remove method
print(fruit)

print(len(fruit))       # you can find out how many elements are in a list by using 'len' function






