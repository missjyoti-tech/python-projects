print("===== SIMPLE CALCULATOR =====")

num1=float(input("Enter first number:"))
num2=float(input("enter second number:"))

operator = input("Enter operator( + , - , *, /):")

if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator =="*":
    result = num1*num2
    print("Result:", result)
elif operator == "/":
    
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result : " , result)
else:
    print("invalid operator !")
    
