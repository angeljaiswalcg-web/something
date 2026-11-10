# num1=int(input("enter your number:"))
# num2=int(input("enter your number:"))
# operation=input("operation to do:")
# if operation=="+":
#     print(num1+num2)
# if operation=="-":
#     print(num1-num2)
# if operation=="*":
#     print(num1*num2)
# if operation=="/":
#     print(num1/num2)
# if operation=="**":
#     print(num1**num2)
# if operation=="%":
#     print(num1%num2)
# perfect  calculator

given = input("Enter your calculation (e.g. 20 - 5): ")

num1, operation, num2 = given.split()

num1 = float(num1)
num2 = float(num2)

if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2)

elif operation == "**":
    print(num1 ** num2)

elif operation == "%":
    print(num1 % num2)

else:
    print("Invalid operation")
