colours = [                             # 2 dimensional list. Each element in a list is also a list.
    ["Red", "Orange", "Yellow"],        # Each element can be accessed by row, column index.
    ["Green", "Black", "Brown"],      # for example, "orange" is in the 0th row and 1st column => [0],[1] is the index.
    ["Blue", "Purple"],
    ["Grey"]
]

print(colours[0][1])                    # prints "orange"


for row in colours:                     # nested for loop can be used to print all elements in all the lists.
    for column in row:                  # prints each column in each row. i.e, prints all the elements.
        print(column)
