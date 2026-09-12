num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
op = str(input("what do you want to use? +, -, /, * "))

if op == "+":
    add = num1 + num2
    print(add)
elif op == "-":
    sub = num1 - num2
    print(sub)
elif op == "/":
    divide = num1 / num2
    print(divide)
elif op == "*":
    multiply = num1 * num2
    print(multiply)
else:
    print("Please choose a operator")
