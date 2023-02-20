def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2


print(calcule(5, "+", 2))
print(calcule(7, "*", 4))
print(calcule(6, "-", 2))
print(calcule(8, "/", 1))
print(calcule(7, "%", 10))