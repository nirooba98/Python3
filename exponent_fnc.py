
def find_exponent_result(num1, num2):
    answer = 1
    for i in range(num2):
        answer = answer * num1
    return answer


x = int(input("Enter the base number: "))
y = int(input("Enter the power number: "))
print(find_exponent_result(x, y))
