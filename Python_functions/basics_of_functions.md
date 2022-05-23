                                                        Basics of Functions in Python


A function is just a set of codes or instructions that performs a specific task in a program.



                                                    def welcome():
                                                        print(“Hello, Let’s learn Python”)

                                                    welcome()


‘Def’ in a function is a keyword. It is a rule in python to include this keyword whenever we create a function. 

The set of code lines to be included in the function should always be indented. 

Note in the example, the print statement is indented and is a part of the function. Whereas the function call statement is not 
indented and is not considered to be a part of the function.
  

                                                              Passing arguments

Function also takes values which are referred to as ‘parameters’ or ‘arguments’.
We can pass any type of value (string, integer, boolean, etc..) and any number of parameters in a function.



                                                      def welcome(name):
                                                          print(“Hello ” + name)


                                                      welcome(“Shiva”)



                                                               Return statement
                                                               

We can also get values from a function using the return statement. 
In a function the ‘return’ keyword is used to get a value from the function.



                                                      def add(x, y):
                                                          return  x + y


                                                          print(add(4, 3))
                                                          

This function will return the added value ‘7’. We can call the function in a print statement to print the final value from the function.



                                                      def power(y):
                                                          result = y * y * y
                                                          return result


                                                          print(power(2))
                                                          

You can also store the value in a variable and return the variable from the function.
