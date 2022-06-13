"""
The "try and except" concept is very important in python. This block of code is used in python to prevent the
program from breaking when an exception is thrown. The try block essentially catches the error in a program and the
except block handles the error.
"""
try:                                                    # codes within the block are indented
    new_num = int(input("Enter a whole number: "))      # variable accepts only integers. Any value except integer
    print(new_num)                                      # value is an exception.
    print(x)                                            # another error where the 'x' is undefined.
except ValueError:          # when there is an exception (e.g. float value is entered ), this block of code is executed
    print("invalid input")
except NameError as err:    # the type of error can be stored in any variable(e.g. "err" in this case)
    print(err)              # prints the following error. (name 'x' is not defined)
