operator = (input("Enter an Operator (+,-,*,/):"))
number1 = float(input("Enter the 1st Number:"))
number2 =float(input("Enter the 2st number:"))
if operator == "+":
    result = number1 + number2
    print(round(result,3))
elif operator == "-":
     result = number1 - number2
     print(round(result,3))
elif operator == "*":
     result = number1 * number2
     print(round(result,3))
elif operator == "/":
     result = number1 / number2
     print(round(result,3))
else:
     print(f"{operator} is not a valid operator")

                                             
