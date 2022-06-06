
def find_exponent_result(num1, num2):           # defining a function to calculate exponent value. Here, (num1 = base value) and (num2 = power value)
    answer = 1
    for i in range(num2):                       # we can write a for loop with the power value as the range.
        answer = answer * num1                  # the base value is multiplied with itself until the loop ends.
    return answer


x = int(input("Enter the base number: "))
y = int(input("Enter the power number: "))
print(find_exponent_result(x, y))
