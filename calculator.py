num1 = int(input("Enter first number: "))
operator = input("Enter the operator: ")


if operator == "+":
    num2 = int(input("Enter second number: "))
    print(num1 + num2)
elif operator == "-":
    num2 = int(input("Enter second number: "))
    print(num1 - num2)
elif operator == "*":
    num2 = int(input("Enter second number: "))
    print(num1 * num2)
elif operator == "/":
    num2 = int(input("Enter second number: "))
    print(num1 / num2)
elif operator == "^":
    num2 = int(input("Enter second number: "))
    def pow(num1 , num2) :
        result = 1
        for i in range(num2):
            result = result * num1
        return result
    print (pow(num1 , num2))
elif operator == "**":
    result = 1
    if num1 >= 0:
        result = num1 ** 0.5
    print(result)
else:
    print("worng operator please try again")