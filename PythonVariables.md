					           All about Python variables

Python variables are simply containers that store basically any type of value that we assign to it. For example,

					          var = “python”

is a valid python variable. The variable type in the above example is a string.


In python, the variables do not need to be specified with a type. It is automatically set when the variable is defined. For example,


                                              num = 35			(type : integer)

                                              var = “python” 		(type : string)

                                              answer = True			(type : Boolean)


There are many data types available in python and the above examples are just the basic data types which are more commonly used. Check out the
complete list of data types here. https://www.w3schools.com/python/python_datatypes.asp

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Multiple word variables


While declaring variables in any program, the most important part is the variable name. To make the name of a variable understandable, we might have 
to use multiple words to define them. For example,


	  studentname, studname, xyz - not invalid but not recommended

	  student_name - makes it more readable and clean.
    

There are three techniques that can be used to make multiple word variables more readable. 



PascalCase 

		StudentNameIs = “Shiva”

camelCase

		studentNameIs = “Shiva”

snake_case

		student_name_is = “Shiva”
    

Note that python variables are case sensitive. 

                            var = “python”

                            Var = “python”

are two different variables. A python variable can only contain alphabets (a-z or A-Z), numbers(0-9) and underscores.

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Try these simple programs.

(Example 1)

	number = “12”			#variable type is string
	character_name = “John”		#variable type is string
	print(“There are ” + number + “ apples in a dozen. ” + character_name + “ bought two dozens of apples”)


You can concatenate the value of a variable into the output statement by adding a ‘+’ sign before and after the variable name.
             
-----------------------------------------------------------------------------------------------------------------------------------------------------------
         
(Example 2)

	x = 10
	y = 20
	print(x+y)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

